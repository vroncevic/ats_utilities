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
    Unit tests for OptionBundleDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.setup.dependencies import OptionBundleDependencies
from ats_utilities.option.setup.dep_validator import OptionBundleDependenciesValidator
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class DepValidatorTest(unittest.TestCase):
    '''
        Defines class DepValidatorTest with attribute(s) and method(s).
        Tests OptionBundleDependenciesValidator logic.
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
        deps: OptionBundleDependencies = {
            "strategy": self.mock_strategy,
            "context_bundle": self.mock_context
        }
        OptionBundleDependenciesValidator.validate(deps)

    def test_validate_none(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            OptionBundleDependenciesValidator.validate(None)
        self.assertEqual(str(context.exception), "option_bundle_dependencies_validator::validate(...) - the option bundle dependencies must be provided")

    def test_validate_not_mapping(self) -> None:
        with self.assertRaises(ATSTypeError) as context:
            OptionBundleDependenciesValidator.validate("invalid")
        self.assertEqual(str(context.exception), "option_bundle_dependencies_validator::validate(...) - the option bundle dependencies must be a Mapping")

    def test_validate_missing_dependency(self) -> None:
        deps: OptionBundleDependencies = {
            "strategy": self.mock_strategy
        }
        with self.assertRaises(ATSValueError) as context:
            OptionBundleDependenciesValidator.validate(deps)
        self.assertEqual(str(context.exception), "option_bundle_dependencies_validator::validate(...) - the context bundle must be provided")

    def test_validate_invalid_dependency_type(self) -> None:
        deps: OptionBundleDependencies = {
            "strategy": "invalid",
            "context_bundle": self.mock_context
        }
        with self.assertRaises(ATSTypeError) as context:
            OptionBundleDependenciesValidator.validate(deps)
        self.assertEqual(str(context.exception), "option_bundle_dependencies_validator::validate(...) - the strategy must be an instance of IParserStrategy")


if __name__ == "__main__":
    unittest.main()
