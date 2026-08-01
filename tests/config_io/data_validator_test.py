# -*- coding: UTF-8 -*-

'''
Module
    data_validator_test.py
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
    Unit tests for FileDataValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.config_io.data import FileData
from ats_utilities.config_io.data_validator import FileDataValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class FileDataValidatorTest(unittest.TestCase):
    '''
        Defines class FileDataValidatorTest with attribute(s) and method(s).
        Tests FileDataValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

    def test_validate_valid(self) -> None:
        data = FileData(
            file_path="/path/to/file",
            file_mode="r",
            context_bundle=self.mock_context
        )
        FileDataValidator.validate(data)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            FileDataValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            FileDataValidator.validate("invalid")  # type: ignore

    def test_validate_missing_attributes(self) -> None:
        with self.assertRaises(ATSValueError):
            data = FileData(
                file_path=None,  # type: ignore
                file_mode="r",
                context_bundle=self.mock_context
            )
            FileDataValidator.validate(data)

        with self.assertRaises(ATSValueError):
            data = FileData(
                file_path="/path/to/file",
                file_mode=None,  # type: ignore
                context_bundle=self.mock_context
            )
            FileDataValidator.validate(data)

        with self.assertRaises(ATSValueError):
            data = FileData(
                file_path="/path/to/file",
                file_mode="r",
                context_bundle=None  # type: ignore
            )
            FileDataValidator.validate(data)

    def test_validate_invalid_attribute_types(self) -> None:
        with self.assertRaises(ATSTypeError):
            data = FileData(
                file_path=123,  # type: ignore
                file_mode="r",
                context_bundle=self.mock_context
            )
            FileDataValidator.validate(data)

        with self.assertRaises(ATSTypeError):
            data = FileData(
                file_path="/path/to/file",
                file_mode=123,  # type: ignore
                context_bundle=self.mock_context
            )
            FileDataValidator.validate(data)

        with self.assertRaises(ATSTypeError):
            data = FileData(
                file_path="/path/to/file",
                file_mode="r",
                context_bundle="invalid"  # type: ignore
            )
            FileDataValidator.validate(data)

    def test_validate_empty_attributes(self) -> None:
        with self.assertRaises(ATSValueError):
            data = FileData(
                file_path="",
                file_mode="r",
                context_bundle=self.mock_context
            )
            FileDataValidator.validate(data)

        with self.assertRaises(ATSValueError):
            data = FileData(
                file_path="/path/to/file",
                file_mode="",
                context_bundle=self.mock_context
            )
            FileDataValidator.validate(data)


if __name__ == "__main__":
    unittest.main()
