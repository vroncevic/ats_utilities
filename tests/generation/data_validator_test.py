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
    Unit tests for GeneratorDataValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.generation.data import GeneratorData
from ats_utilities.generation.data_validator import GeneratorDataValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class GeneratorDataValidatorTest(unittest.TestCase):
    '''
        Defines class GeneratorDataValidatorTest with attribute(s) and method(s).
        Tests GeneratorDataValidator component logic.
    '''

    def setUp(self) -> None:
        self.valid_params = {
            "archive_path": "/path/to/archive.tgz",
            "target_dir": "/path/to/target",
            "template_key": "python_library",
            "scheme": {"author": "Vladimir"},
            "template_values": {"NAME": "ats_utilities"}
        }

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_validate_valid_dict_scheme(self, mock_check_exists: MagicMock) -> None:
        data = GeneratorData(**self.valid_params)
        GeneratorDataValidator.validate(data)
        mock_check_exists.assert_called_once_with(
            "/path/to/archive.tgz",
            "generator_data_validator::validate(...)",
            "the archive file does not exist"
        )

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_validate_valid_str_scheme(self, mock_check_exists: MagicMock) -> None:
        params = self.valid_params.copy()
        params["scheme"] = "/path/to/scheme.json"
        data = GeneratorData(**params)
        GeneratorDataValidator.validate(data)
        self.assertEqual(mock_check_exists.call_count, 2)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            GeneratorDataValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            GeneratorDataValidator.validate("not_generator_data")

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_validate_missing_attributes(self, mock_check_exists: MagicMock) -> None:
        fields = ["archive_path", "target_dir", "template_key", "scheme", "template_values"]
        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None
                data = GeneratorData(**invalid_params)
                with self.assertRaises(ATSValueError):
                    GeneratorDataValidator.validate(data)

    @patch("ats_utilities.generation.data_validator.check_file_exists")
    def test_validate_invalid_types(self, mock_check_exists: MagicMock) -> None:
        type_mismatches = {
            "archive_path": 123,
            "target_dir": 123,
            "template_key": 123,
            "scheme": 123,
            "template_values": "not_a_mapping"
        }
        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value
                data = GeneratorData(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    GeneratorDataValidator.validate(data)


if __name__ == "__main__":
    unittest.main()
