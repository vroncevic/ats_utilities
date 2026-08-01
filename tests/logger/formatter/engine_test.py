# -*- coding: UTF-8 -*-

import unittest

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.formatter.engine import LogFormatter
from ats_utilities.logger.formatter.iformatter import ILogFormatter


class TestLogFormatter(unittest.TestCase):
    """Unit tests covering all behaviors and edge cases for the LogFormatter class."""

    def test_initialization_defaults(self):
        """Test initializing with None values sets standard defaults."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)

        self.assertEqual(formatter.get_format(), LogFormatter.DEFAULT_LOG_FORMAT)
        self.assertEqual(formatter.get_date_format(), LogFormatter.DEFAULT_LOG_DATEFMT)

    def test_initialization_custom_values(self):
        """Test initializing with custom format and date format strings."""
        custom_format = "%(levelname)s: %(message)s"
        custom_datefmt = "%Y-%m-%d %H:%M:%S"

        formatter = LogFormatter(log_format=custom_format, log_datefmt=custom_datefmt)

        self.assertEqual(formatter.get_format(), custom_format)
        self.assertEqual(formatter.get_date_format(), custom_datefmt)

    def test_initialization_invalid_type(self):
        """Test initialization raises ATSTypeError when arguments are not strings."""
        with self.assertRaises(ATSTypeError):
            LogFormatter(log_format=123, log_datefmt="%Y-%m-%d")  # type: ignore

        with self.assertRaises(ATSTypeError):
            LogFormatter(log_format="%(message)s", log_datefmt=456)  # type: ignore

    def test_initialization_empty_string(self):
        """Test initialization raises ATSValueError when format strings are empty."""
        with self.assertRaises(ATSValueError):
            LogFormatter(log_format="", log_datefmt="%Y-%m-%d")

        with self.assertRaises(ATSValueError):
            LogFormatter(log_format="%(message)s", log_datefmt="")

    def test_set_and_get_format_success(self):
        """Test setting and retrieving a valid log format string."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)
        new_format = "[%(asctime)s] %(message)s"

        formatter.set_format(new_format)
        self.assertEqual(formatter.get_format(), new_format)

    def test_set_format_none_raises_exception(self):
        """Test setting format to None raises ATSValueError."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)

        with self.assertRaises(ATSValueError):
            formatter.set_format(None)  # type: ignore

    def test_set_format_invalid_type(self):
        """Test setting format to a non-string value raises ATSTypeError."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)

        with self.assertRaises(ATSTypeError):
            formatter.set_format(100)  # type: ignore

    def test_set_format_empty_string(self):
        """Test setting format to an empty string raises ATSValueError."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)

        with self.assertRaises(ATSValueError):
            formatter.set_format("")

    def test_set_and_get_date_format_success(self):
        """Test setting and retrieving a valid date format string."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)
        new_date_format = "%Y/%m/%d %H:%M"

        formatter.set_date_format(new_date_format)
        self.assertEqual(formatter.get_date_format(), new_date_format)

    def test_set_date_format_none_raises_exception(self):
        """Test setting date format to None raises ATSValueError."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)

        with self.assertRaises(ATSValueError):
            formatter.set_date_format(None)  # type: ignore

    def test_set_date_format_invalid_type(self):
        """Test setting date format to a non-string value raises ATSTypeError."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)

        with self.assertRaises(ATSTypeError):
            formatter.set_date_format(["invalid_type"])  # type: ignore

    def test_set_date_format_empty_string(self):
        """Test setting date format to an empty string raises ATSValueError."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)

        with self.assertRaises(ATSValueError):
            formatter.set_date_format("")

    def test_protocol_conformance(self):
        """Test if LogFormatter satisfies the ILogFormatter protocol."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)
        self.assertIsInstance(formatter, ILogFormatter)

    def test_string_representation(self):
        """Test __str__ output via to_str helper."""
        formatter = LogFormatter(log_format=None, log_datefmt=None)
        result = str(formatter)

        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
