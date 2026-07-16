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
    Factory universally injects instances, gets private instances
    and setup instance string representation.
    Encapsulates core utilities to minimize constructor overhead.
    Provides a simple factory mechanism for dependency injection.
'''

from __future__ import annotations

from typing import Any
from collections.abc import Callable
from functools import wraps

from ats_utilities.validation.context_error import raise_error

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


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
                    raise_error(
                        fallback_prefix=context,
                        fallback_msg=f'missing or empty attribute {attr}',
                        exc_message=None
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
                val_str = f'{val_str} at {v_id_hex}' if isinstance(v, str) else f'{val_str} at {v_id_hex}'
            else:
                val_str = f'{val_str} at {v_id_hex}'

        formatted_lines.append(f'    {clean_key}={val_str}')

    formatted_attrs = ',\n'.join(formatted_lines)

    if not formatted_attrs:
        return f'{class_name} at 0x{id(instance):x}'

    return f'{class_name}(\n{formatted_attrs}\n) at 0x{id(instance):x}'
