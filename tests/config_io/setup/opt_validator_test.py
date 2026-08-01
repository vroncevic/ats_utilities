# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
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
    Unit tests for ConfigIOOptionsValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.config_io.setup.options import ConfigIOOptions
from ats_utilities.config_io.setup.opt_validator import ConfigIOOptionsValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class ConfigIOOptionsValidatorTest(unittest.TestCase):
    '''
        Defines class ConfigIOOptionsValidatorTest with attribute(s) and method(s).
        Tests ConfigIOOptionsValidator component logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

    def test_validate_valid(self) -> None:
        options = ConfigIOOptions(
            file_path="/path/to/file",
            scheme={"some": "val"},
            context_bundle=self.mock_context
        )
        ConfigIOOptionsValidator.validate(options)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            ConfigIOOptionsValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            ConfigIOOptionsValidator.validate("not_a_mapping")  # type: ignore

    def test_validate_invalid_option_types(self) -> None:
        options = ConfigIOOptions(
            file_path=123,  # type: ignore
            scheme={"some": "val"},
            context_bundle=self.mock_context
        )
        with self.assertRaises(ATSTypeError):
            ConfigIOOptionsValidator.validate(options)

    def test_validate_none_fields(self) -> None:
        options = ConfigIOOptions(
            file_path=None,
            scheme=None,
            context_bundle=self.mock_context
        )
        ConfigIOOptionsValidator.validate(options)


if __name__ == "__main__":
    unittest.main()
