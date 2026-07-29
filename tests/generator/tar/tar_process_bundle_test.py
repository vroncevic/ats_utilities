# -*- coding: UTF-8 -*-

'''
Module
    tar_process_bundle_test.py
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
    Unit tests for the TarData dataclass and TarDataValidator.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError

from ats_utilities.generation.tar.data import TarData
from ats_utilities.generation.tar.data_validator import TarDataValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestTarProcessBundle(unittest.TestCase):
    """Unit tests for the TarData dataclass and TarDataValidator."""

    def setUp(self) -> None:
        """Set up standard parameters for a valid TarData configuration."""
        self.valid_params = {
            "archive_path": "/path/to/archive.tgz",
            "target_dir": "/path/to/target",
            "source_dir": "templates/core",
            "path_replacements": {"__name__": "my_module"},
            "exclude_patterns": ["*.pyc", "__pycache__"],
            "vals": {"author": "Vladimir", "version": "1.0.0"}
        }

    def test_successful_initialization(self) -> None:
        """Test successful initialization with valid type definitions."""
        bundle = TarData(**self.valid_params)

        self.assertEqual(bundle.archive_path, "/path/to/archive.tgz")
        self.assertEqual(bundle.target_dir, "/path/to/target")
        self.assertEqual(bundle.source_dir, "templates/core")
        self.assertEqual(bundle.path_replacements, {"__name__": "my_module"})
        self.assertEqual(bundle.exclude_patterns, ["*.pyc", "__pycache__"])
        self.assertEqual(bundle.vals, {"author": "Vladimir", "version": "1.0.0"})

    def test_immutability_frozen_slots(self) -> None:
        """Test that modifying a value after initialization raises FrozenInstanceError."""
        bundle = TarData(**self.valid_params)
        
        with self.assertRaises(FrozenInstanceError):
            bundle.archive_path = "/new/path.tgz"  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional initialization is restricted by kw_only config."""
        with self.assertRaises(TypeError):
            TarData(
                "/path/to/archive.tgz", 
                "/path/to/target", 
                "templates/core", 
                {"__name__": "my_module"}, 
                ["*.pyc"], 
                {"author": "Vladimir"}
            )

    def test_validation_missing_or_none_fields(self) -> None:
        """Test that providing a None value triggers a validation error hook."""
        fields_to_test = [
            "archive_path", "target_dir", "source_dir", 
            "path_replacements", "exclude_patterns", "vals"
        ]

        for field in fields_to_test:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None
                
                bundle = TarData(**invalid_params)
                with self.assertRaises(ATSValueError):
                    TarDataValidator.validate(bundle)

    def test_validation_type_mismatches(self) -> None:
        """Test that incorrect data types trigger validation errors."""
        type_mismatches = {
            "archive_path": 12345,                # Expected str
            "target_dir": ["/not/a/string"],      # Expected str
            "source_dir": {"not": "a string"},    # Expected str
            "path_replacements": "not a mapping", # Expected Mapping
            "exclude_patterns": 123456,           # Expected Sequence
            "vals": ["not", "a", "mapping"]       # Expected Mapping
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value
                
                bundle = TarData(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    TarDataValidator.validate(bundle)

    def test_to_dict(self) -> None:
        """Test that to_dict cleanly transforms the dataclass properties into a raw dictionary."""
        bundle = TarData(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params)
        self.assertEqual(set(exported_dict.keys()), set(bundle.__slots__))


if __name__ == '__main__':
    unittest.main()