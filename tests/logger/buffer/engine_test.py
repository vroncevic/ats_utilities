# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import Mock, call

from ats_utilities.logger.buffer.engine import LogBuffer
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.exceptions import ATSTypeError


class TestLogBuffer(unittest.TestCase):
    """Unit tests covering all behaviors and edge cases of the LogBuffer class."""

    def test_initialization_defaults(self):
        """Test default initialization behavior."""
        log_buffer = LogBuffer(limit=None)
        
        self.assertTrue(log_buffer.is_enabled)
        self.assertEqual(log_buffer._limit, LogBuffer.DEFAULT_LIMIT)
        self.assertEqual(len(log_buffer._buffer), 0)

    def test_initialization_custom_limit(self):
        """Test initialization with a custom limit."""
        custom_limit = 50
        log_buffer = LogBuffer(limit=custom_limit)
        
        self.assertEqual(log_buffer._limit, custom_limit)

    def test_initialization_invalid_limit(self):
        """Test initialization with non-integer limit raises ATSTypeError."""
        with self.assertRaises(ATSTypeError):
            LogBuffer(limit="invalid_limit")  # type: ignore

    def test_add_messages(self):
        """Test adding messages up to limit."""
        log_buffer = LogBuffer(limit=2)
        
        log_buffer.add(10, "Debug message")
        log_buffer.add(20, "Info message")
        
        # Adding past limit should be ignored
        log_buffer.add(30, "Warning message")

        self.assertEqual(len(log_buffer._buffer), 2)
        self.assertEqual(
            log_buffer._buffer,
            [(10, "Debug message"), (20, "Info message")]
        )

    def test_flush_behavior(self):
        """Test flushing buffered logs to a writer callback."""
        log_buffer = LogBuffer(limit=10)
        log_buffer.add(20, "First message")
        log_buffer.add(40, "Second message")

        mock_writer = Mock()
        log_buffer.flush(mock_writer)

        # Ensure the writer callback received the expected entries in order
        expected_calls = [
            call(20, "First message"),
            call(40, "Second message")
        ]
        mock_writer.assert_has_calls(expected_calls)
        self.assertEqual(mock_writer.call_count, 2)

        # Buffer should be empty and buffering disabled after flush
        self.assertEqual(len(log_buffer._buffer), 0)
        self.assertFalse(log_buffer.is_enabled)

    def test_add_after_flush(self):
        """Test that adding messages after flushing has no effect (disabled state)."""
        log_buffer = LogBuffer(limit=10)
        log_buffer.add(10, "Message before flush")
        
        mock_writer = Mock()
        log_buffer.flush(mock_writer)

        # Attempt adding when enabled flag is False
        log_buffer.add(20, "Message after flush")
        self.assertEqual(len(log_buffer._buffer), 0)

    def test_clear_buffer(self):
        """Test clearing the buffer manually."""
        log_buffer = LogBuffer(limit=10)
        log_buffer.add(10, "Debug message")
        
        log_buffer.clear()

        self.assertEqual(len(log_buffer._buffer), 0)
        self.assertFalse(log_buffer.is_enabled)

    def test_protocol_conformance(self):
        """Test if LogBuffer conforms to the ILogBuffer Protocol interface."""
        log_buffer = LogBuffer(limit=10)
        self.assertIsInstance(log_buffer, ILogBuffer)

    def test_string_representation(self):
        """Test __str__ output representation calls to_str helper correctly."""
        log_buffer = LogBuffer(limit=5)
        log_buffer.add(10, "Test string")
        
        # Verify it returns a non-empty string representation
        result = str(log_buffer)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
