# -*- coding: UTF-8 -*-

'''
Module
    test_iformatter.py
Info
    Unit tests for ILogFormatter protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.logger.formatter.iformatter import ILogFormatter


class ConcreteLogFormatter:
    '''Mock implementation of ILogFormatter protocol for testing purposes.'''

    def __init__(
        self,
        log_format: str = "%(asctime)s - %(levelname)s - %(message)s",
        log_datefmt: str = "%Y-%m-%d %H:%M:%S"
    ) -> None:
        self._log_format = log_format
        self._log_datefmt = log_datefmt

    def set_format(self, log_format: str) -> None:
        self._log_format = log_format

    def get_format(self) -> str:
        return self._log_format

    def set_date_format(self, log_datefmt: str) -> None:
        self._log_datefmt = log_datefmt

    def get_date_format(self) -> str:
        return self._log_datefmt

    def __str__(self) -> str:
        return "ConcreteLogFormatter"


class IncompleteLogFormatter:
    '''Class that lacks most methods from ILogFormatter protocol.'''

    def get_format(self) -> str:
        return "%(message)s"


class TestILogFormatter(unittest.TestCase):
    '''Test suite for ILogFormatter protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Test environment setup and instance preparation before each test.'''
        self.formatter = ConcreteLogFormatter()

    def test_protocol_conformance(self) -> None:
        '''Tests if the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.formatter, ILogFormatter))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if the incomplete class fails the isinstance check.'''
        incomplete = IncompleteLogFormatter()
        self.assertFalse(isinstance(incomplete, ILogFormatter))

    def test_format_get_and_set(self) -> None:
        '''Tests set_format and get_format methods.'''
        default_fmt = "%(asctime)s - %(levelname)s - %(message)s"
        new_fmt = "[%(levelname)s]: %(message)s"

        self.assertEqual(self.formatter.get_format(), default_fmt)
        
        self.formatter.set_format(new_fmt)
        self.assertEqual(self.formatter.get_format(), new_fmt)

    def test_date_format_get_and_set(self) -> None:
        '''Tests set_date_format and get_date_format methods.'''
        default_datefmt = "%Y-%m-%d %H:%M:%S"
        new_datefmt = "%H:%M:%S"

        self.assertEqual(self.formatter.get_date_format(), default_datefmt)
        
        self.formatter.set_date_format(new_datefmt)
        self.assertEqual(self.formatter.get_date_format(), new_datefmt)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.formatter), "ConcreteLogFormatter")


if __name__ == '__main__':
    unittest.main()
