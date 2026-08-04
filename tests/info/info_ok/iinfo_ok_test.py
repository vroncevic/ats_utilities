# -*- coding: UTF-8 -*-

'''
Module
    test_iinfo_ok.py
Info
    Unit tests for IInfoOk protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.info_ok.iinfo_ok import IInfoOk


class ConcreteInfoOk:
    '''Mock implementation of IInfoOk protocol.'''

    def __init__(self, info_ok: object = None) -> None:
        self._info_ok = info_ok

    @property
    def info_ok(self) -> object:
        return self._info_ok

    @info_ok.setter
    def info_ok(self, info_ok: object) -> None:
        self._info_ok = info_ok

    def not_none(self) -> bool:
        return self._info_ok is not None

    def __str__(self) -> str:
        return str(self._info_ok) if self._info_ok is not None else ""


class IncompleteInfoOk:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestIInfoOk(unittest.TestCase):
    '''Test suite for IInfoOk protocol.'''

    def setUp(self) -> None:
        self.info_ok_inst = ConcreteInfoOk(True)

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.info_ok_inst, IInfoOk))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteInfoOk()
        self.assertFalse(isinstance(incomplete, IInfoOk))

    def test_property_getter_setter(self) -> None:
        self.assertTrue(self.info_ok_inst.info_ok)
        self.info_ok_inst.info_ok = False
        self.assertFalse(self.info_ok_inst.info_ok)

    def test_not_none(self) -> None:
        self.assertTrue(self.info_ok_inst.not_none())
        empty_inst = ConcreteInfoOk()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.info_ok_inst), "True")


if __name__ == '__main__':
    unittest.main()
