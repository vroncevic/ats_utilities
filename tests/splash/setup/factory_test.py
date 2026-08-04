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
    Unit tests for SplashBundleFactory class.
'''

from __future__ import annotations

import unittest
from unittest.mock import patch, MagicMock

from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.exceptions import ATSTypeError
from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.info.setup.keys import InfoBundleKeys
from ats_utilities.splash.setup.factory import SplashBundleFactory
from ats_utilities.splash.setup.options import SplashBundleOptions


@patch("ats_utilities.splash.setup.validator.check_file_exists")
class SplashFactoryTest(unittest.TestCase):
    '''
        Defines class SplashFactoryTest with attribute(s) and method(s).
        Tests SplashBundleFactory logic.
    '''

    def _get_valid_prop(self) -> dict[str, object]:
        return {
            "enabled": True,
            InfoBundleKeys.ATS_NAME: "ats_utilities",
            InfoBundleKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoBundleKeys.ATS_ORGANIZATION: "vroncevic",
            InfoBundleKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
        }

    @patch("ats_utilities.splash.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_github(self, mock_size: MagicMock, mock_check: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextBundleFactory.create_bundle()
        prop = self._get_valid_prop()
        options = SplashBundleOptions(prop=prop, context_bundle=context_bundle)

        bundle = SplashBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.splash_property.is_settings_enabled())
        self.assertTrue(bundle.ext.infrastructure_property)

    @patch("ats_utilities.splash.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_external(self, mock_size: MagicMock, mock_check: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextBundleFactory.create_bundle()
        prop = self._get_valid_prop()
        prop[InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False
        options = SplashBundleOptions(prop=prop, context_bundle=context_bundle)

        bundle = SplashBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertTrue(bundle.splash_property.is_settings_enabled())
        self.assertTrue(bundle.ext.infrastructure_property)

    @patch("ats_utilities.splash.terminal.terminal_properties.TerminalProperties.size")
    def test_create_splash_bundle_disabled(self, mock_size: MagicMock, mock_check: MagicMock) -> None:
        mock_size.return_value = (24, 80, 0, 0)
        context_bundle = ContextBundleFactory.create_bundle()
        prop = {"enabled": False}
        options = SplashBundleOptions(prop=prop, context_bundle=context_bundle)

        bundle = SplashBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, SplashBundle)
        self.assertFalse(bundle.splash_property.is_settings_enabled())

    def test_create_splash_bundle_invalid_context(self, mock_check: MagicMock) -> None:
        prop = self._get_valid_prop()
        with self.assertRaises(ATSTypeError):
            SplashBundleFactory.create_bundle(SplashBundleOptions(prop=prop, context_bundle=None))  # type: ignore

        with self.assertRaises(ATSTypeError):
            SplashBundleFactory.create_bundle(SplashBundleOptions(prop=prop, context_bundle=object()))  # type: ignore


if __name__ == "__main__":
    unittest.main()
