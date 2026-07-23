# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
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
    Unit tests for GeneratorRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.generator.setup.registry import GeneratorRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.setup.bundle import GeneratorBundle
from ats_utilities.generator.setup.dependencies import GeneratorDependencies
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestGeneratorRegistry(unittest.TestCase):
    """Unit tests for the GeneratorRegistry class."""

    def setUp(self) -> None:
        """Set up standard context bundle dependency mock."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

    def test_create_bundle(self) -> None:
        """Test create_bundle on GeneratorRegistry."""
        template_proc = MagicMock(spec=ITemplateProcessor)
        scheme_load = MagicMock(spec=ISchemeLoader)
        tar_proc = MagicMock(spec=ITarProcessor)

        result = GeneratorRegistry.create_bundle(
            GeneratorDependencies(
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
