# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch, mock_open
from collections.abc import Mapping
from typing import Any

# Adjust imports according to your project structure
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.context_bundle import ContextBundle


class TestConfFile(unittest.TestCase):
    """Unit tests for the ConfFile context manager."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for ConfFile instances."""
        self.mock_file_path = "/path/to/config.cfg"
        self.mock_file_mode = "r"
        
        # Build mock bundle dependencies
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_bundle = MagicMock(spec=ConfFileBundle)
        self.mock_bundle.file_path = self.mock_file_path
        self.mock_bundle.file_mode = self.mock_file_mode
        self.mock_bundle.context_bundle = self.mock_context_bundle

        # Setup mock reporter to satisfy the @vreport decorator requirements
        self.mock_reporter = MagicMock(spec=IReporter)

    def test_initialization(self) -> None:
        """Test successful initialization and attribute assignment."""
        # Act
        conf_file = ConfFile(self.mock_bundle)

        # Assert
        self.assertEqual(conf_file._file_path, self.mock_file_path)
        self.assertEqual(conf_file._file_mode, self.mock_file_mode)
        self.assertIsNone(conf_file._file)

    def test_initialization_fails_when_bundle_is_none(self) -> None:
        """Test initialization failure when file_bundle is None."""
        with self.assertRaises(Exception):
            ConfFile(None)  # type: ignore

    def test_initialization_fails_when_bundle_type_invalid(self) -> None:
        """Test initialization failure when file_bundle is of an invalid type."""
        with self.assertRaises(Exception):
            ConfFile(MagicMock())  # type: ignore

    @patch("builtins.open", new_callable=mock_open)
    @patch("ats_utilities.config_io.conf_file.check_file_exists")
    def test_enter_in_read_mode(
        self, mock_check_exists: MagicMock, mock_file_open: MagicMock
    ) -> None:
        """Test __enter__ execution flow when opening a file in read ('r') mode."""
        # Arrange
        conf_file = ConfFile(self.mock_bundle)
        conf_file._reporter = self.mock_reporter  # Satisfy decorator signature

        # Act
        result = conf_file.__enter__()

        # Assert
        mock_check_exists.assert_called_once_with(
            self.mock_file_path, 'conf_file::enter(...)', f'file {self.mock_file_path} does not exist'
        )
        mock_file_open.assert_called_once_with(self.mock_file_path, "r", encoding="utf-8")
        self.assertEqual(result, mock_file_open.return_value)
        self.assertEqual(conf_file._file, mock_file_open.return_value)

    @patch("builtins.open", new_callable=mock_open)
    @patch("ats_utilities.config_io.conf_file.check_file_exists")
    def test_enter_in_write_mode(
        self, mock_check_exists: MagicMock, mock_file_open: MagicMock
    ) -> None:
        """Test __enter__ execution flow when opening a file in write ('w') mode."""
        # Arrange
        self.mock_bundle.file_mode = "w"
        conf_file = ConfFile(self.mock_bundle)
        conf_file._reporter = self.mock_reporter

        # Act
        result = conf_file.__enter__()

        # Assert
        # check_file_exists should not be triggered for write modes
        mock_check_exists.assert_not_called()
        mock_file_open.assert_called_once_with(self.mock_file_path, "w", encoding="utf-8")
        self.assertEqual(result, mock_file_open.return_value)

    def test_exit_closes_file(self) -> None:
        """Test that __exit__ closes the managed file resource safely."""
        # Arrange
        conf_file = ConfFile(self.mock_bundle)
        conf_file._reporter = self.mock_reporter
        
        mock_file = MagicMock()
        mock_file.closed = False
        conf_file._file = mock_file

        # Act
        conf_file.__exit__(None, None, None)

        # Assert
        mock_file.close.assert_called_once()
        self.assertIsNone(conf_file._file)

    def test_exit_handles_exceptions_gracefully(self) -> None:
        """Test that __exit__ suppresses exceptions during closing operations."""
        # Arrange
        conf_file = ConfFile(self.mock_bundle)
        conf_file._reporter = self.mock_reporter
        
        mock_file = MagicMock()
        mock_file.closed = False
        mock_file.close.side_effect = RuntimeError("Failed to close file")
        conf_file._file = mock_file

        # Act & Assert
        try:
            conf_file.__exit__(None, None, None)
        except Exception as e:
            self.fail(f"__exit__ raised an exception unexpectedly: {e}")
        
        self.assertIsNone(conf_file._file)

    def test_exit_when_file_is_none(self) -> None:
        """Test __exit__ when _file is None."""
        conf_file = ConfFile(self.mock_bundle)
        conf_file._reporter = self.mock_reporter
        conf_file._file = None
        conf_file.__exit__(None, None, None)
        self.assertIsNone(conf_file._file)

    def test_exit_when_file_is_already_closed(self) -> None:
        """Test __exit__ when _file is already closed."""
        conf_file = ConfFile(self.mock_bundle)
        conf_file._reporter = self.mock_reporter
        mock_file = MagicMock()
        mock_file.closed = True
        conf_file._file = mock_file
        conf_file.__exit__(None, None, None)
        mock_file.close.assert_not_called()
        self.assertIsNone(conf_file._file)

    @patch("ats_utilities.config_io.conf_file.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test __str__ serialization proxies through to_str utility correctly."""
        # Arrange
        conf_file = ConfFile(self.mock_bundle)
        mock_to_str.return_value = "ConfFile{path=/path/to/config.cfg}"

        # Act
        result = str(conf_file)

        # Assert
        mock_to_str.assert_called_once_with(conf_file)
        self.assertEqual(result, "ConfFile{path=/path/to/config.cfg}")


if __name__ == '__main__':
    unittest.main()