# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch

# Adjust imports according to your project structure
from ats_utilities.config_io.conf_file_registry import ConfFileRegistry
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.context.context_bundle import ContextBundle


class TestConfFileRegistry(unittest.TestCase):
    """Unit tests for the ConfFileRegistry factory methods."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for registry creation."""
        self.mock_file_path = "/path/to/config.cfg"
        self.mock_file_mode = "r+"
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

    @patch("ats_utilities.config_io.conf_file_registry.ConfFileBundle")
    def test_create_conf_file_bundle(self, mock_bundle_cls: MagicMock) -> None:
        """Test successful creation of ConfFileBundle through the registry factory."""
        # Arrange
        mock_expected_bundle = MagicMock(spec=ConfFileBundle)
        mock_bundle_cls.return_value = mock_expected_bundle

        # Act
        result = ConfFileRegistry.create_conf_file_bundle(
            file_path=self.mock_file_path,
            file_mode=self.mock_file_mode,
            context_bundle=self.mock_context_bundle
        )

        # Assert
        # Check if ConfFileBundle was initialized with the exact passed parameters
        mock_bundle_cls.assert_called_once_with(
            file_path=self.mock_file_path,
            file_mode=self.mock_file_mode,
            context_bundle=self.mock_context_bundle
        )

        # Ensure the factory returns the constructed ConfFileBundle instance
        self.assertEqual(result, mock_expected_bundle)


if __name__ == '__main__':
    unittest.main()
