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
    Unit tests for BaseBundle class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock
from typing import Any

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.context.bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestBaseBundle(unittest.TestCase):
    """Unit tests for the BaseBundle dataclass."""

    def setUp(self) -> None:
        """Set up valid mock objects and parameters for bundle instantiation."""
        self.mock_config_loader = MagicMock(spec=ILoader)
        self.mock_info_manager = MagicMock(spec=IInfoManager)
        self.mock_options_parser = MagicMock(spec=IOptionManager)
        self.mock_splasher = MagicMock(spec=ISplasher)
        self.mock_generator = MagicMock(spec=IGenerator)
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        
        self.valid_params = {
            "info_file": "/path/to/info.cfg",
            "config_loader": self.mock_config_loader,
            "info_manager": self.mock_info_manager,
            "options_parser": self.mock_options_parser,
            "splasher": self.mock_splasher,
            "generator": self.mock_generator,
            "use_generator": True,
            "context_bundle": self.mock_context_bundle
        }

    def test_successful_initialization(self) -> None:
        """Test successful initialization when all parameters match types and constraints."""
        bundle = BaseBundle(**self.valid_params)

        self.assertEqual(bundle.info_file, "/path/to/info.cfg")
        self.assertEqual(bundle.config_loader, self.mock_config_loader)
        self.assertEqual(bundle.info_manager, self.mock_info_manager)
        self.assertEqual(bundle.options_parser, self.mock_options_parser)
        self.assertEqual(bundle.splasher, self.mock_splasher)
        self.assertEqual(bundle.generator, self.mock_generator)
        self.assertTrue(bundle.use_generator)
        self.assertEqual(bundle.context_bundle, self.mock_context_bundle)

    def test_successful_initialization_with_optional_generator_none(self) -> None:
        """Test successful initialization when generator attribute is explicitly set to None."""
        params = self.valid_params.copy()
        params["generator"] = None
        
        bundle = BaseBundle(**params)
        self.assertIsNone(bundle.generator)

    def test_immutability_frozen_slots(self) -> None:
        """Test that altering an attribute post-initialization throws a FrozenInstanceError."""
        bundle = BaseBundle(**self.valid_params)
        
        with self.assertRaises(FrozenInstanceError):
            bundle.info_file = "/attempt/new/path.cfg"  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional arguments are barred under kw_only configuration rules."""
        with self.assertRaises(TypeError):
            BaseBundle(
                # pyrefly: ignore [unexpected-positional-argument]
                "/path/to/info.cfg",
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_config_loader,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_info_manager,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_options_parser,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_splasher,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_generator,
                # pyrefly: ignore [unexpected-positional-argument]
                True,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_context_bundle
            )

    def test_to_dict(self) -> None:
        """Test that to_dict compiles the structural field components exactly into a dictionary."""
        bundle = BaseBundle(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params)
        self.assertEqual(set(exported_dict.keys()), set(bundle.__dataclass_fields__.keys()))


if __name__ == '__main__':
    unittest.main()
