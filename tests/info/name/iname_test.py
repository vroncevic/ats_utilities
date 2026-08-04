# -*- coding: UTF-8 -*-

'''
Module
    test_iname.py
Info
    Unit tests for IName protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.name.iname import IName


class ConcreteName:
    '''Mock implementation of IName protocol.'''

    def __init__(self, name: object = None) -> None:
        self._name = name

    @property
    def name(self) -> object:
        return self._name

    @name.setter
    def name(self, name: object) -> None:
        self._name = name

    def not_none(self) -> bool:
        return self._name is not None

    def __str__(self) -> str:
        return str(self._name) if self._name is not None else ""


class IncompleteName:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestIName(unittest.TestCase):
    '''Test suite za IName protokol.'''

    def setUp(self) -> None:
        self.name_inst = ConcreteName("ats_utilities")

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.name_inst, IName))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteName()
        self.assertFalse(isinstance(incomplete, IName))

    def test_property_getter_setter(self) -> None:
        self.assertEqual(self.name_inst.name, "ats_utilities")
        self.name_inst.name = "ats_core"
        self.assertEqual(self.name_inst.name, "ats_core")

    def test_not_none(self) -> None:
        self.assertTrue(self.name_inst.not_none())
        empty_inst = ConcreteName()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.name_inst), "ats_utilities")


if __name__ == '__main__':
    unittest.main()
