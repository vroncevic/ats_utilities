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
    Creates an API for handling parameter description format validation.
'''

from __future__ import annotations

from typing import Final, override

from ats_utilities.factory_class import to_str
from ats_utilities.checker.format.iformat_validator import IFormatValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class FormatValidator(IFormatValidator):
    '''
        Defines class FormatValidator with attribute(s) and method(s).
        Creates an API for parameter description format validation.
        Mechanism for checking function or method parameters (format).

        It defines:

            :attributes:
                | EXPECTED_FORMAT_PARTS - Expected number of parts in the format string.
            :methods:
                | is_valid - Checks if the string follows the expected format.
                | split - Splits the format string into type and name parts.
                | __str__ - Returns the format vcheck as string representation.
    '''

    EXPECTED_FORMAT_PARTS: Final[int] = 2

    @override
    def is_valid(self, exp_type: str) -> bool:
        '''
            Checks if the string follows the expected format.
            Checks if the string follows the type:name format.

            :param exp_type: The expected format string to validate.
            :type exp_type: <str>
            :return: True (success), False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return len(exp_type.split(sep=':')) == self.EXPECTED_FORMAT_PARTS

    @override
    def split(self, exp_type: str) -> tuple[str, str]:
        '''
            Splits the format string into type and name parts.

            :param exp_type: The format string to split.
            :type exp_type: <str>
            :return: A tuple containing the split components.
            :rtype: <tuple[str, str]>
            :exceptions: None.
        '''
        parts = exp_type.split(sep=':')
        return parts[0], parts[1]

    @override
    def __str__(self) -> str:
        '''
            Returns the format vcheck as string representation.

            :return: The format vcheck as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
