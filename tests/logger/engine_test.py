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
import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests Logger component logic.
    '''

    def setUp(self) -> None:
        self.mock_logger = MagicMock(spec=IUnderlyingLogger)
        self.mock_logger.has_handlers.return_value = True
        self.mock_formatter = MagicMock(spec=ILogFormatter)
        self.mock_buffer = MagicMock(spec=ILogBuffer)
        self.mock_buffer.is_enabled = True
        self.mock_handler_manager = MagicMock(spec=ILogHandlerManager)
        self.mock_message_processor = MagicMock(spec=IMessageProcessor)
        self.mock_message_processor.process.side_effect = lambda x: x

        self.valid_bundle = LoggerBundle(
            logger=self.mock_logger,
            has_file_handler=True,
            formatter=self.mock_formatter,
            buffer=self.mock_buffer,
            handler_manager=self.mock_handler_manager,
            message_processor=self.mock_message_processor
        )

    def test_init_success(self) -> None:
        logger = Logger(self.valid_bundle)
        self.assertTrue(logger.is_initialized())
        self.assertIs(logger.get_bundle().logger, self.mock_logger)

    def test_init_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError):
            Logger(None)  # type: ignore
        with self.assertRaises(ATSTypeError):
            Logger("invalid")  # type: ignore

    def test_write_log(self) -> None:
        logger = Logger(self.valid_bundle)
        logger.write_log(logging.INFO, "hello world")
        self.mock_message_processor.process.assert_called_once_with("hello world")
        self.mock_logger.log.assert_called_once_with(logging.INFO, "hello world")

    def test_write_log_buffering(self) -> None:
        bundle = LoggerBundle(
            logger=self.mock_logger,
            has_file_handler=False,
            formatter=self.mock_formatter,
            buffer=self.mock_buffer,
            handler_manager=self.mock_handler_manager,
            message_processor=self.mock_message_processor
        )
        logger = Logger(bundle)
        logger.write_log(logging.WARNING, "buffered alert")
        self.mock_buffer.add.assert_called_once_with("buffered alert", logging.WARNING)

    def test_set_level(self) -> None:
        logger = Logger(self.valid_bundle)
        logger.set_level(logging.DEBUG)
        self.mock_logger.set_level.assert_called_once_with(logging.DEBUG)

    def test_set_log_file(self) -> None:
        logger = Logger(self.valid_bundle)
        self.mock_handler_manager.set_log_file.return_value = True
        self.assertTrue(logger.set_log_file("test.log"))
        self.mock_handler_manager.set_log_file.assert_called_once_with("test.log")

    def test_set_stdout(self) -> None:
        logger = Logger(self.valid_bundle)
        self.mock_handler_manager.set_stdout.return_value = True
        self.assertTrue(logger.set_stdout())
        self.mock_handler_manager.set_stdout.assert_called_once()

    def test_stop_buffering(self) -> None:
        logger = Logger(self.valid_bundle)
        logger.stop_buffering()
        self.mock_buffer.clear.assert_called_once()

    def test_update_bundle(self) -> None:
        logger = Logger(self.valid_bundle)
        new_logger = MagicMock(spec=IUnderlyingLogger)
        new_logger.has_handlers.return_value = True
        new_bundle = LoggerBundle(
            logger=new_logger,
            has_file_handler=False,
            formatter=self.mock_formatter,
            buffer=self.mock_buffer,
            handler_manager=self.mock_handler_manager,
            message_processor=self.mock_message_processor
        )
        self.assertTrue(logger.update_bundle(new_bundle))
        self.assertIs(logger.get_bundle().logger, new_logger)

    def test_update_bundle_invalid(self) -> None:
        logger = Logger(self.valid_bundle)
        self.assertFalse(logger.update_bundle("invalid" * 10))  # type: ignore

    def test_set_log_file_fail(self) -> None:
        logger = Logger(self.valid_bundle)
        self.mock_handler_manager.set_log_file.return_value = False
        self.assertFalse(logger.set_log_file("test.log"))

    def test_set_stdout_fail(self) -> None:
        logger = Logger(self.valid_bundle)
        self.mock_handler_manager.set_stdout.return_value = False
        self.assertFalse(logger.set_stdout())

    def test_write_log_invalid_message(self) -> None:
        logger = Logger(self.valid_bundle)
        # Empty string
        logger.write_log(logging.INFO, "")
        self.mock_logger.log.assert_not_called()
        # Invalid type
        logger.write_log(logging.INFO, 123)  # type: ignore
        self.mock_logger.log.assert_not_called()

    def test_string_representation(self) -> None:
        logger = Logger(self.valid_bundle)
        self.assertIn("Logger", str(logger))

    def test_flush_buffer_disabled(self) -> None:
        self.mock_buffer.is_enabled = False
        bundle = LoggerBundle(
            logger=self.mock_logger,
            has_file_handler=False,
            formatter=self.mock_formatter,
            buffer=self.mock_buffer,
            handler_manager=self.mock_handler_manager,
            message_processor=self.mock_message_processor
        )
        logger = Logger(bundle)
        logger._flush_buffer()
        self.mock_buffer.flush.assert_not_called()


if __name__ == "__main__":
    unittest.main()
