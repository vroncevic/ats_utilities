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
    Unit tests for StrategyDataValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.option.strategy.data_validator import StrategyDataValidator
from ats_utilities.option.underlying.iunderlying import IUnderlyingParser
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class StrategyDataValidatorTest(unittest.TestCase):
    '''
        Defines class StrategyDataValidatorTest with attribute(s) and method(s).
        Tests StrategyDataValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

        self.mock_parser = MagicMock(spec=IUnderlyingParser)

    def test_validate_valid(self) -> None:
        data = StrategyData(
            context_bundle=self.mock_context,
            parser=self.mock_parser
        )
        # Should not raise any error
        StrategyDataValidator.validate(data)

    def test_validate_none(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            StrategyDataValidator.validate(None)  # type: ignore
        self.assertEqual(str(context.exception), "strategy_data_validator::validate(...) - the strategy data must be provided")

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError) as context:
            StrategyDataValidator.validate(object())  # type: ignore
        self.assertEqual(str(context.exception), "strategy_data_validator::validate(...) - the strategy data must be an instance of StrategyData")

    def test_validate_missing_fields(self) -> None:
        with self.assertRaises(ATSValueError) as context:
            data = StrategyData(context_bundle=None, parser=self.mock_parser)  # type: ignore
            StrategyDataValidator.validate(data)
        self.assertEqual(str(context.exception), "strategy_data_validator::validate(...) - the context bundle must be provided")

        with self.assertRaises(ATSValueError) as context:
            data = StrategyData(context_bundle=self.mock_context, parser=None)  # type: ignore
            StrategyDataValidator.validate(data)
        self.assertEqual(str(context.exception), "strategy_data_validator::validate(...) - the parser must be provided")

    def test_validate_invalid_field_types(self) -> None:
        with self.assertRaises(ATSTypeError) as context:
            data = StrategyData(context_bundle="not a context", parser=self.mock_parser)  # type: ignore
            StrategyDataValidator.validate(data)
        self.assertEqual(str(context.exception), "strategy_data_validator::validate(...) - the context bundle must be a ContextBundle instance")

        with self.assertRaises(ATSTypeError) as context:
            data = StrategyData(context_bundle=self.mock_context, parser="not a parser")  # type: ignore
            StrategyDataValidator.validate(data)
        self.assertEqual(str(context.exception), "strategy_data_validator::validate(...) - the parser must be an instance of IUnderlyingParser")


if __name__ == "__main__":
    unittest.main()
