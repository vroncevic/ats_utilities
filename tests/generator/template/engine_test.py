# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping

# Adjust imports according to your project structure
from ats_utilities.generator.template.engine import TemplateProcessor
from ats_utilities.context.context_bundle import ContextBundle


class TestTemplateProcessor(unittest.TestCase):
    """Unit tests for the TemplateProcessor class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies and sample template variants."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.sample_text_bytes = b"Hello, $name! Welcome to $project."
        self.sample_vals = {"name": "Alice", "project": "ATS"}

    @patch("ats_utilities.generator.template.engine.inject_context_bundle")
    def test_initialization(self, mock_inject: MagicMock) -> None:
        """Test successful initialization and verification of context injection."""
        processor = TemplateProcessor(self.mock_context_bundle)

        self.assertTrue(processor._initialized)
        mock_inject.assert_called_once_with(processor, self.mock_context_bundle)

    @patch("ats_utilities.generator.template.engine.inject_context_bundle")
    def test_is_initialized_returns_true(self, mock_inject: MagicMock) -> None:
        """Test that is_initialized returns True when the processor is ready."""
        processor = TemplateProcessor(self.mock_context_bundle)
        self.assertTrue(processor.is_initialized())

    @patch("ats_utilities.generator.template.engine.inject_context_bundle")
    def test_render_with_valid_utf8_template(self, mock_inject: MagicMock) -> None:
        """Test template rendering with valid UTF-8 content and exact variable matching."""
        processor = TemplateProcessor(self.mock_context_bundle)
        
        result = processor.render(self.sample_text_bytes, self.sample_vals)
        
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Hello, Alice! Welcome to ATS.")

    @patch("ats_utilities.generator.template.engine.inject_context_bundle")
    def test_render_uses_safe_substitution_on_missing_placeholders(self, mock_inject: MagicMock) -> None:
        """Test that placeholders missing from the mapping are left intact without raising KeyError."""
        processor = TemplateProcessor(self.mock_context_bundle)
        incomplete_vals = {"name": "Bob"}  # 'project' is intentionally omitted
        
        result = processor.render(self.sample_text_bytes, incomplete_vals)
        
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Hello, Bob! Welcome to $project.")

    @patch("ats_utilities.generator.template.engine.inject_context_bundle")
    def test_render_fallback_on_binary_or_corrupted_bytes(self, mock_inject: MagicMock) -> None:
        """Test that text rendering gracefully returns original bytes when decoding fails."""
        processor = TemplateProcessor(self.mock_context_bundle)
        # 0x80 is an invalid stand-alone byte sequence in UTF-8
        corrupted_binary_data = b"Some template text \x80 with binary indicators."
        
        result = processor.render(corrupted_binary_data, self.sample_vals)
        
        # Verify the exception was caught internally and raw bytes were returned
        self.assertIsInstance(result, bytes)
        self.assertEqual(result, corrupted_binary_data)

    @patch("ats_utilities.generator.template.engine.to_str")
    @patch("ats_utilities.generator.template.engine.inject_context_bundle")
    def test_string_representation(self, mock_inject: MagicMock, mock_to_str: MagicMock) -> None:
        """Test that __str__ delegates tracking cleanly to reflection serialization utilities."""
        processor = TemplateProcessor(self.mock_context_bundle)
        mock_to_str.return_value = "TemplateProcessor{initialized=True}"

        result = str(processor)

        mock_to_str.assert_called_once_with(processor)
        self.assertEqual(result, "TemplateProcessor{initialized=True}")


if __name__ == '__main__':
    unittest.main()
