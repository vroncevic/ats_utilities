# -*- coding: UTF-8 -*-

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock
from typing import Any

# Adjust imports according to your project structure
from ats_utilities.base.base_bundle import BaseBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.context.bundle import ContextBundle


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

    def test_validation_missing_or_none_fields(self) -> None:
        """Test that passing None for any non-optional attribute triggers a validation error."""
        # Non-optional fields under not_none evaluation rules
        fields = [
            "info_file", "config_loader", "info_manager", 
            "options_parser", "splasher", "use_generator", "context_bundle"
        ]

        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None  # type: ignore
                
                with self.assertRaises(Exception):
                    BaseBundle(**invalid_params)

    def test_validation_type_mismatches(self) -> None:
        """Test that providing an incorrect class type fails the type check constraints."""
        type_mismatches = {
            "info_file": 12345,                                      # Expected str
            "config_loader": MagicMock(spec=IInfoManager),           # Expected ILoader
            "info_manager": MagicMock(spec=ILoader),                 # Expected IInfoManager
            "options_parser": MagicMock(spec=ISplasher),             # Expected IOptionManager
            "splasher": MagicMock(spec=IOptionManager),              # Expected ISplasher
            "use_generator": "True",                                 # Expected bool
            "generator": MagicMock(spec=ContextBundle),              # Expected IGenerator or None
            "context_bundle": MagicMock(spec=IGenerator)             # Expected ContextBundle
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value
                
                with self.assertRaises(Exception):
                    BaseBundle(**invalid_params)

    def test_to_dict(self) -> None:
        """Test that to_dict compiles the structural field components exactly into a dictionary."""
        bundle = BaseBundle(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params)
        self.assertEqual(set(exported_dict.keys()), set(bundle.__dataclass_fields__.keys()))


if __name__ == '__main__':
    unittest.main()
