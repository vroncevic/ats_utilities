# -*- coding: UTF-8 -*-

'''
Module
    test_itype_validator.py
Info
    Unit tests for ITypeValidator protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.type.itype_validator import ITypeValidator


class ConcreteTypeValidator:
    '''Mock for ITypeValidator'''

    def is_match(self, instance: object, expected_type_name: str) -> bool:
        return type(instance).__name__ == expected_type_name

    def is_subtype(self, instance: object, expected_type_name: str) -> bool:
        target_cls = instance if isinstance(instance, type) else type(instance)
        return any(cls.__name__ == expected_type_name for cls in target_cls.__mro__)

    def get_type_name(self, instance: object) -> str:
        return type(instance).__name__

    def __str__(self) -> str:
        return "ConcreteTypeValidator"


class IncompleteTypeValidator:
    '''Incomplete mock for ITypeValidator'''

    def get_type_name(self, instance: object) -> str:
        return type(instance).__name__


class TestITypeValidator(unittest.TestCase):
    '''Test suite for ITypeValidator using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.validator = ConcreteTypeValidator()

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.validator, ITypeValidator))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteTypeValidator()
        self.assertFalse(isinstance(incomplete, ITypeValidator))

    def test_get_type_name(self) -> None:
        '''Test get_type_name method.'''
        self.assertEqual(self.validator.get_type_name(123), "int")
        self.assertEqual(self.validator.get_type_name("hello"), "str")

    def test_is_match(self) -> None:
        '''Test is_match method for exact type matching.'''
        self.assertTrue(self.validator.is_match("test", "str"))
        self.assertFalse(self.validator.is_match(123, "str"))

    def test_is_subtype(self) -> None:
        '''Test is_subtype method for inheritance checking.'''
        class CustomBool(int):
            pass

        instance = CustomBool()
        self.assertTrue(self.validator.is_subtype(instance, "int"))
        self.assertFalse(self.validator.is_subtype(instance, "float"))

    def test_string_representation(self) -> None:
        '''Test __str__ method.'''
        self.assertEqual(str(self.validator), "ConcreteTypeValidator")


if __name__ == '__main__':
    unittest.main()
