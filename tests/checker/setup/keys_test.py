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
    Unit tests for CheckerKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.checker.setup.keys import CheckerKeys


class CheckerKeysTest(unittest.TestCase):
    '''
        Defines class CheckerKeysTest with attribute(s) and method(s).
        Tests CheckerKeys constants and mapping helper methods.
    '''

    def test_keys(self) -> None:
        self.assertEqual(CheckerKeys.DEPENDENCY_FORMAT_VALIDATOR, 'format_validator')
        self.assertEqual(CheckerKeys.DEPENDENCY_TYPE_VALIDATOR, 'type_validator')
        self.assertEqual(CheckerKeys.DEPENDENCY_CONTEXT_PROVIDER, 'context_provider')
        self.assertEqual(CheckerKeys.DEPENDENCY_CHECK_REPORTER, 'check_reporter')

        self.assertEqual(CheckerKeys.OPTION_SEPARATOR, 'separator')
        self.assertEqual(CheckerKeys.OPTION_ABSTRACT_TYPES, 'abstract_types')
        self.assertEqual(CheckerKeys.OPTION_STACK_INDEX_CALLER, 'stack_index_caller')
        self.assertEqual(CheckerKeys.OPTION_MESSAGES_PROVIDER, 'messages_provider')

    def test_get_dependency_to_type(self) -> None:
        mapping = CheckerKeys.get_dependency_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(CheckerKeys.DEPENDENCY_FORMAT_VALIDATOR, mapping)
        self.assertIn(CheckerKeys.DEPENDENCY_TYPE_VALIDATOR, mapping)

    def test_get_option_to_type(self) -> None:
        mapping = CheckerKeys.get_option_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertEqual(mapping[CheckerKeys.OPTION_SEPARATOR], str)
        self.assertEqual(mapping[CheckerKeys.OPTION_STACK_INDEX_CALLER], int)


if __name__ == "__main__":
    unittest.main()
