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
    Defines FileData DTO class.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import instance_to_dict

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class FileData:
    '''
        Defines FileData DTO class for config I/O operations.

        It defines:

            :attributes:
                | file_path - File path.
                | file_mode - File mode.
                | context_bundle - Context bundle for dependency injection.
            :methods:
                | to_dict - Converts the file data instance to a dictionary.
    '''

    file_path: str
    file_mode: str
    context_bundle: ContextBundle

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the file data instance to a dictionary.

            :return: Dictionary representation of the file data.
            :rtype: dict[str, Any]
            :exceptions: None.
        '''
        return instance_to_dict(self)
