# -*- coding: UTF-8 -*-

'''
Module
    parser_strategy_bundle_test.py
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
    Unit tests for ParserStrategyBundle class.
'''

from __future__ import annotations

import unittest
from typing import Any
from unittest.mock import MagicMock

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.strategy.parser_strategy_bundle import ParserStrategyBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyParser(IArgParser):
    '''
        Dummy parser class for strategy bundle tests.
    '''
    def __init__(self, component_bundle: Any) -> None:
        pass

    def error(self, message: str) -> Any:
        pass

    def add_argument(self, *args: Any, **kwargs: Any) -> None:
        pass

    def add_subparsers(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def parse_args(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def parse_known_args(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def __str__(self) -> str:
        return "DummyParser"


class ParserStrategyBundleTest(unittest.TestCase):
    '''
        Defines class ParserStrategyBundleTest with attribute(s) and method(s).
        Tests ParserStrategyBundle dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful ParserStrategyBundle initialization.
                | test_init_invalid_none - Tests ParserStrategyBundle initialization with None values.
                | test_init_invalid_type - Tests ParserStrategyBundle initialization with wrong types.
                | test_init_invalid_parser_class - Tests ParserStrategyBundle initialization with invalid parser class.
                | test_to_dict - Tests ParserStrategyBundle to_dict method.
    '''

    def test_init_valid(self) -> None:
        '''
            Tests successful ParserStrategyBundle initialization.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)

        try:
            bundle = ParserStrategyBundle(
                parameters={"name": "test"},
                context_bundle=mock_context,
                parser_class=DummyParser
            )
            self.assertEqual(bundle.parameters, {"name": "test"})
            self.assertIs(bundle.context_bundle, mock_context)
            self.assertIs(bundle.parser_class, DummyParser)
        except (ATSValueError, ATSTypeError, TypeError):
            self.fail("Failed to instantiate ParserStrategyBundle with valid arguments.")

    def test_init_invalid_none(self) -> None:
        '''
            Tests ParserStrategyBundle initialization with None values.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)

        with self.assertRaises(ATSValueError):
            ParserStrategyBundle(parameters=None, context_bundle=mock_context, parser_class=DummyParser)  # type: ignore

        with self.assertRaises(ATSValueError):
            ParserStrategyBundle(parameters={"name": "test"}, context_bundle=None, parser_class=DummyParser)  # type: ignore

        with self.assertRaises(ATSValueError):
            ParserStrategyBundle(parameters={"name": "test"}, context_bundle=mock_context, parser_class=None)  # type: ignore

    def test_init_invalid_type(self) -> None:
        '''
            Tests ParserStrategyBundle initialization with wrong types.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)

        with self.assertRaises(ATSTypeError):
            ParserStrategyBundle(parameters="not mapping", context_bundle=mock_context, parser_class=DummyParser)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ParserStrategyBundle(parameters={"name": "test"}, context_bundle="not context", parser_class=DummyParser)  # type: ignore

    def test_init_invalid_parser_class(self) -> None:
        '''
            Tests ParserStrategyBundle initialization with invalid parser class.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)

        with self.assertRaises(TypeError):
            ParserStrategyBundle(parameters={"name": "test"}, context_bundle=mock_context, parser_class=123)  # type: ignore

    def test_to_dict(self) -> None:
        '''
            Tests ParserStrategyBundle to_dict method.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)
        bundle = ParserStrategyBundle(
            parameters={"name": "test"},
            context_bundle=mock_context,
            parser_class=DummyParser
        )
        expected = {
            "parameters": {"name": "test"},
            "context_bundle": mock_context,
            "parser_class": DummyParser
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
