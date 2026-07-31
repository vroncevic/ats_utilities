# -*- coding: UTF-8 -*-

'''
Module
    keys.py
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
    Runtime components and interface constraints for Config I/O bundle.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar
from types import MappingProxyType

from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ConfigIOKeys:
    '''
        Runtime components and interface constraints for Config I/O bundle.

        It defines:

            :attributes:
                | DEPENDENCY_FILE_PATH: File path interface constant.
                | DEPENDENCY_PROCESSOR: Processor interface constant.
                | DEPENDENCY_CONTEXT_BUNDLE: Context bundle interface constant.
                | OPTION_FILE_PATH: File path option constant.
                | OPTION_SCHEME: Scheme option constant.
                | OPTION_CONTEXT_BUNDLE: Context bundle option constant.
            :methods:
                | get_dependency_to_type - Returns mapping of Config I/O dependencies to their types.
                | get_option_to_type - Returns mapping of Config I/O options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_FILE_PATH: ClassVar[str] = 'file_path'
    DEPENDENCY_PROCESSOR: ClassVar[str] = 'processor'
    DEPENDENCY_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    # Option Keys
    OPTION_FILE_PATH: ClassVar[str] = 'file_path'
    OPTION_SCHEME: ClassVar[str] = 'scheme'
    OPTION_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of Config I/O dependencies to their types.

            :return: Mapping of Config I/O dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_FILE_PATH: str,
            cls.DEPENDENCY_PROCESSOR: IConfigProcessor,
            cls.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of Config I/O options to their types.

            :return: Mapping of Config I/O options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_FILE_PATH: str,
            cls.OPTION_SCHEME: Mapping,
            cls.OPTION_CONTEXT_BUNDLE: ContextBundle,
        })
