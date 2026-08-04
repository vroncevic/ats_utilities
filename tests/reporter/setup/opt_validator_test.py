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
    Unit tests for ReporterBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.setup.options import CheckerBundleOptions
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.setup.options import LoggerBundleOptions
from ats_utilities.reporter.setup.options import ReporterBundleOptions
from ats_utilities.reporter.setup.opt_validator import ReporterBundleOptionsValidator


class OptValidatorTest(unittest.TestCase):
    '''
        Defines class OptValidatorTest with attribute(s) and method(s).
        Tests ReporterBundleOptionsValidator logic.
    '''

    def test_validate_valid(self) -> None:
        checker_opts: CheckerBundleOptions = {}
        logger_opts: LoggerBundleOptions = {
            "log_level": 20
        }
        theme_opts = {
            "success": "green"
        }

        opts: ReporterBundleOptions = {
            "checker": checker_opts,
            "theme": theme_opts,
            "logger": logger_opts
        }
        # Should not raise any error
        ReporterBundleOptionsValidator.validate(opts)

    def test_validate_none(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            ReporterBundleOptionsValidator.validate(None)  # type: ignore
        self.assertEqual(str(context.exception), "reporter_options_validator::validate(...) - the options must be provided")

    def test_validate_not_mapping(self) -> None:
        with self.assertRaises(ATSTypeError) as context:
            ReporterBundleOptionsValidator.validate("invalid")  # type: ignore
        self.assertEqual(str(context.exception), "reporter_options_validator::validate(...) - the options must be a Mapping")

    def test_validate_invalid_option_type(self) -> None:
        opts: ReporterBundleOptions = {
            "checker": "invalid"  # type: ignore
        }
        with self.assertRaises(ATSTypeError) as context:
            ReporterBundleOptionsValidator.validate(opts)
        self.assertEqual(str(context.exception), "reporter_options_validator::validate(...) - the checker must be an instance of CheckerBundleOptions")

    def test_validate_none_fields(self) -> None:
        opts: ReporterBundleOptions = {
            "checker": None,
            "theme": None,
            "logger": None
        }
        # Should not raise error
        ReporterBundleOptionsValidator.validate(opts)


if __name__ == "__main__":
    unittest.main()
