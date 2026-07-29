# -*- coding: UTF-8 -*-

'''
Module
    tar_process_member_bundle_test.py
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
    Unit tests for the TarMemberData dataclass and TarMemberDataValidator.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from tarfile import TarFile, TarInfo
from unittest.mock import MagicMock

from ats_utilities.generation.tar.data import TarMemberData
from ats_utilities.generation.tar.data_validator import TarMemberDataValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class TestTarProcessMemberBundle(unittest.TestCase):
    """Unit tests for the TarMemberData dataclass and TarMemberDataValidator."""

    def setUp(self) -> None:
        """Set up valid mock objects and parameters for bundle instantiation."""
        self.mock_tar = MagicMock(spec=TarFile)
        self.mock_member = MagicMock(spec=TarInfo)
        self.valid_dest_path = "/absolute/target/dir/file.txt"
        self.valid_vals = {"key": "value", "project": "ats_utilities"}

        self.valid_params = {
            "tar": self.mock_tar,
            "member": self.mock_member,
            "dest_full_path": self.valid_dest_path,
            "vals": self.valid_vals
        }

    def test_successful_initialization(self) -> None:
        """Test successful initialization when all parameters match types and constraints."""
        bundle = TarMemberData(**self.valid_params)

        self.assertEqual(bundle.tar, self.mock_tar)
        self.assertEqual(bundle.member, self.mock_member)
        self.assertEqual(bundle.dest_full_path, self.valid_dest_path)
        self.assertEqual(bundle.vals, self.valid_vals)

    def test_immutability_frozen_slots(self) -> None:
        """Test that altering a property post-initialization throws a FrozenInstanceError."""
        bundle = TarMemberData(**self.valid_params)
        
        with self.assertRaises(FrozenInstanceError):
            bundle.dest_full_path = "/attempt/new/path.txt"  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional arguments are barred under kw_only configuration rules."""
        with self.assertRaises(TypeError):
            # Attempting positional construction should raise a TypeError
            TarMemberData(
                self.mock_tar,
                self.mock_member, 
                self.valid_dest_path, 
                self.valid_vals
            )

    def test_validation_missing_or_none_fields(self) -> None:
        """Test that passing None for any attribute triggers a validation hook exception."""
        fields = ["tar", "member", "dest_full_path", "vals"]

        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None  # type: ignore
                
                bundle = TarMemberData(**invalid_params)
                with self.assertRaises(ATSValueError):
                    TarMemberDataValidator.validate(bundle)

    def test_validation_type_mismatches(self) -> None:
        """Test that providing an incorrect type fails the type check constraints."""
        type_mismatches = {
            "tar": "not a TarFile instance",           # Expected TarFile
            "member": 12345,                            # Expected TarInfo
            "dest_full_path": ["/not/a/raw/string"],   # Expected str
            "vals": ["not", "a", "mapping"]             # Expected Mapping
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value  # type: ignore
                
                bundle = TarMemberData(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    TarMemberDataValidator.validate(bundle)

    def test_to_dict(self) -> None:
        """Test that to_dict compiles the slot fields exactly into a standard dictionary mapping."""
        bundle = TarMemberData(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params)
        self.assertEqual(set(exported_dict.keys()), set(bundle.__slots__))


if __name__ == '__main__':
    unittest.main()
