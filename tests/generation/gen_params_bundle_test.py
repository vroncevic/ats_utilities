# -*- coding: UTF-8 -*-

'''
Module
    gen_params_bundle_test.py
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
    Unit tests for the GeneratorData dataclass and GeneratorDataValidator.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch
from dataclasses import FrozenInstanceError

from ats_utilities.generation.data import GeneratorData
from ats_utilities.generation.data_validator import GeneratorDataValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class TestGenParamsBundle(unittest.TestCase):
    """Unit tests for the GeneratorData dataclass and GeneratorDataValidator."""

    def setUp(self) -> None:
        """Set up standard parameters for a valid GeneratorData configuration."""
        self.archive_path = "/path/to/archive.tgz"
        self.target_dir = "/path/to/target_dir"
        self.template_key = "python_library"
        self.scheme_dict = {"author": "Vladimir", "license": "GPL"}
        self.scheme_path = "/path/to/scheme.json"
        self.template_values = {"NAME": "ats_utilities", "VERSION": "3.4.4"}

        self.valid_params_with_dict_scheme = {
            "archive_path": self.archive_path,
            "target_dir": self.target_dir,
            "template_key": self.template_key,
            "scheme": self.scheme_dict,
            "template_values": self.template_values
        }

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_successful_initialization_with_dict_scheme(self, mock_check_file: MagicMock) -> None:
        """Test successful validation with a dictionary scheme mapping."""
        bundle = GeneratorData(**self.valid_params_with_dict_scheme)

        self.assertEqual(bundle.archive_path, self.archive_path)
        self.assertEqual(bundle.target_dir, self.target_dir)
        self.assertEqual(bundle.template_key, self.template_key)
        self.assertEqual(bundle.scheme, self.scheme_dict)
        self.assertEqual(bundle.template_values, self.template_values)
        
        GeneratorDataValidator.validate(bundle)
        mock_check_file.assert_called_once_with(
            self.archive_path,
            "generator_data_validator::validate(...)",
            f"archive file does not exist: {self.archive_path}"
        )

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_successful_initialization_with_string_scheme(self, mock_check_file: MagicMock) -> None:
        """Test successful validation and secondary file existence validation for string schemes."""
        params = self.valid_params_with_dict_scheme.copy()
        params["scheme"] = self.scheme_path

        bundle = GeneratorData(**params)
        self.assertEqual(bundle.scheme, self.scheme_path)

        GeneratorDataValidator.validate(bundle)
        mock_check_file.assert_any_call(
            self.archive_path,
            "generator_data_validator::validate(...)",
            f"archive file does not exist: {self.archive_path}"
        )
        mock_check_file.assert_any_call(
            self.scheme_path,
            "generator_data_validator::validate(...)",
            f"scheme file does not exist: {self.scheme_path}"
        )
        self.assertEqual(mock_check_file.call_count, 2)

    def test_immutability_frozen_slots(self) -> None:
        """Test that altering a property post-initialization throws a FrozenInstanceError."""
        bundle = GeneratorData(**self.valid_params_with_dict_scheme)
        
        with self.assertRaises(FrozenInstanceError):
            bundle.target_dir = "/new/target/dir"  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional arguments are strictly barred under kw_only rules."""
        with self.assertRaises(TypeError):
            GeneratorData(
                self.archive_path,
                self.target_dir,
                self.template_key,
                self.scheme_dict,
                self.template_values
            )

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_validation_missing_or_none_fields(self, mock_check_file: MagicMock) -> None:
        """Test that passing None for any attribute triggers a validation hook exception."""
        fields = ["archive_path", "target_dir", "template_key", "scheme", "template_values"]

        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params_with_dict_scheme.copy()
                invalid_params[field] = None  # type: ignore
                
                bundle = GeneratorData(**invalid_params)
                with self.assertRaises(ATSValueError):
                    GeneratorDataValidator.validate(bundle)

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_validation_type_mismatches(self, mock_check_file: MagicMock) -> None:
        """Test that providing an incorrect type fails the type check constraints."""
        type_mismatches = {
            "archive_path": 12345,                  # Expected str
            "target_dir": ["/not/a/string"],        # Expected str
            "template_key": {"key": "not-a-str"},   # Expected str
            "scheme": 44.55,                        # Expected str or Mapping
            "template_values": "not-a-mapping"      # Expected Mapping
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params_with_dict_scheme.copy()
                invalid_params[field] = bad_value  # type: ignore
                
                bundle = GeneratorData(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    GeneratorDataValidator.validate(bundle)

    def test_to_dict(self) -> None:
        """Test that to_dict compiles the slot fields exactly into a standard dictionary mapping."""
        bundle = GeneratorData(**self.valid_params_with_dict_scheme)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params_with_dict_scheme)
        self.assertEqual(set(exported_dict.keys()), set(bundle.__slots__))


if __name__ == '__main__':
    unittest.main()
