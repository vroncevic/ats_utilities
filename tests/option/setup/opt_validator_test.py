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
    Unit tests for OptionBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.setup.options import OptionBundleOptions
from ats_utilities.option.setup.opt_validator import OptionBundleOptionsValidator
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class OptValidatorTest(unittest.TestCase):
    '''
        Defines class OptValidatorTest with attribute(s) and method(s).
        Tests OptionBundleOptionsValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

        self.valid_params = {
            "ats_name": "mytool",
            "ats_version": "1.0.0",
            "ats_licence": "GPLv3",
            "ats_build_date": "2026-08-01"
        }

    def test_validate_valid(self) -> None:
        opts: OptionBundleOptions = {
            "parameters": self.valid_params,
            "context_bundle": self.mock_context
        }
        # Should not raise error
        OptionBundleOptionsValidator.validate(opts)

    def test_validate_none(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            OptionBundleOptionsValidator.validate(None)
        self.assertEqual(str(context.exception), "option_bundle_options_validator::validate(...) - the option bundle options must be provided")

    def test_validate_not_mapping(self) -> None:
        with self.assertRaises(ATSTypeError) as context:
            OptionBundleOptionsValidator.validate("invalid")
        self.assertEqual(str(context.exception), "option_bundle_options_validator::validate(...) - the option bundle options must be a Mapping")

    def test_validate_missing_parameter(self) -> None:
        opts: OptionBundleOptions = {
            "context_bundle": self.mock_context
        }
        with self.assertRaises(ATSValueError) as context:
            OptionBundleOptionsValidator.validate(opts)
        self.assertEqual(str(context.exception), "option_bundle_options_validator::validate(...) - the parameters must be provided")

    def test_validate_missing_required_config_key(self) -> None:
        invalid_params = {
            "ats_name": "mytool"
            # missing version, licence, build_date
        }
        opts: OptionBundleOptions = {
            "parameters": invalid_params,
            "context_bundle": self.mock_context
        }
        with self.assertRaises(ATSValueError) as context:
            OptionBundleOptionsValidator.validate(opts)
        self.assertIn("the missing configuration keys", str(context.exception))


if __name__ == "__main__":
    unittest.main()
