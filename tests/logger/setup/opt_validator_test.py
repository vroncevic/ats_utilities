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
    Unit tests for LoggerOptionsValidator class.
'''

from __future__ import annotations

import unittest

from ats_utilities.logger.setup.options import LoggerOptions
from ats_utilities.logger.setup.opt_validator import LoggerOptionsValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class LoggerOptionsValidatorTest(unittest.TestCase):
    '''
        Defines class LoggerOptionsValidatorTest with attribute(s) and method(s).
        Tests LoggerOptionsValidator component logic.
    '''

    def test_validate_valid(self) -> None:
        options = LoggerOptions(log_file="test.log", log_level=10)
        LoggerOptionsValidator.validate(options)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            LoggerOptionsValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            LoggerOptionsValidator.validate("invalid")  # type: ignore

    def test_validate_invalid_option_types(self) -> None:
        options = LoggerOptions(log_file=123)  # type: ignore
        with self.assertRaises(ATSTypeError):
            LoggerOptionsValidator.validate(options)


if __name__ == "__main__":
    unittest.main()
