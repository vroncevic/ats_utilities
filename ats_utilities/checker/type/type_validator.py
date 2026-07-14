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
    Creates an API for handling type validation parameters for method(s) and function(s).
'''

from __future__ import annotations

from typing import Any, override
from collections.abc import Mapping, Sequence, Iterable

from ats_utilities.factory_class import to_str
from ats_utilities.checker.type.itype_validator import ITypeValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TypeValidator(ITypeValidator):
    '''
        Defines class TypeValidator with attribute(s) and method(s).
        Creates an API for type validation between instances and type names.
        Mechanism for validating function or method parameters (type).

        It defines:

            :attributes:
                | _ABSTRACT_TYPES - Mapping of abstract type names to their implementations.
            :methods:
                | is_match - Compares instance type with expected type name.
                | is_subtype - Checks if instance is a subtype of expected type name.
                | get_type_name - Returns the string representation of an instance type.
                | __str__ - Returns the ATS type vcheck as string representation.
    '''

    _ABSTRACT_TYPES: dict[str, type] = {
        'Mapping': Mapping,
        'Sequence': Sequence,
        'Iterable': Iterable,
    }

    @override
    def is_match(self, inst: Any, expected_type_name: str) -> bool:
        '''
            Compares instance type with expected type name.
            Compares the __name__ of the instance type with expected string.

            :param inst: The instance to check.
            :type inst: <Any>
            :param expected_type_name: The expected type name.
            :type expected_type_name: <str>
            :return: True (success), False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._ABSTRACT_TYPES:
            return isinstance(inst, self._ABSTRACT_TYPES[base_type_name])

        return any(cls.__name__ == base_type_name for cls in type(inst).mro())

    @override
    def is_subtype(self, inst: Any, expected_type_name: str) -> bool:
        '''
            Checks if instance is a subtype of expected type name.
            Traverses the Method Resolution Order (MRO) to find a match.

            :param inst: The instance to check.
            :type inst: <Any>
            :param expected_type_name: The expected parent type name.
            :type expected_type_name: <str>
            :return: True (is), False (not).
            :rtype: <bool>
            :exceptions: None.
        '''
        base_type_name = expected_type_name.split('[')[0]

        if base_type_name in self._ABSTRACT_TYPES:
            return isinstance(inst, self._ABSTRACT_TYPES[base_type_name])

        return any(cls.__name__ == base_type_name for cls in type(inst).mro())

    @override
    def get_type_name(self, inst: Any) -> str:
        '''
            Returns the string representation of an instance type.

            :param inst: The instance to inspect.
            :type inst: <Any>
            :return: String name of the type.
            :rtype: <str>
            :exceptions: None.
        '''
        return type(inst).__name__

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS type vcheck as string representation.

            :return: The ATS type vcheck as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
