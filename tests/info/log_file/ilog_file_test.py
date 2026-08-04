# -*- coding: UTF-8 -*-

'''
Module
    test_ilog_file.py
Info
    Unit tests for ILogFile protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.log_file.ilog_file import ILogFile


class ConcreteLogFile:
    '''Mock implementation of ILogFile protocol.'''

    def __init__(self, log_file: object = None) -> None:
        self._log_file = log_file

    @property
    def log_file(self) -> object:
        return self._log_file

    @log_file.setter
    def log_file(self, log_file: object) -> None:
        self._log_file = log_file

    def not_none(self) -> bool:
        return self._log_file is not None

    def __str__(self) -> str:
        return str(self._log_file) if self._log_file is not None else ""


class IncompleteLogFile:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestILogFile(unittest.TestCase):
    '''Test suite for ILogFile protocol.'''

    def setUp(self) -> None:
        self.log_file_inst = ConcreteLogFile("/var/log/ats.log")

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.log_file_inst, ILogFile))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteLogFile()
        self.assertFalse(isinstance(incomplete, ILogFile))

    def test_property_getter_setter(self) -> None:
        self.assertEqual(self.log_file_inst.log_file, "/var/log/ats.log")
        self.log_file_inst.log_file = "/tmp/ats.log"
        self.assertEqual(self.log_file_inst.log_file, "/tmp/ats.log")

    def test_not_none(self) -> None:
        self.assertTrue(self.log_file_inst.not_none())
        empty_inst = ConcreteLogFile()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.log_file_inst), "/var/log/ats.log")


if __name__ == '__main__':
    unittest.main()
