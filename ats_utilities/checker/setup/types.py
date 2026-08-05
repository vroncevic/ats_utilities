# -*- coding: UTF-8 -*-

'''
Module
    types.py
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
    Defines types for the Checker.
'''

from __future__ import annotations

from collections.abc import Sequence
from enum import Enum

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'

# Parameters specification: (('expected type:param name', instance), ...)
type Parameters = Sequence[tuple[str, object]]

# Parameters metadata specification: (('expected type', 'param name'), ...)
type ParametersMeta = Sequence[tuple[str, str, object]]

# Result type: ((error message report, error id), ...)
type Result = tuple[str, int]


class CheckerErrorType(int, Enum):
    '''
        Defines the CheckerErrorType class with attribute(s).
        Marks error types for the Checker.

        It defines:

            :attributes:
                | NO_ERROR - The marks no error report (0).
                | TYPE_ERROR - The marks type error report (1).
                | FORMAT_ERROR - The marks wrong format error report (2).
    '''

    NO_ERROR = 0
    TYPE_ERROR = 1
    FORMAT_ERROR = 2
