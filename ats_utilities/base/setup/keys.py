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
    Runtime components and interface constraints for base bundle.
'''

from __future__ import annotations

from typing import ClassVar
from types import MappingProxyType

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BaseBundleKeys:
    '''
        Runtime components and interface constraints for base bundle.

        It defines:

            :attributes:
                | DEPENDENCY_CONTEXT_BUNDLE - The context bundle interface constant for base bundle.
                | DEPENDENCY_INFO_MANAGER - The information manager interface constant for base bundle.
                | DEPENDENCY_OPTION_MANAGER - The option manager interface constant for base bundle.
                | DEPENDENCY_SPLASH_MANAGER - The splash manager interface constant for base bundle.
                | DEPENDENCY_GENERATION_MANAGER - The generator manager interface constant for base bundle.
                | OPTION_INFO_FILE - The information file constant for base bundle.
                | OPTION_USE_GENERATOR - The use generator constant for base bundle.
                | OPTION_CONTEXT_BUNDLE - The context bundle constant for base bundle.
            :methods:
                | get_dependency_to_type - Returns the mapping of the base bundle dependencies to their types.
                | get_option_to_type - Returns the mapping of the base bundle options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'
    DEPENDENCY_INFO_MANAGER: ClassVar[str] = 'info_manager'
    DEPENDENCY_OPTION_MANAGER: ClassVar[str] = 'option_manager'
    DEPENDENCY_SPLASH_MANAGER: ClassVar[str] = 'splash_manager'
    DEPENDENCY_GENERATION_MANAGER: ClassVar[str] = 'generation_manager'

    # Option Keys
    OPTION_INFO_FILE: ClassVar[str] = 'info_file'
    OPTION_USE_GENERATOR: ClassVar[str] = 'use_generator'
    OPTION_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the base bundle dependencies to their types.

            :return: The mapping of the base bundle dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
            cls.DEPENDENCY_INFO_MANAGER: IInfoManager,
            cls.DEPENDENCY_OPTION_MANAGER: IOptionManager,
            cls.DEPENDENCY_SPLASH_MANAGER: ISplashManager,
            cls.DEPENDENCY_GENERATION_MANAGER: IGeneratorManager,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the base bundle options to their types.

            :return: The mapping of the base bundle options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_INFO_FILE: str,
            cls.OPTION_USE_GENERATOR: bool,
            cls.OPTION_CONTEXT_BUNDLE: ContextBundle,
        })
