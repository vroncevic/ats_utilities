# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock

from ats_utilities.generator.generator_registry import GeneratorRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.generator_params import GeneratorParams

class TestGeneratorRegistry(unittest.TestCase):
    """Unit tests for the GeneratorRegistry class."""

    def setUp(self) -> None:
        """Set up standard context bundle dependency mock."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

    def test_create_bundle(self) -> None:
        """Test create_bundle on GeneratorRegistry."""
        template_proc = MagicMock()
        scheme_load = MagicMock()
        tar_proc = MagicMock()

        result = GeneratorRegistry.create_bundle(
            GeneratorParams(
                context_bundle=self.mock_context_bundle,
                template_processor=template_proc,
                scheme_loader=scheme_load,
                tar_processor=tar_proc
            )
        )
        self.assertIsInstance(result, GeneratorBundle)
        self.assertEqual(result.context_bundle, self.mock_context_bundle)
        self.assertEqual(result.template_processor, template_proc)
        self.assertEqual(result.scheme_loader, scheme_load)
        self.assertEqual(result.tar_processor, tar_proc)


if __name__ == '__main__':
    unittest.main()
