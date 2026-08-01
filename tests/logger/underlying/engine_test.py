# -*- coding: UTF-8 -*-

import logging
import unittest
from unittest.mock import Mock, patch, MagicMock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.underlying.engine import LoggerAdapter
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter


class TestLoggerAdapter(unittest.TestCase):
    """Unit tests covering all behaviors and edge cases for LoggerAdapter."""

    def setUp(self):
        """Set up standard mocks for logger and formatter instances."""
        self.mock_logger = Mock(spec=logging.Logger)
        self.mock_formatter = Mock(spec=ILogFormatter)
        
        # Configure standard mock formatter responses
        self.mock_formatter.get_format.return_value = "%(asctime)s - %(message)s"
        self.mock_formatter.get_date_format.return_value = "%Y-%m-%d"

    def test_initialization_success(self):
        """Test initializing LoggerAdapter with valid arguments."""
        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        self.assertEqual(adapter._logger, self.mock_logger)
        self.assertEqual(adapter._formatter, self.mock_formatter)

    def test_initialization_none_logger(self):
        """Test initialization raises ATSValueError when logger is None."""
        with self.assertRaises(ATSValueError):
            LoggerAdapter(None, self.mock_formatter)  # type: ignore

    def test_initialization_none_formatter(self):
        """Test initialization raises ATSValueError when formatter is None."""
        with self.assertRaises(ATSValueError):
            LoggerAdapter(self.mock_logger, None)  # type: ignore

    def test_initialization_invalid_logger_type(self):
        """Test initialization raises ATSTypeError when logger is not standard Logger."""
        with self.assertRaises(ATSTypeError):
            LoggerAdapter("not_a_logger", self.mock_formatter)  # type: ignore

    def test_initialization_invalid_formatter_type(self):
        """Test initialization raises ATSTypeError when formatter violates ILogFormatter protocol."""
        invalid_formatter = "not_a_formatter"
        with self.assertRaises(ATSTypeError):
            LoggerAdapter(self.mock_logger, invalid_formatter)  # type: ignore

    def test_log_delegation(self):
        """Test delegating log calls to the underlying logger instance."""
        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        adapter.log(logging.INFO, "Test log message")

        self.mock_logger.log.assert_called_once_with(logging.INFO, "Test log message")

    def test_set_level_delegation(self):
        """Test delegating set_level calls to the underlying logger instance."""
        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        adapter.set_level(logging.DEBUG)

        self.mock_logger.setLevel.assert_called_once_with(logging.DEBUG)

    def test_has_handlers_delegation(self):
        """Test delegating has_handlers calls to the underlying logger instance."""
        self.mock_logger.hasHandlers.return_value = True
        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)

        self.assertTrue(adapter.has_handlers())
        self.mock_logger.hasHandlers.assert_called_once()

    @patch("ats_utilities.logger.underlying.engine.FileHandler")
    def test_add_file_handler_success(self, mock_file_handler_cls):
        """Test successfully attaching a FileHandler to the logger."""
        mock_handler_instance = MagicMock()
        mock_file_handler_cls.return_value = mock_handler_instance

        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        result = adapter.add_file_handler("app.log")

        self.assertTrue(result)
        mock_file_handler_cls.assert_called_once_with("app.log")
        self.mock_logger.addHandler.assert_called_once_with(mock_handler_instance)

    @patch("ats_utilities.logger.underlying.engine.FileHandler")
    def test_add_file_handler_failure(self, mock_file_handler_cls):
        """Test add_file_handler handles exceptions gracefully and returns False."""
        mock_file_handler_cls.side_effect = Exception("OS File Permission Error")

        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        result = adapter.add_file_handler("/restricted/app.log")

        self.assertFalse(result)
        self.mock_logger.addHandler.assert_not_called()

    @patch("ats_utilities.logger.underlying.engine.StreamHandler")
    def test_add_stdout_handler_success(self, mock_stream_handler_cls):
        """Test successfully attaching a StreamHandler to the logger."""
        mock_handler_instance = MagicMock()
        mock_stream_handler_cls.return_value = mock_handler_instance

        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        result = adapter.add_stdout_handler()

        self.assertTrue(result)
        self.mock_logger.addHandler.assert_called_once_with(mock_handler_instance)

    @patch("ats_utilities.logger.underlying.engine.StreamHandler")
    def test_add_stdout_handler_failure(self, mock_stream_handler_cls):
        """Test add_stdout_handler handles exceptions gracefully and returns False."""
        mock_stream_handler_cls.side_effect = Exception("Stream error")

        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        result = adapter.add_stdout_handler()

        self.assertFalse(result)
        self.mock_logger.addHandler.assert_not_called()

    def test_protocol_conformance(self):
        """Test if LoggerAdapter conforms to the IUnderlyingLogger protocol interface."""
        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        self.assertIsInstance(adapter, IUnderlyingLogger)

    def test_string_representation(self):
        """Test __str__ output representation calls reflection helper correctly."""
        adapter = LoggerAdapter(self.mock_logger, self.mock_formatter)
        result = str(adapter)

        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
