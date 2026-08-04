# -*- coding: UTF-8 -*-

'''
Module
    proxy_validator.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
    Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines mcheck decorator for checking method parameters.
    Utility for parameter validation borrowing Checker from class instances.
    Mechanism for parameters checking in methods and functions.
'''

from __future__ import annotations

from collections.abc import Callable, Sequence
from inspect import signature, Signature
from functools import wraps
from typing import cast

from ats_utilities.checker.setup.factory import CheckerBundleFactory
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.types import Parameters, CheckerErrorType
from ats_utilities.exceptions import (
    ATSRuntimeError, ATSTypeError, ATSValueError
)
from ats_utilities.validation.context_error import raise_error
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def validate_specs(specs: Parameters, context: str) -> None:
    '''
        Validates the specifications list structure.

        :param specs: The parameter specification list to validate.
        :param context: The context string for error reporting.
        :exceptions:
            | ATSValueError: The specs must be provided.
            | ATSTypeError:  The specs must be a list of (str, object) tuples.
    '''
    ctx: str = context if context else 'validate_specs(...)'
    fmt_msg: str = "the expected format: [('expected_type:param_name', default_value), ...]"
    msg_not_none: str = f'the specs must be provided, {fmt_msg}'
    msg_specs_istype: str = f'the specs must be a Sequence, {fmt_msg}'

    not_none(specs, ctx, msg_not_none)
    istype(specs, Sequence, ctx, msg_specs_istype)

    for index, item in enumerate(specs):
        msg_item_istype: str = f'the spec item at index {index} must be a list/tuple, {fmt_msg}'
        istype(item, tuple, ctx, msg_item_istype)

        if len(item) != 2:
            raise_error(
                fallback_context=ctx,
                fallback_msg=f'the spec item at index {index} must be a tuple of length 2, {fmt_msg}',
                exc_context=ctx,
                exc_message=None
            )

        istype(item[0], str, ctx, f'the spec key at index {index} must be a string, {fmt_msg}')


def validate_args(
    func: Callable[..., object],
    args: tuple[object, ...],
    kwargs: dict[str, object],
    specs: Parameters,
    checker: IChecker,
    exc_context: str
) -> None:
    '''
        Validates the argument values against parameter specification.

        :param func: The decorated function.
        :param args: The position arguments passed.
        :param kwargs: The keyword arguments passed.
        :param specs: The parameter specification list.
        :param checker: The checker instance to validate with.
        :param exc_context: The exception context.
        :exceptions:
            | ATSValueError: The specification format is invalid.
            | ATSTypeError:  The parameter type validation failed.
            | ATSValueError: The parameter format validation failed.
    '''
    # Safely bind the passed args and kwargs to the function's signature
    func_signature: Signature = signature(func)
    bound_arguments = func_signature.bind(*args, **kwargs)

    # Fill in empty optional parameters with their default values from definition
    bound_arguments.apply_defaults()
    actual_params_dict = bound_arguments.arguments

    runtime_parameters: Parameters = []

    # Iterate through specs and map them to actual arguments dynamically
    for exp_type, _ in specs:
        separator: str = checker.get_format_validator().get_separator()

        if separator not in exp_type:
            raise_error(
                fallback_context=exc_context,
                fallback_msg=f'the format of parameter {exp_type} is not valid',
                exc_context=exc_context,
                exc_message=None,
                exc_class=ATSValueError
            )

        raw_type, pname = checker.get_format_validator().split(exp_type)

        # Validate only if the specified parameter is bound to the function
        if pname in actual_params_dict:
            actual_value = actual_params_dict[pname]

            # We check if the type uses | None union syntax
            is_optional = raw_type.endswith(' | None')

            if is_optional:
                # We highlight the internal type, e.g. str | None -> str
                target_type = raw_type[:-7].strip()

                # If the value is None, it is valid and we skip the check
                if actual_value is None:
                    continue
            else:
                target_type = raw_type

            # If it is not optional and the value is None, it is immediately a type error
            if actual_value is None:
                runtime_parameters.append((f'{target_type}{separator}{pname}', actual_value))
                continue

            # We form a cleaned specification string for Checker (eg str:version)
            clean_exp_type = f'{target_type}{separator}{pname}'
            runtime_parameters.append((clean_exp_type, actual_value))

    # Process parameter validation
    if runtime_parameters:
        report_message, error_id = checker.validates_parameters(runtime_parameters)

        if error_id != CheckerErrorType.NO_ERROR:
            if error_id == CheckerErrorType.TYPE_ERROR:
                raise_error(
                    fallback_context=exc_context,
                    fallback_msg=f'the type error: {report_message}',
                    exc_context=exc_context,
                    exc_message=None,
                    exc_class=ATSTypeError
                )
            else:
                raise_error(
                    fallback_context=exc_context,
                    fallback_msg=f'the format error: {report_message}',
                    exc_context=exc_context,
                    exc_message=None,
                    exc_class=ATSValueError
                )


def mcheck[F: Callable[..., object]](specs: Parameters) -> Callable[[F], F]:
    '''
        Decorator supporting class methods (instance methods, classmethods).
        Borrows the checker object dynamically from the class instance 
        to validate method parameters.
        Mechanism for parameters checking in methods only.

        :param specs: The specification for parameters.
        :return: The wrapped function.
        :exceptions:
            | ATSTypeError:      The parameter type validation failed.
            | ATSValueError:     The parameter format validation failed.
            | ATSRuntimeError:   The decorator used on a non-class method.
            | ATSAttributeError: The class does not provide a _checker object.
    '''
    validate_specs(specs, 'mcheck(...)')

    def decorator(func: F) -> F:

        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            # Capturing the class instance (self is always the first argument in args)
            self_instance = args[0] if args else None

            if self_instance is None:
                raise_error(
                    fallback_context='mcheck::decorator(...)',
                    fallback_msg=f'the decorator @mcheck on {func.__name__} can only be used on class methods',
                    exc_context='mcheck::decorator(...)',
                    exc_message=None,
                    exc_class=ATSRuntimeError
                )

            context_bundle = getattr(self_instance, '_context', None)

            if context_bundle is None and hasattr(self_instance, 'get_context'):
                context_bundle = self_instance.get_context()

            if context_bundle is not None:
                checker = context_bundle.checker
            else:
                cls_name = self_instance.__class__.__name__
                checker = getattr(
                    self_instance, '_checker',
                    getattr(self_instance, f'_{cls_name}_checker', None)
                )

            if checker is None:
                raise_error(
                    fallback_context='mcheck::decorator(...)',
                    fallback_msg=f'the class {self_instance.__class__.__name__} must provide a checker to use the @mcheck decorator',
                    exc_context='mcheck::decorator(...)',
                    exc_message=None,
                    exc_class=ATSRuntimeError
                )

            context = f"{self_instance.__class__.__name__.lower()}::{func.__name__}"
            validate_args(func, args, kwargs, specs, checker, context)

            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator


def fcheck[F: Callable[..., object]](specs: Parameters, checker: IChecker | None = None) -> Callable[[F], F]:
    '''
        Decorator supporting free functions.
        Uses a default Checker to validate function parameters.
        Mechanism for parameters checking in functions only.

        :param specs: The specification for parameters.
        :param checker: The checker instance to validate with.
        :return: The wrapped function.
        :exceptions:
            | ATSTypeError:  The parameter type validation failed.
            | ATSValueError: The parameter format validation failed.
    '''
    validate_specs(specs, 'fcheck(...)')

    active_checker: IChecker = checker or Checker(CheckerBundleFactory.create_bundle())

    def decorator(func: F) -> F:

        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            validate_args(func, args, kwargs, specs, active_checker, func.__name__)

            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator
