# -*- coding: UTF-8 -*-

'''
Module
    type_validator.py
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
    Defines class TypeValidator with attribute(s) and method(s).
    Creates an API for handling type validation parameters of method(s) and function(s).
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence, Iterable
from types import MappingProxyType
from typing import Any, Final, override

from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TypeValidator(ITypeValidator):
    '''
        Defines class TypeValidator with attribute(s) and method(s).
        Creates an API for handling type validation parameters of method(s) and function(s).

        It defines:

            :attributes:
                | _ABSTRACT_TYPES - Mapping of abstract type names to their implementations.
                | _abstract_types - Mapping of abstract type names to their implementations.
            :methods:
                | __init__ - Initializes TypeValidator constructor.
                | is_match - Compares instance type with expected type name.
                | is_subtype - Checks if instance is a subtype of expected type name.
                | get_type_name - Returns the string representation of an instance type.
                | __str__ - Returns the type validator as string representation.
    '''

    _ABSTRACT_TYPES: Final[Mapping[str, type]] = MappingProxyType({
        'Mapping': Mapping,
        'Sequence': Sequence,
        'Iterable': Iterable,
    })
    _abstract_types: Mapping[str, type]

    def __init__(self, abstract_types: Mapping[str, type] | None = None) -> None:
        '''
            Initializes TypeValidator constructor.

            :param abstract_types: Mapping of abstract type names to their implementations.
            :type abstract_types: <Mapping[str, type] | None>
            :exceptions:
                | ATSTypeError: Abstract types must be a Mapping.
        '''
        if abstract_types is not None:
            ctx: str = r'type_validator::init(...)'
            istype(abstract_types, Mapping, ctx, r'abstract types must be a Mapping[str, Any]')
            self._abstract_types = MappingProxyType(abstract_types)
        else:
            self._abstract_types = self._ABSTRACT_TYPES

    @override
    def is_match(self, instance: Any, expected_type_name: str) -> bool:
        '''
            Compares instance type with expected type name.
            Compares the __name__ of the instance type with expected string.

            :param instance: The instance to be checked.
            :type instance: Any
            :param expected_type_name: The expected type name.
            :type expected_type_name: str
            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions:
                | ATSValueError: Instance must be provided.
                | ATSValueError: Expected type name must be provided.
                | ATSTypeError: Expected type name must be a string.
        '''
        ctx: str = r'type_validator::is_match(...)'
        not_none(instance, ctx, r'instance must be provided')
        not_none(expected_type_name, ctx, r'expected type name must be provided')
        istype(expected_type_name, str, ctx, r'expected type name must be a string')
        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._abstract_types:
            return isinstance(instance, self._abstract_types[base_type_name])

        return any(cls.__name__ == base_type_name for cls in type(instance).mro())

    @override
    def is_subtype(self, instance: Any, expected_type_name: str) -> bool:
        '''
            Checks if instance is a subtype of expected type name.
            Traverses the Method Resolution Order (MRO) to find a match.

            :param instance: The instance to be checked.
            :type instance: Any
            :param expected_type_name: The expected parent type name.
            :type expected_type_name: str
            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions:
                | ATSValueError: Instance must be provided.
                | ATSValueError: Expected type name must be provided.
                | ATSTypeError: Expected type name must be a string.
        '''
        ctx: str = r'type_validator::is_subtype(...)'
        not_none(instance, ctx, r'instance must be provided')
        not_none(expected_type_name, ctx, r'expected type name must be provided')
        istype(expected_type_name, str, ctx, r'expected type name must be a string')
        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._abstract_types:
            return isinstance(instance, self._abstract_types[base_type_name])

        return any(cls.__name__ == base_type_name for cls in type(instance).mro())

    @override
    def get_type_name(self, instance: Any) -> str:
        '''
            Returns the string representation of an instance type.

            :param instance: The instance to be inspected.
            :type instance: Any
            :return: String name of the type.
            :rtype: str
            :exceptions:
                | ATSValueError: Instance must be provided.
        '''
        ctx: str = r'type_validator::get_type_name(...)'
        not_none(instance, ctx, r'instance must be provided')

        return type(instance).__name__

    @override
    def __str__(self) -> str:
        '''
            Returns the type validator as string representation.

            :return: The type validator as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
