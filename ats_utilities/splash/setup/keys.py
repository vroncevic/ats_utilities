# -*- coding: UTF-8 -*-

'''
Module
    splash_keys.py
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
    Defines constants for ATS splash screen keys.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import ClassVar
from types import MappingProxyType

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@dataclass(frozen=True, slots=True, kw_only=True)
class SplashKeys:
    '''
        Defines keys for splash screen.

        It defines:

            :attributes:
                | DEPENDENCY_SPLASH_PROPERTY - The dependency key for splash property.
                | DEPENDENCY_TERMINAL_PROPERTY - The dependency key for terminal properties.
                | DEPENDENCY_EXT - The dependency key for external infrastructure.
                | DEPENDENCY_PB - The dependency key for progress bar.
                | DEPENDENCY_CONTEXT_BUNDLE - The dependency key for context bundle.
                | OPTION_PROP - The option key for splash properties.
                | OPTION_CONTEXT_BUNDLE - The option key for context bundle.
            :methods:
                | get_dependency_to_type - Returns mapping of splash dependencies to their types.
                | get_option_to_type - Returns mapping of splash options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_SPLASH_PROPERTY: ClassVar[str] = 'splash_property'
    DEPENDENCY_TERMINAL_PROPERTY: ClassVar[str] = 'terminal_property'
    DEPENDENCY_EXT: ClassVar[str] = 'ext'
    DEPENDENCY_PB: ClassVar[str] = 'pb'
    DEPENDENCY_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    # Option Keys
    OPTION_PROP: ClassVar[str] = 'prop'
    OPTION_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of splash dependencies to their types.

            :return: The mapping of splash dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_SPLASH_PROPERTY: ISplashProperty,
            cls.DEPENDENCY_TERMINAL_PROPERTY: ITerminalProperties,
            cls.DEPENDENCY_EXT: IExtInfrastructure,
            cls.DEPENDENCY_PB: IProgressBar,
            cls.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of splash options to their types.

            :return: The mapping of splash options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_PROP: Mapping,
            cls.OPTION_CONTEXT_BUNDLE: ContextBundle,
        })
