# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping

# Adjust imports according to your project structure
from ats_utilities.config_io.storer.engine import Storer
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor


class TestStorer(unittest.TestCase):
    """Unit tests for the Storer engine class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for Storer instances."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_processor = MagicMock(spec=IConfigProcessor)
        
        # Build a valid ConfigIOBundle mock
        self.mock_component_bundle = MagicMock(spec=ConfigIOBundle)
        self.mock_component_bundle.context_bundle = self.mock_context_bundle
        self.mock_component_bundle.processor = self.mock_processor
        self.mock_component_bundle.file_path = "/path/to/output.json"
        self.mock_component_bundle.WRITE_MODE = "w"

        self.valid_config = {"hostname": "127.0.0.1", "port": "80"}

    @patch("ats_utilities.config_io.storer.engine.ConfFileBundle")
    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_initialization(self, mock_inject: MagicMock, mock_conf_file_bundle_cls: MagicMock) -> None:
        """Test successful initialization and configuration assembly."""
        mock_file_bundle_instance = MagicMock()
        mock_conf_file_bundle_cls.return_value = mock_file_bundle_instance

        # Act
        storer = Storer(self.mock_component_bundle)

        # Assert
        self.assertEqual(storer._context_bundle_shared, self.mock_context_bundle)
        mock_inject.assert_called_once_with(storer, self.mock_context_bundle)
        self.assertEqual(storer._processor, self.mock_processor)
        
        mock_conf_file_bundle_cls.assert_called_once_with(
            file_path="/path/to/output.json",
            file_mode="w",
            context_bundle=self.mock_context_bundle
        )
        self.assertEqual(storer._conf_file_bundle, mock_file_bundle_instance)

    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_initialization_fails_when_bundle_is_none(self, mock_inject: MagicMock) -> None:
        """Test initialization failure when component_bundle is missing."""
        with self.assertRaises(Exception):
            Storer(None)  # type: ignore

    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_initialization_fails_with_invalid_bundle_type(self, mock_inject: MagicMock) -> None:
        """Test initialization failure when component_bundle type is incorrect."""
        with self.assertRaises(Exception):
            Storer(MagicMock())  # type: ignore

    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_get_shared_context(self, mock_inject: MagicMock) -> None:
        """Test that get_shared_context correctly exposes the shared context instance."""
        storer = Storer(self.mock_component_bundle)
        self.assertEqual(storer.get_shared_context(), self.mock_context_bundle)

    @patch("ats_utilities.config_io.storer.engine.ConfFile")
    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_store_configuration_success(self, mock_inject: MagicMock, mock_conf_file_cls: MagicMock) -> None:
        """Test a perfectly valid workflow returning True when file writes succeed."""
        # Arrange
        storer = Storer(self.mock_component_bundle)
        self.mock_processor.update_data.return_value = True
        self.mock_processor.serialize.return_value = '{"serialized": "data"}'

        mock_file_io = MagicMock()
        mock_file_io.write.return_value = True
        mock_conf_file_cls.return_value.__enter__.return_value = mock_file_io

        # Act
        result = storer.store_configuration(self.valid_config)

        # Assert
        self.assertTrue(result)
        self.mock_processor.update_data.assert_called_once_with(self.valid_config)
        self.mock_processor.serialize.assert_called_once()
        mock_conf_file_cls.assert_called_once_with(storer._conf_file_bundle)
        mock_file_io.write.assert_called_once_with('{"serialized": "data"}')

    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_store_configuration_empty_input_returns_false(self, mock_inject: MagicMock) -> None:
        """Test that passing an empty configuration mapping yields False immediately."""
        storer = Storer(self.mock_component_bundle)
        
        # Test with empty dictionary
        self.assertFalse(storer.store_configuration({}))
        self.mock_processor.update_data.assert_not_called()

    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_store_configuration_fails_on_processor_update(self, mock_inject: MagicMock) -> None:
        """Test that storing returns False if processor schema updates reject the data."""
        storer = Storer(self.mock_component_bundle)
        self.mock_processor.update_data.return_value = False

        result = storer.store_configuration(self.valid_config)

        self.assertFalse(result)
        self.mock_processor.update_data.assert_called_once_with(self.valid_config)
        self.mock_processor.serialize.assert_not_called()

    @patch("ats_utilities.config_io.storer.engine.ConfFile")
    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_store_configuration_handles_file_io_exceptions(
        self, mock_inject: MagicMock, mock_conf_file_cls: MagicMock
    ) -> None:
        """Test that file context manager exceptions are caught gracefully, returning False."""
        storer = Storer(self.mock_component_bundle)
        self.mock_processor.update_data.return_value = True
        self.mock_processor.serialize.return_value = "raw data"

        # Force the context manager to crash on entry
        mock_conf_file_cls.return_value.__enter__.side_effect = IOError("Disk full or permission denied")

        result = storer.store_configuration(self.valid_config)

        self.assertFalse(result)

    @patch("ats_utilities.config_io.storer.engine.to_str")
    @patch("ats_utilities.config_io.storer.engine.inject_context_bundle")
    def test_string_representation(self, mock_inject: MagicMock, mock_to_str: MagicMock) -> None:
        """Test that __str__ hooks cleanly into the reflection utility string parser."""
        storer = Storer(self.mock_component_bundle)
        mock_to_str.return_value = "Storer{processor=IConfigProcessor}"

        result = str(storer)

        mock_to_str.assert_called_once_with(storer)
        self.assertEqual(result, "Storer{processor=IConfigProcessor}")


if __name__ == '__main__':
    unittest.main()
