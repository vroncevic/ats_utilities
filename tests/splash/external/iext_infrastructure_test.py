# -*- coding: UTF-8 -*-

'''
Module
    test_iext_infrastructure.py
Info
    Unit tests for IExtInfrastructure protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure


class ConcreteExtInfrastructure:
    '''Mock implementation of IExtInfrastructure protocol for testing purposes.'''

    def __init__(self, initial_property: Any = None) -> None:
        self._infrastructure_property: Any = initial_property or {
            "info_url": "https://github.com/vroncevic/ats_utilities",
            "issues_url": "https://github.com/vroncevic/ats_utilities/issues",
            "author_url": "https://vroncevic.github.io"
        }

    @property
    def infrastructure_property(self) -> Any:
        return self._infrastructure_property

    @infrastructure_property.setter
    def infrastructure_property(self, setup: Any) -> None:
        if isinstance(setup, dict):
            self._infrastructure_property = setup

    def get_info_text(self) -> str:
        return f"Info: {self._infrastructure_property.get('info_url', '')}"

    def get_issue_text(self) -> str:
        return f"Issues: {self._infrastructure_property.get('issues_url', '')}"

    def get_author_text(self) -> str:
        return f"Author: {self._infrastructure_property.get('author_url', '')}"

    def __str__(self) -> str:
        return "ConcreteExtInfrastructure"


class IncompleteExtInfrastructure:
    '''Incomplete class lacking methods from IExtInfrastructure protocol.'''

    def get_info_text(self) -> str:
        return "Incomplete Info"


class TestIExtInfrastructure(unittest.TestCase):
    '''Test suite for IExtInfrastructure protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.infrastructure = ConcreteExtInfrastructure()

    def test_protocol_conformance(self) -> None:
        '''Tests whether the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.infrastructure, IExtInfrastructure))

    def test_protocol_non_conformance(self) -> None:
        '''Tests whether the incomplete class fails the isinstance check.'''
        incomplete = IncompleteExtInfrastructure()
        self.assertFalse(isinstance(incomplete, IExtInfrastructure))

    def test_infrastructure_property_getter_and_setter(self) -> None:
        '''Tests getter and setter for infrastructure_property.'''
        current_prop = self.infrastructure.infrastructure_property
        self.assertIn("info_url", current_prop)

        new_prop = {
            "info_url": "https://github.com/vroncevic/new_repo",
            "issues_url": "https://github.com/vroncevic/new_repo/issues",
            "author_url": "https://vroncevic.github.io"
        }
        self.infrastructure.infrastructure_property = new_prop
        self.assertEqual(self.infrastructure.infrastructure_property, new_prop)

    def test_get_info_text(self) -> None:
        '''Tests get_info_text method for preprocessing info text.'''
        expected = "Info: https://github.com/vroncevic/ats_utilities"
        self.assertEqual(self.infrastructure.get_info_text(), expected)

    def test_get_issue_text(self) -> None:
        '''Tests get_issue_text method for preprocessing issue text.'''
        expected = "Issues: https://github.com/vroncevic/ats_utilities/issues"
        self.assertEqual(self.infrastructure.get_issue_text(), expected)

    def test_get_author_text(self) -> None:
        '''Tests get_author_text method for preprocessing author text.'''
        expected = "Author: https://vroncevic.github.io"
        self.assertEqual(self.infrastructure.get_author_text(), expected)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.infrastructure), "ConcreteExtInfrastructure")


if __name__ == '__main__':
    unittest.main()
