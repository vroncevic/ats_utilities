# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Unit tests for GeneratorBundle class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.generation.setup.bundle import GeneratorBundle


class GeneratorBundleTest(unittest.TestCase):
    '''
        Defines class GeneratorBundleTest with attribute(s) and method(s).
        Tests GeneratorBundle dataclass logic.
    '''

    def setUp(self) -> None:
        self.mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        self.mock_tar_processor = MagicMock(spec=ITarProcessor)
        self.mock_context = MagicMock(spec=ContextBundle)

        self.valid_params = {
            "scheme_loader": self.mock_scheme_loader,
            "tar_processor": self.mock_tar_processor,
            "context_bundle": self.mock_context
        }

    def test_init_valid(self) -> None:
        bundle = GeneratorBundle(**self.valid_params)
        self.assertIs(bundle.scheme_loader, self.mock_scheme_loader)
        self.assertIs(bundle.tar_processor, self.mock_tar_processor)
        self.assertIs(bundle.context_bundle, self.mock_context)

    def test_immutability_frozen_slots(self) -> None:
        bundle = GeneratorBundle(**self.valid_params)
        with self.assertRaises(FrozenInstanceError):
            bundle.context_bundle = MagicMock(spec=ContextBundle)  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        with self.assertRaises(TypeError):
            GeneratorBundle(
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_scheme_loader,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_tar_processor,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_context
            )

    def test_to_dict(self) -> None:
        bundle = GeneratorBundle(**self.valid_params)
        exported_dict = bundle.to_dict()
        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict["scheme_loader"], self.mock_scheme_loader)
        self.assertEqual(exported_dict["tar_processor"], self.mock_tar_processor)
        self.assertEqual(exported_dict["context_bundle"], self.mock_context)


if __name__ == "__main__":
    unittest.main()
