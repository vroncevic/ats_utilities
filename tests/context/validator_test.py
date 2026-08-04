# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Unit tests for ContextBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSValueError, ATSTypeError


class TestContextValidator(unittest.TestCase):
    """Unit tests for the ContextBundleValidator class."""

    def setUp(self) -> None:
        """Set up standard context bundle mocks."""
        self.mock_checker = MagicMock(spec=IChecker)
        self.mock_logger = MagicMock(spec=ILogger)
        self.mock_reporter = MagicMock(spec=IReporter)

        self.valid_params = {
            "checker": self.mock_checker,
            "logger": self.mock_logger,
            "reporter": self.mock_reporter,
            "verbose": True
        }

    def test_validate_valid(self) -> None:
        """Test validation succeeds with a valid ContextBundle."""
        bundle = ContextBundle(**self.valid_params)
        try:
            ContextBundleValidator.validate(bundle)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error: {e}")

    def test_validate_invalid_bundle(self) -> None:
        """Test validation fails when bundle itself is None or wrong type."""
        with self.assertRaises(ATSValueError):
            ContextBundleValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ContextBundleValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self) -> None:
        """Test validation fails when a required field is None."""
        fields = ["checker", "logger", "reporter", "verbose"]

        for field in fields:
            with self.subTest(field=field):
                mocks = self.valid_params.copy()
                mocks[field] = None  # type: ignore
                bundle = ContextBundle.__new__(ContextBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                with self.assertRaises(ATSValueError):
                    ContextBundleValidator.validate(bundle)

    def test_validate_invalid_type(self) -> None:
        """Test validation fails when a field has an incorrect type."""
        type_mismatches = {
            "checker": "not_a_checker",
            "logger": "not_a_logger",
            "reporter": "not_a_reporter",
            "verbose": "not_a_bool"
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                mocks = self.valid_params.copy()
                mocks[field] = bad_value
                bundle = ContextBundle.__new__(ContextBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                with self.assertRaises(ATSTypeError):
                    ContextBundleValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
