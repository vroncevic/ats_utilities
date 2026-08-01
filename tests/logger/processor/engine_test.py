# -*- coding: UTF-8 -*-

import os
import re
import unittest
from unittest.mock import patch

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.processor.engine import MessageProcessor
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor


class TestMessageProcessor(unittest.TestCase):
    """Unit tests covering all behaviors and edge cases for MessageProcessor."""

    def test_initialization_default_pattern(self):
        """Test default initialization sets the standard ANSI escape pattern."""
        processor = MessageProcessor()
        self.assertEqual(processor.get_pattern(), MessageProcessor.DEFAULT_ESCAPE)

    def test_initialization_custom_pattern(self):
        """Test initializing with a custom compiled regex pattern."""
        custom_pattern = re.compile(r"\[FOO\]")
        processor = MessageProcessor(pattern=custom_pattern)
        self.assertEqual(processor.get_pattern(), custom_pattern)

    def test_initialization_invalid_pattern_type(self):
        """Test initialization raises ATSTypeError when pattern is not a compiled regex."""
        with self.assertRaises(ATSTypeError):
            MessageProcessor(pattern="not_a_regex_pattern")  # type: ignore

    def test_set_and_get_pattern_success(self):
        """Test setting and retrieving a new compiled regex pattern."""
        processor = MessageProcessor()
        new_pattern = re.compile(r"\d+")
        processor.set_pattern(new_pattern)

        self.assertEqual(processor.get_pattern(), new_pattern)

    def test_set_pattern_none_raises_exception(self):
        """Test setting pattern to None raises ATSValueError."""
        processor = MessageProcessor()
        with self.assertRaises(ATSValueError):
            processor.set_pattern(None)  # type: ignore

    def test_set_pattern_invalid_type(self):
        """Test setting pattern to a non-Pattern object raises ATSTypeError."""
        processor = MessageProcessor()
        with self.assertRaises(ATSTypeError):
            processor.set_pattern(12345)  # type: ignore

    @patch("ats_utilities.logger.processor.engine.stdout.isatty", return_value=True)
    @patch.dict(os.environ, {}, clear=True)
    def test_process_terminal_with_colors_enabled(self, mock_isatty):
        """Test message processing when output is a terminal and no NO_COLOR flag is set."""
        processor = MessageProcessor()
        colored_message = "\x1b[31mRed Text\x1b[0m"

        # ANSI color codes should remain intact
        processed = processor.process(colored_message)
        self.assertEqual(processed, colored_message)

    @patch("ats_utilities.logger.processor.engine.stdout.isatty", return_value=True)
    @patch.dict(os.environ, {"NO_COLOR": "1"}, clear=True)
    def test_process_no_color_environment_variable(self, mock_isatty):
        """Test message processing strips colors when NO_COLOR environment variable is present."""
        processor = MessageProcessor()
        colored_message = "\x1b[31mRed Text\x1b[0m"

        processed = processor.process(colored_message)
        self.assertEqual(processed, "Red Text")

    @patch("ats_utilities.logger.processor.engine.stdout.isatty", return_value=False)
    @patch.dict(os.environ, {}, clear=True)
    def test_process_non_terminal_without_force_color(self, mock_isatty):
        """Test message processing strips colors when not running in an interactive terminal."""
        processor = MessageProcessor()
        colored_message = "\x1b[32mGreen Text\x1b[0m"

        processed = processor.process(colored_message)
        self.assertEqual(processed, "Green Text")

    @patch("ats_utilities.logger.processor.engine.stdout.isatty", return_value=False)
    @patch.dict(os.environ, {"FORCE_COLOR": "1"}, clear=True)
    def test_process_non_terminal_with_force_color(self, mock_isatty):
        """Test message processing preserves colors in non-terminal mode if FORCE_COLOR is set."""
        processor = MessageProcessor()
        colored_message = "\x1b[32mGreen Text\x1b[0m"

        processed = processor.process(colored_message)
        self.assertEqual(processed, colored_message)

    @patch("ats_utilities.logger.processor.engine.stdout.isatty", return_value=False)
    @patch.dict(os.environ, {"NO_COLOR": "1", "FORCE_COLOR": "1"}, clear=True)
    def test_process_no_color_overrides_force_color(self, mock_isatty):
        """Test NO_COLOR takes precedence even if FORCE_COLOR is also present."""
        processor = MessageProcessor()
        colored_message = "\x1b[33mYellow Text\x1b[0m"

        processed = processor.process(colored_message)
        self.assertEqual(processed, "Yellow Text")

    def test_process_custom_pattern(self):
        """Test processing a log message with a custom filtering pattern."""
        custom_pattern = re.compile(r"\[SECRET_\d+\]")
        processor = MessageProcessor(pattern=custom_pattern)

        raw_message = "User auth success [SECRET_12345] welcome!"
        
        # Non-terminal or NO_COLOR triggers replacement
        with patch("ats_utilities.logger.processor.engine.stdout.isatty", return_value=False):
            processed = processor.process(raw_message)
            self.assertEqual(processed, "User auth success  welcome!")

    def test_protocol_conformance(self):
        """Test if MessageProcessor conforms to the IMessageProcessor protocol interface."""
        processor = MessageProcessor()
        self.assertIsInstance(processor, IMessageProcessor)

    def test_string_representation(self):
        """Test __str__ output representation calls reflection helper correctly."""
        processor = MessageProcessor()
        result = str(processor)

        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
