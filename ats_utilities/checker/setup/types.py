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
    Defines types for Checker.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import Any
from enum import Enum

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Parameters specification: (('expected type:param name', instance), ...)
type Parameters = Sequence[tuple[str, Any]]

# Parameters metadata specification: (('expected type', 'param name'), ...)
type ParametersMeta = Sequence[tuple[str, str, Any]]

# Result type: ((error message report, error id), ...)
type Result = tuple[str, int]

# Split result: ((expected type, param name), ...)
type SplitResult = tuple[str, str]


class CheckerErrorType(int, Enum):
    '''
        Defines class CheckerErrorType with attribute(s).
        Marks error types for the Checker.

        It defines:

            :attributes:
                | NO_ERROR - Marks no error report (0).
                | TYPE_ERROR - Marks type error report (1).
                | FORMAT_ERROR - Marks wrong format error report (2).
    '''

    NO_ERROR = 0
    TYPE_ERROR = 1
    FORMAT_ERROR = 2
