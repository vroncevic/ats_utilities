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
    Unit tests for CheckerBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.checker.setup.keys import CheckerBundleKeys


class CheckerKeysTest(unittest.TestCase):
    '''
        Defines class CheckerKeysTest with attribute(s) and method(s).
        Tests CheckerBundleKeys constants and mapping helper methods.
    '''

    def test_keys(self) -> None:
        self.assertEqual(CheckerBundleKeys.DEPENDENCY_FORMAT_VALIDATOR, 'format_validator')
        self.assertEqual(CheckerBundleKeys.DEPENDENCY_TYPE_VALIDATOR, 'type_validator')
        self.assertEqual(CheckerBundleKeys.DEPENDENCY_CONTEXT_PROVIDER, 'context_provider')
        self.assertEqual(CheckerBundleKeys.DEPENDENCY_CHECK_REPORTER, 'check_reporter')

        self.assertEqual(CheckerBundleKeys.OPTION_SEPARATOR, 'separator')
        self.assertEqual(CheckerBundleKeys.OPTION_ABSTRACT_TYPES, 'abstract_types')
        self.assertEqual(CheckerBundleKeys.OPTION_STACK_INDEX_CALLER, 'stack_index_caller')
        self.assertEqual(CheckerBundleKeys.OPTION_MESSAGES_PROVIDER, 'messages_provider')

    def test_get_dependency_to_type(self) -> None:
        mapping = CheckerBundleKeys.get_dependency_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(CheckerBundleKeys.DEPENDENCY_FORMAT_VALIDATOR, mapping)
        self.assertIn(CheckerBundleKeys.DEPENDENCY_TYPE_VALIDATOR, mapping)

    def test_get_option_to_type(self) -> None:
        mapping = CheckerBundleKeys.get_option_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertEqual(mapping[CheckerBundleKeys.OPTION_SEPARATOR], str)
        self.assertEqual(mapping[CheckerBundleKeys.OPTION_STACK_INDEX_CALLER], int)


if __name__ == "__main__":
    unittest.main()
