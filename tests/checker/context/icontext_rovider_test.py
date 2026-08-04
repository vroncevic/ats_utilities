# -*- coding: UTF-8 -*-

'''
Module
    test_icontext_provider.py
Info
    Unit tests for IContextProvider protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.context.icontext_provider import IContextProvider


class ConcreteContextProvider:
    '''Mock implementation of IContextProvider'''

    def __init__(self, initial_stack_index: int = 1) -> None:
        self._stack_index_caller = initial_stack_index

    def set_stack_index_caller(self, stack_index_caller: int) -> None:
        self._stack_index_caller = stack_index_caller

    def get_stack_index_caller(self) -> int:
        return self._stack_index_caller

    def get_context(self) -> str:
        return f"caller_context_level_{self._stack_index_caller}"

    def __str__(self) -> str:
        return "ConcreteContextProvider"


class IncompleteContextProvider:
    '''Incomplete mock for IContextProvider'''

    def get_context(self) -> str:
        return "incomplete"


class TestIContextProvider(unittest.TestCase):
    '''Test suite for IContextProvider using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.context_provider = ConcreteContextProvider(initial_stack_index=2)

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.context_provider, IContextProvider))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteContextProvider()
        self.assertFalse(isinstance(incomplete, IContextProvider))

    def test_get_stack_index_caller(self) -> None:
        '''Test get_stack_index_caller method.'''
        self.assertEqual(self.context_provider.get_stack_index_caller(), 2)

    def test_set_stack_index_caller(self) -> None:
        '''Test set_stack_index_caller method.'''
        self.context_provider.set_stack_index_caller(5)
        self.assertEqual(self.context_provider.get_stack_index_caller(), 5)

    def test_get_context(self) -> None:
        '''Test get_context method.'''
        self.assertEqual(self.context_provider.get_context(), "caller_context_level_2")
        self.context_provider.set_stack_index_caller(3)
        self.assertEqual(self.context_provider.get_context(), "caller_context_level_3")

    def test_string_representation(self) -> None:
        '''Test __str__ method.'''
        self.assertEqual(str(self.context_provider), "ConcreteContextProvider")


if __name__ == '__main__':
    unittest.main()
