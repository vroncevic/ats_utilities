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
    Unit tests for SplashRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.splash.setup.registry import SplashRegistry
from ats_utilities.splash.setup.dependencies import SplashDependencies
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar


@patch("ats_utilities.splash.setup.registry.SplashValidator")
@patch("ats_utilities.splash.setup.registry.SplashDependenciesValidator")
class SplashRegistryTest(unittest.TestCase):
    '''
        Defines class SplashRegistryTest with attribute(s) and method(s).
        Tests SplashRegistry.
    '''

    def test_create_bundle(self, mock_dep_val: MagicMock, mock_val: MagicMock) -> None:
        """Tests create_bundle on SplashRegistry."""
        context_bundle = MagicMock(spec=ContextBundle)
        mock_prop = MagicMock(spec=ISplashProperty)
        mock_term = MagicMock(spec=ITerminalProperties)
        mock_ext = MagicMock(spec=IExtInfrastructure)
        mock_pb = MagicMock(spec=IProgressBar)

        params = SplashDependencies(
            context_bundle=context_bundle,
            splash_property=mock_prop,
            terminal_property=mock_term,
            ext=mock_ext,
            pb=mock_pb
        )

        bundle = SplashRegistry.create_bundle(params)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertEqual(bundle.context_bundle, context_bundle)
        self.assertEqual(bundle.splash_property, mock_prop)
        self.assertEqual(bundle.terminal_property, mock_term)
        self.assertEqual(bundle.ext, mock_ext)
        self.assertEqual(bundle.pb, mock_pb)

        mock_dep_val.validate.assert_called_once_with(params)
        mock_val.validate.assert_called_once_with(bundle)


if __name__ == "__main__":
    unittest.main()
