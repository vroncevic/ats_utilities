# -*- coding: UTF-8 -*-

'''
Module
    splash_registry_test.py
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
from typing import Any
from unittest.mock import patch, MagicMock

from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splasher.splash_bundle import SplashBundle
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.splasher.splash_registry import SplashRegistry

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashRegistryTest(unittest.TestCase):
    '''
        Defines class SplashRegistryTest with attribute(s) and method(s).
        Tests SplashRegistry factory parsing.

        It defines:

            :attributes: None.
            :methods:
                | test_create_splash_bundle_github - Tests creation with GitHub infrastructure.
                | test_create_splash_bundle_external - Tests creation with external infrastructure.
                | test_create_splash_bundle_disabled - Tests creation when splash screen is disabled.
                | test_create_splash_bundle_none_prop - Tests creation with None prop.
                | test_create_splash_bundle_invalid_context - Tests error cases for invalid contexts.
    '''

    def _get_valid_prop(self) -> dict[str, Any]:
        return {
            "enabled": True,
            SplashKeys.ATS_NAME: "ats_utilities",
            SplashKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            SplashKeys.ATS_ORGANIZATION: "vroncevic",
            SplashKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
        }

    @patch("ats_utilities.splasher.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_github(self, mock_size: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextRegistry.create_default_context_bundle()
        prop = self._get_valid_prop()
        bundle = SplashRegistry.create_splash_bundle_from_dict(prop, context_bundle)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.property_validated)
        self.assertTrue(bundle.github.infrastructure_property)

    @patch("ats_utilities.splasher.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_external(self, mock_size: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextRegistry.create_default_context_bundle()
        prop = self._get_valid_prop()
        prop[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False
        bundle = SplashRegistry.create_splash_bundle_from_dict(prop, context_bundle)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.property_validated)
        self.assertTrue(bundle.ext.infrastructure_property)

    @patch("ats_utilities.splasher.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_disabled(self, mock_size: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextRegistry.create_default_context_bundle()
        prop = {"enabled": False}
        bundle = SplashRegistry.create_splash_bundle_from_dict(prop, context_bundle)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.property_validated)

    @patch("ats_utilities.splasher.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_none_prop(self, mock_size: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = SplashRegistry.create_splash_bundle_from_dict(None, context_bundle)  # type: ignore
        self.assertIsInstance(bundle, SplashBundle)
        self.assertFalse(bundle.property_validated)
        self.assertEqual(bundle.prop, {})

    def test_create_splash_bundle_invalid_context(self) -> None:
        prop = self._get_valid_prop()
        with self.assertRaises(ATSValueError):
            SplashRegistry.create_splash_bundle_from_dict(prop, None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            SplashRegistry.create_splash_bundle_from_dict(prop, object())  # type: ignore

    @patch("ats_utilities.splasher.terminal.terminal_properties.TerminalProperties.size")
    def test_create_bundle(self, mock_size: MagicMock) -> None:
        """Tests create_bundle on SplashRegistry."""
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextRegistry.create_default_context_bundle()
        prop = self._get_valid_prop()
        bundle = SplashRegistry.create_bundle(prop=prop, context_bundle=context_bundle)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.property_validated)
        self.assertTrue(bundle.github.infrastructure_property)


if __name__ == "__main__":
    unittest.main()
