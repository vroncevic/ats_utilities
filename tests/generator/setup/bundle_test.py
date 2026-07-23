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

from ats_utilities.generator.setup.bundle import GeneratorBundle
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestGeneratorBundle(unittest.TestCase):
    """Unit tests for the GeneratorBundle dataclass."""

    def setUp(self) -> None:
        """Set up standard mock parameters conforming to explicit sub-module interfaces."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        self.mock_tar_processor = MagicMock(spec=ITarProcessor)
        self.mock_template_processor = MagicMock(spec=ITemplateProcessor)

        self.valid_params = {
            "context_bundle": self.mock_context_bundle,
            "scheme_loader": self.mock_scheme_loader,
            "tar_processor": self.mock_tar_processor,
            "template_processor": self.mock_template_processor
        }

    def test_successful_initialization(self) -> None:
        """Test successful initialization when all parameters match types and constraints."""
        bundle = GeneratorBundle(**self.valid_params)

        self.assertEqual(bundle.context_bundle, self.mock_context_bundle)
        self.assertEqual(bundle.scheme_loader, self.mock_scheme_loader)
        self.assertEqual(bundle.tar_processor, self.mock_tar_processor)
        self.assertEqual(bundle.template_processor, self.mock_template_processor)

    def test_immutability_frozen_slots(self) -> None:
        """Test that altering a property post-initialization throws a FrozenInstanceError."""
        bundle = GeneratorBundle(**self.valid_params)
        
        with self.assertRaises(FrozenInstanceError):
            bundle.context_bundle = MagicMock(spec=ContextBundle)  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional arguments are strictly barred under kw_only configuration rules."""
        with self.assertRaises(TypeError):
            # Attempting positional construction should raise a TypeError
            GeneratorBundle(
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_scheme_loader,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_tar_processor,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_template_processor,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_context_bundle
            )

    def test_to_dict(self) -> None:
        """Test that to_dict compiles the structural field components exactly into a dictionary."""
        bundle = GeneratorBundle(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict["context_bundle"], self.mock_context_bundle)
        self.assertEqual(exported_dict["scheme_loader"], self.mock_scheme_loader)
        self.assertEqual(exported_dict["tar_processor"], self.mock_tar_processor)
        self.assertEqual(exported_dict["template_processor"], self.mock_template_processor)


if __name__ == "__main__":
    unittest.main()
