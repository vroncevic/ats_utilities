# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.base.base_registry import BaseRegistry
from ats_utilities.base.base_bundle import BaseBundle
from ats_utilities.base.base_params import BaseParams
from ats_utilities.context.bundle import ContextBundle


class TestBaseRegistry(unittest.TestCase):
    """Unit tests for the BaseRegistry class."""

    def test_create_bundle(self) -> None:
        """Test create_bundle delegates correctly."""
        info_file = "/opt/ats/config/info.json"
        mock_context_bundle = MagicMock(spec=ContextBundle)

        config_loader = MagicMock()
        info_manager = MagicMock()
        options_parser = MagicMock()
        splasher = MagicMock()
        generator = MagicMock()

        bundle = BaseRegistry.create_bundle(
            BaseParams(
                info_file=info_file,
                context_bundle=mock_context_bundle,
                use_generator=True,
                config_loader=config_loader,
                info_manager=info_manager,
                options_parser=options_parser,
                splasher=splasher,
                generator=generator
            )
        )
        self.assertIsInstance(bundle, BaseBundle)
        self.assertEqual(bundle.info_file, info_file)
        self.assertIs(bundle.context_bundle, mock_context_bundle)
        self.assertIs(bundle.config_loader, config_loader)
        self.assertIs(bundle.info_manager, info_manager)
        self.assertIs(bundle.options_parser, options_parser)
        self.assertIs(bundle.splasher, splasher)
        self.assertIs(bundle.generator, generator)
        self.assertTrue(bundle.use_generator)


if __name__ == '__main__':
    unittest.main()
