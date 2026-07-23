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
    Unit tests for BaseRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.base.setup.registry import BaseRegistry
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.dependencies import BaseDependencies
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestBaseRegistry(unittest.TestCase):
    """Unit tests for the BaseRegistry class."""

    def test_create_bundle(self) -> None:
        """Test create_bundle delegates correctly."""
        info_file = "/opt/ats/config/info.json"
        mock_context_bundle = MagicMock(spec=ContextBundle)

        config_loader = MagicMock(spec=ILoader)
        info_manager = MagicMock(spec=IInfoManager)
        options_parser = MagicMock(spec=IOptionManager)
        splasher = MagicMock(spec=ISplasher)
        generator = MagicMock(spec=IGenerator)

        bundle = BaseRegistry.create_bundle(
            BaseDependencies(
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
