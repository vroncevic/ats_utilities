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
    Runtime components and interface constraints for generator bundle.
'''

from __future__ import annotations

from typing import ClassVar
from types import MappingProxyType

from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class GeneratorBundleKeys:
    '''
        Runtime components and interface constraints for generator bundle.

        It defines:

            :attributes:
                | DEPENDENCY_SCHEME_LOADER - The scheme loader interface constant for generator bundle.
                | DEPENDENCY_TAR_PROCESSOR - The tar processor interface constant for generator bundle.
                | DEPENDENCY_CONTEXT_BUNDLE - The context bundle constant for generator bundle.
                | OPTION_CONTEXT_BUNDLE - The context bundle option constant for generator bundle.
            :methods:
                | get_dependency_to_type - Returns mapping of generator bundle dependencies to their types.
                | get_option_to_type - Returns mapping of generator bundle options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_SCHEME_LOADER: ClassVar[str] = 'scheme_loader'
    DEPENDENCY_TAR_PROCESSOR: ClassVar[str] = 'tar_processor'
    DEPENDENCY_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    # Option Keys
    OPTION_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of generator bundle dependencies to their types.

            :return: The mapping of generator bundle dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_SCHEME_LOADER: ISchemeLoader,
            cls.DEPENDENCY_TAR_PROCESSOR: ITarProcessor,
            cls.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of generator bundle options to their types.

            :return: The mapping of generator bundle options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_CONTEXT_BUNDLE: ContextBundle,
        })
