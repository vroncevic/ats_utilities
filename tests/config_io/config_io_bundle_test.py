# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock
from collections.abc import Mapping
from dataclasses import FrozenInstanceError

# Assuming the class is located in a module accessible via import
# Replace with the actual module import if necessary
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor

# Mock implementations of custom exceptions for isolated testing if needed,
# or let standard exceptions pass through based on validation module behavior.

class TestConfigIOBundle(unittest.TestCase):
    """Unit tests for the ConfigIOBundle dataclass."""

    def setUp(self) -> None:
        """Set up standard mock dependencies for a valid bundle."""
        self.valid_file_path = "/path/to/config.json"
        
        # Mocking a Mapping object (like a dict)
        self.valid_scheme = MagicMock(spec=Mapping)
        
        # Mocking interface classes
        self.valid_processor = MagicMock(spec=IConfigProcessor)
        self.valid_context_bundle = MagicMock(spec=ContextBundle)

    def test_successful_initialization(self) -> None:
        """Test that ConfigIOBundle initializes successfully with valid arguments."""
        bundle = ConfigIOBundle(
            file_path=self.valid_file_path,
            scheme=self.valid_scheme,
            processor=self.valid_processor,
            context_bundle=self.valid_context_bundle
        )
        
        self.assertEqual(bundle.file_path, self.valid_file_path)
        self.assertEqual(bundle.scheme, self.valid_scheme)
        self.assertEqual(bundle.processor, self.valid_processor)
        self.assertEqual(bundle.context_bundle, self.valid_context_bundle)
        self.assertEqual(bundle.READ_MODE, 'r')
        self.assertEqual(bundle.WRITE_MODE, 'w')

    def test_validation_fails_when_file_path_is_none(self) -> None:
        """Test validation error when file_path is None."""
        with self.assertRaises(Exception):  # Catching base Exception to cover ATSValueError
            ConfigIOBundle(
                file_path=None,  # type: ignore
                scheme=self.valid_scheme,
                processor=self.valid_processor,
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_file_path_is_invalid_type(self) -> None:
        """Test validation error when file_path is not a string."""
        with self.assertRaises(Exception):  # Covers ATSTypeError
            ConfigIOBundle(
                file_path=123,  # type: ignore
                scheme=self.valid_scheme,
                processor=self.valid_processor,
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_scheme_is_none(self) -> None:
        """Test validation error when scheme is None."""
        with self.assertRaises(Exception):
            ConfigIOBundle(
                file_path=self.valid_file_path,
                scheme=None,  # type: ignore
                processor=self.valid_processor,
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_scheme_is_invalid_type(self) -> None:
        """Test validation error when scheme does not implement Mapping."""
        with self.assertRaises(Exception):
            ConfigIOBundle(
                file_path=self.valid_file_path,
                scheme="not-a-mapping",  # type: ignore
                processor=self.valid_processor,
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_processor_is_none(self) -> None:
        """Test validation error when processor is None."""
        with self.assertRaises(Exception):
            ConfigIOBundle(
                file_path=self.valid_file_path,
                scheme=self.valid_scheme,
                processor=None,  # type: ignore
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_processor_is_invalid_type(self) -> None:
        """Test validation error when processor is not an IConfigProcessor."""
        with self.assertRaises(Exception):
            ConfigIOBundle(
                file_path=self.valid_file_path,
                scheme=self.valid_scheme,
                processor=MagicMock(),  # Plain Mock without IConfigProcessor spec
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_context_bundle_is_none(self) -> None:
        """Test validation error when context_bundle is None."""
        with self.assertRaises(Exception):
            ConfigIOBundle(
                file_path=self.valid_file_path,
                scheme=self.valid_scheme,
                processor=self.valid_processor,
                context_bundle=None,  # type: ignore
            )

    def test_validation_fails_when_context_bundle_is_invalid_type(self) -> None:
        """Test validation error when context_bundle is not a ContextBundle."""
        with self.assertRaises(Exception):
            ConfigIOBundle(
                file_path=self.valid_file_path,
                scheme=self.valid_scheme,
                processor=self.valid_processor,
                context_bundle=MagicMock()  # Plain Mock without ContextBundle spec
            )

    def test_to_dict(self) -> None:
        """Test that to_dict successfully exports all slot values to a dictionary."""
        bundle = ConfigIOBundle(
            file_path=self.valid_file_path,
            scheme=self.valid_scheme,
            processor=self.valid_processor,
            context_bundle=self.valid_context_bundle
        )
        
        expected_dict = {
            'file_path': self.valid_file_path,
            'scheme': self.valid_scheme,
            'processor': self.valid_processor,
            'context_bundle': self.valid_context_bundle
        }
        
        self.assertEqual(bundle.to_dict(), expected_dict)

    def test_is_frozen(self) -> None:
        """Test that modifying an attribute on the bundle raises an exception (frozen dataclass)."""
        bundle = ConfigIOBundle(
            file_path=self.valid_file_path,
            scheme=self.valid_scheme,
            processor=self.valid_processor,
            context_bundle=self.valid_context_bundle
        )
        
        with self.assertRaises(FrozenInstanceError if 'FrozenInstanceError' in globals() else Exception):
            bundle.file_path = "new/path.json"  # type: ignore


if __name__ == '__main__':
    unittest.main()
