# -*- coding: UTF-8 -*-

'''
Module
    itype_validator.py
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
    Defines abstract class ITypeValidator with method(s).
    Provides an interface for validating parameters used by method(s) and function(s).
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable
from typing import Any

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class ITypeValidator[NameType, ValidType](Protocol):
    '''
        Defines abstract class ITypeValidator with method(s).
        Provides an interface for validating parameters used by method(s) and function(s).

        It defines:

            :methods:
                | is_match - Compares instance type with expected type name.
                | is_subtype - Checks if instance is a subtype of expected type name.
                | get_type_name - Returns type name representation of an instance type.
                | __str__ - Returns type validator as string representation.
    '''

    def is_match(self, instance: Any, expected_type_name: NameType) -> ValidType:
        '''
            Compares instance type with expected type name.

            :param instance: The instance whose type is to be checked.
            :param expected_type_name: The expected type name.
            :return: The result of the comparison.
        '''
        ...

    def is_subtype(self, instance: Any, expected_type_name: NameType) -> ValidType:
        '''
            Checks if instance is a subtype of expected type name.

            :param instance: The instance whose type is to be checked.
            :param expected_type_name: The expected parent type name.
            :return: The result of the comparison.
        '''
        ...

    def get_type_name(self, instance: Any) -> NameType:
        '''
            Returns type name of an instance.

            :param instance: The instance to inspect.
            :return: The type name of the instance.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns type validator as string representation.

            :return: Type validator as string representation.
        '''
        ...
