# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping
from tarfile import TarFile, TarInfo

# Adjust imports according to your project structure
from ats_utilities.generator.tar.tar_process_member_registry import TarProcessRegistry
from ats_utilities.generator.tar.tar_process_member_bundle import TarProcessMemberBundle
from ats_utilities.generator.tar.tar_process_member_params import TarProcessMemberParams


class TestTarProcessMemberRegistry(unittest.TestCase):
    """Unit tests for the TarProcessRegistry class responsible for member bundles."""

    def setUp(self) -> None:
        """Set up standard parameter mocks for member bundle creation."""
        self.mock_tar = MagicMock(spec=TarFile)
        self.mock_member = MagicMock(spec=TarInfo)
        self.dest_full_path = "/absolute/target/path/extracted_file.py"
        self.vals = {"project_name": "ats_system", "version": "3.4.4"}

    @patch("ats_utilities.generator.tar.tar_process_member_registry.TarProcessMemberBundle")
    def test_create_tar_process_member_bundle_delegation(self, mock_bundle_cls: MagicMock) -> None:
        """Test that create_tar_process_member_bundle properly forwards arguments to the bundle class."""
        # Arrange
        mock_bundle_instance = MagicMock(spec=TarProcessMemberBundle)
        mock_bundle_cls.return_value = mock_bundle_instance

        # Act
        result = TarProcessRegistry.create_tar_process_member_bundle(
            tar=self.mock_tar,
            member=self.mock_member,
            dest_full_path=self.dest_full_path,
            vals=self.vals
        )

        # Assert
        mock_bundle_cls.assert_called_once_with(
            tar=self.mock_tar,
            member=self.mock_member,
            dest_full_path=self.dest_full_path,
            vals=self.vals
        )
        self.assertEqual(result, mock_bundle_instance)

    def test_create_tar_process_member_bundle_integration(self) -> None:
        """Test integration factory creation yielding an authentic validated bundle instance."""
        # Act
        result = TarProcessRegistry.create_tar_process_member_bundle(
            tar=self.mock_tar,
            member=self.mock_member,
            dest_full_path=self.dest_full_path,
            vals=self.vals
        )

        # Assert
        self.assertIsInstance(result, TarProcessMemberBundle)
        self.assertEqual(result.tar, self.mock_tar)
        self.assertEqual(result.member, self.mock_member)
        self.assertEqual(result.dest_full_path, self.dest_full_path)
        self.assertEqual(result.vals, self.vals)

    def test_create_bundle(self) -> None:
        """Test create_bundle on TarProcessRegistry."""
        result = TarProcessRegistry.create_bundle(
            TarProcessMemberParams(
                tar=self.mock_tar,
                member=self.mock_member,
                dest_full_path=self.dest_full_path,
                vals=self.vals
            )
        )
        self.assertIsInstance(result, TarProcessMemberBundle)
        self.assertEqual(result.tar, self.mock_tar)
        self.assertEqual(result.member, self.mock_member)
        self.assertEqual(result.dest_full_path, self.dest_full_path)
        self.assertEqual(result.vals, self.vals)


if __name__ == '__main__':
    unittest.main()
