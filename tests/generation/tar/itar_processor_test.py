# -*- coding: UTF-8 -*-

'''
Module
    test_itar_processor.py
Info
    Unit tests for ITarProcessor protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.generation.tar.itar_processor import ITarProcessor


class ConcreteTarProcessor:
    '''Mock implementation of ITarProcessor protocol for testing purposes.'''

    def __init__(self) -> None:
        self.processed_members: list[Any] = []
        self.processed_tars: list[Any] = []
        self._initialized = True

    def process_tar_member(self, tar_process_member_bundle: Any) -> None:
        self.processed_members.append(tar_process_member_bundle)

    def process(self, tar_process_bundle: Any) -> None:
        self.processed_tars.append(tar_process_bundle)

    def is_initialized(self) -> bool:
        return self._initialized

    def __str__(self) -> str:
        return "ConcreteTarProcessor"


class IncompleteTarProcessor:
    '''Incomplete class missing process_tar_member method.'''

    def process(self, tar_process_bundle: Any) -> None:
        pass


class TestITarProcessor(unittest.TestCase):
    '''Test suite for ITarProcessor protocol.'''

    def setUp(self) -> None:
        self.tar_processor = ConcreteTarProcessor()

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.tar_processor, ITarProcessor))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteTarProcessor()
        self.assertFalse(isinstance(incomplete, ITarProcessor))

    def test_process_tar_member(self) -> None:
        member_bundle = {"member_name": "module.py", "is_dir": False}
        self.tar_processor.process_tar_member(member_bundle)
        self.assertEqual(len(self.tar_processor.processed_members), 1)
        self.assertEqual(self.tar_processor.processed_members[0], member_bundle)

    def test_process(self) -> None:
        tar_bundle = {"tar_path": "template.tgz", "dest": "/target"}
        self.tar_processor.process(tar_bundle)
        self.assertEqual(len(self.tar_processor.processed_tars), 1)
        self.assertEqual(self.tar_processor.processed_tars[0], tar_bundle)

    def test_is_initialized(self) -> None:
        self.assertTrue(self.tar_processor.is_initialized())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.tar_processor), "ConcreteTarProcessor")


if __name__ == '__main__':
    unittest.main()
