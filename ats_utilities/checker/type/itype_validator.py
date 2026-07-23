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
    Creates an interface for validating parameters for method(s) and function(s).
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ITypeValidator(ABC):
    '''
        Defines abstract class ITypeValidator with method(s).
        Creates an interface for validating parameters for method(s) and function(s).

        It defines:

            :methods:
                | is_match - Compares instance type with expected type name.
                | is_subtype - Checks if instance is a subtype of expected type name.
                | get_type_name - Returns the string representation of an instance type.
                | __str__ - Returns the mcheck as string representation.
    '''

    @abstractmethod
    def is_match(self, instance: Any, expected_type_name: str) -> bool:
        '''
            Compares instance type with expected type name.

            :param instance: The instance to check.
            :type instance: Any
            :param expected_type_name: The expected type name.
            :type expected_type_name: str
            :return: <True> successfully, <False> otherwise.
            :rtype: bool
            :exceptions:
                | ATSTypeError: Expected type name must be a string.
        '''
        pass

    @abstractmethod
    def is_subtype(self, instance: Any, expected_type_name: str) -> bool:
        '''
            Checks if instance is a subtype of expected type name.

            :param instance: The instance to check.
            :type instance: Any
            :param expected_type_name: The expected parent type name.
            :type expected_type_name: str
            :return: <True> successfully, <False> otherwise.
            :rtype: bool
            :exceptions:
                | ATSTypeError: Expected type name must be a string.
        '''
        pass

    @abstractmethod
    def get_type_name(self, instance: Any) -> str:
        '''
            Returns the string representation of an instance type.

            :param instance: The instance to inspect.
            :type instance: Any
            :return: String name of the type.
            :rtype: str
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the mcheck as string representation.

            :return: The mcheck as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
