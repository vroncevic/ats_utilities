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
    Defines class FormatValidator with attribute(s) and method(s).
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
        Defines class FormatValidator with attribute(s) and method(s).
        Provides an API for validating parameters used by method(s) and function(s).

        It defines:

            :attributes:
                | EXPECTED_FORMAT_PARTS - Expected number of parts in the format string.
                | EXPECTED_SEPARATOR - Expected separator between type and name.
            :methods:
                | __init__ - Initializes format validator.
                | set_separator - Sets separator used in parameter specifications.
                | get_separator - Returns separator used in parameter specifications.
                | is_valid - Checks if format follows expected format.
                | split - Splits format into parts.
                | __str__ - Returns format validator as string representation.

        Expected format (in string format):

            type:name

        where:
            type - expected parameter type
            name - expected parameter name

        Examples:
            >>> from ats_utilities.checker.format.format_validator import FormatValidator
            >>> fv = FormatValidator()
            >>> fv.is_valid(r'str:name')
            True
            >>> fv.split(r'str:name')
            ('str', 'name')
    '''

    EXPECTED_FORMAT_PARTS: Final[int] = 2
    EXPECTED_SEPARATOR: Final[str] = ':'

    def __init__(self, separator: str | None = None) -> None:
        '''
            Initializes format validator.

            :param separator: The separator to use for splitting the format string | None.
            :exceptions:
                | ATSTypeError:  Separator must be a string.
                | ATSValueError: Separator must not be empty.
        '''
        if separator is not None:
            ctx: str = 'format_validator::init(...)'
            istype(separator, str, ctx, 'separator must be a string')
            not_empty(separator, ctx, 'separator must not be empty')
            self._separator = separator
        else:
            self._separator = self.EXPECTED_SEPARATOR

    def set_separator(self, separator: str) -> None:
        '''
            Sets separator used in parameter specifications.

            :param separator: Separator used in parameter specifications.
            :exceptions:
                | ATSTypeError:  Separator must be a string.
                | ATSValueError: Separator must not be empty.
        '''
        ctx: str = 'format_validator::set_separator(...)'
        istype(separator, str, ctx, 'separator must be a string')
        not_empty(separator, ctx, 'separator must not be empty')
        self._separator = separator

    def get_separator(self) -> str:
        '''
            Returns separator used in parameter specifications.

            :return: Separator used in parameter specifications.
            :exceptions: None.
        '''
        return self._separator

    def is_valid(self, format_to_check: str) -> bool:
        '''
            Checks if format follows expected format.

            :param format_to_check: Format to be validated.
            :return: True if successfully, otherwise False.
            :exceptions:
                | ATSValueError: Format to be validated must be provided.
                | ATSTypeError:  Format to be validated must be a string.
                | ATSValueError: Format to be validated must contain the separator.
        '''
        ctx: str = 'format_validator::is_valid(...)'
        not_none(format_to_check, ctx, 'format to be validated must be provided')
        istype(format_to_check, str, ctx, 'format to be validated must be a string')

        return len(self.split(format_to_check)) == self.EXPECTED_FORMAT_PARTS

    def split(self, format_to_split: str) -> Sequence[str]:
        '''
            Splits the format string into parts.

            :param format_to_split: The format string to split.
            :return: A Sequence containing the split components (type, name).
            :exceptions:
                | ATSValueError: Format to be validated must be provided.
                | ATSTypeError:  Format to be validated must be a string.
                | ATSValueError: Format to be validated must contain the separator.
        '''
        ctx: str = 'format_validator::split(...)'
        not_none(format_to_split, ctx, 'format to split must be provided')
        istype(format_to_split, str, ctx, 'format to split must be a string')
        not_satisfied(
            self._separator not in format_to_split, ctx,
            f'format to split must contain the separator "{self._separator}"'
        )

        return tuple(format_to_split.split(sep=self._separator))

    def __str__(self) -> str:
        '''
            Returns format validator as string representation.

            :return: Format validator as string representation.
            :exceptions: None.
        '''
        return to_str(self)
