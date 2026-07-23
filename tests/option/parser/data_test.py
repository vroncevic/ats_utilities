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
    Unit tests for ParserData class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.data import ParserData
from ats_utilities.option.parser.data_validator import ParserDataValidator
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_type_error import ATSTypeError


class ParserDataTest(unittest.TestCase):
    """Unit tests for ParserData and ParserDataValidator classes."""

    def setUp(self) -> None:
        """Set up context mock dependencies."""
        self.mock_context = unittest.mock.MagicMock(spec=ContextBundle)

    def test_slots(self) -> None:
        """Tests that ParserData has slots and cannot have dynamic attributes."""
        data = ParserData(
            prog="mytool",
            epilog="mytool copyright",
            description="mytool desc",
            context_bundle=self.mock_context
        )
        self.assertFalse(hasattr(data, "__dict__"))

    def test_immutability(self) -> None:
        """Tests that ParserData is frozen and cannot be modified."""
        data = ParserData(
            prog="mytool",
            epilog="mytool copyright",
            description="mytool desc",
            context_bundle=self.mock_context
        )
        with self.assertRaises(FrozenInstanceError):
            data.prog = "newtool"  # type: ignore
        with self.assertRaises(FrozenInstanceError):
            data.context_bundle = self.mock_context  # type: ignore

    def test_to_dict(self) -> None:
        """Tests ParserData to_dict method."""
        data = ParserData(
            prog="mytool",
            epilog="mytool copyright",
            description="mytool desc",
            context_bundle=self.mock_context
        )
        expected = {
            "prog": "mytool",
            "epilog": "mytool copyright",
            "description": "mytool desc",
            "context_bundle": self.mock_context
        }
        self.assertEqual(data.to_dict(), expected)

    def test_validation_success(self) -> None:
        """Tests ParserDataValidator with valid input data."""
        data = ParserData(
            prog="mytool",
            epilog="mytool copyright",
            description="mytool desc",
            context_bundle=self.mock_context
        )
        # Should not raise any exception
        ParserDataValidator.validate(data)

    def test_validation_invalid_none(self) -> None:
        """Tests ParserDataValidator with None values."""
        with self.assertRaises(ATSValueError):
            ParserDataValidator.validate(
                ParserData(
                    prog=None,  # type: ignore
                    epilog="mytool copyright",
                    description="mytool desc",
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSValueError):
            ParserDataValidator.validate(
                ParserData(
                    prog="mytool",
                    epilog=None,  # type: ignore
                    description="mytool desc",
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSValueError):
            ParserDataValidator.validate(
                ParserData(
                    prog="mytool",
                    epilog="mytool copyright",
                    description=None,  # type: ignore
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSValueError):
            ParserDataValidator.validate(
                ParserData(
                    prog="mytool",
                    epilog="mytool copyright",
                    description="mytool desc",
                    context_bundle=None  # type: ignore
                )
            )

    def test_validation_invalid_type(self) -> None:
        """Tests ParserDataValidator with wrong types."""
        with self.assertRaises(ATSTypeError):
            ParserDataValidator.validate(
                ParserData(
                    prog=123,  # type: ignore
                    epilog="mytool copyright",
                    description="mytool desc",
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSTypeError):
            ParserDataValidator.validate(
                ParserData(
                    prog="mytool",
                    epilog=123,  # type: ignore
                    description="mytool desc",
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSTypeError):
            ParserDataValidator.validate(
                ParserData(
                    prog="mytool",
                    epilog="mytool copyright",
                    description=123,  # type: ignore
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSTypeError):
            ParserDataValidator.validate(
                ParserData(
                    prog="mytool",
                    epilog="mytool copyright",
                    description="mytool desc",
                    context_bundle="not-a-bundle"  # type: ignore
                )
            )


if __name__ == "__main__":
    unittest.main()
