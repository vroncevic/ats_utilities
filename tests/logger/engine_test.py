# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Unit tests for Logger class.
'''

from __future__ import annotations

import logging
import os
import sys
import unittest
from typing import Any
from unittest.mock import MagicMock, patch

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.bundle import LoggerBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests Logger component logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_standard_logger - Tests Logger initialization with standard logging.Logger.
                | test_init_custom_logger - Tests Logger initialization with custom logger object.
                | test_init_invalid - Tests Logger initialization with invalid inputs.
                | test_process_message_ansi_strip - Tests stripping ANSI color codes.
                | test_write_log_standard - Tests write_log with standard logger.
                | test_write_log_custom - Tests write_log with custom logger.
                | test_early_logs_buffering_and_flush_standard - Tests early logging and flushing with standard logger.
                | test_early_logs_buffering_and_flush_custom - Tests early logging and flushing with custom logger.
                | test_is_initialized - Tests is_initialized method.
                | test_set_level - Tests set_level method.
                | test_set_log_file_handler_replacement - Tests set_log_file with directory creation and handler replacement.
                | test_stop_buffering - Tests stop_buffering method.
                | test_str - Tests __str__ representation.
    '''

    def test_init_standard_logger(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        self.assertIs(logger._logger, mock_std_logger)
        self.assertIn(logging.INFO, logger._log_methods)

    def test_init_custom_logger(self) -> None:
        class CustomLogger:
            def write_log(self, message: str, ctrl: int) -> None:
                pass

        custom = CustomLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        self.assertIs(logger._logger, custom)
        self.assertIn(logging.INFO, logger._log_methods)

    def test_init_invalid(self) -> None:
        with self.assertRaises(ATSValueError):
            Logger(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            Logger("invalid")  # type: ignore

    def test_process_message_ansi_strip(self) -> None:
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()
        bundle = LoggerBundle(
            logger=mock_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)

        # Test normal message
        self.assertEqual(logger._process_message("hello"), "hello")

        # Test stripping when NO_COLOR is present
        with patch.dict(os.environ, {"NO_COLOR": "1"}):
            self.assertEqual(logger._process_message("\x1b[31mred\x1b[0m"), "red")

        # Test stripping when not a tty and FORCE_COLOR not set
        with patch.object(sys.stdout, "isatty", return_value=False):
            with patch.dict(os.environ, {}, clear=True):
                self.assertEqual(logger._process_message("\x1b[31mred\x1b[0m"), "red")

        # Test preserving when force color is present even if not a tty
        with patch.object(sys.stdout, "isatty", return_value=False):
            with patch.dict(os.environ, {"FORCE_COLOR": "1"}):
                self.assertEqual(logger._process_message("\x1b[31mred\x1b[0m"), "\x1b[31mred\x1b[0m")

    def test_write_log_standard(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("test message", logging.INFO)
        mock_std_logger.info.assert_called_once_with("test message")

    def test_write_log_custom(self) -> None:
        class CustomLogger:
            def __init__(self) -> None:
                self.write_log = MagicMock()

        custom = CustomLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("test custom message", logging.WARNING)
        custom.write_log.assert_called_once_with("test custom message", logging.WARNING)

    def test_early_logs_buffering_and_flush_standard(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_std_logger.handlers = []
        # log_file="" makes self._has_file_handler = False
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        self.assertFalse(logger._has_file_handler)

        logger.write_log("buffered msg", logging.INFO)
        self.assertEqual(len(logger._early_logs_buffer), 1)
        self.assertEqual(logger._early_logs_buffer[0], ("buffered msg", logging.INFO))

        # calling set_log_file will flush early logs
        with patch("ats_utilities.logger.engine.FileHandler") as mock_handler:
            logger.set_log_file("some_file.log")
            self.assertTrue(logger._has_file_handler)
            self.assertEqual(len(logger._early_logs_buffer), 0)
            mock_std_logger.log.assert_called_once_with(logging.INFO, "buffered msg")

    def test_early_logs_buffering_and_flush_custom(self) -> None:
        class CustomLogger:
            def __init__(self) -> None:
                self.calls = []
            def write_log(self, message: str, ctrl: int) -> None:
                self.calls.append((message, ctrl))
            def set_log_file(self, log_file: str) -> None:
                pass

        custom = CustomLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("custom buffered msg", logging.WARNING)
        self.assertEqual(len(logger._early_logs_buffer), 1)

        logger.set_log_file("some_custom.log")
        self.assertEqual(custom.calls, [
            ("custom buffered msg", logging.WARNING),
            ("custom buffered msg", logging.WARNING)
        ])
        self.assertEqual(len(logger._early_logs_buffer), 0)

    def test_early_logs_buffering_and_flush_custom_no_log_methods(self) -> None:
        """Tests branch 224->228 when logger has neither log nor write_log during flush."""
        class CustomLogger:
            def __init__(self) -> None:
                self.write_log = MagicMock()
            def set_log_file(self, log_file: str) -> None:
                pass

        custom = CustomLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        # Delete write_log attribute to simulate a logger without log/write_log methods
        if hasattr(custom, 'write_log'):
            delattr(custom, 'write_log')
        if hasattr(CustomLogger, 'write_log'):
            delattr(CustomLogger, 'write_log')

        logger._early_logs_buffer.append(("msg", logging.INFO))
        logger.set_log_file("some_custom.log")
        self.assertEqual(len(logger._early_logs_buffer), 0)

    def test_init_logger_with_no_log_methods(self) -> None:
        """Tests branch 112->exit when custom logger has neither info nor write_log."""
        class MinimalLogger:
            def write_log(self, message: str, ctrl: int) -> None:
                pass
        custom = MinimalLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="test.log",
            log_level=logging.INFO
        )
        delattr(MinimalLogger, "write_log")
        logger = Logger(bundle)
        self.assertFalse(hasattr(logger, "_log_methods"))

    def test_set_level_with_no_set_level_methods(self) -> None:
        """Tests branch 187->exit when custom logger has neither setLevel nor set_level."""
        class MinimalLogger:
            def write_log(self, message: str, ctrl: int) -> None:
                pass
        custom = MinimalLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        # Should exit cleanly without raising an exception
        logger.set_level(logging.DEBUG)

    def test_is_initialized(self) -> None:
        # Case 1: Custom logger
        class CustomLogger:
            def write_log(self, message: str, ctrl: int) -> None:
                pass

        bundle = LoggerBundle(
            logger=CustomLogger(),
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        self.assertTrue(logger.is_initialized())

        # Case 2: standard Logger
        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_std_logger.hasHandlers = MagicMock(return_value=True)
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        self.assertTrue(logger.is_initialized())

    def test_set_level(self) -> None:
        # Case 1: Standard setLevel
        mock_std_logger = MagicMock(spec=logging.Logger)
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.set_level(logging.DEBUG)
        mock_std_logger.setLevel.assert_called_once_with(logging.DEBUG)

        # Case 2: Custom set_level
        class CustomLogger:
            def __init__(self) -> None:
                self.write_log = MagicMock()
                self.set_level = MagicMock()

        custom = CustomLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.set_level(logging.DEBUG)
        custom.set_level.assert_called_once_with(logging.DEBUG)

    def test_set_log_file_handler_replacement(self) -> None:
        class DummyFileHandler(logging.FileHandler):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                pass

        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_handler = MagicMock(spec=DummyFileHandler)
        mock_std_logger.handlers = [mock_handler]

        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)

        with patch("ats_utilities.logger.engine.FileHandler", DummyFileHandler):
            logger.set_log_file("new_dir/test.log")
            # Should have removed the old handler
            mock_std_logger.removeHandler.assert_called_once_with(mock_handler)
            # Should have added the new one
            mock_std_logger.addHandler.assert_called_once()

    def test_stop_buffering(self) -> None:
        # Case 1: Custom stop_buffering
        class CustomLogger:
            def __init__(self) -> None:
                self.write_log = MagicMock()
                self.stop_buffering = MagicMock()

        custom = CustomLogger()
        bundle = LoggerBundle(
            logger=custom,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("buffered msg", logging.INFO)
        self.assertEqual(len(logger._early_logs_buffer), 1)

        logger.stop_buffering()
        custom.stop_buffering.assert_called_once()
        self.assertEqual(len(logger._early_logs_buffer), 0)
        self.assertTrue(logger._has_file_handler)

    def test_write_log_invalid_params(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        # Empty message (bool(message) is False)
        logger.write_log("", logging.INFO)
        mock_std_logger.info.assert_not_called()

        # Non-string message
        logger.write_log(123, logging.INFO)  # type: ignore
        mock_std_logger.info.assert_not_called()

        # Invalid control level (not in _log_methods keys)
        logger.write_log("test", 999)
        mock_std_logger.info.assert_not_called()

    def test_set_log_file_no_set_or_add_handler(self) -> None:
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()
        # Delete addHandler and set_log_file
        if hasattr(mock_logger, 'addHandler'):
            del mock_logger.addHandler
        if hasattr(mock_logger, 'set_log_file'):
            del mock_logger.set_log_file

        bundle = LoggerBundle(
            logger=mock_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.set_log_file("new.log")

    def test_set_log_file_create_directory(self) -> None:
        import tempfile
        import shutil

        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_std_logger.handlers = []
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)

        temp_dir = tempfile.mkdtemp()
        try:
            nested_log_file = os.path.join(temp_dir, "new_subdir", "test.log")
            logger.set_log_file(nested_log_file)
            self.assertTrue(os.path.exists(os.path.join(temp_dir, "new_subdir")))
        finally:
            if mock_std_logger.addHandler.called:
                for call_args in mock_std_logger.addHandler.call_args_list:
                    handler = call_args[0][0]
                    if hasattr(handler, "close"):
                        handler.close()
            shutil.rmtree(temp_dir)

    def test_set_log_file_non_file_handler(self) -> None:
        class DummyFileHandler(logging.FileHandler):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                pass

        mock_std_logger = MagicMock(spec=logging.Logger)
        # Put both a FileHandler mock and a non-FileHandler mock
        mock_fh = MagicMock(spec=DummyFileHandler)
        mock_sh = MagicMock(spec=logging.StreamHandler)
        mock_std_logger.handlers = [mock_fh, mock_sh]

        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)

        with patch("ats_utilities.logger.engine.FileHandler", DummyFileHandler):
            logger.set_log_file("new_dir/test.log")
            # Should have removed only the FileHandler
            mock_std_logger.removeHandler.assert_called_once_with(mock_fh)

    def test_stop_buffering_no_stop_method(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("test", logging.INFO)
        self.assertEqual(len(logger._early_logs_buffer), 1)

        logger.stop_buffering()
        self.assertEqual(len(logger._early_logs_buffer), 0)

    def test_str(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        self.assertIn("Logger", str(logger))

    def test_set_stdout(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_std_logger.handlers = []
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.set_stdout()
        self.assertTrue(logger._has_file_handler)
        mock_std_logger.addHandler.assert_called_once()
        handler = mock_std_logger.addHandler.call_args[0][0]
        self.assertIsInstance(handler, logging.StreamHandler)
        self.assertIs(handler.stream, sys.stdout)

    def test_set_stderr(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_std_logger.handlers = []
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.set_stderr()
        self.assertTrue(logger._has_file_handler)
        mock_std_logger.addHandler.assert_called_once()
        handler = mock_std_logger.addHandler.call_args[0][0]
        self.assertIsInstance(handler, logging.StreamHandler)
        self.assertIs(handler.stream, sys.stderr)

    def test_set_stdout_flushes_early_logs(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_std_logger.handlers = []
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("early message", logging.INFO)
        self.assertEqual(len(logger._early_logs_buffer), 1)

        logger.set_stdout()
        self.assertEqual(len(logger._early_logs_buffer), 0)
        mock_std_logger.log.assert_called_once_with(logging.INFO, "early message")

    def test_set_stderr_flushes_early_logs(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        mock_std_logger.handlers = []
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("early message", logging.INFO)
        self.assertEqual(len(logger._early_logs_buffer), 1)

        logger.set_stderr()
        self.assertEqual(len(logger._early_logs_buffer), 0)
        mock_std_logger.log.assert_called_once_with(logging.INFO, "early message")

    def test_set_stdout_removes_other_handlers(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        file_handler = MagicMock(spec=logging.FileHandler)
        stderr_stream = MagicMock(spec=logging.StreamHandler)
        stderr_stream.stream = sys.stderr
        stdout_stream = MagicMock(spec=logging.StreamHandler)
        stdout_stream.stream = sys.stdout

        mock_std_logger.handlers = [file_handler, stderr_stream, stdout_stream]
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.set_stdout()

        mock_std_logger.removeHandler.assert_any_call(file_handler)
        mock_std_logger.removeHandler.assert_any_call(stderr_stream)
        self.assertEqual(mock_std_logger.removeHandler.call_count, 2)

    def test_set_stderr_removes_other_handlers(self) -> None:
        mock_std_logger = MagicMock(spec=logging.Logger)
        file_handler = MagicMock(spec=logging.FileHandler)
        stderr_stream = MagicMock(spec=logging.StreamHandler)
        stderr_stream.stream = sys.stderr
        stdout_stream = MagicMock(spec=logging.StreamHandler)
        stdout_stream.stream = sys.stdout

        mock_std_logger.handlers = [file_handler, stderr_stream, stdout_stream]
        bundle = LoggerBundle(
            logger=mock_std_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.set_stderr()

        mock_std_logger.removeHandler.assert_any_call(file_handler)
        mock_std_logger.removeHandler.assert_any_call(stdout_stream)
        self.assertEqual(mock_std_logger.removeHandler.call_count, 2)

    def test_set_stdout_custom_logger_flushes_write_log(self) -> None:
        class CustomLoggerMock:
            def __init__(self):
                self.logs = []
                self.handlers = []
            def addHandler(self, h):
                pass
            def removeHandler(self, h):
                pass
            def write_log(self, msg, level):
                self.logs.append((msg, level))

        custom_logger = CustomLoggerMock()
        bundle = LoggerBundle(
            logger=custom_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("custom early", logging.INFO)
        logger.set_stdout()
        self.assertEqual(custom_logger.logs, [
            ("custom early", logging.INFO),
            ("custom early", logging.INFO)
        ])

    def test_set_stderr_custom_logger_flushes_write_log(self) -> None:
        class CustomLoggerMock:
            def __init__(self):
                self.logs = []
                self.handlers = []
            def addHandler(self, h):
                pass
            def removeHandler(self, h):
                pass
            def write_log(self, msg, level):
                self.logs.append((msg, level))

        custom_logger = CustomLoggerMock()
        bundle = LoggerBundle(
            logger=custom_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("custom early", logging.INFO)
        logger.set_stderr()
        self.assertEqual(custom_logger.logs, [
            ("custom early", logging.INFO),
            ("custom early", logging.INFO)
        ])

    def test_set_stdout_logger_no_add_handler(self) -> None:
        class MinimalLogger:
            def __init__(self):
                self.calls = []
            def write_log(self, msg, level):
                pass
            def log(self, level, msg):
                self.calls.append((msg, level))

        minimal_logger = MinimalLogger()
        bundle = LoggerBundle(
            logger=minimal_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("early message", logging.INFO)
        logger.set_stdout()
        self.assertEqual(minimal_logger.calls, [("early message", logging.INFO)])

    def test_set_stderr_logger_no_add_handler(self) -> None:
        class MinimalLogger:
            def __init__(self):
                self.calls = []
            def write_log(self, msg, level):
                pass
            def log(self, level, msg):
                self.calls.append((msg, level))

        minimal_logger = MinimalLogger()
        bundle = LoggerBundle(
            logger=minimal_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger.write_log("early message", logging.INFO)
        logger.set_stderr()
        self.assertEqual(minimal_logger.calls, [("early message", logging.INFO)])

    def test_set_stdout_logger_no_log_methods_flushes_nothing(self) -> None:
        class DummyLogger:
            def __init__(self):
                self.handlers = []
            def addHandler(self, h):
                pass
            def removeHandler(self, h):
                pass
            def debug(self, msg): pass
            def info(self, msg): pass
            def warning(self, msg): pass
            def error(self, msg): pass
            def critical(self, msg): pass

        dummy_logger = DummyLogger()
        bundle = LoggerBundle(
            logger=dummy_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger._early_logs_buffer.append(("msg", logging.INFO))
        logger.set_stdout()
        self.assertEqual(len(logger._early_logs_buffer), 0)

    def test_set_stderr_logger_no_log_methods_flushes_nothing(self) -> None:
        class DummyLogger:
            def __init__(self):
                self.handlers = []
            def addHandler(self, h):
                pass
            def removeHandler(self, h):
                pass
            def debug(self, msg): pass
            def info(self, msg): pass
            def warning(self, msg): pass
            def error(self, msg): pass
            def critical(self, msg): pass

        dummy_logger = DummyLogger()
        bundle = LoggerBundle(
            logger=dummy_logger,
            log_file="",
            log_level=logging.INFO
        )
        logger = Logger(bundle)
        logger._early_logs_buffer.append(("msg", logging.INFO))
        logger.set_stderr()
        self.assertEqual(len(logger._early_logs_buffer), 0)


if __name__ == "__main__":
    unittest.main()
