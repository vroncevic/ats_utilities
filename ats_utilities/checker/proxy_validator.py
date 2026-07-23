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

from collections.abc import Callable
import inspect
from functools import wraps
from typing import Any, cast

from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.ichecker import IChecker, ParametersSpecs
from ats_utilities.exceptions import (
    ATSRuntimeError, ATSTypeError, ATSValueError
)
from ats_utilities.validation.context_error import raise_error

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def proxy_validator_split(exp_type: str) -> tuple[str, str]:
    '''
        Splits the format string into type and name parts.

        :param exp_type: The format string to split.
        :type exp_type: str
        :return: A tuple containing the split components.
        :rtype: <tuple[str, str]>
        :exceptions:
            | ATSValueError: Parameter format validation failed.
    '''
    parts = exp_type.split(sep=':')

    if len(parts) != 2:
        raise_error(
            fallback_context=r'proxy_validator_split(...)',
            fallback_msg=f'Invalid parameter format: {exp_type}',
            exc_context=r'proxy_validator_split(...)',
            exc_message=None,
            exc_class=ATSValueError
        )

    return parts[0], parts[1]


def validate_args(
    func: Callable[..., Any],
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    specs: list[tuple[str, Any]],
    checker: IChecker,
    exc_context: str
) -> None:
    '''
        Validates argument values against parameter specification.

        :param func: Decorated function.
        :type func: Callable[..., Any]
        :param args: Position arguments passed.
        :type args: tuple[Any, ...]
        :param kwargs: Keyword arguments passed.
        :type kwargs: dict[str, Any]
        :param specs: Parameter specification list.
        :type specs: <list[tuple[str, Any]]>
        :param checker: Checker instance to validate with.
        :type checker: <IChecker>
        :param exc_context: Exception context.
        :type exc_context: str
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | ATSValueError: Parameter format validation failed.
    '''
    # Safely bind the passed args and kwargs to the function's signature
    func_signature = inspect.signature(func)
    bound_arguments = func_signature.bind(*args, **kwargs)

    # Fill in empty optional parameters with their default values from definition
    bound_arguments.apply_defaults()
    actual_params_dict = bound_arguments.arguments

    runtime_parameters: ParametersSpecs = []

    # Iterate through specs and map them to actual arguments dynamically
    for exp_type, _ in specs:
        raw_type, pname = proxy_validator_split(exp_type)

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
                runtime_parameters.append((f'{target_type}:{pname}', actual_value))
                continue

            # We form a cleaned specification string for Checker (eg str:version)
            clean_exp_type = f'{target_type}:{pname}'
            runtime_parameters.append((clean_exp_type, actual_value))

    # Process parameter validation
    if runtime_parameters:
        report_message, error_id = checker.validates_parameters(runtime_parameters)

        if error_id != checker.ERRORS.NO_ERROR:
            if error_id == checker.ERRORS.TYPE_ERROR:
                raise_error(
                    fallback_context=exc_context,
                    fallback_msg=f'type error: {report_message}',
                    exc_context=exc_context,
                    exc_message=None,
                    exc_class=ATSTypeError
                )
            else:
                raise_error(
                    fallback_context=exc_context,
                    fallback_msg=f'format error: {report_message}',
                    exc_context=exc_context,
                    exc_message=None,
                    exc_class=ATSValueError
                )


def mcheck[F: Callable[..., Any]](specs: list[tuple[str, Any]]) -> Callable[[F], F]:
    '''
        Decorator supporting class methods (instance methods, classmethods).
        Borrows the checker object dynamically from the class instance 
        to validate method parameters.
        Mechanism for parameters checking in methods only.

        :param specs: Specification for parameters.
        :type specs: <list[tuple[str, Any]]>
        :return: Wrapped function.
        :rtype: <Callable[[F], F]>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | ATSValueError: Parameter format validation failed.
            | ATSRuntimeError: Decorator used on a non-class method.
            | ATSAttributeError: Class does not provide a _checker object.
    '''
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Capturing the class instance (self is always the first argument in args)
            self_instance = args[0] if args else None

            if self_instance is None:
                raise_error(
                    fallback_context=r'mcheck::decorator(...)',
                    fallback_msg=f'decorator @mcheck on {func.__name__} can only be used on class methods',
                    exc_context=r'mcheck::decorator(...)',
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
                    fallback_context=r'mcheck::decorator(...)',
                    fallback_msg=f'class {self_instance.__class__.__name__} must provide a checker to use @mcheck decorator',
                    exc_context=r'mcheck::decorator(...)',
                    exc_message=None,
                    exc_class=ATSRuntimeError
                )

            context = f"{self_instance.__class__.__name__.lower()}::{func.__name__}"
            validate_args(func, args, kwargs, specs, checker, context)

            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator


def fcheck[F: Callable[..., Any]](specs: list[tuple[str, Any]]) -> Callable[[F], F]:
    '''
        Decorator supporting free functions.
        Uses a default Checker to validate function parameters.
        Mechanism for parameters checking in functions only.

        :param specs: Specification for parameters.
        :type specs: <list[tuple[str, Any]]>
        :return: Wrapped function.
        :rtype: <Callable[[F], F]>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | ATSValueError: Parameter format validation failed.
    '''
    checker = Checker(CheckerFactory.create_default_checker_bundle())

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            validate_args(func, args, kwargs, specs, checker, func.__name__)
            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator
