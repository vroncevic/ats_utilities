# -*- coding: UTF-8 -*-

'''
Module
    test_imessage_processor.py
Info
    Unit tests for IMessageProcessor protocol interface using unittest.
'''

from __future__ import annotations

import re
import unittest

from ats_utilities.logger.processor.imessage_processor import IMessageProcessor


class ConcreteMessageProcessor:
    '''Mock implementation of IMessageProcessor protocol for testing purposes.'''

    def __init__(self, pattern: str = r"password=\w+") -> None:
        self._pattern: str = pattern

    def get_pattern(self) -> str:
        return self._pattern

    def set_pattern(self, pattern: str) -> None:
        self._pattern = pattern

    def process(self, message: str) -> str:
        return re.sub(self._pattern, "password=***", message)

    def __str__(self) -> str:
        return "ConcreteMessageProcessor"


class IncompleteMessageProcessor:
    '''Incomplete class that lacks process and set_pattern methods from IMessageProcessor protocol.'''

    def get_pattern(self) -> str:
        return r"\d+"


class TestIMessageProcessor(unittest.TestCase):
    '''Test suite for IMessageProcessor protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Test environment setup and instance preparation before each test.'''
        self.processor = ConcreteMessageProcessor()

    def test_protocol_conformance(self) -> None:
        '''Tests if the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.processor, IMessageProcessor))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if the incomplete class fails the isinstance check.'''
        incomplete = IncompleteMessageProcessor()
        self.assertFalse(isinstance(incomplete, IMessageProcessor))

    def test_get_and_set_pattern(self) -> None:
        '''Tests get_pattern and set_pattern methods.'''
        self.assertEqual(self.processor.get_pattern(), r"password=\w+")
        
        new_pattern = r"token=\w+"
        self.processor.set_pattern(new_pattern)
        self.assertEqual(self.processor.get_pattern(), new_pattern)

    def test_process(self) -> None:
        '''Tests process method for message sanitization/processing.'''
        raw_message = "User login failed for admin with password=secret123"
        expected_message = "User login failed for admin with password=***"
        
        processed = self.processor.process(raw_message)
        self.assertEqual(processed, expected_message)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.processor), "ConcreteMessageProcessor")


if __name__ == '__main__':
    unittest.main()
