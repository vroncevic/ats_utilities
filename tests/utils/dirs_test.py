# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path

# Adjust imports according to your project structure
from ats_utilities.utils.dirs import check_dir_exists
from ats_utilities.exceptions import ATSValueError


class TestDirsUtility(unittest.TestCase):
    """Unit tests for the directory validation utility functions."""

    def test_check_dir_exists_success(self) -> None:
        """Test that a valid, existing directory path passes verification silently."""
        with patch.object(Path, "is_dir", return_value=True):
            # Should run cleanly without raising any exception hooks
            try:
                check_dir_exists("/valid/existing/directory/path", 'testdirsutility::test_check_dir_exists_success')
            except Exception as exc:
                self.fail(f"check_dir_exists raised an exception unexpectedly: {exc}")

    def test_check_dir_exists_invalid_type(self) -> None:
        """Test that passing a non-string type fails the strict type check."""
        # The istype checker hook should trigger a failure before checking existence
        with self.assertRaises(Exception):
            check_dir_exists(12345, 'testdirsutility::test_check_dir_exists_invalid_type')  # type: ignore

        with self.assertRaises(Exception):
            check_dir_exists(["/not/a/raw/string"], 'testdirsutility::test_check_dir_exists_invalid_type')  # type: ignore

    @patch("ats_utilities.utils.dirs.raise_error")
    def test_check_dir_exists_empty_string(self, mock_raise_error: MagicMock) -> None:
        """Test that an empty directory path defaults to the path provision error flow."""
        check_dir_exists("", 'testdirsutility::test_check_dir_exists_empty_string', exc_message="Custom empty path error message")

        mock_raise_error.assert_called_once_with(
            fallback_context="dirs::check_dir_exists(...)",
            fallback_msg="directory path must be provided",
            exc_context="testdirsutility::test_check_dir_exists_empty_string",
            exc_message="Custom empty path error message",
            exc_class=ATSValueError
        )

    @patch("ats_utilities.utils.dirs.raise_error")
    @patch.object(Path, "is_dir", return_value=False)
    def test_check_dir_exists_missing_directory(self, mock_is_dir: MagicMock, mock_raise_error: MagicMock) -> None:
        """Test that a non-existent path properly registers a directory existence error."""
        missing_path = "/path/to/nowhere"
        
        check_dir_exists(missing_path, 'testdirsutility::test_check_dir_exists_missing_directory', exc_message="Missing directory context")

        mock_is_dir.assert_called_once()
        mock_raise_error.assert_called_once_with(
            fallback_context="dirs::check_dir_exists(...)",
            fallback_msg=f"directory at the provided path does not exist: {missing_path}",
            exc_context="testdirsutility::test_check_dir_exists_missing_directory",
            exc_message="Missing directory context",
            exc_class=ATSValueError
        )

    @patch("ats_utilities.utils.dirs.raise_error")
    @patch.object(Path, "is_dir", return_value=False)
    def test_check_dir_exists_custom_exception_class(self, mock_is_dir: MagicMock, mock_raise_error: MagicMock) -> None:
        """Test that custom exception classes are accurately passed down to the raise_error handler."""
        class CustomTestException(BaseException):
            pass

        missing_path = "/path/to/missing/dir"
        
        check_dir_exists(
            missing_path, 'testdirsutility::test_check_dir_exists_custom_exception_class', 
            exc_message="Custom exception testing", 
            exc_class=CustomTestException
        )

        mock_is_dir.assert_called_once()
        mock_raise_error.assert_called_once_with(
            fallback_context="dirs::check_dir_exists(...)",
            fallback_msg=f"directory at the provided path does not exist: {missing_path}",
            exc_context="testdirsutility::test_check_dir_exists_custom_exception_class",
            exc_message="Custom exception testing",
            exc_class=CustomTestException
        )


if __name__ == '__main__':
    unittest.main()
