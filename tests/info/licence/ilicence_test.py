# -*- coding: UTF-8 -*-

'''
Module
    test_ilicence.py
Info
    Unit tests for ILicence protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.licence.ilicence import ILicence


class ConcreteLicence:
    '''Mock implementation of ILicence protocol.'''

    def __init__(self, licence: object = None) -> None:
        self._licence = licence

    @property
    def licence(self) -> object:
        return self._licence

    @licence.setter
    def licence(self, licence: object) -> None:
        self._licence = licence

    def not_none(self) -> bool:
        return self._licence is not None

    def __str__(self) -> str:
        return str(self._licence) if self._licence is not None else ""


class IncompleteLicence:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestILicence(unittest.TestCase):
    '''Test suite for ILicence protocol.'''

    def setUp(self) -> None:
        self.licence_inst = ConcreteLicence("GPL-3.0")

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.licence_inst, ILicence))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteLicence()
        self.assertFalse(isinstance(incomplete, ILicence))

    def test_property_getter_setter(self) -> None:
        self.assertEqual(self.licence_inst.licence, "GPL-3.0")
        self.licence_inst.licence = "MIT"
        self.assertEqual(self.licence_inst.licence, "MIT")

    def test_not_none(self) -> None:
        self.assertTrue(self.licence_inst.not_none())
        empty_inst = ConcreteLicence()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.licence_inst), "GPL-3.0")


if __name__ == '__main__':
    unittest.main()
