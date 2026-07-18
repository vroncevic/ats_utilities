# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping

# Adjust imports according to your project structure
from ats_utilities.generator.gen_params_registry import GenParamsRegistry
from ats_utilities.generator.gen_params_bundle import GenParamsBundle


class TestGenParamsRegistry(unittest.TestCase):
    """Unit tests for the GenParamsRegistry factory class."""

    def setUp(self) -> None:
        """Set up standard parameters for testing GenParamsBundle instantiation."""
        self.archive_path = "/path/to/templates.tgz"
        self.target_dir = "/path/to/destination"
        self.template_key = "cpp_application"
        self.scheme = {"project_type": "binary", "standard": "c++20"}
        self.template_values = {"PROJECT_NAME": "ats_core", "YEAR": "2026"}

    @patch("ats_utilities.generator.gen_params_registry.GenParamsBundle")
    def test_create_gen_params_bundle_delegation(self, mock_bundle_cls: MagicMock) -> None:
        """Test that create_gen_params_bundle correctly passes all arguments to GenParamsBundle."""
        # Arrange
        mock_bundle_instance = MagicMock(spec=GenParamsBundle)
        mock_bundle_cls.return_value = mock_bundle_instance

        # Act
        result = GenParamsRegistry.create_gen_params_bundle(
            archive_path=self.archive_path,
            target_dir=self.target_dir,
            template_key=self.template_key,
            scheme=self.scheme,
            template_values=self.template_values
        )

        # Assert
        mock_bundle_cls.assert_called_once_with(
            archive_path=self.archive_path,
            target_dir=self.target_dir,
            template_key=self.template_key,
            scheme=self.scheme,
            template_values=self.template_values
        )
        self.assertEqual(result, mock_bundle_instance)

    @patch("ats_utilities.generator.gen_params_bundle.check_file_exists")
    def test_create_gen_params_bundle_integration(self, mock_check_file: MagicMock) -> None:
        """Test integration factory creation yielding an authentic validated bundle instance."""
        # Act
        result = GenParamsRegistry.create_gen_params_bundle(
            archive_path=self.archive_path,
            target_dir=self.target_dir,
            template_key=self.template_key,
            scheme=self.scheme,
            template_values=self.template_values
        )

        # Assert
        self.assertIsInstance(result, GenParamsBundle)
        self.assertEqual(result.archive_path, self.archive_path)
        self.assertEqual(result.target_dir, self.target_dir)
        self.assertEqual(result.template_key, self.template_key)
        self.assertEqual(result.scheme, self.scheme)
        self.assertEqual(result.template_values, self.template_values)
        mock_check_file.assert_called_once()


if __name__ == '__main__':
    unittest.main()
