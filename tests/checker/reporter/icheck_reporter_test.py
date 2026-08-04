# -*- coding: UTF-8 -*-

'''
Module
    test_icheck_reporter.py
Info
    Unit tests for ICheckReporter protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter


class ConcreteCheckReporter:
    '''Mock for ICheckReporter'''

    def build_message(self, data: dict[str, Any]) -> str:
        status = "PASSED" if data.get("success", False) else "FAILED"
        return f"Report Status: {status} - Details: {data.get('details', '')}"

    def __str__(self) -> str:
        return "ConcreteCheckReporter"


class IncompleteCheckReporter:
    '''Incomplete mock for ICheckReporter'''

    def some_other_method(self) -> None:
        pass


class TestICheckReporter(unittest.TestCase):
    '''Test suite for ICheckReporter using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.reporter = ConcreteCheckReporter()

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.reporter, ICheckReporter))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteCheckReporter()
        self.assertFalse(isinstance(incomplete, ICheckReporter))

    def test_build_message(self) -> None:
        '''Test build_message method for both positive and negative outcomes.'''
        success_data = {"success": True, "details": "All checks passed."}
        failure_data = {"success": False, "details": "Type mismatch found."}

        self.assertEqual(
            self.reporter.build_message(success_data),
            "Report Status: PASSED - Details: All checks passed."
        )
        self.assertEqual(
            self.reporter.build_message(failure_data),
            "Report Status: FAILED - Details: Type mismatch found."
        )

    def test_string_representation(self) -> None:
        '''Test __str__ method.'''
        self.assertEqual(str(self.reporter), "ConcreteCheckReporter")


if __name__ == '__main__':
    unittest.main()
