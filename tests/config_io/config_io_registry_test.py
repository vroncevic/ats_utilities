# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping

# Adjust imports according to your project structure
from ats_utilities.config_io.config_io_registry import ConfigIORegistry
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.config_io.config_io_params import ConfigIOParams
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.context_bundle import ContextBundle


class TestConfigIORegistry(unittest.TestCase):
    """Unit tests for the ConfigIORegistry factory methods."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for registry creation."""
        self.mock_file_path = "/path/to/config.yaml"
        self.mock_scheme = MagicMock(spec=Mapping)
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_processor = MagicMock(spec=IConfigProcessor)

    @patch("ats_utilities.config_io.config_io_registry.ConfigProcessorFactory")
    @patch("ats_utilities.config_io.config_io_registry.ConfigIOBundle")
    def test_create_by_file_path_and_scheme(
        self, mock_bundle_cls: MagicMock, mock_factory_cls: MagicMock
    ) -> None:
        """Test successful creation of bundle via file path and configuration scheme."""
        # Arrange
        mock_factory_cls.create_from_file_path.return_value = self.mock_processor
        mock_expected_bundle = MagicMock(spec=ConfigIOBundle)
        mock_bundle_cls.return_value = mock_expected_bundle

        # Act
        result = ConfigIORegistry.create_config_io_bundle_by_file_path_and_scheme(
            file_path=self.mock_file_path,
            scheme=self.mock_scheme,
            context_bundle=self.mock_context_bundle
        )

        # Assert
        # Check if the factory was called correctly to construct a processor
        mock_factory_cls.create_from_file_path.assert_called_once_with(
            file_path=self.mock_file_path,
            scheme=self.mock_scheme
        )

        # Check if the bundle instance was initialized with all resolved parts
        mock_bundle_cls.assert_called_once_with(
            file_path=self.mock_file_path,
            scheme=self.mock_scheme,
            processor=self.mock_processor,
            context_bundle=self.mock_context_bundle
        )

        # Ensure the factory returned the constructed bundle object
        self.assertEqual(result, mock_expected_bundle)

    @patch("ats_utilities.config_io.config_io_registry.ConfigIOBundle")
    def test_create_by_injected_processor(self, mock_bundle_cls: MagicMock) -> None:
        """Test successful creation of bundle using a direct injected processor instance."""
        # Arrange
        mock_expected_bundle = MagicMock(spec=ConfigIOBundle)
        mock_bundle_cls.return_value = mock_expected_bundle

        # Act
        result = ConfigIORegistry.create_config_io_bundle_by_injected_processor(
            processor=self.mock_processor,
            context_bundle=self.mock_context_bundle
        )

        # Assert
        # Check that defaults (empty string and dict) are appropriately supplied
        mock_bundle_cls.assert_called_once_with(
            file_path='',
            scheme={},
            processor=self.mock_processor,
            context_bundle=self.mock_context_bundle
        )
        
        self.assertEqual(result, mock_expected_bundle)

    def test_create_bundle_by_file_path_and_scheme(self) -> None:
        """Test create_bundle delegates to create_config_io_bundle_by_file_path_and_scheme when processor is None."""
        mock_expected_bundle = MagicMock(spec=ConfigIOBundle)
        with patch.object(ConfigIORegistry, "create_config_io_bundle_by_file_path_and_scheme", return_value=mock_expected_bundle) as mock_create:
            result = ConfigIORegistry.create_bundle(
                ConfigIOParams(
                    file_path=self.mock_file_path,
                    scheme=self.mock_scheme,
                    context_bundle=self.mock_context_bundle,
                    processor=None
                )
            )
            mock_create.assert_called_once_with(
                file_path=self.mock_file_path,
                scheme=self.mock_scheme,
                context_bundle=self.mock_context_bundle
            )
            self.assertEqual(result, mock_expected_bundle)

    def test_create_bundle_by_injected_processor(self) -> None:
        """Test create_bundle delegates to create_config_io_bundle_by_injected_processor when processor is provided."""
        mock_expected_bundle = MagicMock(spec=ConfigIOBundle)
        with patch.object(ConfigIORegistry, "create_config_io_bundle_by_injected_processor", return_value=mock_expected_bundle) as mock_create:
            result = ConfigIORegistry.create_bundle(
                ConfigIOParams(
                    file_path=self.mock_file_path,
                    scheme=self.mock_scheme,
                    context_bundle=self.mock_context_bundle,
                    processor=self.mock_processor
                )
            )
            mock_create.assert_called_once_with(
                processor=self.mock_processor,
                context_bundle=self.mock_context_bundle
            )
            self.assertEqual(result, mock_expected_bundle)


if __name__ == '__main__':
    unittest.main()
