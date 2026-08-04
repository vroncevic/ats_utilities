# -*- coding: UTF-8 -*-

'''
Module
    test_ireporter.py
Info
    Unit tests for IReporter protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.reporter.ireporter import IReporter


class ConcreteReporter:
    '''Mock implementation of IReporter protocol for testing.'''

    def __init__(self, bundle: object = None) -> None:
        self._bundle: object = bundle or {}
        self._level: int = 1
        self._reported_messages: list[tuple[str, str]] = []

    def get_bundle(self) -> object:
        return self._bundle

    def update_bundle(self, bundle: object) -> bool:
        if isinstance(bundle, dict):
            self._bundle = bundle
            return True
        return False

    def verbose(self, is_verbose: bool, message: str) -> None:
        if is_verbose:
            self._reported_messages.append(("VERBOSE", message))

    def success(self, message: str) -> None:
        self._reported_messages.append(("SUCCESS", message))

    def warning(self, message: str) -> None:
        self._reported_messages.append(("WARNING", message))

    def error(self, message: str) -> None:
        self._reported_messages.append(("ERROR", message))

    def set_level(self, level: int) -> None:
        self._level = level

    def is_initialized(self) -> bool:
        return bool(self._bundle)

    def __str__(self) -> str:
        return "ConcreteReporter"


class IncompleteReporter:
    '''Incomplete class lacking most methods from IReporter protocol.'''

    def success(self, message: str) -> None:
        pass


class TestIReporter(unittest.TestCase):
    '''Unit tests za IReporter protocol koristeći unittest framework.'''

    def setUp(self) -> None:
        '''Preparing test environment and instance before each test.'''
        self.mock_bundle = {"theme": "dark", "output": "stdout"}
        self.reporter = ConcreteReporter(bundle=self.mock_bundle)

    def test_protocol_conformance(self) -> None:
        '''Tests if the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.reporter, IReporter))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if the incomplete class fails the isinstance check.'''
        incomplete = IncompleteReporter()
        self.assertFalse(isinstance(incomplete, IReporter))

    def test_get_bundle(self) -> None:
        '''Tests the get_bundle method.'''
        self.assertEqual(self.reporter.get_bundle(), self.mock_bundle)

    def test_update_bundle(self) -> None:
        '''Tests the update_bundle method with valid and invalid input.'''
        new_bundle = {"theme": "light", "output": "stderr"}
        self.assertTrue(self.reporter.update_bundle(new_bundle))
        self.assertEqual(self.reporter.get_bundle(), new_bundle)

        self.assertFalse(self.reporter.update_bundle("invalid_bundle"))

    def test_verbose(self) -> None:
        '''Tests the verbose method when the option is enabled and disabled.'''
        self.reporter.verbose(True, "Detailed diagnostic info")
        self.assertIn(("VERBOSE", "Detailed diagnostic info"), self.reporter._reported_messages)

        self.reporter.verbose(False, "Ignored message")
        self.assertNotIn(("VERBOSE", "Ignored message"), self.reporter._reported_messages)

    def test_reporting_levels(self) -> None:
        '''Tests the success, warning, and error methods for reporting.'''
        self.reporter.success("Operation completed successfully")
        self.reporter.warning("Resource usage is high")
        self.reporter.error("Failed to connect to host")

        self.assertIn(("SUCCESS", "Operation completed successfully"), self.reporter._reported_messages)
        self.assertIn(("WARNING", "Resource usage is high"), self.reporter._reported_messages)
        self.assertIn(("ERROR", "Failed to connect to host"), self.reporter._reported_messages)

    def test_set_level(self) -> None:
        '''Tests the set_level method.'''
        self.reporter.set_level(3)
        self.assertEqual(self.reporter._level, 3)

    def test_is_initialized(self) -> None:
        '''Tests the is_initialized method.'''
        self.assertTrue(self.reporter.is_initialized())

        uninit_reporter = ConcreteReporter()
        self.assertFalse(uninit_reporter.is_initialized())

    def test_string_representation(self) -> None:
        '''Tests the __str__ method.'''
        self.assertEqual(str(self.reporter), "ConcreteReporter")


if __name__ == '__main__':
    unittest.main()
