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
    Defines validator decorator for checking method parameters.
    Utility for parameter validation borrowing Checker from class instances.
'''

import inspect
from functools import wraps
from typing import Any, Callable, List, Tuple, TypeVar, cast
from ats_utilities.checker.ichecker import ParametersSpecs
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Allows decorator to remember signature wrapped method/function
F = TypeVar('F', bound=Callable[..., Any])


def proxy_validator_split(exp_type: str) -> Tuple[str, str]:
    '''
        Splits the format string into type and name parts.

        :param exp_type: The format string to split.
        :type exp_type: <str>
        :return: A tuple containing the split components.
        :rtype: <Tuple[str, str]>
        :exceptions: None.
    '''
    parts = exp_type.split(sep=':')
    return parts[0], parts[1]


def validator(specs: List[Tuple[str, Any]]) -> Callable[[F], F]:
    '''
        Decorator supporting class methods (instance methods, classmethods).
        Borrows the checker object dynamically from the class instance 
        to validate method parameters.

        :param specs: Specification for parameters.
        :type specs: <List[Tuple[str, Any]]>
        :return: Wrapped function.
        :rtype: <Callable[[F], F]>
        :exceptions: ATSTypeError, ATSValueError, RuntimeError, AttributeError.
    '''
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Capturing the class instance (self is always the first argument in args)
            self_instance = args[0] if args else None

            if not self_instance:
                raise RuntimeError(
                    f"Decorator @validator on '{func.__name__}' "
                    f"can only be used on class methods."
                )

            # BORROWING: Extracting the checker object that the class is responsible for.
            # Supports protected '_checker' or name-mangled private '__checker' attributes.
            checker = getattr(
                self_instance, '_checker',
                getattr(self_instance, f'_{self_instance.__class__.__name__}__checker', None)
            )

            if checker is None:
                raise AttributeError(
                    f"Class '{self_instance.__class__.__name__}' is required to provide "
                    f"a '_checker' object to use the @validator decorator."
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

                    # We check if the type is declared as Optional
                    is_optional = raw_type.startswith("Optional[") and raw_type.endswith("]")

                    if is_optional:
                        # We highlight the internal type, e.g. "Optional[str]" -> "str"
                        target_type = raw_type[9:-1]

                        # If the value is None, it is valid for Optional and we skip the check
                        if actual_value is None:
                            continue
                    else:
                        target_type = raw_type

                        # If it is NOT optional and the value is None, it is immediately a type error
                        if actual_value is None:
                            runtime_parameters.append((f"{target_type}:{pname}", actual_value))
                            continue

                    # We form a cleaned specification string for Checker (eg "str:version")
                    clean_exp_type = f"{target_type}:{pname}"
                    runtime_parameters.append((clean_exp_type, actual_value))

            # FORWARDING: Process parameter validation via the borrowed checker instance
            if runtime_parameters:
                report_message, error_id = checker.validates_parameters(runtime_parameters)

                if error_id != checker.ERRORS.NO_ERROR:
                    if error_id == checker.ERRORS.TYPE_ERROR:
                        raise ATSTypeError(report_message)
                    elif error_id == checker.ERRORS.FORMAT_ERROR:
                        raise ATSValueError(report_message)

            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator
