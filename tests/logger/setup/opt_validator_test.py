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
    Unit tests for LoggerBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from ats_utilities.logger.setup.options import LoggerBundleOptions
from ats_utilities.logger.setup.opt_validator import LoggerBundleOptionsValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class LoggerOptionsValidatorTest(unittest.TestCase):
    '''
        Defines class LoggerOptionsValidatorTest with attribute(s) and method(s).
        Tests LoggerBundleOptionsValidator component logic.
    '''

    def test_validate_valid(self) -> None:
        options = LoggerBundleOptions(log_file="test.log", log_level=10)
        LoggerBundleOptionsValidator.validate(options)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            LoggerBundleOptionsValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            LoggerBundleOptionsValidator.validate("invalid")  # type: ignore

    def test_validate_invalid_option_types(self) -> None:
        options = LoggerBundleOptions(log_file=123)  # type: ignore
        with self.assertRaises(ATSTypeError):
            LoggerBundleOptionsValidator.validate(options)


if __name__ == "__main__":
    unittest.main()
