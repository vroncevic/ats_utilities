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
    Defines abstract class IFormatValidator with attribute(s) and method(s).
    Creates an interface for validating parameters for method(s) and function(s).
'''

from abc import ABC, abstractmethod
from typing import List, Tuple

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IFormatValidator(ABC):
    '''
        Defines abstract class IFormatValidator with attribute(s) and method(s).
        Creates an interface for validating parameters for method(s) and function(s).

        It defines:

            :attributes: None
            :methods:
                | is_valid - Checks if the string follows the expected format.
                | split - Splits the format string into components.
    '''

    @abstractmethod
    def is_valid(self, exp_type: str) -> bool:
        '''
            Checks if the string follows the expected format.

            :param exp_type: The expected format string to validate
            :type exp_type: <str>
            :return: True if the format is valid, False otherwise
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('is_valid method must be implemented by subclasses')

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
        raise NotImplementedError('split method must be implemented by subclasses')
