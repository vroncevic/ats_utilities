# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
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
    Unit tests for LoggerBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor


class BundleTest(unittest.TestCase):
    '''
        Defines class BundleTest with attribute(s) and method(s).
        Tests LoggerBundle dataclass logic.
    '''

    def setUp(self) -> None:
        self.mock_logger = MagicMock(spec=IUnderlyingLogger)
        self.mock_formatter = MagicMock(spec=ILogFormatter)
        self.mock_buffer = MagicMock(spec=ILogBuffer)
        self.mock_handler_manager = MagicMock(spec=ILogHandlerManager)
        self.mock_message_processor = MagicMock(spec=IMessageProcessor)

        self.valid_params = {
            "logger": self.mock_logger,
            "has_file_handler": True,
            "formatter": self.mock_formatter,
            "buffer": self.mock_buffer,
            "handler_manager": self.mock_handler_manager,
            "message_processor": self.mock_message_processor
        }

    def test_init_valid(self) -> None:
        bundle = LoggerBundle(**self.valid_params)
        self.assertIs(bundle.logger, self.mock_logger)
        self.assertTrue(bundle.has_file_handler)
        self.assertIs(bundle.formatter, self.mock_formatter)
        self.assertIs(bundle.buffer, self.mock_buffer)
        self.assertIs(bundle.handler_manager, self.mock_handler_manager)
        self.assertIs(bundle.message_processor, self.mock_message_processor)

    def test_to_dict(self) -> None:
        bundle = LoggerBundle(**self.valid_params)
        exported_dict = bundle.to_dict()
        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict["logger"], self.mock_logger)
        self.assertEqual(exported_dict["has_file_handler"], True)
        self.assertEqual(exported_dict["formatter"], self.mock_formatter)
        self.assertEqual(exported_dict["buffer"], self.mock_buffer)
        self.assertEqual(exported_dict["handler_manager"], self.mock_handler_manager)
        self.assertEqual(exported_dict["message_processor"], self.mock_message_processor)


if __name__ == "__main__":
    unittest.main()
