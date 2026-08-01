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
    Unit tests for GeneratorOptionsValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.generation.setup.options import GeneratorOptions
from ats_utilities.generation.setup.opt_validator import GeneratorOptionsValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class GeneratorOptionsValidatorTest(unittest.TestCase):
    '''
        Defines class GeneratorOptionsValidatorTest with attribute(s) and method(s).
        Tests GeneratorOptionsValidator component logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

    def test_validate_valid(self) -> None:
        options = GeneratorOptions(context_bundle=self.mock_context)
        GeneratorOptionsValidator.validate(options)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            GeneratorOptionsValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            GeneratorOptionsValidator.validate("invalid")  # type: ignore

    def test_validate_invalid_option_types(self) -> None:
        options = GeneratorOptions(context_bundle="invalid")  # type: ignore
        with self.assertRaises(ATSTypeError):
            GeneratorOptionsValidator.validate(options)

    @patch("ats_utilities.generation.setup.opt_validator.GeneratorKeys.get_option_to_type")
    def test_validate_additional_options(self, mock_get_opt_to_type: MagicMock) -> None:
        from types import MappingProxyType
        mock_get_opt_to_type.return_value = MappingProxyType({
            "context_bundle": ContextBundle,
            "dummy_opt": str
        })
        
        # When dummy_opt is None
        options_none = GeneratorOptions(context_bundle=self.mock_context)
        options_none["dummy_opt"] = None  # type: ignore
        GeneratorOptionsValidator.validate(options_none)
        
        # When dummy_opt is not None (and matches type)
        options_val = GeneratorOptions(context_bundle=self.mock_context)
        options_val["dummy_opt"] = "hello"  # type: ignore
        GeneratorOptionsValidator.validate(options_val)

        # When dummy_opt has wrong type
        options_bad = GeneratorOptions(context_bundle=self.mock_context)
        options_bad["dummy_opt"] = 123  # type: ignore
        with self.assertRaises(ATSTypeError):
            GeneratorOptionsValidator.validate(options_bad)


if __name__ == "__main__":
    unittest.main()
