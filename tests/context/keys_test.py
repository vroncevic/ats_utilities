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
    Unit tests for ContextKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.context.keys import ContextKeys
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.setup.options import CheckerOptions
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.setup.options import ReporterOptions
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.setup.options import LoggerOptions


class TestContextKeys(unittest.TestCase):
    """Unit tests for the ContextKeys class."""

    def test_get_dependency_to_type(self) -> None:
        """Test get_dependency_to_type returns correct MappingProxyType with all dependency classes."""
        dep_mapping = ContextKeys.get_dependency_to_type()
        self.assertIsInstance(dep_mapping, MappingProxyType)

        self.assertEqual(dep_mapping.get(ContextKeys.DEPENDENCY_CHECKER), IChecker)
        self.assertEqual(dep_mapping.get(ContextKeys.DEPENDENCY_LOGGER), ILogger)
        self.assertEqual(dep_mapping.get(ContextKeys.DEPENDENCY_REPORTER), IReporter)
        self.assertEqual(dep_mapping.get(ContextKeys.DEPENDENCY_VERBOSE), bool)

    def test_get_option_to_type(self) -> None:
        """Test get_option_to_type returns correct MappingProxyType with all option types."""
        opt_mapping = ContextKeys.get_option_to_type()
        self.assertIsInstance(opt_mapping, MappingProxyType)

        self.assertEqual(opt_mapping.get(ContextKeys.OPTION_CHECKER), CheckerOptions)
        self.assertEqual(opt_mapping.get(ContextKeys.OPTION_LOGGER), LoggerOptions)
        self.assertEqual(opt_mapping.get(ContextKeys.OPTION_REPORTER), ReporterOptions)
        self.assertEqual(opt_mapping.get(ContextKeys.OPTION_VERBOSE), bool)


if __name__ == '__main__':
    unittest.main()
