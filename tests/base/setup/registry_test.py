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
    Unit tests for BaseBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.base.setup.registry import BaseBundleRegistry
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.dependencies import BaseBundleDependencies
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager


@patch("ats_utilities.base.setup.registry.BaseBundleValidator")
@patch("ats_utilities.base.setup.registry.BaseBundleDependenciesValidator")
class TestBaseRegistry(unittest.TestCase):
    """Unit tests for the BaseBundleRegistry class."""

    def test_create_bundle(self, mock_dep_val: MagicMock, mock_val: MagicMock) -> None:
        """Test create_bundle delegates correctly."""
        mock_context_bundle = MagicMock(spec=ContextBundle)
        info_manager = MagicMock(spec=IInfoManager)
        option_manager = MagicMock(spec=IOptionManager)
        splash_manager = MagicMock(spec=ISplashManager)
        generation_manager = MagicMock(spec=IGeneratorManager)

        bundle = BaseBundleRegistry.create_bundle(
            BaseBundleDependencies(
                context_bundle=mock_context_bundle,
                info_manager=info_manager,
                option_manager=option_manager,
                splash_manager=splash_manager,
                generation_manager=generation_manager
            )
        )
        self.assertIsInstance(bundle, BaseBundle)
        self.assertIs(bundle.context_bundle, mock_context_bundle)
        self.assertIs(bundle.info_manager, info_manager)
        self.assertIs(bundle.option_manager, option_manager)
        self.assertIs(bundle.splash_manager, splash_manager)
        self.assertIs(bundle.generation_manager, generation_manager)

        mock_dep_val.validate.assert_called_once()
        mock_val.validate.assert_called_once_with(bundle)


if __name__ == '__main__':
    unittest.main()
