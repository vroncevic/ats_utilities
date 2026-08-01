# -*- coding: UTF-8 -*-

'''
Module
    check_type.py
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
    Defines type utility functions.
'''

from __future__ import annotations

from typing import get_origin, Union
from types import UnionType

from ats_utilities.validation.context_error import raise_error
from ats_utilities.exceptions import ATSTypeError

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def _resolve_type(type_to_resolve: object) -> object:
    '''
        Resolves nested Union types.
        Handles cases like Union[int, float] by flattening them 
        into a tuple of concrete types (int, float).

        :param type_to_resolve: The type to resolve.
        :return: The resolved type.
        :exceptions: None.
    '''
    origin = get_origin(type_to_resolve)

    if origin in (Union, UnionType):
        args = getattr(type_to_resolve, '__args__', ())
        resolved_args = []

        for arg in args:
            res = _resolve_type(arg)

            if isinstance(res, tuple):
                resolved_args.extend(res)
            else:
                resolved_args.append(res)

        return tuple(resolved_args)

    is_typed_dict: bool = (
        isinstance(type_to_resolve, type) and
        issubclass(type_to_resolve, dict) and
        hasattr(type_to_resolve, '__total__')
    )

    if is_typed_dict:
        return dict

    return origin or type_to_resolve


def istype(
    instance: object,
    class_or_tuple: type | UnionType | tuple[type | UnionType, ...],
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSTypeError
) -> None:
    '''
        Checks if an instance is of a specified type.

        :param instance: The instance to check.
        :param class_or_tuple: The type or tuple of types to check against.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if instance is not of the specified type.
        :exceptions:
            | Dynamically raises the provided exc_class (e.g., ATSTypeError).
    '''
    if isinstance(class_or_tuple, tuple):
        check_types = []

        for type_to_check in class_or_tuple:
            res = _resolve_type(type_to_check)

            if isinstance(res, tuple):
                check_types.extend(res)
            else:
                check_types.append(res)

        check_types = tuple(check_types)

    else:
        check_types = _resolve_type(class_or_tuple)

    if not isinstance(instance, check_types):
        raise_error(
            fallback_context='check_type::istype(...)',
            fallback_msg=f'the expected {class_or_tuple} for instance, got {type(instance).__name__}',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )
