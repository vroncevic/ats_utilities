# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Encapsulates config I/O components for simplification of config I/O bundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, ClassVar

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class ConfigIOBundle:
    '''
        Encapsulates config I/O components for simplification of config I/O bundle creation.

        It defines:

            :attributes:
                | READ_MODE - Default file opening mode (class variable, default 'r').
                | WRITE_MODE - Default file opening mode (class variable, default 'w').
                | file_path - Configuration file path.
                | scheme - Configuration scheme.
                | processor - Configuration processor.
                | context_bundle - Context bundle.
            :methods:
                | to_dict - Converts config I/O bundle to a dictionary.
    '''

    READ_MODE: ClassVar[str] = 'r'
    WRITE_MODE: ClassVar[str] = 'w'
    file_path: str
    scheme: Mapping[str, str]
    processor: IConfigProcessor
    context_bundle: ContextBundle

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts config I/O bundle to a dictionary.

            :return: Dictionary representation of the config I/O bundle.
            :rtype: dict[str, Any]
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
