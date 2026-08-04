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
    Unit tests for GeneratorBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.generation.setup.keys import GeneratorBundleKeys


class GeneratorKeysTest(unittest.TestCase):
    '''
        Defines class GeneratorKeysTest with attribute(s) and method(s).
        Tests GeneratorBundleKeys constants and mapping helper methods.
    '''

    def test_keys(self) -> None:
        self.assertEqual(GeneratorBundleKeys.DEPENDENCY_SCHEME_LOADER, 'scheme_loader')
        self.assertEqual(GeneratorBundleKeys.DEPENDENCY_TAR_PROCESSOR, 'tar_processor')
        self.assertEqual(GeneratorBundleKeys.DEPENDENCY_CONTEXT_BUNDLE, 'context_bundle')
        self.assertEqual(GeneratorBundleKeys.OPTION_CONTEXT_BUNDLE, 'context_bundle')

    def test_get_dependency_to_type(self) -> None:
        mapping = GeneratorBundleKeys.get_dependency_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(GeneratorBundleKeys.DEPENDENCY_SCHEME_LOADER, mapping)

    def test_get_option_to_type(self) -> None:
        mapping = GeneratorBundleKeys.get_option_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertEqual(mapping[GeneratorBundleKeys.OPTION_CONTEXT_BUNDLE], GeneratorBundleKeys.get_option_to_type()[GeneratorBundleKeys.OPTION_CONTEXT_BUNDLE])


if __name__ == "__main__":
    unittest.main()
