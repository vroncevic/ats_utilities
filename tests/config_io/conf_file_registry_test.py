# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.config_io.conf_file_registry import ConfFileRegistry
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.config_io.conf_file_params import ConfFileParams
from ats_utilities.context.context_bundle import ContextBundle


class TestConfFileRegistry(unittest.TestCase):
    """Unit tests for the ConfFileRegistry class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for registry creation."""
        self.mock_file_path = "/path/to/config.cfg"
        self.mock_file_mode = "r+"
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

    @patch("ats_utilities.config_io.conf_file_registry.ConfFileBundle")
    def test_create_bundle(self, mock_bundle_cls: MagicMock) -> None:
        """Test create_bundle delegates correctly."""
        mock_expected_bundle = MagicMock(spec=ConfFileBundle)
        mock_bundle_cls.return_value = mock_expected_bundle

        result = ConfFileRegistry.create_bundle(
            ConfFileParams(
                file_path=self.mock_file_path,
                file_mode=self.mock_file_mode,
                context_bundle=self.mock_context_bundle
            )
        )

        mock_bundle_cls.assert_called_once_with(
            file_path=self.mock_file_path,
            file_mode=self.mock_file_mode,
            context_bundle=self.mock_context_bundle
        )
        self.assertEqual(result, mock_expected_bundle)


if __name__ == '__main__':
    unittest.main()
