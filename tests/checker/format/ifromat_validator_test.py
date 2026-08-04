# -*- coding: UTF-8 -*-

'''
Module
    test_iformat_validator.py
Info
    Unit tests for IFormatValidator protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.format.iformat_validator import IFormatValidator


class ConcreteFormatValidator:
    '''Mock for IFormatValidator'''

    def __init__(self, separator: str = "::") -> None:
        self._separator = separator

    def set_separator(self, separator: str) -> None:
        self._separator = separator

    def get_separator(self) -> str:
        return self._separator

    def is_valid(self, format_to_check: str) -> bool:
        return self._separator in format_to_check

    def split(self, format_to_split: str) -> list[str]:
        return format_to_split.split(self._separator)

    def __str__(self) -> str:
        return "ConcreteFormatValidator"


class IncompleteFormatValidator:
    '''Incomplete mock for IFormatValidator'''

    def get_separator(self) -> str:
        return "::"


class TestIFormatValidator(unittest.TestCase):
    '''Test suite for IFormatValidator using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.validator = ConcreteFormatValidator(separator="::")

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.validator, IFormatValidator))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteFormatValidator()
        self.assertFalse(isinstance(incomplete, IFormatValidator))

    def test_get_separator(self) -> None:
        '''Test get_separator method.'''
        self.assertEqual(self.validator.get_separator(), "::")

    def test_set_separator(self) -> None:
        '''Test set_separator method.'''
        self.validator.set_separator("/")
        self.assertEqual(self.validator.get_separator(), "/")

    def test_is_valid(self) -> None:
        '''Test is_valid method.'''
        self.assertTrue(self.validator.is_valid("module::function"))
        self.assertFalse(self.validator.is_valid("module_function"))

    def test_split(self) -> None:
        '''Test split method.'''
        result = self.validator.split("module::function")
        self.assertEqual(result, ["module", "function"])

    def test_string_representation(self) -> None:
        '''Test __str__ method.'''
        self.assertEqual(str(self.validator), "ConcreteFormatValidator")


if __name__ == '__main__':
    unittest.main()
