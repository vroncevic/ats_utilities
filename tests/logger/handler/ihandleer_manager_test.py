# -*- coding: UTF-8 -*-

'''
Module
    test_ihandler_manager.py
Info
    Unit tests for ILogHandlerManager protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager


class ConcreteLogHandlerManager:
    '''Mock implementation of ILogHandlerManager protocol for testing purposes.'''

    def __init__(self) -> None:
        self._active_file_handler: str | None = None
        self._stdout_configured: bool = False

    def set_log_file(self, log_file: str) -> bool:
        if isinstance(log_file, str) and log_file:
            self._active_file_handler = log_file
            return True
        return False

    def set_stdout(self) -> bool:
        self._stdout_configured = True
        return True

    def __str__(self) -> str:
        return "ConcreteLogHandlerManager"


class IncompleteLogHandlerManager:
    '''Class that lacks set_stdout method from ILogHandlerManager protocol.'''

    def set_log_file(self, log_file: str) -> bool:
        return True


class TestILogHandlerManager(unittest.TestCase):
    '''Test suite for ILogHandlerManager protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Test environment setup and instance preparation before each test.'''
        self.handler_manager = ConcreteLogHandlerManager()

    def test_protocol_conformance(self) -> None:
        '''Tests if the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.handler_manager, ILogHandlerManager))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if the incomplete class fails the isinstance check.'''
        incomplete = IncompleteLogHandlerManager()
        self.assertFalse(isinstance(incomplete, ILogHandlerManager))

    def test_set_log_file(self) -> None:
        '''Tests set_log_file method with valid and invalid paths.'''
        self.assertTrue(self.handler_manager.set_log_file("/var/log/syslog.log"))
        self.assertEqual(self.handler_manager._active_file_handler, "/var/log/syslog.log")

        # Invalid filename should return False
        self.assertFalse(self.handler_manager.set_log_file(""))

    def test_set_stdout(self) -> None:
        '''Tests set_stdout method for configuring stdout handler.'''
        self.assertFalse(self.handler_manager._stdout_configured)
        self.assertTrue(self.handler_manager.set_stdout())
        self.assertTrue(self.handler_manager._stdout_configured)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.handler_manager), "ConcreteLogHandlerManager")


if __name__ == '__main__':
    unittest.main()
