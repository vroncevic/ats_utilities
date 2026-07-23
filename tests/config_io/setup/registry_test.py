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
    Unit tests for ConfigIORegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.registry import ConfigIORegistry
from ats_utilities.config_io.setup.dependencies import ConfigIODependencies

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ConfigIORegistryTest(unittest.TestCase):
    '''
        Defines class ConfigIORegistryTest with attribute(s) and method(s).
        Tests ConfigIORegistry logic.
    '''

    def test_create_bundle(self) -> None:
        """Tests create_bundle on ConfigIORegistry."""
        mock_processor = MagicMock(spec=IConfigProcessor)
        mock_context = MagicMock(spec=ContextBundle)

        bundle = ConfigIORegistry.create_bundle(
            ConfigIODependencies(
                file_path="/tmp/config.json",
                scheme={"key": "val"},
                processor=mock_processor,
                context_bundle=mock_context
            )
        )

        self.assertIsInstance(bundle, ConfigIOBundle)
        self.assertEqual(bundle.file_path, "/tmp/config.json")
        self.assertEqual(bundle.scheme, {"key": "val"})
        self.assertIs(bundle.processor, mock_processor)
        self.assertIs(bundle.context_bundle, mock_context)

    @patch("ats_utilities.config_io.setup.registry.ConfigProcessorFactory")
    def test_create_config_io_bundle_by_file_path_and_scheme(self, mock_factory: MagicMock) -> None:
        """Tests create_config_io_bundle_by_file_path_and_scheme helper."""
        mock_processor = MagicMock(spec=IConfigProcessor)
        mock_factory.create_from_file_path.return_value = mock_processor
        mock_context = MagicMock(spec=ContextBundle)

        bundle = ConfigIORegistry.create_config_io_bundle_by_file_path_and_scheme(
            file_path="/tmp/config.json",
            scheme={"key": "val"},
            context_bundle=mock_context
        )
        self.assertIsInstance(bundle, ConfigIOBundle)
        self.assertEqual(bundle.file_path, "/tmp/config.json")
        self.assertEqual(bundle.scheme, {"key": "val"})
        self.assertIs(bundle.processor, mock_processor)
        self.assertIs(bundle.context_bundle, mock_context)

    def test_create_config_io_bundle_by_injected_processor(self) -> None:
        """Tests create_config_io_bundle_by_injected_processor helper."""
        mock_processor = MagicMock(spec=IConfigProcessor)
        mock_context = MagicMock(spec=ContextBundle)
        bundle = ConfigIORegistry.create_config_io_bundle_by_injected_processor(
            processor=mock_processor,
            context_bundle=mock_context
        )
        self.assertIsInstance(bundle, ConfigIOBundle)
        self.assertEqual(bundle.file_path, "")
        self.assertEqual(bundle.scheme, {})
        self.assertIs(bundle.processor, mock_processor)
        self.assertIs(bundle.context_bundle, mock_context)


if __name__ == "__main__":
    unittest.main()
