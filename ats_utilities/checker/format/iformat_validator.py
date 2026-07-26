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
    Defines abstract class IFormatValidator with method(s).
    Provides an interface for validating parameters used by method(s) and function(s).
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IFormatValidator[SeparatorType, FormatType, SplitType, ValidType](Protocol):
    '''
        Defines abstract class IFormatValidator with method(s).
        Provides an interface for validating parameters used by method(s) and function(s).

        It defines:

            :methods:
                | set_separator - Sets separator used in parameter specifications.
                | get_separator - Returns separator used in parameter specifications.
                | is_valid - Checks if format follows expected format.
                | split - Splits format into parts.
                | __str__ - Returns format validator as string representation.
    '''

    def set_separator(self, separator: SeparatorType) -> None:
        '''
            Sets separator used in parameter specifications.

            :param separator: Separator used in parameter specifications.
        '''
        ...

    def get_separator(self) -> SeparatorType:
        '''
            Returns separator used in parameter specifications.

            :return: Separator used in parameter specifications.
        '''
        ...

    def is_valid(self, format_to_check: FormatType) -> ValidType:
        '''
            Checks if format follows expected format.

            :param format_to_check: Format to be validated.
            :return: Validation result.
        '''
        ...

    def split(self, format_to_split: FormatType) -> SplitType:
        '''
            Splits format into parts.

            :param format_to_split: Format to be split.
            :return: Split format parts.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns format validator as string representation.

            :return: Format validator as string representation.
        '''
        ...
