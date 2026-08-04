# -*- coding: UTF-8 -*-

'''
Module
    test_iconf_file.py
Info
    Unit tests for IConfFile protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock
from typing import IO

from ats_utilities.config_io.iconf_file import IConfFile


class ConcreteConfFile:
    '''Mock IConfFile for testing.'''

    def __init__(self, mock_file_handle: object = None) -> None:
        self._file_handle = mock_file_handle or MagicMock(spec=IO)
        self.is_opened = False
        self.is_closed = False

    def __enter__(self) -> object:
        self.is_opened = True
        return self._file_handle

    def __exit__(self, *args: object, **kwargs: object) -> None:
        self.is_closed = True

    def __str__(self) -> str:
        return "ConcreteConfFile"


class IncompleteConfFile:
    '''Class that lacks context manager logic from IConfFile protocol.'''

    def __enter__(self) -> object:
        return None


class TestIConfFile(unittest.TestCase):
    '''Test suite for IConfFile protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Prepares test environment and instance before each test.'''
        self.mock_file_handle = MagicMock()
        self.conf_file = ConcreteConfFile(mock_file_handle=self.mock_file_handle)

    def test_protocol_conformance(self) -> None:
        '''Tests if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.conf_file, IConfFile))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if incomplete class fails isinstance check.'''
        incomplete = IncompleteConfFile()
        self.assertFalse(isinstance(incomplete, IConfFile))

    def test_context_manager_usage(self) -> None:
        '''Tests entry and exit from context manager block (__enter__ and __exit__).'''
        self.assertFalse(self.conf_file.is_opened)
        self.assertFalse(self.conf_file.is_closed)

        with self.conf_file as f:
            self.assertTrue(self.conf_file.is_opened)
            self.assertEqual(f, self.mock_file_handle)

        self.assertTrue(self.conf_file.is_closed)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.conf_file), "ConcreteConfFile")


if __name__ == '__main__':
    unittest.main()
