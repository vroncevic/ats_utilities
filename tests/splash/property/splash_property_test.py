# -*- coding: UTF-8 -*-

'''
Module
    splash_property_test.py
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
    Unit tests for SplashProperty class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splash.property.splash_property import SplashProperty
from ats_utilities.info.setup.keys import InfoBundleKeys


class SplashPropertyTest(unittest.TestCase):
    """Unit tests for SplashProperty class."""

    def _get_valid_prop(self) -> dict[str, object]:
        return {
            InfoBundleKeys.ATS_NAME: "ats_utilities",
            InfoBundleKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoBundleKeys.ATS_ORGANIZATION: "vroncevic",
            InfoBundleKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
        }

    def test_init(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        sp = SplashProperty(context_bundle)
        self.assertEqual(sp.settings[SplashProperty.ENABLED_SETTING], False)
        self.assertIsNone(sp.settings[SplashProperty.NAME_SETTING])

    def test_getter_setter(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        sp = SplashProperty(context_bundle)
        prop = self._get_valid_prop()
        sp.settings = prop

        self.assertEqual(sp.get_name(), "ats_utilities")
        self.assertEqual(sp.get_repository(), "https://github.com/vroncevic/ats_utilities")
        self.assertEqual(sp.get_organization(), "vroncevic")
        self.assertEqual(sp.get_logo(), "/path/to/logo.png")
        self.assertTrue(sp.get_use_github_infrastructure())
        self.assertTrue(sp.is_settings_enabled())

    def test_setter_invalid(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        sp = SplashProperty(context_bundle)

        # Invalid type
        with self.assertRaises(ATSTypeError):
            sp.settings = "not a mapping"  # type: ignore

        # Missing key for name
        invalid_prop = self._get_valid_prop()
        del invalid_prop[InfoBundleKeys.ATS_NAME]
        # In the actual setter implementation, it allows missing keys (assigning None).
        # But wait! If we pass missing key, it assigns None, and name is None.
        # Let's test that if name is not present, it stays None and settings are not enabled.
        sp.settings = invalid_prop
        self.assertIsNone(sp.get_name())
        self.assertFalse(sp.is_settings_enabled())

    def test_str(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        sp = SplashProperty(context_bundle)
        self.assertIn("SplashProperty", str(sp))


if __name__ == "__main__":
    unittest.main()
