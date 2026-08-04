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
    Unit tests for OptionBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.validator import OptionBundleValidator
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class OptionValidatorTest(unittest.TestCase):
    '''
        Defines class OptionValidatorTest with attribute(s) and method(s).
        Tests OptionBundleValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_strategy = MagicMock(spec=IParserStrategy)
        self.mock_strategy.is_initialized.return_value = True
        
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

    def test_validate_valid(self) -> None:
        bundle = OptionBundle(
            strategy=self.mock_strategy,
            context_bundle=self.mock_context
        )
        OptionBundleValidator.validate(bundle)

    def test_validate_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            OptionBundleValidator.validate(None)
        self.assertEqual(str(context.exception), "option_bundle_validator::validate(...) - the option bundle must be provided")

        with self.assertRaises(ATSTypeError) as context:
            OptionBundleValidator.validate(object())
        self.assertEqual(str(context.exception), "option_bundle_validator::validate(...) - the option bundle must be an instance of OptionBundle")

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            bundle = OptionBundle(strategy=None, context_bundle=self.mock_context)
            OptionBundleValidator.validate(bundle)
        self.assertEqual(str(context.exception), "option_bundle_validator::validate(...) - the strategy must be provided")

        with self.assertRaises(ATSValueError) as context:
            bundle = OptionBundle(strategy=self.mock_strategy, context_bundle=None)
            OptionBundleValidator.validate(bundle)
        self.assertEqual(str(context.exception), "option_bundle_validator::validate(...) - the context bundle must be provided")

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError) as context:
            bundle = OptionBundle(strategy="not a strategy", context_bundle=self.mock_context)
            OptionBundleValidator.validate(bundle)
        self.assertEqual(str(context.exception), "option_bundle_validator::validate(...) - the strategy must be an IParserStrategy instance")

        with self.assertRaises(ATSTypeError) as context:
            bundle = OptionBundle(strategy=self.mock_strategy, context_bundle="not a context")
            OptionBundleValidator.validate(bundle)
        self.assertEqual(str(context.exception), "option_bundle_validator::validate(...) - the context bundle must be a ContextBundle instance")


if __name__ == "__main__":
    unittest.main()
