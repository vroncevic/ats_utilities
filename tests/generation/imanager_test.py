# -*- coding: UTF-8 -*-

'''
Module
    test_imanager_generator.py
Info
    Unit tests for IGeneratorManager protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.generation.imanager import IGeneratorManager


class ConcreteGeneratorManager:
    '''Mock implementation of IGeneratorManager protocol for testing purposes.'''

    def __init__(self, bundle: Any = None, context: Any = None) -> None:
        self._bundle: Any = bundle or {}
        self._context: Any = context or {}
        self._generated_data: list[Any] = []

    def get_bundle(self) -> Any:
        return self._bundle

    def update_bundle(self, bundle: Any) -> bool:
        if isinstance(bundle, dict):
            self._bundle = bundle
            return True
        return False

    def get_context(self) -> Any:
        return self._context

    def prepare_template_values(self, template_values: dict[str, str]) -> dict[str, str]:
        prepared = template_values.copy()
        prepared["PREPARED"] = "TRUE"
        return prepared

    def generate(self, data: Any) -> bool:
        if data:
            self._generated_data.append(data)
            return True
        return False

    def is_initialized(self) -> bool:
        return bool(self._bundle) and bool(self._context)

    def __str__(self) -> str:
        return "ConcreteGeneratorManager"


class IncompleteGeneratorManager:
    '''Incomplete class missing key protocol methods.'''

    def generate(self, data: Any) -> bool:
        return True


class TestIGeneratorManager(unittest.TestCase):
    '''Test suite for IGeneratorManager protocol.'''

    def setUp(self) -> None:
        self.mock_bundle = {"template_dir": "/templates", "archive": "package.tgz"}
        self.mock_context = {"target_dir": "/output"}
        self.manager = ConcreteGeneratorManager(
            bundle=self.mock_bundle,
            context=self.mock_context
        )

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.manager, IGeneratorManager))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteGeneratorManager()
        self.assertFalse(isinstance(incomplete, IGeneratorManager))

    def test_get_bundle(self) -> None:
        self.assertEqual(self.manager.get_bundle(), self.mock_bundle)

    def test_update_bundle(self) -> None:
        new_bundle = {"template_dir": "/new_templates"}
        self.assertTrue(self.manager.update_bundle(new_bundle))
        self.assertEqual(self.manager.get_bundle(), new_bundle)
        self.assertFalse(self.manager.update_bundle("invalid_bundle"))

    def test_get_context(self) -> None:
        self.assertEqual(self.manager.get_context(), self.mock_context)

    def test_prepare_template_values(self) -> None:
        vals = {"PROJECT": "ats_utilities"}
        res = self.manager.prepare_template_values(vals)
        self.assertEqual(res.get("PROJECT"), "ats_utilities")
        self.assertEqual(res.get("PREPARED"), "TRUE")

    def test_generate(self) -> None:
        self.assertTrue(self.manager.generate({"archive": "data.tgz"}))
        self.assertFalse(self.manager.generate(None))

    def test_is_initialized(self) -> None:
        self.assertTrue(self.manager.is_initialized())
        uninit = ConcreteGeneratorManager()
        self.assertFalse(uninit.is_initialized())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.manager), "ConcreteGeneratorManager")


if __name__ == '__main__':
    unittest.main()
