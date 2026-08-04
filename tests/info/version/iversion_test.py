# -*- coding: UTF-8 -*-

'''
Module
    test_iversion.py
Info
    Unit tests for IVersion protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.info.version.iversion import IVersion


class ConcreteVersion:
    '''Mock implementation of IVersion protocol for testing purposes.'''

    def __init__(self, version: Any = None) -> None:
        self._version = version

    @property
    def version(self) -> Any:
        return self._version

    @version.setter
    def version(self, version: Any) -> None:
        self._version = version

    def not_none(self) -> bool:
        return self._version is not None

    def __str__(self) -> str:
        return str(self._version) if self._version is not None else ""


class IncompleteVersion:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestIVersion(unittest.TestCase):
    '''Test suite for IVersion protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.version_inst = ConcreteVersion("3.4.5")

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.version_inst, IVersion))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteVersion()
        self.assertFalse(isinstance(incomplete, IVersion))

    def test_property_getter_setter(self) -> None:
        '''Test getter and setter for version property.'''
        self.assertEqual(self.version_inst.version, "3.4.5")
        self.version_inst.version = "3.5.0"
        self.assertEqual(self.version_inst.version, "3.5.0")

    def test_not_none(self) -> None:
        '''Test not_none method.'''
        self.assertTrue(self.version_inst.not_none())
        empty_inst = ConcreteVersion()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        '''Test __str__ method.'''
        self.assertEqual(str(self.version_inst), "3.4.5")


if __name__ == '__main__':
    unittest.main()
