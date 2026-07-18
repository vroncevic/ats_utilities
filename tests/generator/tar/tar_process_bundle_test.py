# -*- coding: UTF-8 -*-

import unittest
from dataclasses import FrozenInstanceError
from collections.abc import Mapping, Sequence

# Adjust imports according to your project structure
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

class TestTarProcessBundle(unittest.TestCase):
    """Unit tests for the TarProcessBundle dataclass."""

    def setUp(self) -> None:
        """Set up standard parameters for a valid TarProcessBundle configuration."""
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
        bundle = TarProcessBundle(**self.valid_params)

        self.assertEqual(bundle.archive_path, "/path/to/archive.tgz")
        self.assertEqual(bundle.target_dir, "/path/to/target")
        self.assertEqual(bundle.source_dir, "templates/core")
        self.assertEqual(bundle.path_replacements, {"__name__": "my_module"})
        self.assertEqual(bundle.exclude_patterns, ["*.pyc", "__pycache__"])
        self.assertEqual(bundle.vals, {"author": "Vladimir", "version": "1.0.0"})

    def test_immutability_frozen_slots(self) -> None:
        """Test that modifying a value after initialization raises FrozenInstanceError."""
        bundle = TarProcessBundle(**self.valid_params)
        
        with self.assertRaises(FrozenInstanceError):
            bundle.archive_path = "/new/path.tgz"  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional initialization is restricted by kw_only config."""
        with self.assertRaises(TypeError):
            # Attempt to instantiate via positional parameters instead of keywords
            TarProcessBundle(
                # pyrefly: ignore [unexpected-positional-argument]
                "/path/to/archive.tgz", 
                # pyrefly: ignore [unexpected-positional-argument]
                "/path/to/target", 
                # pyrefly: ignore [unexpected-positional-argument]
                "templates/core", 
                # pyrefly: ignore [unexpected-positional-argument]
                {"__name__": "my_module"}, 
                # pyrefly: ignore [unexpected-positional-argument]
                ["*.pyc"], 
                # pyrefly: ignore [unexpected-positional-argument]
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
                
                with self.assertRaises(Exception):  # Catches value or check errors from not_none
                    TarProcessBundle(**invalid_params)

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
                
                with self.assertRaises(ATSTypeError):  # Catches check errors from istype
                    TarProcessBundle(
                        archive_path=invalid_params["archive_path"],
                        target_dir=invalid_params["target_dir"],
                        source_dir=invalid_params["source_dir"],
                        path_replacements=invalid_params["path_replacements"],
                        exclude_patterns=invalid_params["exclude_patterns"],
                        vals=invalid_params["vals"]
                    )

    def test_to_dict(self) -> None:
        """Test that to_dict cleanly transforms the dataclass properties into a raw dictionary."""
        bundle = TarProcessBundle(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params)
        # Ensure it handles extraction via slots definition boundaries explicitly
        self.assertEqual(set(exported_dict.keys()), set(bundle.__slots__))


if __name__ == '__main__':
    unittest.main()