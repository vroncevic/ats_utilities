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
    Unit tests for ReporterBundleKeys class.
'''

from __future__ import annotations

import unittest
from collections.abc import Mapping
from types import MappingProxyType

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.setup.options import CheckerBundleOptions
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.setup.options import LoggerBundleOptions
from ats_utilities.reporter.setup.keys import ReporterBundleKeys


class KeysTest(unittest.TestCase):
    '''
        Defines class KeysTest with attribute(s) and method(s).
        Tests ReporterBundleKeys logic.
    '''

    def test_dependency_keys(self) -> None:
        self.assertEqual(ReporterBundleKeys.DEPENDENCY_CHECKER, "checker")
        self.assertEqual(ReporterBundleKeys.DEPENDENCY_THEME, "theme")
        self.assertEqual(ReporterBundleKeys.DEPENDENCY_LOGGER, "logger")

    def test_option_keys(self) -> None:
        self.assertEqual(ReporterBundleKeys.OPTION_CHECKER, "checker")
        self.assertEqual(ReporterBundleKeys.OPTION_THEME, "theme")
        self.assertEqual(ReporterBundleKeys.OPTION_LOGGER, "logger")

    def test_get_dependency_to_type(self) -> None:
        dep_map = ReporterBundleKeys.get_dependency_to_type()
        self.assertIsInstance(dep_map, MappingProxyType)
        self.assertEqual(len(dep_map), 3)
        self.assertIs(dep_map[ReporterBundleKeys.DEPENDENCY_CHECKER], IChecker)
        self.assertIs(dep_map[ReporterBundleKeys.DEPENDENCY_THEME], IConsoleTheme)
        self.assertIs(dep_map[ReporterBundleKeys.DEPENDENCY_LOGGER], ILogger)

    def test_get_option_to_type(self) -> None:
        opt_map = ReporterBundleKeys.get_option_to_type()
        self.assertIsInstance(opt_map, MappingProxyType)
        self.assertEqual(len(opt_map), 3)
        self.assertIs(opt_map[ReporterBundleKeys.OPTION_CHECKER], CheckerBundleOptions)
        self.assertEqual(opt_map[ReporterBundleKeys.OPTION_THEME], Mapping[str, str])
        self.assertIs(opt_map[ReporterBundleKeys.OPTION_LOGGER], LoggerBundleOptions)


if __name__ == "__main__":
    unittest.main()
