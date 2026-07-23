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
    Unit tests for CenterData class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError

from ats_utilities.splasher.data import CenterData
from ats_utilities.splasher.data_validator import CenterDataValidator
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_type_error import ATSTypeError


class CenterDataTest(unittest.TestCase):
    """Unit tests for CenterData and CenterDataValidator classes."""

    def test_slots(self) -> None:
        """Tests that CenterData has slots and cannot have dynamic attributes."""
        data = CenterData(
            columns=80,
            additional_shifter=2
        )
        self.assertFalse(hasattr(data, "__dict__"))

    def test_immutability(self) -> None:
        """Tests that CenterData is frozen and cannot be modified."""
        data = CenterData(
            columns=80,
            additional_shifter=2
        )
        with self.assertRaises(FrozenInstanceError):
            data.columns = 100  # type: ignore
        with self.assertRaises(FrozenInstanceError):
            data.additional_shifter = 5  # type: ignore

    def test_to_dict(self) -> None:
        """Tests CenterData to_dict method."""
        data = CenterData(
            columns=80,
            additional_shifter=2
        )
        expected = {
            "columns": 80,
            "additional_shifter": 2
        }
        self.assertEqual(data.to_dict(), expected)

    def test_validation_success(self) -> None:
        """Tests CenterDataValidator with valid input data."""
        data = CenterData(
            columns=80,
            additional_shifter=2
        )
        # Should not raise any exception
        CenterDataValidator.validate(data)

    def test_validation_invalid_none(self) -> None:
        """Tests CenterDataValidator with None values."""
        with self.assertRaises(ATSValueError):
            CenterDataValidator.validate(
                CenterData(
                    columns=None,  # type: ignore
                    additional_shifter=2
                )
            )
        with self.assertRaises(ATSValueError):
            CenterDataValidator.validate(
                CenterData(
                    columns=80,
                    additional_shifter=None  # type: ignore
                )
            )

    def test_validation_invalid_type(self) -> None:
        """Tests CenterDataValidator with wrong types."""
        with self.assertRaises(ATSTypeError):
            CenterDataValidator.validate(
                CenterData(
                    columns="80",  # type: ignore
                    additional_shifter=2
                )
            )
        with self.assertRaises(ATSTypeError):
            CenterDataValidator.validate(
                CenterData(
                    columns=80,
                    additional_shifter="2"  # type: ignore
                )
            )

    def test_validation_negative_values(self) -> None:
        """Tests CenterDataValidator with negative values."""
        with self.assertRaises(ATSValueError):
            CenterDataValidator.validate(
                CenterData(
                    columns=-80,
                    additional_shifter=2
                )
            )
        with self.assertRaises(ATSValueError):
            CenterDataValidator.validate(
                CenterData(
                    columns=80,
                    additional_shifter=-2
                )
            )


if __name__ == "__main__":
    unittest.main()
