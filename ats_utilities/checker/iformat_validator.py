# -*- coding: UTF-8 -*-

'''
Module
    iformat_validator.py
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
    Defines abstract class IATSFormatValidator with attribute(s) and method(s).
    Creates an interface for validating parameters for method(s) and function(s).
'''

from abc import ABC, abstractmethod
from typing import List, Tuple

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IATSFormatValidator(ABC):
    '''
        Defines abstract class IATSFormatValidator with attribute(s) and method(s).
        Creates an interface for validating parameters for method(s) and function(s).

        It defines:

            :attributes: None
            :methods:
                | is_valid - Checks if the string follows the expected format.
                | split - Splits the format string into components.
                | __str__ - Returns a human-readable string representation of the validator.
    '''

    @abstractmethod
    def is_valid(self, exp_type: str) -> bool:
        '''
            Checks if the string follows the expected format.

            :param exp_type: The expected format string to validate
            :type exp_type: <str>
            :return: True (success), False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_valid() must be implemented.")

    @abstractmethod
    def split(self, exp_type: str) -> Tuple[str, str]:
        '''
            Splits the format string into components.

            :param exp_type: The format string to split
            :type exp_type: <str>
            :return: A tuple containing the split components
            :rtype: <Tuple[str, str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method split() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns a human-readable string representation of the validator.

            :return: String representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
