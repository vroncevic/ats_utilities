# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Unit tests for GeneratorFactory class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.generator.setup.factory import GeneratorFactory
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.setup.bundle import GeneratorBundle
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestGeneratorFactory(unittest.TestCase):
    """Unit tests for the GeneratorFactory class."""

    def setUp(self) -> None:
        """Set up standard context bundle dependency mock."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

    @patch("ats_utilities.generator.setup.factory.GeneratorRegistry")
    @patch("ats_utilities.generator.setup.factory.TarProcessor")
    @patch("ats_utilities.generator.setup.factory.SchemeLoader")
    @patch("ats_utilities.generator.setup.factory.TemplateProcessor")
    def test_create_default_generator_bundle_orchestration(
        self, mock_template_cls: MagicMock, mock_scheme_cls: MagicMock,
        mock_tar_cls: MagicMock, mock_registry_cls: MagicMock
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
        mock_registry_cls.create_bundle.return_value = mock_bundle_inst

        # Act
        result = GeneratorFactory.create_default_generator_bundle(self.mock_context_bundle)

        # Assert
        mock_template_cls.assert_called_once_with(context_bundle=self.mock_context_bundle)
        mock_scheme_cls.assert_called_once_with(context_bundle=self.mock_context_bundle)
        mock_tar_cls.assert_called_once_with(
            context_bundle=self.mock_context_bundle,
            template_processor=mock_template_inst
        )

        mock_registry_cls.create_bundle.assert_called_once()
        self.assertEqual(result, mock_bundle_inst)

    @patch("ats_utilities.generator.setup.factory.TarProcessor")
    @patch("ats_utilities.generator.setup.factory.SchemeLoader")
    @patch("ats_utilities.generator.setup.factory.TemplateProcessor")
    @patch("ats_utilities.generator.setup.factory.GeneratorRegistry")
    def test_create_default_generator_bundle_integration(
        self, mock_registry_cls: MagicMock, mock_template_cls: MagicMock,
        mock_scheme_cls: MagicMock, mock_tar_cls: MagicMock
    ) -> None:
        """Test integration factory flow to verify an operational bundle structure is returned."""
        # Arrange
        mock_template = MagicMock(spec=ITemplateProcessor)
        mock_scheme = MagicMock(spec=ISchemeLoader)
        mock_tar = MagicMock(spec=ITarProcessor)
        
        mock_template_cls.return_value = mock_template
        mock_scheme_cls.return_value = mock_scheme
        mock_tar_cls.return_value = mock_tar
        
        mock_registry_cls.create_bundle.side_effect = lambda deps: GeneratorBundle(
            scheme_loader=deps['scheme_loader'],
            tar_processor=deps['tar_processor'],
            template_processor=deps['template_processor'],
            context_bundle=deps['context_bundle']
        )

        # Act
        result = GeneratorFactory.create_default_bundle({
            "context_bundle": self.mock_context_bundle
        })

        # Assert
        self.assertIsInstance(result, GeneratorBundle)
        self.assertEqual(result.context_bundle, self.mock_context_bundle)
        self.assertEqual(result.template_processor, mock_template)
        self.assertEqual(result.scheme_loader, mock_scheme)
        self.assertEqual(result.tar_processor, mock_tar)


if __name__ == '__main__':
    unittest.main()
