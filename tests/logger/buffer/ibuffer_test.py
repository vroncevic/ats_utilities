# -*- coding: UTF-8 -*-

'''
Module
    test_ibuffer.py
Info
    Unit tests for ILogBuffer protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock
from collections.abc import Callable

from ats_utilities.logger.buffer.ibuffer import ILogBuffer


class ConcreteLogBuffer:
    '''Mock implementation of ILogBuffer protocol for testing purposes.'''

    def __init__(self, enabled: bool = True) -> None:
        self._buffer: list[tuple[object, object]] = []
        self._enabled: bool = enabled

    def add(self, level: object, message: object) -> None:
        if self._enabled:
            self._buffer.append((level, message))

    def flush(self, writer: Callable[[object, object], None]) -> None:
        for level, message in self._buffer:
            writer(level, message)
        self.clear()

    def clear(self) -> None:
        self._buffer.clear()

    @property
    def is_enabled(self) -> bool:
        return self._enabled

    def __str__(self) -> str:
        return "ConcreteLogBuffer"


class IncompleteLogBuffer:
    '''Class that lacks is_enabled property and clear method from ILogBuffer protocol.'''

    def add(self, level: object, message: object) -> None:
        pass


class TestILogBuffer(unittest.TestCase):
    '''Test suite for ILogBuffer protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Test environment setup and instance preparation before each test.'''
        self.buffer = ConcreteLogBuffer(enabled=True)

    def test_protocol_conformance(self) -> None:
        '''Tests if the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.buffer, ILogBuffer))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if the incomplete class fails the isinstance check.'''
        incomplete = IncompleteLogBuffer()
        self.assertFalse(isinstance(incomplete, ILogBuffer))

    def test_is_enabled_property(self) -> None:
        '''Tests is_enabled property.'''
        self.assertTrue(self.buffer.is_enabled)
        
        disabled_buffer = ConcreteLogBuffer(enabled=False)
        self.assertFalse(disabled_buffer.is_enabled)

    def test_add_and_clear(self) -> None:
        '''Tests adding messages to the buffer and clearing the buffer.'''
        self.buffer.add("INFO", "Starting initialization")
        self.buffer.add("DEBUG", "Connecting to database")
        
        self.assertEqual(len(self.buffer._buffer), 2)
        
        self.buffer.clear()
        self.assertEqual(len(self.buffer._buffer), 0)

    def test_flush(self) -> None:
        '''Tests buffer flushing by passing a writer function/mock.'''
        mock_writer = MagicMock()
        
        self.buffer.add("WARNING", "Low disk space")
        self.buffer.add("ERROR", "Unhandled exception")
        
        self.buffer.flush(mock_writer)
        
        # Check if the writer was called exactly with the expected arguments
        self.assertEqual(mock_writer.call_count, 2)
        mock_writer.assert_any_call("WARNING", "Low disk space")
        mock_writer.assert_any_call("ERROR", "Unhandled exception")
        
        # Flush should automatically clear the buffer
        self.assertEqual(len(self.buffer._buffer), 0)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.buffer), "ConcreteLogBuffer")


if __name__ == '__main__':
    unittest.main()
