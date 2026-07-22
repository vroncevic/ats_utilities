# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock
from dataclasses import FrozenInstanceError

# Adjust imports according to your project structure
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.context.bundle import ContextBundle


class TestConfFileBundle(unittest.TestCase):
    """Unit tests for the ConfFileBundle dataclass."""

    def setUp(self) -> None:
        """Set up standard mock dependencies for a valid bundle instance."""
        self.valid_file_path = "/path/to/config.txt"
        self.valid_file_mode = "r"
        self.valid_context_bundle = MagicMock(spec=ContextBundle)

    def test_successful_initialization(self) -> None:
        """Test that ConfFileBundle initializes successfully with valid arguments."""
        bundle = ConfFileBundle(
            file_path=self.valid_file_path,
            file_mode=self.valid_file_mode,
            context_bundle=self.valid_context_bundle
        )
        
        self.assertEqual(bundle.file_path, self.valid_file_path)
        self.assertEqual(bundle.file_mode, self.valid_file_mode)
        self.assertEqual(bundle.context_bundle, self.valid_context_bundle)

    def test_validation_fails_when_file_path_is_none(self) -> None:
        """Test validation error when file_path is None."""
        with self.assertRaises(Exception):  # Catches ATSValueError or validation exceptions
            ConfFileBundle(
                file_path=None,  # type: ignore
                file_mode=self.valid_file_mode,
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_file_path_is_invalid_type(self) -> None:
        """Test validation error when file_path is not a string."""
        with self.assertRaises(Exception):  # Catches ATSTypeError
            ConfFileBundle(
                file_path=12345,  # type: ignore
                file_mode=self.valid_file_mode,
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_file_mode_is_none(self) -> None:
        """Test validation error when file_mode is None."""
        with self.assertRaises(Exception):
            ConfFileBundle(
                file_path=self.valid_file_path,
                file_mode=None,  # type: ignore
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_file_mode_is_invalid_type(self) -> None:
        """Test validation error when file_mode is not a string."""
        with self.assertRaises(Exception):
            ConfFileBundle(
                file_path=self.valid_file_path,
                file_mode=True,  # type: ignore
                context_bundle=self.valid_context_bundle
            )

    def test_validation_fails_when_context_bundle_is_none(self) -> None:
        """Test validation error when context_bundle is None."""
        with self.assertRaises(Exception):
            ConfFileBundle(
                file_path=self.valid_file_path,
                file_mode=self.valid_file_mode,
                context_bundle=None  # type: ignore
            )

    def test_validation_fails_when_context_bundle_is_invalid_type(self) -> None:
        """Test validation error when context_bundle is not a ContextBundle instance."""
        with self.assertRaises(Exception):
            ConfFileBundle(
                file_path=self.valid_file_path,
                file_mode=self.valid_file_mode,
                context_bundle=MagicMock()  # Generic Mock lacking ContextBundle spec
            )

    def test_to_dict(self) -> None:
        """Test that to_dict successfully exports instance fields to a dictionary."""
        bundle = ConfFileBundle(
            file_path=self.valid_file_path,
            file_mode=self.valid_file_mode,
            context_bundle=self.valid_context_bundle
        )
        
        expected_dict = {
            'file_path': self.valid_file_path,
            'file_mode': self.valid_file_mode,
            'context_bundle': self.valid_context_bundle
        }
        
        self.assertEqual(bundle.to_dict(), expected_dict)

    def test_is_frozen(self) -> None:
        """Test that modifying an attribute raises FrozenInstanceError due to frozen=True constraint."""
        bundle = ConfFileBundle(
            file_path=self.valid_file_path,
            file_mode=self.valid_file_mode,
            context_bundle=self.valid_context_bundle
        )
        
        with self.assertRaises(FrozenInstanceError):
            bundle.file_path = "/new/path.txt"  # type: ignore


if __name__ == '__main__':
    unittest.main()
