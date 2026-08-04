# -*- coding: UTF-8 -*-

'''
Module
    test_irepository.py
Info
    Unit tests for IRepository protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.info.repository.irepository import IRepository


class ConcreteRepository:
    '''Mock implementation of IRepository protocol.'''

    def __init__(self, repository: object = None) -> None:
        self._repository = repository

    @property
    def repository(self) -> object:
        return self._repository

    @repository.setter
    def repository(self, repository: object) -> None:
        self._repository = repository

    def not_none(self) -> bool:
        return self._repository is not None

    def __str__(self) -> str:
        return str(self._repository) if self._repository is not None else ""


class IncompleteRepository:
    '''Incomplete class for negative testing.'''

    def not_none(self) -> bool:
        return False


class TestIRepository(unittest.TestCase):
    '''Test suite for IRepository protocol.'''

    def setUp(self) -> None:
        self.repo_inst = ConcreteRepository("https://github.com/vroncevic/ats_utilities")

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.repo_inst, IRepository))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteRepository()
        self.assertFalse(isinstance(incomplete, IRepository))

    def test_property_getter_setter(self) -> None:
        self.assertEqual(
            self.repo_inst.repository,
            "https://github.com/vroncevic/ats_utilities"
        )
        self.repo_inst.repository = "https://github.com/vroncevic/new_repo"
        self.assertEqual(
            self.repo_inst.repository,
            "https://github.com/vroncevic/new_repo"
        )

    def test_not_none(self) -> None:
        self.assertTrue(self.repo_inst.not_none())
        empty_inst = ConcreteRepository()
        self.assertFalse(empty_inst.not_none())

    def test_string_representation(self) -> None:
        self.assertEqual(
            str(self.repo_inst),
            "https://github.com/vroncevic/ats_utilities"
        )


if __name__ == '__main__':
    unittest.main()
