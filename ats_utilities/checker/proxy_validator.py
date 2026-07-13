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
    Defines vcheck decorator for checking method parameters.
    Utility for parameter validation borrowing Checker from class instances.
'''

from __future__ import annotations

from collections.abc import Callable
import inspect
from functools import wraps
from typing import Any, cast

from ats_utilities.checker.ichecker import ParametersSpecs
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.factory_context_error import raise_context_error

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

def proxy_validator_split(exp_type: str) -> tuple[str, str]:
    '''
        Splits the format string into type and name parts.

        :param exp_type: The format string to split.
        :type exp_type: <str>
        :return: A tuple containing the split components.
        :rtype: <tuple[str, str]>
        :exceptions: None.
    '''
    parts = exp_type.split(sep=':')

    return parts[0], parts[1]

def vcheck[F: Callable[..., Any]](specs: list[tuple[str, Any]]) -> Callable[[F], F]:
    '''
        Decorator supporting class methods (instance methods, classmethods).
        Borrows the checker object dynamically from the class instance 
        to validate method parameters.

        :param specs: Specification for parameters.
        :type specs: <list[tuple[str, Any]]>
        :return: Wrapped function.
        :rtype: <Callable[[F], F]>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | ATSValueError: Parameter format validation failed.
            | ATSRuntimeError: Decorator used on a non-class method.
            | ATSAttributeError: Class does not provide a '_checker' object.
    '''
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Capturing the class instance (self is always the first argument in args)
            self_instance = args[0] if args else None

            if self_instance is None:
                raise_context_error(
                    fallback_prefix='vcheck::decorator',
                    fallback_msg=f'Decorator @vcheck on {func.__name__} can only be used on class methods',
                    exc_message=None,
                    exception_class=ATSRuntimeError,
                    depth=3
                )

            cls_name: str = self_instance.__class__.__name__

            # BORROWING: Extracting the checker object that the class is responsible for.
            # Supports protected '_checker' or name-mangled private '_checker' attributes.
            checker = getattr(
                self_instance, '_checker',
                getattr(self_instance, f'_{cls_name}_checker', None)
            )

            if checker is None:
                raise_context_error(
                    fallback_prefix='vcheck::decorator',
                    fallback_msg=f'Class {cls_name} must have _checker attribute to use @vcheck decorator',
                    exc_message=None,
                    exception_class=ATSAttributeError,
                    depth=3
                )

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

            # FORWARDING: Process parameter validation via the borrowed checker instance
            if runtime_parameters:
                report_message, error_id = checker.validates_parameters(runtime_parameters)

                if error_id != checker.ERRORS.NO_ERROR:
                    if error_id == checker.ERRORS.TYPE_ERROR:
                        raise_context_error(
                            fallback_prefix=r'vcheck::decorator',
                            fallback_msg=f'Type error: {report_message}',
                            exc_message=None,
                            exception_class=ATSTypeError,
                            depth=3
                        )
                    
                    else:
                        raise_context_error(
                            fallback_prefix=r'vcheck::decorator',
                            fallback_msg=f'Format error: {report_message}',
                            exc_message=None,
                            exception_class=ATSValueError,
                            depth=3
                        )

            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator
