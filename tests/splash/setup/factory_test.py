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
    Unit tests for SplashFactory class.
'''

from __future__ import annotations

import unittest
from unittest.mock import patch, MagicMock

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError
from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.splash.setup.factory import SplashFactory
from ats_utilities.splash.setup.options import SplashOptions


@patch("ats_utilities.splash.setup.validator.check_file_exists")
class SplashFactoryTest(unittest.TestCase):
    '''
        Defines class SplashFactoryTest with attribute(s) and method(s).
        Tests SplashFactory logic.
    '''

    def _get_valid_prop(self) -> dict[str, object]:
        return {
            "enabled": True,
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
        }

    @patch("ats_utilities.splash.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_github(self, mock_size: MagicMock, mock_check: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextFactory.create_bundle()
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=context_bundle)

        bundle = SplashFactory.create_bundle(options)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.splash_property.is_settings_enabled())
        self.assertTrue(bundle.ext.infrastructure_property)

    @patch("ats_utilities.splash.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_external(self, mock_size: MagicMock, mock_check: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextFactory.create_bundle()
        prop = self._get_valid_prop()
        prop[InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False
        options = SplashOptions(prop=prop, context_bundle=context_bundle)

        bundle = SplashFactory.create_bundle(options)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.splash_property.is_settings_enabled())
        self.assertTrue(bundle.ext.infrastructure_property)

    @patch("ats_utilities.splash.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_disabled(self, mock_size: MagicMock, mock_check: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextFactory.create_bundle()
        prop = {"enabled": False}
        options = SplashOptions(prop=prop, context_bundle=context_bundle)

        bundle = SplashFactory.create_bundle(options)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertFalse(bundle.splash_property.is_settings_enabled())

    def test_create_splash_bundle_invalid_context(self, mock_check: MagicMock) -> None:
        prop = self._get_valid_prop()
        with self.assertRaises(ATSTypeError):
            SplashFactory.create_bundle(SplashOptions(prop=prop, context_bundle=None))  # type: ignore

        with self.assertRaises(ATSTypeError):
            SplashFactory.create_bundle(SplashOptions(prop=prop, context_bundle=object()))  # type: ignore


if __name__ == "__main__":
    unittest.main()
