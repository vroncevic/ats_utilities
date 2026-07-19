# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch

# Adjust imports according to your project structure
from ats_utilities.generator.generator_registry import GeneratorRegistry
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor

class TestGeneratorRegistry(unittest.TestCase):
    """Unit tests for the GeneratorRegistry factory class."""

    def setUp(self) -> None:
        """Set up standard context bundle dependency mock."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

    @patch("ats_utilities.generator.generator_registry.GeneratorBundle")
    @patch("ats_utilities.generator.generator_registry.TarProcessor")
    @patch("ats_utilities.generator.generator_registry.SchemeLoader")
    @patch("ats_utilities.generator.generator_registry.TemplateProcessor")
    def test_create_default_generator_bundle_orchestration(
        self, mock_template_cls: MagicMock, mock_scheme_cls: MagicMock,
        mock_tar_cls: MagicMock, mock_bundle_cls: MagicMock
    ) -> None:
        """Test that the factory properly orchestrates component instantiation and bundle assembly."""
        # Arrange
        mock_template_inst = MagicMock()
        mock_scheme_inst = MagicMock()
        mock_tar_inst = MagicMock()
        mock_bundle_inst = MagicMock(spec=GeneratorBundle)

        mock_template_cls.return_value = mock_template_inst
        mock_scheme_cls.return_value = mock_scheme_inst
        mock_tar_cls.return_value = mock_tar_inst
        mock_bundle_cls.return_value = mock_bundle_inst

        # Act
        result = GeneratorRegistry.create_default_generator_bundle(self.mock_context_bundle)

        # Assert
        # Verify internal processors receive correct initialization parameters
        mock_template_cls.assert_called_once_with(context_bundle=self.mock_context_bundle)
        mock_scheme_cls.assert_called_once_with(context_bundle=self.mock_context_bundle)
        mock_tar_cls.assert_called_once_with(
            context_bundle=self.mock_context_bundle, 
            template_processor=mock_template_inst
        )

        # Verify bundle class aggregation mapping match rules
        mock_bundle_cls.assert_called_once_with(
            template_processor=mock_template_inst,
            scheme_loader=mock_scheme_inst,
            tar_processor=mock_tar_inst,
            context_bundle=self.mock_context_bundle
        )
        self.assertEqual(result, mock_bundle_inst)

    @patch("ats_utilities.generator.generator_registry.TarProcessor")
    @patch("ats_utilities.generator.generator_registry.SchemeLoader")
    @patch("ats_utilities.generator.generator_registry.TemplateProcessor")
    @patch("ats_utilities.generator.generator_registry.GeneratorBundle")
    def test_create_default_generator_bundle_integration(
        self, mock_bundle_cls: MagicMock, mock_template_cls: MagicMock,
        mock_scheme_cls: MagicMock, mock_tar_cls: MagicMock
    ) -> None:
        """Test integration factory flow to verify an operational bundle structure is returned."""
        # Arrange un-mocked fallback integration properties
        mock_template = MagicMock(spec=ITemplateProcessor)
        mock_scheme = MagicMock(spec=ISchemeLoader)
        mock_tar = MagicMock(spec=ITarProcessor)
        
        mock_template_cls.return_value = mock_template
        mock_scheme_cls.return_value = mock_scheme
        mock_tar_cls.return_value = mock_tar
        
        # We allow fallback generation execution loop to construct structural bundle fields
        mock_bundle_cls.side_effect = lambda **kwargs: GeneratorBundle(**kwargs)

        # Act
        result = GeneratorRegistry.create_default_generator_bundle(self.mock_context_bundle)

        # Assert
        self.assertIsInstance(result, GeneratorBundle)
        self.assertEqual(result.context_bundle, self.mock_context_bundle)
        self.assertEqual(result.template_processor, mock_template)
        self.assertEqual(result.scheme_loader, mock_scheme)
        self.assertEqual(result.tar_processor, mock_tar)

    @patch("ats_utilities.generator.generator_registry.GeneratorBundle")
    def test_create_bundle(self, mock_bundle_cls: MagicMock) -> None:
        """Test create_bundle on GeneratorRegistry."""
        mock_bundle_inst = MagicMock(spec=GeneratorBundle)
        mock_bundle_cls.return_value = mock_bundle_inst
        result = GeneratorRegistry.create_bundle(context_bundle=self.mock_context_bundle)
        self.assertEqual(result, mock_bundle_inst)


if __name__ == '__main__':
    unittest.main()
