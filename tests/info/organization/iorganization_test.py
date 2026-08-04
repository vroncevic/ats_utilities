# -*- coding: UTF-8 -*-

'''
Module
    test_iorganization.py
Info
    Unit tests for IOrganization protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.organization.iorganization import IOrganization


class ConcreteOrganization:
    '''Mock implementation of IOrganization protocol.'''

    def __init__(self, organization: object = None) -> None:
        self._organization = organization

    @property
    def organization(self) -> object:
        return self._organization

    @organization.setter
    def organization(self, organization: object) -> None:
        self._organization = organization

    def not_none(self) -> bool:
        return self._organization is not None

    def __str__(self) -> str:
        return str(self._organization) if self._organization is not None else ""


class IncompleteOrganization:
    ''' Incomplete class for negative testing. '''

    def not_none(self) -> bool:
        return False


class TestIOrganization(unittest.TestCase):
    '''Test suite za IOrganization protokol.'''

    def setUp(self) -> None:
        self.org_inst = ConcreteOrganization("vroncevic")

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.org_inst, IOrganization))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteOrganization()
        self.assertFalse(isinstance(incomplete, IOrganization))

    def test_property_getter_setter(self) -> None:
        self.assertEqual(self.org_inst.organization, "vroncevic")
        self.org_inst.organization = "python-foundation"
        self.assertEqual(self.org_inst.organization, "python-foundation")

    def test_not_none(self) -> None:
        self.assertTrue(self.org_inst.not_none())
        empty_inst = ConcreteOrganization()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.org_inst), "vroncevic")


if __name__ == '__main__':
    unittest.main()
