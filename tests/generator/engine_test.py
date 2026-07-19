# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping

# Adjust imports according to your project structure
from ats_utilities.generator.engine import Generator
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.gen_params_bundle import GenParamsBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor


class TestGenerator(unittest.TestCase):
    """Unit tests for the primary Generator orchestrator engine."""

    def setUp(self) -> None:
        """Set up standard mocks and parameter bundles for Generator execution."""
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        self.mock_tar_processor = MagicMock(spec=ITarProcessor)

        # Build valid structural GeneratorBundle
        self.mock_component_bundle = MagicMock(spec=GeneratorBundle)
        self.mock_component_bundle.context_bundle = self.mock_context
        self.mock_component_bundle.scheme_loader = self.mock_scheme_loader
        self.mock_component_bundle.tar_processor = self.mock_tar_processor

        # Build valid configuration parameters GenParamsBundle
        self.mock_gen_params = MagicMock(spec=GenParamsBundle)
        self.mock_gen_params.archive_path = "/path/to/archive.tgz"
        self.mock_gen_params.target_dir = "/path/to/target"
        self.mock_gen_params.template_key = "python_pkg"
        self.mock_gen_params.scheme = "scheme_config.json"
        self.mock_gen_params.template_values = {"project_name": "ats_utilities"}

    def test_initialization_success(self) -> None:
        """Test successful initialization and structural property mapping bindings."""
        generator = Generator(self.mock_component_bundle)

        self.assertEqual(generator.get_shared_context(), self.mock_context)
        self.assertEqual(generator._scheme_loader, self.mock_scheme_loader)
        self.assertEqual(generator._tar_processor, self.mock_tar_processor)
        self.assertTrue(generator._is_initialized)

    def test_initialization_invalid_bundle(self) -> None:
        """Test initialization failure when passing an invalid object configuration type."""
        with self.assertRaises(Exception):
            Generator(None)  # type: ignore

        with self.assertRaises(Exception):
            Generator(MagicMock())  # type: ignore

    def test_prepare_template_values_case_variations(self) -> None:
        """Test computing and formatting name case alterations from input template dictionary configurations."""
        generator = Generator(self.mock_component_bundle)
        input_values = {"project_name": "sample_project_module"}

        expected_output = {
            "project_name": "sample_project_module",
            "project_name_dashed": "sample-project-module",
            "project_name_camel": "SampleProjectModule",
            "project_name_upper": "SAMPLE_PROJECT_MODULE"
        }

        result = generator.prepare_template_values(input_values)
        self.assertEqual(result, expected_output)

    def test_prepare_template_values_with_predefined_variations(self) -> None:
        """Test prepare_template_values when case variations are already present in values."""
        generator = Generator(self.mock_component_bundle)
        input_values = {
            "project_name": "sample_project",
            "project_name_dashed": "predefined-dashed",
            "project_name_camel": "PredefinedCamel",
            "project_name_upper": "PREDEFINED_UPPER"
        }

        result = generator.prepare_template_values(input_values)
        self.assertEqual(result["project_name_dashed"], "predefined-dashed")
        self.assertEqual(result["project_name_camel"], "PredefinedCamel")
        self.assertEqual(result["project_name_upper"], "PREDEFINED_UPPER")

    def test_prepare_template_values_missing_project_name(self) -> None:
        """Test validation check errors when missing key field designations inside inputs."""
        generator = Generator(self.mock_component_bundle)
        
        with self.assertRaises(Exception):
            generator.prepare_template_values({"version": "1.0.0"})

        with self.assertRaises(Exception):
            generator.prepare_template_values({"project_name": ""})

    @patch("ats_utilities.generator.engine.TarProcessBundle")
    def test_generate_success_flow(self, mock_tar_bundle_cls: MagicMock) -> None:
        """Test a clean execution flow where processing and template rendering map perfectly."""
        # Arrange
        generator = Generator(self.mock_component_bundle)
        
        resolved_scheme_mock = {
            "python_pkg": {
                "source_dir": "templates/python",
                "path_replacements": {"__pkg__": "ats_utilities"},
                "exclude": ["*.pyc", ".git"]
            }
        }
        self.mock_scheme_loader.load.return_value = resolved_scheme_mock
        
        mock_tar_bundle_instance = MagicMock()
        mock_tar_bundle_cls.return_value = mock_tar_bundle_instance

        # Act
        success = generator.generate(self.mock_gen_params)

        # Assert
        self.assertTrue(success)
        self.mock_scheme_loader.load.assert_called_once_with("scheme_config.json")
        mock_tar_bundle_cls.assert_called_once_with(
            archive_path="/path/to/archive.tgz",
            target_dir="/path/to/target",
            source_dir="templates/python",
            path_replacements={"__pkg__": "ats_utilities"},
            exclude_patterns=["*.pyc", ".git"],
            vals=generator.prepare_template_values(self.mock_gen_params.template_values)
        )
        self.mock_tar_processor.process.assert_called_once_with(mock_tar_bundle_instance)

    def test_generate_fails_when_template_key_missing_in_scheme(self) -> None:
        """Test that missing template keys stop processing loops immediately."""
        generator = Generator(self.mock_component_bundle)
        self.mock_scheme_loader.load.return_value = {"different_key": {}}

        with self.assertRaises(Exception):
            generator.generate(self.mock_gen_params)

    def test_generate_fails_when_source_dir_missing_in_scheme(self) -> None:
        """Test that missing internal structural fields like source_dir raise operation faults."""
        generator = Generator(self.mock_component_bundle)
        self.mock_scheme_loader.load.return_value = {"python_pkg": {"exclude": []}}

        with self.assertRaises(Exception):
            generator.generate(self.mock_gen_params)

    def test_generate_handles_processing_exceptions_gracefully(self) -> None:
        """Test that exceptions encountered in lower execution layers raise unified validation failures."""
        generator = Generator(self.mock_component_bundle)
        self.mock_scheme_loader.load.return_value = {"python_pkg": {"source_dir": "templates"}}
        self.mock_tar_processor.process.side_effect = RuntimeError("Disk full or archive bad")

        with self.assertRaises(Exception):
            generator.generate(self.mock_gen_params)

    def test_is_initialized_propagation(self) -> None:
        """Test that initialization checks accurately propagate sub-component readiness flags."""
        generator = Generator(self.mock_component_bundle)

        # Both sub-components operational
        self.mock_scheme_loader.is_initialized.return_value = True
        self.mock_tar_processor.is_initialized.return_value = True
        self.assertTrue(generator.is_initialized())

        # Scheme loader uninitialized
        self.mock_scheme_loader.is_initialized.return_value = False
        self.mock_tar_processor.is_initialized.return_value = True
        self.assertFalse(generator.is_initialized())

    @patch("ats_utilities.generator.engine.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test string casting reflection invocation properties mapping."""
        generator = Generator(self.mock_component_bundle)
        mock_to_str.return_value = "Generator{_shared_context=ContextBundle}"

        result = str(generator)

        mock_to_str.assert_called_once_with(generator)
        self.assertEqual(result, "Generator{_shared_context=ContextBundle}")


if __name__ == '__main__':
    unittest.main()
