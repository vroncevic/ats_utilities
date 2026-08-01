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
    Defines the class FormatValidator with attribute(s) and method(s).
    Provides an API for validating parameters used by method(s) and function(s).
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import Final

from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_empty, not_none, not_satisfied

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class FormatValidator:
    '''
        Defines the class FormatValidator with attribute(s) and method(s).
        Provides an API for validating parameters used by method(s) and function(s).

        It defines:

            :attributes:
                | EXPECTED_FORMAT_PARTS - The expected number of parts in the format string.
                | EXPECTED_SEPARATOR - The expected separator between type and name.
            :methods:
                | __init__ - Initializes the format validator.
                | set_separator - Sets the separator used in the format specifications.
                | get_separator - Returns the separator used in the format specifications.
                | is_valid - Checks if the format follows the expected format.
                | split - Splits the format into parts.
                | __str__ - Returns the format validator as a string representation.

        Expected format (in string format):

            type:name

        where:
            type - The expected parameter type.
            name - The expected parameter name.

        Examples:
            >>> from ats_utilities.checker.format.format_validator import FormatValidator
            >>> fv = FormatValidator()
            >>> fv.is_valid('str:name')
            True
            >>> fv.split('str:name')
            ('str', 'name')
    '''

    EXPECTED_FORMAT_PARTS: Final[int] = 2
    EXPECTED_SEPARATOR: Final[str] = ':'

    def __init__(self, separator: str | None = None) -> None:
        '''
            Initializes the format validator.

            :param separator: The separator to use for splitting the format string | None.
            :exceptions:
                | ATSTypeError:  The separator must be a string.
                | ATSValueError: The separator must not be empty.
        '''
        if separator is not None:
            ctx: str = 'format_validator::init(...)'
            msg_separator_istype: str = 'the separator must be a string'
            msg_separator_empty: str = 'the separator must not be empty'

            istype(separator, str, ctx, msg_separator_istype)
            not_empty(separator, ctx, msg_separator_empty)

            self._separator = separator
        else:
            self._separator = self.EXPECTED_SEPARATOR

    def set_separator(self, separator: str) -> None:
        '''
            Sets the separator used in the format specifications.

            :param separator: The separator used in the format specifications.
            :exceptions:
                | ATSTypeError:  The separator must be a string.
                | ATSValueError: The separator must not be empty.
        '''
        ctx: str = 'format_validator::set_separator(...)'
        msg_separator_istype: str = 'the separator must be a string'
        msg_separator_empty: str = 'the separator must not be empty'

        istype(separator, str, ctx, msg_separator_istype)
        not_empty(separator, ctx, msg_separator_empty)

        self._separator = separator

    def get_separator(self) -> str:
        '''
            Returns the separator used in the format specifications.

            :return: The separator used in the format specifications.
            :exceptions: None.
        '''
        return self._separator

    def is_valid(self, format_to_check: str) -> bool:
        '''
            Checks if the format follows the expected format.

            :param format_to_check: The format to be validated.
            :return: True if successfully, otherwise False.
            :exceptions:
                | ATSValueError: The format to be validated must be provided.
                | ATSTypeError:  The format to be validated must be a string.
                | ATSValueError: The format to be validated must contain the separator.
        '''
        ctx: str = 'format_validator::is_valid(...)'
        msg_format_to_check_none: str = 'the format to be validated must be provided'
        msg_format_to_check_istype: str = 'the format to be validated must be a string'

        not_none(format_to_check, ctx, msg_format_to_check_none)
        istype(format_to_check, str, ctx, msg_format_to_check_istype)

        return len(self.split(format_to_check)) == self.EXPECTED_FORMAT_PARTS

    def split(self, format_to_split: str) -> Sequence[str]:
        '''
            Splits the format string into parts.

            :param format_to_split: The format string to split.
            :return: A Sequence containing the split components (type, name).
            :exceptions:
                | ATSValueError: The format to be validated must be provided.
                | ATSTypeError:  The format to be validated must be a string.
                | ATSValueError: The format to be validated must contain the separator.
        '''
        ctx: str = 'format_validator::split(...)'
        msg_format_to_split_none: str = 'the format to split must be provided'
        msg_format_to_split_istype: str = 'the format to split must be a string'
        msg_format_to_split_separator: str = f'the format to split must contain the separator "{self._separator}"'

        not_none(format_to_split, ctx, msg_format_to_split_none)
        istype(format_to_split, str, ctx, msg_format_to_split_istype)
        not_satisfied(self._separator not in format_to_split, ctx, msg_format_to_split_separator)

        return tuple(format_to_split.split(sep=self._separator))

    def __str__(self) -> str:
        '''
            Returns the format validator as a string representation.

            :return: The format validator as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
