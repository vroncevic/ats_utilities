# -*- coding: UTF-8 -*-

'''
Module
    test_iconfig_processor.py
Info
    Unit tests for IConfigProcessor protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor


class ConcreteConfigProcessor:
    '''Mock implementation of IConfigProcessor protocol for testing purposes.'''

    def __init__(self, initial_data: dict[str, Any] | None = None) -> None:
        self._data: dict[str, Any] = initial_data or {}

    def deserialize(self, content: object) -> bool:
        if isinstance(content, dict):
            self._data = content.copy()
            return True
        return False

    def serialize(self) -> str:
        return str(self._data)

    def update_data(self, new_data: dict[str, Any]) -> bool:
        if isinstance(new_data, dict):
            self._data.update(new_data)
            return True
        return False

    def to_dict(self) -> dict[str, Any]:
        return self._data.copy()

    def validate_by_scheme(self) -> bool:
        return len(self._data) > 0

    def __str__(self) -> str:
        return "ConcreteConfigProcessor"


class IncompleteConfigProcessor:
    '''Class that lacks most of the IConfigProcessor protocol methods.'''

    def deserialize(self, content: object) -> bool:
        return True


class TestIConfigProcessor(unittest.TestCase):
    '''Test suite for IConfigProcessor protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Prepares test environment and instance before each test.'''
        self.processor = ConcreteConfigProcessor(initial_data={"env": "development"})

    def test_protocol_conformance(self) -> None:
        '''Tests if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.processor, IConfigProcessor))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if incomplete class fails isinstance check.'''
        incomplete = IncompleteConfigProcessor()
        self.assertFalse(isinstance(incomplete, IConfigProcessor))

    def test_deserialize(self) -> None:
        '''Tests deserialize method.'''
        self.assertTrue(self.processor.deserialize({"port": 8080}))
        self.assertEqual(self.processor.to_dict(), {"port": 8080})
        self.assertFalse(self.processor.deserialize("invalid_type"))

    def test_serialize(self) -> None:
        '''Tests serialize method.'''
        self.assertEqual(self.processor.serialize(), "{'env': 'development'}")

    def test_update_data(self) -> None:
        '''Tests update_data method.'''
        self.assertTrue(self.processor.update_data({"debug": True}))
        self.assertEqual(
            self.processor.to_dict(),
            {"env": "development", "debug": True}
        )

    def test_to_dict(self) -> None:
        '''Tests to_dict method.'''
        self.assertEqual(self.processor.to_dict(), {"env": "development"})

    def test_validate_by_scheme(self) -> None:
        '''Tests validate_by_scheme method.'''
        self.assertTrue(self.processor.validate_by_scheme())
        
        empty_processor = ConcreteConfigProcessor()
        self.assertFalse(empty_processor.validate_by_scheme())

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.processor), "ConcreteConfigProcessor")


if __name__ == '__main__':
    unittest.main()
