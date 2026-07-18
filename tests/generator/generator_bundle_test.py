# -*- coding: UTF-8 -*-

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock
from typing import Any

# Adjust imports according to your project structure
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor


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

    def test_validation_missing_or_none_fields(self) -> None:
        """Test that passing None for any attribute triggers a validation hook exception."""
        fields = ["context_bundle", "scheme_loader", "tar_processor", "template_processor"]

        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None  # type: ignore
                
                # Triggers validator exception via not_none helper
                with self.assertRaises(Exception):
                    GeneratorBundle(**invalid_params)

    def test_validation_type_mismatches(self) -> None:
        """Test that providing an incorrect class type fails the type check constraints."""
        type_mismatches = {
            "context_bundle": MagicMock(spec=ISchemeLoader),       # Expected ContextBundle
            "scheme_loader": MagicMock(spec=ContextBundle),        # Expected ISchemeLoader
            "tar_processor": MagicMock(spec=ITemplateProcessor),   # Expected ITarProcessor
            "template_processor": MagicMock(spec=ITarProcessor)    # Expected ITemplateProcessor
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value
                
                # Triggers validator exception via istype helper
                with self.assertRaises(Exception):
                    GeneratorBundle(**invalid_params)

    def test_to_dict(self) -> None:
        """Test that to_dict compiles the structural field components exactly into a dictionary."""
        bundle = GeneratorBundle(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params)
        self.assertEqual(set(exported_dict.keys()), set(bundle.__dataclass_fields__.keys()))


if __name__ == '__main__':
    unittest.main()
