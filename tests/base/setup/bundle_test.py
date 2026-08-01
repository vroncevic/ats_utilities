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

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.context.bundle import ContextBundle


class TestBaseBundle(unittest.TestCase):
    """Unit tests for the BaseBundle dataclass."""

    def setUp(self) -> None:
        """Set up valid mock objects and parameters for bundle instantiation."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_info_manager = MagicMock(spec=IInfoManager)
        self.mock_option_manager = MagicMock(spec=IOptionManager)
        self.mock_splash_manager = MagicMock(spec=ISplashManager)
        self.mock_generation_manager = MagicMock(spec=IGeneratorManager)

        self.valid_params = {
            "context_bundle": self.mock_context_bundle,
            "info_manager": self.mock_info_manager,
            "option_manager": self.mock_option_manager,
            "splash_manager": self.mock_splash_manager,
            "generation_manager": self.mock_generation_manager
        }

    def test_successful_initialization(self) -> None:
        """Test successful initialization when all parameters match types and constraints."""
        bundle = BaseBundle(**self.valid_params)

        self.assertEqual(bundle.context_bundle, self.mock_context_bundle)
        self.assertEqual(bundle.info_manager, self.mock_info_manager)
        self.assertEqual(bundle.option_manager, self.mock_option_manager)
        self.assertEqual(bundle.splash_manager, self.mock_splash_manager)
        self.assertEqual(bundle.generation_manager, self.mock_generation_manager)

    def test_successful_initialization_with_optional_generator_none(self) -> None:
        """Test successful initialization when generation_manager attribute is set to None."""
        params = self.valid_params.copy()
        params["generation_manager"] = None

        bundle = BaseBundle(**params)
        self.assertIsNone(bundle.generation_manager)

    def test_immutability_frozen_slots(self) -> None:
        """Test that altering an attribute post-initialization throws a FrozenInstanceError."""
        bundle = BaseBundle(**self.valid_params)

        with self.assertRaises(FrozenInstanceError):
            bundle.context_bundle = MagicMock(spec=ContextBundle)  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional arguments are barred under kw_only configuration rules."""
        with self.assertRaises(TypeError):
            BaseBundle(
                self.mock_context_bundle,
                self.mock_info_manager,
                self.mock_option_manager,
                self.mock_splash_manager,
                self.mock_generation_manager
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
