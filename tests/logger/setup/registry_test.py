# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
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
    Unit tests for LoggerBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.registry import LoggerBundleRegistry
from ats_utilities.logger.setup.dependencies import LoggerBundleDependencies
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor


class RegistryTest(unittest.TestCase):
    '''
        Defines class RegistryTest with attribute(s) and method(s).
        Tests LoggerBundleRegistry logic.
    '''

    def test_create_bundle(self) -> None:
        mock_logger = MagicMock(spec=IUnderlyingLogger)
        mock_formatter = MagicMock(spec=ILogFormatter)
        mock_buffer = MagicMock(spec=ILogBuffer)
        mock_handler_manager = MagicMock(spec=ILogHandlerManager)
        mock_message_processor = MagicMock(spec=IMessageProcessor)

        dependencies = LoggerBundleDependencies(
            logger=mock_logger,
            has_file_handler=True,
            formatter=mock_formatter,
            buffer=mock_buffer,
            handler_manager=mock_handler_manager,
            message_processor=mock_message_processor
        )

        bundle = LoggerBundleRegistry.create_bundle(dependencies)
        self.assertIsInstance(bundle, LoggerBundle)
        self.assertIs(bundle.logger, mock_logger)
        self.assertTrue(bundle.has_file_handler)
        self.assertIs(bundle.formatter, mock_formatter)
        self.assertIs(bundle.buffer, mock_buffer)
        self.assertIs(bundle.handler_manager, mock_handler_manager)
        self.assertIs(bundle.message_processor, mock_message_processor)


if __name__ == "__main__":
    unittest.main()
