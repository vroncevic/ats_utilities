# -*- coding: UTF-8 -*-

'''
Module
    parser_strategy_registry_test.py
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
    Unit tests for ParserStrategyRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.option.strategy.parser_strategy_bundle import ParserStrategyBundle
from ats_utilities.option.strategy.parser_strategy_registry import ParserStrategyRegistry
from ats_utilities.option.strategy.parser_strategy_params import ParserStrategyParams
from ats_utilities.option.parser.engine import ArgParser

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ParserStrategyRegistryTest(unittest.TestCase):
    '''
        Defines class ParserStrategyRegistryTest with attribute(s) and method(s).
        Tests ParserStrategyRegistry static factory logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.parameters = {"param1": "value1"}

    def test_create_bundle(self) -> None:
        '''
            Tests create_bundle method.
        '''
        bundle = ParserStrategyRegistry.create_bundle(
            ParserStrategyParams(
                parameters=self.parameters,
                context_bundle=self.mock_context,
                parser_class=ArgParser
            )
        )
        self.assertIsInstance(bundle, ParserStrategyBundle)
        self.assertEqual(bundle.parameters, self.parameters)
        self.assertIs(bundle.context_bundle, self.mock_context)
        self.assertIs(bundle.parser_class, ArgParser)

    def test_create_parser_strategy_bundle_from_dict(self) -> None:
        '''
            Tests create_parser_strategy_bundle_from_dict method.
        '''
        bundle = ParserStrategyRegistry.create_parser_strategy_bundle_from_dict(
            parameters=self.parameters,
            context_bundle=self.mock_context,
            parser_class=ArgParser
        )
        self.assertIsInstance(bundle, ParserStrategyBundle)
        self.assertEqual(bundle.parameters, self.parameters)
        self.assertIs(bundle.context_bundle, self.mock_context)
        self.assertIs(bundle.parser_class, ArgParser)


if __name__ == "__main__":
    unittest.main()
