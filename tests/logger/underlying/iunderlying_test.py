# -*- coding: UTF-8 -*-

'''
Module
    test_iunderlying.py
Info
    Unit tests for IUnderlyingLogger protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger


class ConcreteUnderlyingLogger:
    '''Mock implementation of IUnderlyingLogger protocol for testing purposes.'''

    def __init__(self) -> None:
        self._level: str = "INFO"
        self._handlers: list[str] = []
        self._logs: list[tuple[str, str]] = []

    def log(self, level: str, message: str) -> None:
        self._logs.append((level, message))

    def set_level(self, level: str) -> None:
        self._level = level

    def has_handlers(self) -> bool:
        return len(self._handlers) > 0

    def add_file_handler(self, log_file: str) -> bool:
        if isinstance(log_file, str) and log_file:
            self._handlers.append(f"file:{log_file}")
            return True
        return False

    def add_stdout_handler(self) -> bool:
        self._handlers.append("stdout")
        return True

    def __str__(self) -> str:
        return "ConcreteUnderlyingLogger"


class IncompleteUnderlyingLogger:
    '''Incomplete class that lacks most methods from IUnderlyingLogger protocol.'''

    def log(self, level: str, message: str) -> None:
        pass


class TestIUnderlyingLogger(unittest.TestCase):
    '''Test suite for IUnderlyingLogger protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Test environment setup and instance preparation before each test.'''
        self.logger = ConcreteUnderlyingLogger()

    def test_protocol_conformance(self) -> None:
        '''Tests if the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.logger, IUnderlyingLogger))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if the incomplete class fails the isinstance check.'''
        incomplete = IncompleteUnderlyingLogger()
        self.assertFalse(isinstance(incomplete, IUnderlyingLogger))

    def test_log(self) -> None:
        '''Tests log method for writing messages.'''
        self.logger.log("DEBUG", "Executing core logic")
        self.assertIn(("DEBUG", "Executing core logic"), self.logger._logs)

    def test_set_level(self) -> None:
        '''Tests set_level method.'''
        self.logger.set_level("WARNING")
        self.assertEqual(self.logger._level, "WARNING")

    def test_has_handlers(self) -> None:
        '''Tests has_handlers method before and after adding a handler.'''
        self.assertFalse(self.logger.has_handlers())
        
        self.logger.add_stdout_handler()
        self.assertTrue(self.logger.has_handlers())

    def test_add_file_handler(self) -> None:
        '''Tests add_file_handler method with valid and invalid input.'''
        self.assertTrue(self.logger.add_file_handler("/var/log/app.log"))
        self.assertIn("file:/var/log/app.log", self.logger._handlers)
        
        self.assertFalse(self.logger.add_file_handler(""))

    def test_add_stdout_handler(self) -> None:
        '''Tests add_stdout_handler method.'''
        self.assertTrue(self.logger.add_stdout_handler())
        self.assertIn("stdout", self.logger._handlers)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.logger), "ConcreteUnderlyingLogger")


if __name__ == '__main__':
    unittest.main()
