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
    Unit tests for ConfigIOBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.validator import ConfigIOBundleValidator


class ConfigIOValidatorTest(unittest.TestCase):
    '''
        Defines class ConfigIOValidatorTest with attribute(s) and method(s).
        Tests ConfigIOBundleValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_processor = MagicMock(spec=IConfigProcessor)
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

        self.valid_params = {
            "file_path": "/tmp/config.json",
            "processor": self.mock_processor,
            "context_bundle": self.mock_context
        }

    def test_validate_valid(self) -> None:
        bundle = ConfigIOBundle(**self.valid_params)
        ConfigIOBundleValidator.validate(bundle)

    def test_validate_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError):
            ConfigIOBundleValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ConfigIOBundleValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self) -> None:
        fields = ["file_path", "processor", "context_bundle"]

        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None  # type: ignore
                # Note: ConfigIOBundle constructor might not validate on init, so we test validator
                bundle = ConfigIOBundle(**invalid_params)
                with self.assertRaises(ATSValueError):
                    ConfigIOBundleValidator.validate(bundle)

    def test_validate_invalid_type(self) -> None:
        type_mismatches = {
            "file_path": 123,
            "processor": MagicMock(spec=ContextBundle),
            "context_bundle": MagicMock(spec=IConfigProcessor)
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value
                bundle = ConfigIOBundle(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    ConfigIOBundleValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
