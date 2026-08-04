# -*- coding: UTF-8 -*-

'''
Module
    test_ichecker.py
Info
    Unit tests for IChecker protocol interface using standard unittest module.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock
from typing import Any

from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.ichecker import IChecker

class ConcreteChecker:
    '''Mock for IChecker'''

    def __init__(
        self,
        bundle: Any,
        format_validator: Any,
        type_validator: Any,
        context_provider: Any,
        check_reporter: Any
    ) -> None:
        self._bundle = bundle
        self._format_validator = format_validator
        self._type_validator = type_validator
        self._context_provider = context_provider
        self._check_reporter = check_reporter

    def get_bundle(self) -> Any:
        return self._bundle

    def update_bundle(self, bundle: Any) -> bool:
        self._bundle = bundle
        return True

    def get_format_validator(self) -> IFormatValidator:
        return self._format_validator

    def get_type_validator(self) -> ITypeValidator:
        return self._type_validator

    def get_context_provider(self) -> IContextProvider:
        return self._context_provider

    def get_check_reporter(self) -> ICheckReporter:
        return self._check_reporter

    def validates_parameters(self, parameters: Any) -> Any:
        return True

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return "ConcreteChecker"


class IncompleteChecker:
    '''Incomplete mock for IChecker'''

    def get_bundle(self) -> Any:
        return None


class TestIChecker(unittest.TestCase):
    '''Test suite for IChecker using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and mock objects.'''
        self.mock_bundle = MagicMock()
        self.mock_format_validator = MagicMock(spec=IFormatValidator)
        self.mock_type_validator = MagicMock(spec=ITypeValidator)
        self.mock_context_provider = MagicMock(spec=IContextProvider)
        self.mock_check_reporter = MagicMock(spec=ICheckReporter)

        self.checker = ConcreteChecker(
            bundle=self.mock_bundle,
            format_validator=self.mock_format_validator,
            type_validator=self.mock_type_validator,
            context_provider=self.mock_context_provider,
            check_reporter=self.mock_check_reporter
        )

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.checker, IChecker))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteChecker()
        self.assertFalse(isinstance(incomplete, IChecker))

    def test_get_bundle(self) -> None:
        '''Test get_bundle method.'''
        self.assertEqual(self.checker.get_bundle(), self.mock_bundle)

    def test_update_bundle(self) -> None:
        '''Test update_bundle method.'''
        new_bundle = MagicMock()
        result = self.checker.update_bundle(new_bundle)
        self.assertTrue(result)
        self.assertEqual(self.checker.get_bundle(), new_bundle)

    def test_get_format_validator(self) -> None:
        '''Test get_format_validator method.'''
        self.assertEqual(self.checker.get_format_validator(), self.mock_format_validator)

    def test_get_type_validator(self) -> None:
        '''Test get_type_validator method.'''
        self.assertEqual(self.checker.get_type_validator(), self.mock_type_validator)

    def test_get_context_provider(self) -> None:
        '''Test get_context_provider method.'''
        self.assertEqual(self.checker.get_context_provider(), self.mock_context_provider)

    def test_get_check_reporter(self) -> None:
        '''Test get_check_reporter method.'''
        self.assertEqual(self.checker.get_check_reporter(), self.mock_check_reporter)

    def test_validates_parameters(self) -> None:
        '''Test validates_parameters method.'''
        self.assertTrue(self.checker.validates_parameters({"param": "value"}))

    def test_is_initialized(self) -> None:
        '''Test is_initialized method.'''
        self.assertTrue(self.checker.is_initialized())

    def test_string_representation(self) -> None:
        '''Test __str__ method.'''
        self.assertEqual(str(self.checker), "ConcreteChecker")


if __name__ == '__main__':
    unittest.main()
