# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
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
    Unit tests for OptionKeys class.
'''

from __future__ import annotations

import unittest
from collections.abc import Mapping
from types import MappingProxyType

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.keys import OptionKeys
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy


class KeysTest(unittest.TestCase):
    '''
        Defines class KeysTest with attribute(s) and method(s).
        Tests OptionKeys constants and mapping logic.
    '''

    def test_dependency_keys(self) -> None:
        self.assertEqual(OptionKeys.DEPENDENCY_STRATEGY, "strategy")
        self.assertEqual(OptionKeys.DEPENDENCY_CONTEXT_BUNDLE, "context_bundle")

    def test_option_keys(self) -> None:
        self.assertEqual(OptionKeys.OPTION_PARAMETERS, "parameters")
        self.assertEqual(OptionKeys.OPTION_CONTEXT_BUNDLE, "context_bundle")

    def test_get_dependency_to_type(self) -> None:
        dep_map = OptionKeys.get_dependency_to_type()
        self.assertIsInstance(dep_map, MappingProxyType)
        self.assertEqual(len(dep_map), 2)
        self.assertIs(dep_map[OptionKeys.DEPENDENCY_STRATEGY], IParserStrategy)
        self.assertIs(dep_map[OptionKeys.DEPENDENCY_CONTEXT_BUNDLE], ContextBundle)

    def test_get_option_to_type(self) -> None:
        opt_map = OptionKeys.get_option_to_type()
        self.assertIsInstance(opt_map, MappingProxyType)
        self.assertEqual(len(opt_map), 2)
        self.assertEqual(opt_map[OptionKeys.OPTION_PARAMETERS], Mapping)
        self.assertIs(opt_map[OptionKeys.OPTION_CONTEXT_BUNDLE], ContextBundle)


if __name__ == "__main__":
    unittest.main()
