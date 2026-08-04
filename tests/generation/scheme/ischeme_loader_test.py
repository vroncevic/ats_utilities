# -*- coding: UTF-8 -*-

'''
Module
    test_ischeme_loader.py
Info
    Unit tests for ISchemeLoader protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from collections.abc import Mapping
from typing import Any

from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader


class ConcreteSchemeLoader:
    '''Mock implementation of ISchemeLoader protocol for testing purposes.'''

    def __init__(self, initialized: bool = True) -> None:
        self._initialized = initialized

    def load(self, scheme: str | Mapping[str, object]) -> dict[str, object]:
        if isinstance(scheme, str):
            return {"source": "file", "path": scheme, "status": "resolved"}
        if isinstance(scheme, Mapping):
            res = dict(scheme)
            res["status"] = "resolved"
            return res
        return {}

    def is_initialized(self) -> bool:
        return self._initialized

    def __str__(self) -> str:
        return "ConcreteSchemeLoader"


class IncompleteSchemeLoader:
    '''Incomplete class for negative test.'''

    def is_initialized(self) -> bool:
        return False


class TestISchemeLoader(unittest.TestCase):
    '''Test suite for ISchemeLoader protocol.'''

    def setUp(self) -> None:
        self.loader = ConcreteSchemeLoader()

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.loader, ISchemeLoader))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteSchemeLoader()
        self.assertFalse(isinstance(incomplete, ISchemeLoader))

    def test_load_from_path_string(self) -> None:
        res = self.loader.load("configs/scheme.json")
        self.assertEqual(res.get("source"), "file")
        self.assertEqual(res.get("path"), "configs/scheme.json")
        self.assertEqual(res.get("status"), "resolved")

    def test_load_from_mapping(self) -> None:
        raw_scheme = {"template": "python_cli", "version": "1.0.0"}
        res = self.loader.load(raw_scheme)
        self.assertEqual(res.get("template"), "python_cli")
        self.assertEqual(res.get("status"), "resolved")

    def test_is_initialized(self) -> None:
        self.assertTrue(self.loader.is_initialized())
        uninit = ConcreteSchemeLoader(initialized=False)
        self.assertFalse(uninit.is_initialized())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.loader), "ConcreteSchemeLoader")


if __name__ == '__main__':
    unittest.main()
