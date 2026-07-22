# -*- coding: UTF-8 -*-

'''
Module
    option_factory.py
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
    Factory for creating OptionBundle components.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ats_utilities.option.option_bundle import OptionBundle
from ats_utilities.option.strategy.engine import ParserStrategy
from ats_utilities.option.strategy.parser_strategy_registry import ParserStrategyRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.engine import ArgParser

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class OptionFactory:
    '''
        Factory for creating OptionBundle components.
    '''

    @classmethod
    def create_option_bundle_from_dict(
        cls,
        parameters: Mapping[str, str],
        context_bundle: ContextBundle,
        parser_class: type[IArgParser] = ArgParser
    ) -> OptionBundle:
        '''
            Creates an option bundle from parameters in mapping format.

            :param parameters: Metadata parameters in mapping format (read only data).
            :type parameters: <Mapping[str, str]>
            :param context_bundle: Context bundle for option bundle.
            :type context_bundle: <ContextBundle>
            :param parser_class: Injected parser class type.
            :type parser_class: <type[IArgParser]>
            :return: OptionBundle instance.
            :rtype: <OptionBundle>
            :exceptions: None.
        '''
        parser_strategy_bundle = ParserStrategyRegistry.create_parser_strategy_bundle_from_dict(
            parameters=parameters,
            context_bundle=context_bundle,
            parser_class=parser_class
        )
        strategy: ParserStrategy = ParserStrategy(own=parser_strategy_bundle)

        return OptionBundle(
            parameters=parameters,
            strategy=strategy,
            context_bundle=context_bundle
        )
