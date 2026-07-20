# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from typing import Any

from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor


class TestLoader(unittest.TestCase):
    """Unit tests for the Loader engine class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for Loader instances."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_processor = MagicMock(spec=IConfigProcessor)
        
        # Build mock component bundle dependencies
        self.mock_component_bundle = MagicMock(spec=ConfigIOBundle)
        self.mock_component_bundle.context_bundle = self.mock_context_bundle
        self.mock_component_bundle.processor = self.mock_processor
        self.mock_component_bundle.file_path = "/path/to/config.json"
        self.mock_component_bundle.READ_MODE = "r"

    @patch("ats_utilities.config_io.loader.engine.ConfFileFactory.create_conf_file")
    def test_initialization(self, mock_create_conf_file: MagicMock) -> None:
        """Test successful initialization and attribute orchestration from the component bundle."""
        # Arrange
        mock_conf_file = MagicMock()
        mock_create_conf_file.return_value = mock_conf_file

        # Act
        loader = Loader(self.mock_component_bundle)

        # Assert
        self.assertEqual(loader._shared_context, self.mock_context_bundle)
        self.assertEqual(loader._processor, self.mock_processor)
        
        mock_create_conf_file.assert_called_once_with(
            file_path="/path/to/config.json",
            file_mode="r",
            context_bundle=self.mock_context_bundle
        )
        self.assertEqual(loader._conf_file, mock_conf_file)

    def test_initialization_fails_when_bundle_is_none(self) -> None:
        """Test initialization failure when component_bundle is None."""
        with self.assertRaises(Exception):
            Loader(None)  # type: ignore

    def test_initialization_fails_with_invalid_bundle_type(self) -> None:
        """Test initialization failure when component_bundle is of an unexpected type."""
        with self.assertRaises(Exception):
            Loader(MagicMock())  # type: ignore

    def test_get_shared_context(self) -> None:
        """Test that get_shared_context cleanly returns the assigned context bundle instance."""
        loader = Loader(self.mock_component_bundle)
        self.assertEqual(loader.get_shared_context(), self.mock_context_bundle)

    @patch("ats_utilities.config_io.loader.engine.ConfFileFactory.create_conf_file")
    def test_load_configuration_success(self, mock_create_conf_file: MagicMock) -> None:
        """Test load_configuration execution path when file contents parse correctly against the scheme."""
        # Arrange
        mock_conf_file = MagicMock()
        mock_create_conf_file.return_value = mock_conf_file
        
        loader = Loader(self.mock_component_bundle)
        
        # Configure file object context manager mock
        mock_config_file = MagicMock()
        mock_config_file.read.return_value = '{"key": "value"}'
        mock_conf_file.__enter__.return_value = mock_config_file
        
        # Configure configuration format processor simulation responses
        self.mock_processor.deserialize.return_value = True
        self.mock_processor.to_dict.return_value = {"key": "value"}

        # Act
        result = loader.load_configuration()

        # Assert
        mock_create_conf_file.assert_called_once_with(
            file_path="/path/to/config.json",
            file_mode="r",
            context_bundle=self.mock_context_bundle
        )
        mock_conf_file.__enter__.assert_called_once()
        mock_config_file.read.assert_called_once()
        self.mock_processor.deserialize.assert_called_once_with('{"key": "value"}')
        self.mock_processor.to_dict.assert_called_once()
        self.assertEqual(result, {"key": "value"})

    @patch("ats_utilities.config_io.loader.engine.ConfFileFactory.create_conf_file")
    def test_load_configuration_returns_empty_on_file_exception(
        self, mock_create_conf_file: MagicMock
    ) -> None:
        """Test that load_configuration returns an empty dictionary gracefully when file I/O errors occur."""
        # Arrange
        mock_conf_file = MagicMock()
        mock_create_conf_file.return_value = mock_conf_file
        
        loader = Loader(self.mock_component_bundle)
        mock_conf_file.__enter__.side_effect = RuntimeError("File reading blocked")

        # Act
        result = loader.load_configuration()

        # Assert
        self.assertEqual(result, {})
        self.mock_processor.deserialize.assert_not_called()

    @patch("ats_utilities.config_io.loader.engine.ConfFileFactory.create_conf_file")
    def test_load_configuration_returns_empty_when_content_is_none(
        self, mock_create_conf_file: MagicMock
    ) -> None:
        """Test that load_configuration returns an empty dictionary when context manager yields no data."""
        # Arrange
        mock_conf_file = MagicMock()
        mock_create_conf_file.return_value = mock_conf_file
        
        loader = Loader(self.mock_component_bundle)
        
        mock_config_file = MagicMock()
        mock_config_file.read.return_value = None
        mock_conf_file.__enter__.return_value = mock_config_file

        # Act
        result = loader.load_configuration()

        # Assert
        self.assertEqual(result, {})
        self.mock_processor.deserialize.assert_not_called()

    @patch("ats_utilities.config_io.loader.engine.ConfFileFactory.create_conf_file")
    def test_load_configuration_returns_empty_on_deserialization_failure(
        self, mock_create_conf_file: MagicMock
    ) -> None:
        """Test that load_configuration returns an empty dictionary when deserialization validation fails."""
        # Arrange
        mock_conf_file = MagicMock()
        mock_create_conf_file.return_value = mock_conf_file
        
        loader = Loader(self.mock_component_bundle)
        
        mock_config_file = MagicMock()
        mock_config_file.read.return_value = 'invalid content'
        mock_conf_file.__enter__.return_value = mock_config_file
        
        self.mock_processor.deserialize.return_value = False

        # Act
        result = loader.load_configuration()

        # Assert
        self.assertEqual(result, {})
        self.mock_processor.deserialize.assert_called_once_with('invalid content')
        self.mock_processor.to_dict.assert_not_called()

    @patch("ats_utilities.config_io.loader.engine.ConfFileFactory.create_conf_file")
    def test_load_configuration_returns_empty_when_file_is_none(
        self, mock_create_conf_file: MagicMock
    ) -> None:
        """Test that load_configuration returns an empty dictionary when config_file is None."""
        mock_conf_file = MagicMock()
        mock_create_conf_file.return_value = mock_conf_file

        loader = Loader(self.mock_component_bundle)

        mock_conf_file.__enter__.return_value = None

        result = loader.load_configuration()

        self.assertEqual(result, {})
        self.mock_processor.deserialize.assert_not_called()

    @patch("ats_utilities.config_io.loader.engine.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test that __str__ delegates representation tracking cleanly to reflection utilities."""
        # Arrange
        loader = Loader(self.mock_component_bundle)
        mock_to_str.return_value = "Loader{processor=IConfigProcessor}"

        # Act
        result = str(loader)

        # Assert
        mock_to_str.assert_called_once_with(loader)
        self.assertEqual(result, "Loader{processor=IConfigProcessor}")


if __name__ == '__main__':
    unittest.main()
