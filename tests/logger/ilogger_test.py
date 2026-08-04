# -*- coding: UTF-8 -*-

'''
Module
    test_ilogger.py
Info
    Unit tests for ILogger protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.logger.ilogger import ILogger


class ConcreteLogger:
    '''Mock implementation of ILogger protocol for testing purposes.'''

    def __init__(self, bundle: object = None) -> None:
        self._bundle = bundle or {}
        self._level = "INFO"
        self._log_file = None
        self._stdout_enabled = False
        self._buffering = True
        self._logs: list[tuple[str, str]] = []

    def get_bundle(self) -> object:
        return self._bundle

    def is_initialized(self) -> bool:
        return bool(self._bundle)

    def update_bundle(self, bundle: object) -> bool:
        if isinstance(bundle, dict):
            self._bundle = bundle
            return True
        return False

    def set_level(self, level: str) -> None:
        self._level = level

    def set_log_file(self, log_file: str) -> bool:
        if isinstance(log_file, str) and log_file:
            self._log_file = log_file
            return True
        return False

    def set_stdout(self) -> bool:
        self._stdout_enabled = True
        return True

    def stop_buffering(self) -> None:
        self._buffering = False

    def write_log(self, level: str, message: str) -> None:
        self._logs.append((level, message))

    def __str__(self) -> str:
        return "ConcreteLogger"


class IncompleteLogger:
    '''Class that lacks most of the ILogger protocol methods.'''

    def get_bundle(self) -> object:
        return {}


class TestILogger(unittest.TestCase):
    '''Test suite for ILogger protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Prepares test environment and instance before each test.'''
        self.mock_bundle = {"env": "production", "log_dir": "/var/log"}
        self.logger = ConcreteLogger(bundle=self.mock_bundle)

    def test_protocol_conformance(self) -> None:
        '''Tests if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.logger, ILogger))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if incomplete class fails isinstance check.'''
        incomplete = IncompleteLogger()
        self.assertFalse(isinstance(incomplete, ILogger))

    def test_get_bundle(self) -> None:
        '''Tests get_bundle method.'''
        self.assertEqual(self.logger.get_bundle(), self.mock_bundle)

    def test_is_initialized(self) -> None:
        '''Tests is_initialized method.'''
        self.assertTrue(self.logger.is_initialized())
        
        uninit_logger = ConcreteLogger()
        self.assertFalse(uninit_logger.is_initialized())

    def test_update_bundle(self) -> None:
        '''Tests update_bundle method with valid and invalid input.'''
        new_bundle = {"env": "staging", "log_dir": "/tmp"}
        self.assertTrue(self.logger.update_bundle(new_bundle))
        self.assertEqual(self.logger.get_bundle(), new_bundle)
        
        self.assertFalse(self.logger.update_bundle("invalid_bundle"))

    def test_set_level(self) -> None:
        '''Tests set_level method.'''
        self.logger.set_level("DEBUG")
        self.assertEqual(self.logger._level, "DEBUG")

    def test_set_log_file(self) -> None:
        '''Tests set_log_file method.'''
        self.assertTrue(self.logger.set_log_file("app.log"))
        self.assertEqual(self.logger._log_file, "app.log")
        self.assertFalse(self.logger.set_log_file(""))

    def test_set_stdout(self) -> None:
        '''Tests set_stdout method.'''
        self.assertTrue(self.logger.set_stdout())
        self.assertTrue(self.logger._stdout_enabled)

    def test_stop_buffering(self) -> None:
        '''Tests stop_buffering method.'''
        self.assertTrue(self.logger._buffering)
        self.logger.stop_buffering()
        self.assertFalse(self.logger._buffering)

    def test_write_log(self) -> None:
        '''Tests write_log method.'''
        self.logger.write_log("ERROR", "Connection failure")
        self.assertIn(("ERROR", "Connection failure"), self.logger._logs)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.logger), "ConcreteLogger")


if __name__ == '__main__':
    unittest.main()
