# -*- coding: UTF-8 -*-

'''
Module
    dependencies_test.py
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
    Unit tests for ReporterDependencies TypedDict.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.setup.dependencies import ReporterDependencies


class DependenciesTest(unittest.TestCase):
    '''
        Defines class DependenciesTest with attribute(s) and method(s).
        Tests ReporterDependencies structure.
    '''

    def test_dependencies_structure(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        deps: ReporterDependencies = {
            "checker": mock_checker,
            "theme": mock_theme,
            "logger": mock_logger
        }
        self.assertIs(deps["checker"], mock_checker)
        self.assertIs(deps["theme"], mock_theme)
        self.assertIs(deps["logger"], mock_logger)


if __name__ == "__main__":
    unittest.main()
