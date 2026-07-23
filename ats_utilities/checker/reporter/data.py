# -*- coding: UTF-8 -*-

'''
Module
    data.py
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
    Encapsulates checker reporter runtime data.
'''

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from ats_utilities.utils.reflection import instance_to_dict

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Type alias for parameter metadata: (parameter name, expected type, actual value)
type ParamMetadata = tuple[str, str, Any]


@dataclass(slots=True, frozen=True, kw_only=True)
class CheckReporterData:
    '''
        Encapsulates checker reporter runtime data.

        It defines:

            :attributes:
                | context - Message context.
                | parameters_meta - Sequence of parameter name and parameter type tuples.
                | err_indices - Sequence of error indices.
                | is_fmt_err - Flag indicating if format error type has been found.
            :methods:
                | __post_init__ - Post-initialization hook to validate check reporter data.
                | to_dict - Converts the checker reporter data instance to a dictionary.
    '''

    context: str
    parameters_meta: Sequence[ParamMetadata]
    err_indices: Sequence[int]
    is_fmt_err: bool

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the checker reporter data instance to a dictionary.

            :return: Dictionary representation of the checker reporter data instance.
            :rtype: dict[str, Any]
            :exceptions: None.
        '''
        return instance_to_dict(self)
