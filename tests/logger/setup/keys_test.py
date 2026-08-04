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
    Unit tests for LoggerBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.logger.setup.keys import LoggerBundleKeys


class LoggerKeysTest(unittest.TestCase):
    '''
        Defines class LoggerKeysTest with attribute(s) and method(s).
        Tests LoggerBundleKeys constants and mapping helper methods.
    '''

    def test_keys(self) -> None:
        self.assertEqual(LoggerBundleKeys.DEPENDENCY_LOGGER, 'logger')
        self.assertEqual(LoggerBundleKeys.DEPENDENCY_HAS_FILE_HANDLER, 'has_file_handler')
        self.assertEqual(LoggerBundleKeys.OPTION_LOG_FILE, 'log_file')

    def test_get_dependency_to_type(self) -> None:
        mapping = LoggerBundleKeys.get_dependency_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(LoggerBundleKeys.DEPENDENCY_LOGGER, mapping)

    def test_get_option_to_type(self) -> None:
        mapping = LoggerBundleKeys.get_option_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(LoggerBundleKeys.OPTION_LOG_FILE, mapping)


if __name__ == "__main__":
    unittest.main()
