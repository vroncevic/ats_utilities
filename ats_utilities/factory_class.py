# -*- coding: UTF-8 -*-

'''
Module
    factory_class.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Factory universally injects instances, gets private instances and setup instance string representation.
    Encapsulates core utilities to minimize constructor overhead.
    Provides a simple factory mechanism for dependency injection.
'''

from __future__ import annotations

from typing import Any
from collections.abc import Callable
from functools import wraps

from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.factory_context_error import raise_context_error

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

def inject(instance: Any, *dependencies: tuple[str, Any, Any, str | list[str] | tuple[str, ...] | None]) -> None:
    '''
        Universally injects system or domain components into a class instance.
        Adheres to SOLID principles by avoiding hardcoded component names or classes.
        Dynamically handles multi-dependency relationship chains between sequence steps.

        :param instance: The object instance (self) to inject attributes into.
        :type instance: <Any>
        :param dependencies: Variadic sequence of tuples containing injection rules.
                             Format: ('attr_name', value, fallback, 'depends_on_attr')
                             The 'depends_on_attr' can be a string, list, or tuple.
        :type dependencies: <tuple[str, Any, Any, str | list[str] | tuple[str, ...] | None]>
        :exceptions: None.
    '''
    prefix: str = '_'

    for tuple_data in dependencies:
        attr_name: str = tuple_data[0]
        passed_val: Any = tuple_data[1]
        fallback: Any = tuple_data[2]
        depends_on: str | list[str] | tuple[str, ...] | None = tuple_data[3] if len(tuple_data) > 3 else None

        full_attr_name: str = f'{prefix}{attr_name}'

        if passed_val is not None:
            resolved_val: Any = passed_val
        else:
            if isinstance(fallback, type):
                if depends_on:

                    if isinstance(depends_on, str):
                        dep_list: list[str] = [depends_on]
                    else:
                        dep_list = list(depends_on)

                    factory_kwargs: dict[str, Any] = {}

                    for dep in dep_list:
                        target_dep_name: str = f'{prefix}{dep}'
                        dependency_obj: Any = instance.__dict__.get(target_dep_name)

                        if dependency_obj is not None:
                            factory_kwargs[dep] = dependency_obj

                    resolved_val = fallback(**factory_kwargs)
                else:
                    resolved_val = fallback()
            else:
                resolved_val = fallback

        setattr(instance, full_attr_name, resolved_val)

def get_pvt(instance: Any, attr_name: str) -> Any:
    '''
        Dynamically retrieves a private attribute from an instance.

        :param instance: The class instance (self) containing the attribute.
        :type instance: <Any>
        :param attr_name: The target private attribute name (e.g., '_checker').
        :type attr_name: <str>
        :return: The resolved attribute value.
        :rtype: <Any>
        :exceptions:
            | AttributeError: Attribute must start with '_' prefix.
    '''
    name = attr_name if attr_name.startswith('_') else f'_{attr_name}'

    return getattr(instance, name)

def has_attrs(*attr_names: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    '''
        Checks if instance attribute is defined and has value or not.
        In case attribute value is not defined set default value to None.
        In case attribute value is not defined and not empty, raise ATSValueError exception.

        :param attr_names: Tuple of attribute names to check.
        :type attr_names: <tuple[str, ...]>
        :return: Decorated function.
        :rtype: <Callable[..., Any]>
        :exceptions:
            | ATSValueError: Missing or empty attribute: '{attr}'.
    '''
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            class_name: str = self.__class__.__name__.lower()
            method_name: str = func.__name__
            context: str = f'{class_name}::{method_name}'

            for attr in attr_names:
                value: Any = getattr(self, attr, None)

                if not bool(value) and value != 0 and value != False:
                    raise_context_error(
                        fallback_prefix=context,
                        fallback_msg=f'missing or empty attribute {attr}',
                        exc_message_path=None,
                        exception_class=ATSValueError
                    )

            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def cls_name(instance: Any) -> str:
    '''
        Returns the class name of an instance.

        :param instance: The class instance.
        :type instance: <Any>
        :return: The class name in string format.
        :rtype: <str>
        :exceptions: None.
    '''
    return instance.__class__.__name__

def to_str(instance: Any) -> str:
    '''
        Generates a standardized string representation for any class instance.
        Cleans private attributes and appends memory addresses in hex.

        :param instance: The class instance to format.
        :type instance: <Any>
        :return: String representation of the instance.
        :rtype: <str>
        :exceptions: None.
    '''
    class_name: str = instance.__class__.__name__

    formatted_lines: list[str] = []
    for k, v in instance.__dict__.items():
        clean_key: str = k[1:] if k.startswith('_') and not k.startswith('__') else k
        val_str: str = str(v).replace('\n', '\n    ')

        v_id_hex = f'0x{id(v):x}'

        if f'at {v_id_hex}' not in val_str:
            if isinstance(v, (str, int, float, bool)):
                val_str = f"'{val_str}' at {v_id_hex}" if isinstance(v, str) else f"{val_str} at {v_id_hex}"
            else:
                val_str = f"{val_str} at {v_id_hex}"

        formatted_lines.append(f'    {clean_key}={val_str}')

    formatted_attrs = ',\n'.join(formatted_lines)

    if not formatted_attrs:
        return f'{class_name} at 0x{id(instance):x}'

    return f'{class_name}(\n{formatted_attrs}\n) at 0x{id(instance):x}'
