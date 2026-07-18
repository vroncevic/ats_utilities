# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping, Sequence

# Adjust imports according to your project structure
from ats_utilities.generator.tar.tar_process_registry import TarProcessRegistry
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle


class TestTarProcessRegistry(unittest.TestCase):
    """Unit tests for the TarProcessRegistry factory class."""

    def setUp(self) -> None:
        """Set up standard parameters for building a TarProcessBundle."""
        self.archive_path = "/path/to/archive.tgz"
        self.target_dir = "/path/to/target"
        self.source_dir = "templates/base"
        self.path_replacements = {"__project__": "my_app"}
        self.exclude_patterns = ["*.log", ".git"]
        self.vals = {"version": "3.4.3", "debug": "false"}

    @patch("ats_utilities.generator.tar.tar_process_registry.TarProcessBundle")
    def test_create_tar_process_bundle_delegation(self, mock_bundle_cls: MagicMock) -> None:
        """Test that create_tar_process_bundle routes all parameters to TarProcessBundle."""
        # Arrange
        mock_bundle_instance = MagicMock(spec=TarProcessBundle)
        mock_bundle_cls.return_value = mock_bundle_instance

        # Act
        result = TarProcessRegistry.create_tar_process_bundle(
            archive_path=self.archive_path,
            target_dir=self.target_dir,
            source_dir=self.source_dir,
            path_replacements=self.path_replacements,
            exclude_patterns=self.exclude_patterns,
            vals=self.vals
        )

        # Assert
        mock_bundle_cls.assert_called_once_with(
            archive_path=self.archive_path,
            target_dir=self.target_dir,
            source_dir=self.source_dir,
            path_replacements=self.path_replacements,
            exclude_patterns=self.exclude_patterns,
            vals=self.vals
        )
        self.assertEqual(result, mock_bundle_instance)

    def test_create_tar_process_bundle_integration(self) -> None:
        """Test the integration between the registry factory and an actual bundle instance."""
        result = TarProcessRegistry.create_tar_process_bundle(
            archive_path=self.archive_path,
            target_dir=self.target_dir,
            source_dir=self.source_dir,
            path_replacements=self.path_replacements,
            exclude_patterns=self.exclude_patterns,
            vals=self.vals
        )

        # Verify an authentic instance is generated with matching slots
        self.assertIsInstance(result, TarProcessBundle)
        self.assertEqual(result.archive_path, self.archive_path)
        self.assertEqual(result.target_dir, self.target_dir)
        self.assertEqual(result.source_dir, self.source_dir)
        self.assertEqual(result.path_replacements, self.path_replacements)
        self.assertEqual(result.exclude_patterns, self.exclude_patterns)
        self.assertEqual(result.vals, self.vals)


if __name__ == '__main__':
    unittest.main()
