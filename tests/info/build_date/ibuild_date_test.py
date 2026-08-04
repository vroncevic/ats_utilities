# -*- coding: UTF-8 -*-

'''
Module
    test_ibuild_date.py
Info
    Unit tests for IBuildDate protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.build_date.ibuild_date import IBuildDate


class ConcreteBuildDate:
    '''Mock implementation of IBuildDate protocol.'''

    def __init__(self, build_date: object = None) -> None:
        self._build_date = build_date

    @property
    def build_date(self) -> object:
        return self._build_date

    @build_date.setter
    def build_date(self, build_date: object) -> None:
        self._build_date = build_date

    def not_none(self) -> bool:
        return self._build_date is not None

    def __str__(self) -> str:
        return str(self._build_date) if self._build_date is not None else ""


class IncompleteBuildDate:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestIBuildDate(unittest.TestCase):
    '''Test suite for IBuildDate protocol.'''

    def setUp(self) -> None:
        self.build_date_inst = ConcreteBuildDate("2026-08-04")

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.build_date_inst, IBuildDate))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteBuildDate()
        self.assertFalse(isinstance(incomplete, IBuildDate))

    def test_property_getter_setter(self) -> None:
        self.assertEqual(self.build_date_inst.build_date, "2026-08-04")
        self.build_date_inst.build_date = "2026-12-31"
        self.assertEqual(self.build_date_inst.build_date, "2026-12-31")

    def test_not_none(self) -> None:
        self.assertTrue(self.build_date_inst.not_none())
        empty_inst = ConcreteBuildDate()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.build_date_inst), "2026-08-04")


if __name__ == '__main__':
    unittest.main()
