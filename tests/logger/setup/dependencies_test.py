# -*- coding: UTF-8 -*-

'''
Module
    dependencies_test.py
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
    Unit tests for LoggerDependencies class.
'''

from __future__ import annotations

import unittest
from typing import get_type_hints
from unittest.mock import MagicMock

from ats_utilities.logger.setup.dependencies import LoggerDependencies
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor


class LoggerDependenciesTest(unittest.TestCase):
    '''
        Defines class LoggerDependenciesTest with attribute(s) and method(s).
        Tests LoggerDependencies TypedDict structure.
    '''

    def test_type_hints(self) -> None:
        hints = get_type_hints(LoggerDependencies)
        self.assertEqual(hints['logger'], IUnderlyingLogger)
        self.assertEqual(hints['has_file_handler'], bool)
        self.assertEqual(hints['formatter'], ILogFormatter)
        self.assertEqual(hints['buffer'], ILogBuffer)
        self.assertEqual(hints['handler_manager'], ILogHandlerManager)
        self.assertEqual(hints['message_processor'], IMessageProcessor)

    def test_instantiation(self) -> None:
        deps: LoggerDependencies = {
            'logger': MagicMock(spec=IUnderlyingLogger),
            'has_file_handler': True,
            'formatter': MagicMock(spec=ILogFormatter),
            'buffer': MagicMock(spec=ILogBuffer),
            'handler_manager': MagicMock(spec=ILogHandlerManager),
            'message_processor': MagicMock(spec=IMessageProcessor)
        }
        self.assertEqual(len(deps), 6)


if __name__ == "__main__":
    unittest.main()
