# -*- coding: UTF-8 -*-

'''
Module
    reflection.py
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

from collections.abc import Callable
from functools import wraps
from dataclasses import is_dataclass

from ats_utilities.validation.check_value import not_none, not_satisfied
from ats_utilities.validation.context_error import raise_error

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def get_pvt(instance: object, attr_name: str) -> object:
    '''
        Dynamically retrieves a private attribute from an.

        :param instance: The class instance (self) containing the attribute.
        :param attr_name: The target private attribute name (e.g., '_checker').
        :return: The resolved attribute value.
        :exceptions:
            | AttributeError: Attribute must start with '_' prefix.
    '''
    name = attr_name if attr_name.startswith('_') else f'_{attr_name}'

    return getattr(instance, name)


def has_attrs(*attr_names: str) -> Callable[[Callable[..., object]], Callable[..., object]]:
    '''
        Checks if instance attribute is defined and has value or not.
        In case attribute value is not defined set default value to None.
        In case attribute value is not defined and not empty, raise ATSValueError exception.

        :param attr_names: The tuple of attribute names to check.
        :return: The decorated function.
        :exceptions:
            | ATSValueError: Missing or empty attribute: '{attr}'.
    '''
    def decorator(func: Callable[..., object]) -> Callable[..., object]:
        @wraps(func)
        def wrapper(self: object, *args: object, **kwargs: object) -> object:
            class_name: str = self.__class__.__name__.lower()
            method_name: str = func.__name__
            context: str = f'{class_name}::{method_name}'

            for attr in attr_names:
                value: object | None = getattr(self, attr, None)

                if not bool(value) and value != 0 and value != False:
                    raise_error(
                        fallback_context=context,
                        fallback_msg=f'missing or empty attribute {attr}',
                        exc_context=context,
                        exc_message=None
                    )

            return func(self, *args, **kwargs)
        return wrapper
    return decorator


def cls_name(instance: object) -> str:
    '''
        Returns the class name of an.

        :param instance: The class.
        :return: The class name in string format.
        :exceptions: None.
    '''
    return instance.__class__.__name__


def to_str(instance: object) -> str:
    '''
        Generates a standardized string representation for any class.
        Cleans private attributes and appends memory addresses in hex.

        :param instance: The class instance to format.
        :return: The string representation of the.
        :exceptions: None.
    '''
    class_name: str = instance.__class__.__name__

    formatted_lines: list[str] = []
    for k, v in instance.__dict__.items():
        clean_key: str = k[1:] if k.startswith('_') and not k.startswith('__') else k
        val_str: str = str(v).replace('\n', '\n    ')

        v_id_hex: str = f'0x{id(v):x}'

        if f'at {v_id_hex}' not in val_str:
            val_str = f'{val_str} at {v_id_hex}'

        formatted_lines.append(f'    {clean_key}={val_str}')

    formatted_attrs: str = ',\n'.join(formatted_lines)

    if not formatted_attrs:
        return f'{class_name} at 0x{id(instance):x}'

    return f'{class_name}(\n{formatted_attrs}\n) at 0x{id(instance):x}'


def instance_to_dict(instance: object) -> dict[str, object]:
    '''
        Converts a dataclass instance to a dictionary representation.

        :param instance: The dataclass.
        :return: The dictionary representation of the dataclass.
        :exceptions:
            | ATSValueError: Instance must be provided.
            | ATSValueError: Instance must be a dataclass.
    '''
    ctx: str = 'reflection::instance_to_dict(...)'
    msg_instance_none: str = 'the instance must be provided'
    msg_instance_istype: str = 'the instance must be a dataclass instance'

    not_none(instance, ctx, msg_instance_none)
    not_satisfied(not is_dataclass(instance), ctx, msg_instance_istype)

    return {field: getattr(instance, field) for field in instance.__dataclass_fields__}
