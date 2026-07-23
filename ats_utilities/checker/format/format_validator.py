# -*- coding: UTF-8 -*-

'''
Module
    format_validator.py
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
    Creates an API for format validation of parameter-description.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import Final, override

from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.validation.check_value import not_none, not_satisfied
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.reflection import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class FormatValidator(IFormatValidator):
    '''
        Defines class FormatValidator with attribute(s) and method(s).
        Creates an API for format validation of parameter-description.

        It defines:

            :attributes:
                | EXPECTED_FORMAT_PARTS - Expected number of parts in the format string.
                | EXPECTED_SEPARATOR - Expected separator between type and name.
            :methods:
                | __init__ - Initializes the FormatValidator.
                | is_valid - Checks if the string follows the expected format.
                | split - Splits the format string into type and name parts.
                | __str__ - Returns the format validator as string representation.

        Expected format of the string:

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
    EXPECTED_SEPARATOR: Final[str] = r':'

    def __init__(self, separator: str | None = None) -> None:
        '''
            Initializes the FormatValidator.

            :param separator: The separator to use for splitting the format string | None.
            :type separator: str | None
            :exceptions: None.
        '''
        self._separator = self.EXPECTED_SEPARATOR if separator is None else separator

    @override
    def is_valid(self, exp_type: str) -> bool:
        '''
            Checks if the string follows the expected format.

            :param exp_type: The expected-format string to be validated.
            :type exp_type: str
            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions:
                | ATSValueError: Expected-format string must be provided.
                | ATSTypeError: Expected-format string must be a string.
                | ATSValueError: Expected-format string must contain the separator.
        '''
        ctx: str = r'format_validator::is_valid(...)'
        not_none(exp_type, ctx, r'expected type must be provided')
        istype(exp_type, str, ctx, r'expected type must be a string')

        return len(self.split(exp_type)) == self.EXPECTED_FORMAT_PARTS

    @override
    def split(self, exp_type: str) -> Sequence[str]:
        '''
            Splits the format string into parts.

            :param exp_type: The format string to split.
            :type exp_type: str
            :return: A Sequence containing the split components.
            :rtype: Sequence[str]
            :exceptions:
                | ATSValueError: Expected-format string must be provided.
                | ATSTypeError: Expected-format string must be a string.
                | ATSValueError: Expected-format string must contain the separator.
        '''
        ctx: str = r'format_validator::split(...)'
        not_none(exp_type, ctx, r'expected type must be provided')
        istype(exp_type, str, ctx, r'expected type must be a string')
        not_satisfied(
            self._separator not in exp_type, ctx,
            r'expected type must contain the separator'
        )

        return tuple(exp_type.split(sep=self._separator))

    @override
    def __str__(self) -> str:
        '''
            Returns the format validator as string representation.

            :return: The format validator as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
