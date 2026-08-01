# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines the class TypeValidator with attribute(s) and method(s).
    Provides an API for validating types of parameters used by method(s) and function(s).
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence, Iterable
from types import MappingProxyType
from typing import Final

from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_empty

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TypeValidator:
    '''
        Defines the class TypeValidator with attribute(s) and method(s).
        Provides an API for validating types of parameters used by method(s) and function(s).

        It defines:

            :attributes:
                | DEFAULT_TYPES - The default mapping of abstract type names to their implementations.
                | _abstract_types - The mapping of abstract type names to their implementations.
            :methods:
                | __init__ - Initializes the type validator.
                | is_match - Checks if the type of the instance matches the expected type name.
                | is_subtype - Checks if the instance is a subtype of the expected type name.
                | get_type_name - Returns the type name of the instance.
                | __str__ - Returns the type validator as a string representation.
    '''

    DEFAULT_TYPES: Final[MappingProxyType[str, type]] = MappingProxyType({
        'Mapping': Mapping,
        'Sequence': Sequence,
        'Iterable': Iterable,
    })
    _abstract_types: Mapping[str, type]

    def __init__(self, abstract_types: Mapping[str, type] | None = None) -> None:
        '''
            Initializes the type validator.

            :param abstract_types: The mapping of abstract type names to their implementations.
            :exceptions:
                | ATSTypeError:  The abstract types must be a mapping of names to types.
                | ATSValueError: The abstract types must not be empty.
        '''
        if abstract_types is not None:
            ctx: str = 'type_validator::init(...)'
            msg_abstract_types_istype: str = 'the abstract types must be a mapping of names to types'
            msg_abstract_types_empty: str = 'the abstract types must not be empty (names to types)'

            istype(abstract_types, Mapping, ctx, msg_abstract_types_istype)
            not_empty(abstract_types, ctx, msg_abstract_types_empty)

            self._abstract_types = MappingProxyType(abstract_types)
        else:
            self._abstract_types = self.DEFAULT_TYPES

    def is_match(self, instance: object, expected_type_name: str) -> bool:
        '''
            Checks if the type of the instance matches the expected type name.
            Compares the __name__ attribute of the instance type with the expected type name.

            :param instance: The instance whose type is to be checked.
            :param expected_type_name: The expected type name.
            :return: True if the type of the instance matches the expected type name, False otherwise.
            :exceptions:
                | ATSValueError: The instance must be provided.
                | ATSValueError: The expected type name must be provided.
                | ATSTypeError:  The expected type name must be a string.
                | ATSValueError: The expected type name must not be empty.
        '''
        ctx: str = 'type_validator::is_match(...)'
        msg_instance_none: str = 'the instance must be provided'
        msg_expected_type_name_none: str = 'the expected type name must be provided'
        msg_expected_type_name_istype: str = 'the expected type name must be a string'
        msg_expected_type_name_empty: str = 'the expected type name must not be empty'

        not_none(instance, ctx, msg_instance_none)
        not_none(expected_type_name, ctx, msg_expected_type_name_none)
        istype(expected_type_name, str, ctx, msg_expected_type_name_istype)
        not_empty(expected_type_name, ctx, msg_expected_type_name_empty)

        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._abstract_types:
            return isinstance(instance, self._abstract_types[base_type_name])

        return type(instance).__name__ == base_type_name

    def is_subtype(self, instance: object, expected_type_name: str) -> bool:
        '''
            Checks if the instance is a subtype of the expected type name.
            Traverses the method resolution order (MRO) to find a match.

            :param instance: The instance whose type is to be checked.
            :param expected_type_name: The expected parent type name.
            :return: True if the instance is a subtype of the expected type name, False otherwise.
            :exceptions:
                | ATSValueError: The instance must be provided.
                | ATSValueError: The expected type name must be provided.
                | ATSTypeError:  The expected type name must be a string.
                | ATSValueError: The expected type name must not be empty.
        '''
        ctx: str = 'type_validator::is_subtype(...)'

        msg_instance_none: str = 'the instance must be provided'
        msg_expected_type_name_none: str = 'the expected type name must be provided'
        msg_expected_type_name_istype: str = 'the expected type name must be a string'
        msg_expected_type_name_empty: str = 'the expected type name must not be empty'

        not_none(instance, ctx, msg_instance_none)
        not_none(expected_type_name, ctx, msg_expected_type_name_none)
        istype(expected_type_name, str, ctx, msg_expected_type_name_istype)
        not_empty(expected_type_name, ctx, msg_expected_type_name_empty)

        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._abstract_types:
            return isinstance(instance, self._abstract_types[base_type_name])

        return any(cls.__name__ == base_type_name for cls in type(instance).mro())

    def get_type_name(self, instance: object) -> str:
        '''
            Returns the type name of the instance.

            :param instance: The instance to inspect.
            :return: The type name of the instance.
            :exceptions:
                | ATSValueError: The instance must be provided.
        '''
        ctx: str = 'type_validator::get_type_name(...)'
        not_none(instance, ctx, 'the instance must be provided')

        return type(instance).__name__

    def __str__(self) -> str:
        '''
            Returns the type validator as a string representation.

            :return: The type validator as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
