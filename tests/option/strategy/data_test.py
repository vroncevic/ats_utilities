# -*- coding: UTF-8 -*-

'''
Module
    data_test.py
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
    Unit tests for StrategyData class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from types import MappingProxyType

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.engine import ArgParser
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.option.strategy.data_validator import StrategyDataValidator
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_type_error import ATSTypeError


class StrategyDataTest(unittest.TestCase):
    """Unit tests for StrategyData and StrategyDataValidator classes."""

    def setUp(self) -> None:
        """Set up context mock dependencies."""
        self.mock_context = unittest.mock.MagicMock(spec=ContextBundle)
        self.valid_params = MappingProxyType({"verbose": "store_true"})

    def test_slots(self) -> None:
        """Tests that StrategyData has slots and cannot have dynamic attributes."""
        data = StrategyData(
            parameters=self.valid_params,
            context_bundle=self.mock_context,
            parser_class=ArgParser
        )
        self.assertFalse(hasattr(data, "__dict__"))

    def test_immutability(self) -> None:
        """Tests that StrategyData is frozen and cannot be modified."""
        data = StrategyData(
            parameters=self.valid_params,
            context_bundle=self.mock_context,
            parser_class=ArgParser
        )
        with self.assertRaises(FrozenInstanceError):
            data.parameters = MappingProxyType({})  # type: ignore
        with self.assertRaises(FrozenInstanceError):
            data.parser_class = object  # type: ignore

    def test_to_dict(self) -> None:
        """Tests StrategyData to_dict method."""
        data = StrategyData(
            parameters=self.valid_params,
            context_bundle=self.mock_context,
            parser_class=ArgParser
        )
        expected = {
            "parameters": self.valid_params,
            "context_bundle": self.mock_context,
            "parser_class": ArgParser
        }
        self.assertEqual(data.to_dict(), expected)

    def test_validation_success(self) -> None:
        """Tests StrategyDataValidator with valid input data."""
        data = StrategyData(
            parameters=self.valid_params,
            context_bundle=self.mock_context,
            parser_class=ArgParser
        )
        # Should not raise any exception
        StrategyDataValidator.validate(data)

    def test_validation_invalid_none(self) -> None:
        """Tests StrategyDataValidator with None values."""
        with self.assertRaises(ATSValueError):
            StrategyDataValidator.validate(
                StrategyData(
                    parameters=None,  # type: ignore
                    context_bundle=self.mock_context,
                    parser_class=ArgParser
                )
            )
        with self.assertRaises(ATSValueError):
            StrategyDataValidator.validate(
                StrategyData(
                    parameters=self.valid_params,
                    context_bundle=None,  # type: ignore
                    parser_class=ArgParser
                )
            )
        with self.assertRaises(ATSValueError):
            StrategyDataValidator.validate(
                StrategyData(
                    parameters=self.valid_params,
                    context_bundle=self.mock_context,
                    parser_class=None  # type: ignore
                )
            )

    def test_validation_invalid_type(self) -> None:
        """Tests StrategyDataValidator with wrong types."""
        with self.assertRaises(ATSTypeError):
            StrategyDataValidator.validate(
                StrategyData(
                    parameters="not-a-mapping",  # type: ignore
                    context_bundle=self.mock_context,
                    parser_class=ArgParser
                )
            )
        with self.assertRaises(ATSTypeError):
            StrategyDataValidator.validate(
                StrategyData(
                    parameters=self.valid_params,
                    context_bundle="not-a-bundle",  # type: ignore
                    parser_class=ArgParser
                )
            )
        with self.assertRaises(ATSTypeError):
            StrategyDataValidator.validate(
                StrategyData(
                    parameters=self.valid_params,
                    context_bundle=self.mock_context,
                    parser_class="not-a-class"  # type: ignore
                )
            )

    def test_validation_invalid_parser_subclass(self) -> None:
        """Tests StrategyDataValidator with class that is not subclass of IArgParser."""
        class DummyClass:
            pass

        with self.assertRaises(ATSValueError):
            StrategyDataValidator.validate(
                StrategyData(
                    parameters=self.valid_params,
                    context_bundle=self.mock_context,
                    parser_class=DummyClass  # type: ignore
                )
            )


if __name__ == "__main__":
    unittest.main()
