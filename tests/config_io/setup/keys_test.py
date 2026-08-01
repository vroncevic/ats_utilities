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
    Unit tests for ConfigIOKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.config_io.setup.keys import ConfigIOKeys


class ConfigIOKeysTest(unittest.TestCase):
    '''
        Defines class ConfigIOKeysTest with attribute(s) and method(s).
        Tests ConfigIOKeys constants and mapping helper methods.
    '''

    def test_keys(self) -> None:
        self.assertEqual(ConfigIOKeys.DEPENDENCY_FILE_PATH, 'file_path')
        self.assertEqual(ConfigIOKeys.DEPENDENCY_PROCESSOR, 'processor')
        self.assertEqual(ConfigIOKeys.DEPENDENCY_CONTEXT_BUNDLE, 'context_bundle')

        self.assertEqual(ConfigIOKeys.OPTION_FILE_PATH, 'file_path')
        self.assertEqual(ConfigIOKeys.OPTION_SCHEME, 'scheme')
        self.assertEqual(ConfigIOKeys.OPTION_CONTEXT_BUNDLE, 'context_bundle')

    def test_get_dependency_to_type(self) -> None:
        mapping = ConfigIOKeys.get_dependency_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(ConfigIOKeys.DEPENDENCY_FILE_PATH, mapping)
        self.assertIn(ConfigIOKeys.DEPENDENCY_PROCESSOR, mapping)

    def test_get_option_to_type(self) -> None:
        mapping = ConfigIOKeys.get_option_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertEqual(mapping[ConfigIOKeys.OPTION_FILE_PATH], str)


if __name__ == "__main__":
    unittest.main()
