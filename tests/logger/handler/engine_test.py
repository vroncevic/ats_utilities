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
    Unit tests for LogHandlerManager class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.handler.engine import LogHandlerManager
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger


class LogHandlerManagerTest(unittest.TestCase):
    '''
        Defines class LogHandlerManagerTest with attribute(s) and method(s).
        Tests LogHandlerManager logic.
    '''

    def test_init_valid(self) -> None:
        mock_logger = MagicMock(spec=IUnderlyingLogger)
        manager = LogHandlerManager(mock_logger)
        self.assertIs(manager._logger, mock_logger)

    def test_init_invalid(self) -> None:
        with self.assertRaises(ATSValueError):
            LogHandlerManager(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            LogHandlerManager("not a logger")  # type: ignore

    def test_set_log_file(self) -> None:
        mock_logger = MagicMock(spec=IUnderlyingLogger)
        mock_logger.add_file_handler.return_value = True
        manager = LogHandlerManager(mock_logger)
        
        self.assertTrue(manager.set_log_file("test.log"))
        mock_logger.add_file_handler.assert_called_once_with("test.log")

    def test_set_stdout(self) -> None:
        mock_logger = MagicMock(spec=IUnderlyingLogger)
        mock_logger.add_stdout_handler.return_value = True
        manager = LogHandlerManager(mock_logger)
        
        self.assertTrue(manager.set_stdout())
        mock_logger.add_stdout_handler.assert_called_once()

    def test_str(self) -> None:
        mock_logger = MagicMock(spec=IUnderlyingLogger)
        manager = LogHandlerManager(mock_logger)
        self.assertIn("LogHandlerManager", str(manager))


if __name__ == "__main__":
    unittest.main()
