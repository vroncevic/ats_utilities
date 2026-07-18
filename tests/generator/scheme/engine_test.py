# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping
from typing import Any

# Adjust imports according to your project structure
from ats_utilities.generator.scheme.engine import SchemeLoader
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.exceptions import ATSGeneratorError


class TestSchemeLoader(unittest.TestCase):
    """Unit tests for the SchemeLoader class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for SchemeLoader instances."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.valid_dict_scheme = {"param1": "value1", "param2": 42}
        self.valid_file_path = "/path/to/scheme.json"

    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_initialization(self, mock_inject: MagicMock) -> None:
        """Test successful initialization and context injection verification."""
        loader = SchemeLoader(self.mock_context_bundle)

        self.assertEqual(loader._shared_context, self.mock_context_bundle)
        self.assertTrue(loader._initialized)
        mock_inject.assert_called_once_with(loader, self.mock_context_bundle)

    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_is_initialized(self, mock_inject: MagicMock) -> None:
        """Test that is_initialized returns True when the component is ready."""
        loader = SchemeLoader(self.mock_context_bundle)
        self.assertTrue(loader.is_initialized())

    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_load_with_mapping_returns_dict(self, mock_inject: MagicMock) -> None:
        """Test that providing a preloaded Mapping directly returns a standard dictionary copy."""
        loader = SchemeLoader(self.mock_context_bundle)
        
        result = loader.load(self.valid_dict_scheme)
        
        self.assertEqual(result, self.valid_dict_scheme)
        self.assertIsInstance(result, dict)

    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_load_with_invalid_type_raises(self, mock_inject: MagicMock) -> None:
        """Test that an input that is neither a string nor a mapping triggers an error."""
        loader = SchemeLoader(self.mock_context_bundle)
        
        # Passing an invalid type (e.g., integer) should cause an istype validation failure
        with self.assertRaises(Exception):
            loader.load(12345)  # type: ignore

    @patch("ats_utilities.generator.scheme.engine.exists", return_value=False)
    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_load_with_nonexistent_file_path_raises(
        self, mock_inject: MagicMock, mock_exists: MagicMock
    ) -> None:
        """Test that providing a file path that does not exist triggers a validation fault."""
        loader = SchemeLoader(self.mock_context_bundle)
        
        with self.assertRaises(Exception):
            loader.load(self.valid_file_path)
            
        mock_exists.assert_called_once_with(self.valid_file_path)

    @patch("ats_utilities.generator.scheme.engine.exists", return_value=True)
    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_load_with_unsupported_file_extension_raises(
        self, mock_inject: MagicMock, mock_exists: MagicMock
    ) -> None:
        """Test that file paths without a .json extension trigger a validation fault."""
        loader = SchemeLoader(self.mock_context_bundle)
        invalid_extension_path = "/path/to/scheme.xml"
        
        with self.assertRaises(Exception):
            loader.load(invalid_extension_path)

    @patch("ats_utilities.generator.scheme.engine.Loader")
    @patch("ats_utilities.generator.scheme.engine.ConfigIORegistry")
    @patch("ats_utilities.generator.scheme.engine.exists", return_value=True)
    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_load_from_json_file_success(
        self, mock_inject: MagicMock, mock_exists: MagicMock, 
        mock_registry: MagicMock, mock_loader_cls: MagicMock
    ) -> None:
        """Test successful loading and parsing workflow from a valid JSON file path."""
        # Arrange
        loader = SchemeLoader(self.mock_context_bundle)
        
        mock_bundle = MagicMock()
        mock_registry.create_config_io_bundle_by_file_path_and_scheme.return_value = mock_bundle
        
        mock_config_loader = MagicMock(spec=Loader)
        mock_config_loader.load_configuration.return_value = self.valid_dict_scheme
        mock_loader_cls.return_value = mock_config_loader

        # Act
        result = loader.load(self.valid_file_path)

        # Assert
        mock_registry.create_config_io_bundle_by_file_path_and_scheme.assert_called_once_with(
            file_path=self.valid_file_path,
            scheme={},
            context_bundle=self.mock_context_bundle
        )
        mock_loader_cls.assert_called_once_with(mock_bundle)
        mock_config_loader.load_configuration.assert_called_once()
        self.assertEqual(result, self.valid_dict_scheme)

    @patch("ats_utilities.generator.scheme.engine.Loader", return_value=None)
    @patch("ats_utilities.generator.scheme.engine.ConfigIORegistry")
    @patch("ats_utilities.generator.scheme.engine.exists", return_value=True)
    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_load_fails_when_config_loader_setup_is_none(
        self, mock_inject: MagicMock, mock_exists: MagicMock, 
        mock_registry: MagicMock, mock_loader_cls: MagicMock
    ) -> None:
        """Test that an error is thrown if the configuration engine setup resolves to None."""
        loader = SchemeLoader(self.mock_context_bundle)
        
        with self.assertRaises(Exception):
            loader.load(self.valid_file_path)

    @patch("ats_utilities.generator.scheme.engine.format_error_raw")
    @patch("ats_utilities.generator.scheme.engine.ConfigIORegistry")
    @patch("ats_utilities.generator.scheme.engine.exists", return_value=True)
    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_load_catches_internal_exceptions_and_raises_generator_error(
        self, mock_inject: MagicMock, mock_exists: MagicMock, 
        mock_registry: MagicMock, mock_format_error: MagicMock
    ) -> None:
        """Test that internal unexpected crashes are transformed and raised as ATSGeneratorError."""
        # Arrange
        loader = SchemeLoader(self.mock_context_bundle)
        mock_registry.create_config_io_bundle_by_file_path_and_scheme.side_effect = RuntimeError("IO Error")
        mock_format_error.return_value = "Formatted String Error Description"

        # Act & Assert
        with self.assertRaises(ATSGeneratorError):
            loader.load(self.valid_file_path)
            
        mock_format_error.assert_called_once()

    @patch("ats_utilities.generator.scheme.engine.to_str")
    @patch("ats_utilities.generator.scheme.engine.inject_context_bundle")
    def test_string_representation(self, mock_inject: MagicMock, mock_to_str: MagicMock) -> None:
        """Test that __str__ delegates representation tracking cleanly to reflection utilities."""
        loader = SchemeLoader(self.mock_context_bundle)
        mock_to_str.return_value = "SchemeLoader{initialized=True}"

        result = str(loader)

        mock_to_str.assert_called_once_with(loader)
        self.assertEqual(result, "SchemeLoader{initialized=True}")


if __name__ == '__main__':
    unittest.main()
