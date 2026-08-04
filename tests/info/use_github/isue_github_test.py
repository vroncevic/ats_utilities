# -*- coding: UTF-8 -*-

'''
Module
    test_iuse_github.py
Info
    Unit tests for IUseGitHub protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.info.use_github.iuse_github import IUseGitHub


class ConcreteUseGitHub:
    '''Mock implementation of IUseGitHub protocol for testing.'''

    def __init__(self, use_github: Any = None) -> None:
        self._use_github = use_github

    @property
    def use_github(self) -> Any:
        return self._use_github

    @use_github.setter
    def use_github(self, use_github: Any) -> None:
        self._use_github = use_github

    def not_none(self) -> bool:
        return self._use_github is not None

    def __str__(self) -> str:
        return str(self._use_github) if self._use_github is not None else ""


class IncompleteUseGitHub:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestIUseGitHub(unittest.TestCase):
    '''Test suite for IUseGitHub protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.github_inst = ConcreteUseGitHub(True)

    def test_protocol_conformance(self) -> None:
        '''Test if class with all methods passes runtime_checkable check.'''
        self.assertTrue(isinstance(self.github_inst, IUseGitHub))

    def test_protocol_non_conformance(self) -> None:
        '''Test if incomplete class fails isinstance check.'''
        incomplete = IncompleteUseGitHub()
        self.assertFalse(isinstance(incomplete, IUseGitHub))

    def test_property_getter_setter(self) -> None:
        '''Test getter and setter for use_github property.'''
        self.assertTrue(self.github_inst.use_github)
        self.github_inst.use_github = False
        self.assertFalse(self.github_inst.use_github)

    def test_not_none(self) -> None:
        '''Test not_none method.'''
        self.assertTrue(self.github_inst.not_none())
        empty_inst = ConcreteUseGitHub()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        '''Test __str__ method.'''
        self.assertEqual(str(self.github_inst), "True")


if __name__ == '__main__':
    unittest.main()
