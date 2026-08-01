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
    Unit tests for TarDataValidator and TarMemberDataValidator.
'''

from __future__ import annotations

import unittest
from tarfile import TarFile, TarInfo
from unittest.mock import MagicMock

from ats_utilities.generation.tar.data import TarData, TarMemberData
from ats_utilities.generation.tar.data_validator import TarDataValidator, TarMemberDataValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class TarDataValidatorTest(unittest.TestCase):
    '''
        Defines class TarDataValidatorTest with attribute(s) and method(s).
        Tests TarDataValidator and TarMemberDataValidator component logic.
    '''

    def setUp(self) -> None:
        self.valid_tar_params = {
            "archive_path": "/path/to/archive.tgz",
            "target_dir": "/path/to/target",
            "source_dir": "templates/core",
            "path_replacements": {"__name__": "my_module"},
            "exclude_patterns": ["*.pyc"],
            "vals": {"author": "Vladimir"}
        }
        self.mock_tar = MagicMock(spec=TarFile)
        self.mock_member = MagicMock(spec=TarInfo)
        self.valid_member_params = {
            "tar": self.mock_tar,
            "member": self.mock_member,
            "dest_full_path": "/path/to/dest",
            "vals": {"author": "Vladimir"}
        }

    def test_validate_tar_data_valid(self) -> None:
        data = TarData(**self.valid_tar_params)
        TarDataValidator.validate(data)

    def test_validate_tar_data_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            TarDataValidator.validate(None)  # type: ignore

    def test_validate_tar_data_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            TarDataValidator.validate("invalid")  # type: ignore

    def test_validate_tar_data_missing_attributes(self) -> None:
        fields = ["archive_path", "target_dir", "source_dir", "path_replacements", "exclude_patterns", "vals"]
        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_tar_params.copy()
                invalid_params[field] = None  # type: ignore
                data = TarData(**invalid_params)
                with self.assertRaises(ATSValueError):
                    TarDataValidator.validate(data)

    def test_validate_tar_data_invalid_types(self) -> None:
        type_mismatches = {
            "archive_path": 123,
            "target_dir": 123,
            "source_dir": 123,
            "path_replacements": "not_a_mapping",
            "exclude_patterns": 123,
            "vals": "not_a_mapping"
        }
        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_tar_params.copy()
                invalid_params[field] = bad_value  # type: ignore
                data = TarData(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    TarDataValidator.validate(data)

    def test_validate_tar_member_data_valid(self) -> None:
        data = TarMemberData(**self.valid_member_params)
        TarMemberDataValidator.validate(data)

    def test_validate_tar_member_data_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            TarMemberDataValidator.validate(None)  # type: ignore

    def test_validate_tar_member_data_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            TarMemberDataValidator.validate("invalid")  # type: ignore

    def test_validate_tar_member_data_missing_attributes(self) -> None:
        fields = ["tar", "member", "dest_full_path", "vals"]
        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_member_params.copy()
                invalid_params[field] = None  # type: ignore
                data = TarMemberData(**invalid_params)
                with self.assertRaises(ATSValueError):
                    TarMemberDataValidator.validate(data)

    def test_validate_tar_member_data_invalid_types(self) -> None:
        type_mismatches = {
            "tar": "not_a_tarfile",
            "member": "not_a_tarinfo",
            "dest_full_path": 123,
            "vals": "not_a_mapping"
        }
        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_member_params.copy()
                invalid_params[field] = bad_value  # type: ignore
                data = TarMemberData(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    TarMemberDataValidator.validate(data)


if __name__ == "__main__":
    unittest.main()
