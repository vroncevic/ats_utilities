# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
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
    Unit tests for ReporterDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.setup.dependencies import ReporterDependencies
from ats_utilities.reporter.setup.dep_validator import ReporterDependenciesValidator


class DepValidatorTest(unittest.TestCase):
    '''
        Defines class DepValidatorTest with attribute(s) and method(s).
        Tests ReporterDependenciesValidator logic.
    '''

    def test_validate_valid(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        deps: ReporterDependencies = {
            "checker": mock_checker,
            "theme": mock_theme,
            "logger": mock_logger
        }
        # Should not raise any error
        ReporterDependenciesValidator.validate(deps)

    def test_validate_none(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            ReporterDependenciesValidator.validate(None)  # type: ignore
        self.assertEqual(str(context.exception), "reporter_dependencies_validator::validate(...) - the dependencies must be provided")

    def test_validate_not_mapping(self) -> None:
        with self.assertRaises(ATSTypeError) as context:
            ReporterDependenciesValidator.validate("invalid")  # type: ignore
        self.assertEqual(str(context.exception), "reporter_dependencies_validator::validate(...) - the dependencies must be a Mapping")

    def test_validate_missing_dependency(self) -> None:
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        deps: ReporterDependencies = {
            "theme": mock_theme,
            "logger": mock_logger
        }  # type: ignore
        with self.assertRaises(ATSTypeError) as context:
            ReporterDependenciesValidator.validate(deps)
        self.assertEqual(str(context.exception), "reporter_dependencies_validator::validate(...) - the checker must be an instance of IChecker")

    def test_validate_invalid_dependency_type(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)

        deps: ReporterDependencies = {
            "checker": mock_checker,
            "theme": mock_theme,
            "logger": "invalid"  # type: ignore
        }
        with self.assertRaises(ATSTypeError) as context:
            ReporterDependenciesValidator.validate(deps)
        self.assertEqual(str(context.exception), "reporter_dependencies_validator::validate(...) - the logger must be an instance of ILogger")


if __name__ == "__main__":
    unittest.main()
