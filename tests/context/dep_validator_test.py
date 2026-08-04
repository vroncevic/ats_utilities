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
    Unit tests for ContextBundleDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.dep_validator import ContextBundleDependenciesValidator
from ats_utilities.context.dependencies import ContextBundleDependencies
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSValueError, ATSTypeError


class TestContextDependenciesValidator(unittest.TestCase):
    """Unit tests for the ContextBundleDependenciesValidator class."""

    def setUp(self) -> None:
        """Set up valid mock objects and parameters for dependencies validation."""
        self.mock_checker = MagicMock(spec=IChecker)
        self.mock_logger = MagicMock(spec=ILogger)
        self.mock_reporter = MagicMock(spec=IReporter)

        self.valid_dependencies = ContextBundleDependencies(
            checker=self.mock_checker,
            logger=self.mock_logger,
            reporter=self.mock_reporter,
            verbose=True
        )

    def test_successful_validation(self) -> None:
        """Test successful validation with all dependencies present and valid."""
        try:
            ContextBundleDependenciesValidator.validate(self.valid_dependencies)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error: {e}")

    def test_missing_dependencies_raises_value_error(self) -> None:
        """Test that validation fails with ATSValueError when dependencies dict is None or missing keys."""
        with self.assertRaises(ATSValueError):
            ContextBundleDependenciesValidator.validate(None)  # type: ignore

        # Test missing checker
        invalid_deps = self.valid_dependencies.copy()
        del invalid_deps['checker']
        with self.assertRaises(ATSValueError):
            ContextBundleDependenciesValidator.validate(invalid_deps)

    def test_invalid_type_raises_type_error(self) -> None:
        """Test that validation fails with ATSTypeError when attributes have incorrect types."""
        # Test invalid type for checker
        invalid_deps = self.valid_dependencies.copy()
        invalid_deps['checker'] = "not_a_checker"  # type: ignore
        with self.assertRaises(ATSTypeError):
            ContextBundleDependenciesValidator.validate(invalid_deps)

        # Test invalid type for verbose
        invalid_deps2 = self.valid_dependencies.copy()
        invalid_deps2['verbose'] = "not_a_bool"  # type: ignore
        with self.assertRaises(ATSTypeError):
            ContextBundleDependenciesValidator.validate(invalid_deps2)


if __name__ == '__main__':
    unittest.main()
