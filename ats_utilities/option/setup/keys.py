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
    Runtime components and interface constraints for option bundle.
'''

from __future__ import annotations

from typing import ClassVar
from types import MappingProxyType
from collections.abc import Mapping

from ats_utilities.info.setup.schema import InfoSchema
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionBundleKeys:
    '''
        Runtime components and interface constraints for option bundle.

        It defines:

            :attributes:
                | DEPENDENCY_STRATEGY - The strategy interface constant for option bundle.
                | DEPENDENCY_CONTEXT_BUNDLE - The context bundle interface constant for option bundle.
                | OPTION_PARAMETERS - The parameters option constant for option bundle.
                | OPTION_CONTEXT_BUNDLE - The context bundle option constant for option bundle.
                | REQUIRED_CONFIG_KEYS_SET - The set of required information keys for option bundle.
            :methods:
                | get_dependency_to_type - Returns the mapping of the option bundle dependencies to their types.
                | get_option_to_type - Returns the mapping of the option bundle options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_STRATEGY: ClassVar[str] = 'strategy'
    DEPENDENCY_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    # Option Keys
    OPTION_PARAMETERS: ClassVar[str] = 'parameters'
    OPTION_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    # Information Keys
    REQUIRED_CONFIG_KEYS_SET: ClassVar[frozenset[str]] = frozenset(
        InfoSchema.get_required_config_keys()
    )

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the option bundle dependencies to their types.

            :return: The mapping of the option bundle dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_STRATEGY: IParserStrategy,
            cls.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the option bundle options to their types.

            :return: The mapping of the option bundle options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_PARAMETERS: Mapping,
            cls.OPTION_CONTEXT_BUNDLE: ContextBundle,
        })
