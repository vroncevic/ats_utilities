# -*- coding: UTF-8 -*-

'''
Module
    data_test.py
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
    Unit tests for StrategyData class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.option.underlying.iunderlying import IUnderlyingParser


class StrategyDataTest(unittest.TestCase):
    '''
        Defines class StrategyDataTest with attribute(s) and method(s).
        Tests StrategyData class.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_parser = MagicMock(spec=IUnderlyingParser)

    def test_init_valid(self) -> None:
        data = StrategyData(
            context_bundle=self.mock_context,
            parser=self.mock_parser
        )
        self.assertIs(data.context_bundle, self.mock_context)
        self.assertIs(data.parser, self.mock_parser)

    def test_slots(self) -> None:
        data = StrategyData(
            context_bundle=self.mock_context,
            parser=self.mock_parser
        )
        with self.assertRaises(AttributeError):
            data.__dict__  # type: ignore

    def test_frozen(self) -> None:
        data = StrategyData(
            context_bundle=self.mock_context,
            parser=self.mock_parser
        )
        with self.assertRaises(FrozenInstanceError):
            data.parser = MagicMock(spec=IUnderlyingParser)  # type: ignore

    def test_to_dict(self) -> None:
        data = StrategyData(
            context_bundle=self.mock_context,
            parser=self.mock_parser
        )
        expected = {
            "context_bundle": self.mock_context,
            "parser": self.mock_parser
        }
        self.assertEqual(data.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
