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
    Unit tests for FileData class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock
from dataclasses import FrozenInstanceError

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.data import FileData
from ats_utilities.config_io.data_validator import FileDataValidator
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FileDataTest(unittest.TestCase):
    '''
        Defines class FileDataTest with attribute(s) and method(s).
        Tests FileData logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)

    def test_init_valid(self) -> None:
        """Tests successful FileData initialization."""
        data = FileData(
            file_path="/tmp/config.json",
            file_mode="r",
            context_bundle=self.mock_context
        )
        self.assertEqual(data.file_path, "/tmp/config.json")
        self.assertEqual(data.file_mode, "r")
        self.assertIs(data.context_bundle, self.mock_context)

    def test_immutability(self) -> None:
        """Tests that FileData is frozen and cannot be modified."""
        data = FileData(
            file_path="/tmp/config.json",
            file_mode="r",
            context_bundle=self.mock_context
        )
        with self.assertRaises(FrozenInstanceError):
            data.file_path = "/tmp/other.json"

    def test_slots(self) -> None:
        """Tests that FileData has slots and cannot have dynamic attributes."""
        data = FileData(
            file_path="/tmp/config.json",
            file_mode="r",
            context_bundle=self.mock_context
        )
        self.assertFalse(hasattr(data, "__dict__"))

    def test_to_dict(self) -> None:
        """Tests FileData to_dict method."""
        data = FileData(
            file_path="/tmp/config.json",
            file_mode="r",
            context_bundle=self.mock_context
        )
        expected = {
            "file_path": "/tmp/config.json",
            "file_mode": "r",
            "context_bundle": self.mock_context
        }
        self.assertEqual(data.to_dict(), expected)

    def test_validation_invalid_none(self) -> None:
        """Tests FileDataValidator with None values."""
        with self.assertRaises(ATSValueError):
            FileDataValidator.validate(
                FileData(
                    file_path=None,
                    file_mode="r",
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSValueError):
            FileDataValidator.validate(
                FileData(
                    file_path="/tmp/config.json",
                    file_mode=None,
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSValueError):
            FileDataValidator.validate(
                FileData(
                    file_path="/tmp/config.json",
                    file_mode="r",
                    context_bundle=None
                )
            )

    def test_validation_invalid_type(self) -> None:
        """Tests FileDataValidator with wrong types."""
        with self.assertRaises(ATSTypeError):
            FileDataValidator.validate(
                FileData(
                    file_path=123,
                    file_mode="r",
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSTypeError):
            FileDataValidator.validate(
                FileData(
                    file_path="/tmp/config.json",
                    file_mode=123,
                    context_bundle=self.mock_context
                )
            )
        with self.assertRaises(ATSTypeError):
            FileDataValidator.validate(
                FileData(
                    file_path="/tmp/config.json",
                    file_mode="r",
                    context_bundle="not-a-bundle"
                )
            )


if __name__ == "__main__":
    unittest.main()
