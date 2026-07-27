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
    Defines class TypeValidator with attribute(s) and method(s).
    Provides an API for validation parameters used by method(s) and function(s).
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
        Defines class TypeValidator with attribute(s) and method(s).
        Provides an API for validation parameters used by method(s) and function(s).

        It defines:

            :attributes:
                | _DEFAULT_TYPES - Mapping of abstract type names to their implementations.
                | _abstract_types - Mapping of abstract type names to their implementations.
            :methods:
                | __init__ - Initializes type validator.
                | is_match - Compares instance type with expected type name.
                | is_subtype - Checks if instance is a subtype of expected type name.
                | get_type_name - Returns type name representation of an instance type.
                | __str__ - Returns type validator as string representation.
    '''

    _DEFAULT_TYPES: Final[Mapping[str, type]] = MappingProxyType({
        'Mapping': Mapping,
        'Sequence': Sequence,
        'Iterable': Iterable,
    })
    _abstract_types: Mapping[str, type]

    def __init__(self, abstract_types: Mapping[str, type] | None = None) -> None:
        '''
            Initializes type validator.

            :param abstract_types: Mapping of abstract type names to their implementations.
            :exceptions:
                | ATSTypeError:  Abstract types must be a mapping of names to types.
                | ATSValueError: Abstract types must not be empty.
        '''
        if abstract_types is not None:
            ctx: str = 'type_validator::init(...)'
            istype(abstract_types, Mapping, ctx, 'abstract types must be a mapping of names to types')
            not_empty(abstract_types, ctx, 'abstract types must not be empty (names to types)')
            self._abstract_types = MappingProxyType(abstract_types)
        else:
            self._abstract_types = self._DEFAULT_TYPES

    def is_match(self, instance: object, expected_type_name: str) -> bool:
        '''
            Compares instance type with expected type name.
            Compares __name__ of instance type with expected string.

            :param instance: The instance whose type is to be checked.
            :param expected_type_name: The expected type name.
            :return: The result of the comparison.
            :exceptions:
                | ATSValueError: Instance must be provided.
                | ATSValueError: Expected type name must be provided.
                | ATSTypeError:  Expected type name must be a string.
        '''
        ctx: str = 'type_validator::is_match(...)'
        not_none(instance, ctx, 'instance must be provided')
        not_none(expected_type_name, ctx, 'expected type name must be provided')
        istype(expected_type_name, str, ctx, 'expected type name must be a string')
        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._abstract_types:
            return isinstance(instance, self._abstract_types[base_type_name])

        return type(instance).__name__ == base_type_name

    def is_subtype(self, instance: object, expected_type_name: str) -> bool:
        '''
            Checks if instance is a subtype of expected type name.
            Traverses the Method Resolution Order (MRO) to find a match.

            :param instance: The instance whose type is to be checked.
            :param expected_type_name: The expected parent type name.
            :return: The result of the comparison.
            :exceptions:
                | ATSValueError: Instance must be provided.
                | ATSValueError: Expected type name must be provided.
                | ATSTypeError:  Expected type name must be a string.
        '''
        ctx: str = 'type_validator::is_subtype(...)'
        not_none(instance, ctx, 'instance must be provided')
        not_none(expected_type_name, ctx, 'expected type name must be provided')
        istype(expected_type_name, str, ctx, 'expected type name must be a string')
        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._abstract_types:
            return isinstance(instance, self._abstract_types[base_type_name])

        return any(cls.__name__ == base_type_name for cls in type(instance).mro())

    def get_type_name(self, instance: object) -> str:
        '''
            Returns type name representation of an instance type.

            :param instance: The instance to inspect.
            :return: The type name of the instance.
            :exceptions:
                | ATSValueError: Instance must be provided.
        '''
        ctx: str = 'type_validator::get_type_name(...)'
        not_none(instance, ctx, 'instance must be provided')

        return type(instance).__name__

    def __str__(self) -> str:
        '''
            Returns type validator as string representation.

            :return: Type validator as string representation.
            :exceptions: None.
        '''
        return to_str(self)
