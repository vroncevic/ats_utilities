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
    Defines abstract class IATSTypeValidator with attribute(s) and method(s).
    Creates an interface for validating parameters for method(s) and function(s).
'''

from abc import ABC, abstractmethod
from typing import Any, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IATSTypeValidator(ABC):
    '''
        Defines abstract class IATSTypeValidator with attribute(s) and method(s).
        Creates an interface for validating parameters for method(s) and function(s).

        It defines:

            :attributes: None
            :methods:
                | is_match - Compares instance type with expected type name.
                | is_subtype - Checks if instance is a subtype of expected type name.
                | get_type_name - Returns the string representation of an instance type.
    '''

    @abstractmethod
    def is_match(self, inst: Any, expected_type_name: str) -> bool:
        '''
            Compares instance type with expected type name.

            :param inst: The instance to check
            :type inst: <Any>
            :param expected_type_name: The expected type name
            :type expected_type_name: <str>
            :return: True if the types match, False otherwise
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_match() must be implemented.")

    @abstractmethod
    def is_subtype(self, inst: Any, expected_type_name: str) -> bool:
        '''
            Checks if instance is a subtype of expected type name.

            :param inst: The instance to check
            :type inst: <Any>
            :param expected_type_name: The expected parent type name
            :type expected_type_name: <str>
            :return: True if inst is a subtype, False otherwise
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_subtype() must be implemented.")

    @abstractmethod
    def get_type_name(self, inst: Any) -> str:
        '''
            Returns the string representation of an instance type.

            :param inst: The instance to inspect
            :type inst: <Any>
            :return: String name of the type
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method get_type_name() must be implemented.")
