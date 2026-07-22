# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.config_io.conf_file_factory import ConfFileFactory
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.context.bundle import ContextBundle


class TestConfFileFactory(unittest.TestCase):
    """Unit tests for the ConfFileFactory class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for registry creation."""
        self.mock_file_path = "/path/to/config.cfg"
        self.mock_file_mode = "r+"
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

    @patch("ats_utilities.config_io.conf_file_factory.ConfFileBundle")
    @patch("ats_utilities.config_io.conf_file_factory.ConfFile")
    def test_create_conf_file(self, mock_conf_file_cls: MagicMock, mock_bundle_cls: MagicMock) -> None:
        """Test create_conf_file instantiates ConfFile properly."""
        mock_bundle = MagicMock(spec=ConfFileBundle)
        mock_bundle_cls.return_value = mock_bundle

        mock_conf_file = MagicMock()
        mock_conf_file_cls.return_value = mock_conf_file

        result = ConfFileFactory.create_conf_file(
            file_path=self.mock_file_path,
            file_mode=self.mock_file_mode,
            context_bundle=self.mock_context_bundle
        )

        mock_bundle_cls.assert_called_once_with(
            file_path=self.mock_file_path,
            file_mode=self.mock_file_mode,
            context_bundle=self.mock_context_bundle
        )
        mock_conf_file_cls.assert_called_once_with(mock_bundle)
        self.assertEqual(result, mock_conf_file)


if __name__ == '__main__':
    unittest.main()
