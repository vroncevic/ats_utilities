# -*- coding: UTF-8 -*-

'''
Module
    test_ilogo.py
Info
    Unit tests for ILogo protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.logo.ilogo import ILogo


class ConcreteLogo:
    '''Mock implementation of ILogo protocol.'''

    def __init__(self, logo: object = None) -> None:
        self._logo = logo

    @property
    def logo(self) -> object:
        return self._logo

    @logo.setter
    def logo(self, logo: object) -> None:
        self._logo = logo

    def not_none(self) -> bool:
        return self._logo is not None

    def __str__(self) -> str:
        return str(self._logo) if self._logo is not None else ""


class IncompleteLogo:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestILogo(unittest.TestCase):
    '''Test suite for ILogo protocol.'''

    def setUp(self) -> None:
        self.logo_inst = ConcreteLogo("assets/logo.png")

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.logo_inst, ILogo))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteLogo()
        self.assertFalse(isinstance(incomplete, ILogo))

    def test_property_getter_setter(self) -> None:
        self.assertEqual(self.logo_inst.logo, "assets/logo.png")
        self.logo_inst.logo = "assets/new_logo.svg"
        self.assertEqual(self.logo_inst.logo, "assets/new_logo.svg")

    def test_not_none(self) -> None:
        self.assertTrue(self.logo_inst.not_none())
        empty_inst = ConcreteLogo()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.logo_inst), "assets/logo.png")


if __name__ == '__main__':
    unittest.main()
