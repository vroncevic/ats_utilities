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
from typing import Any

from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splasher.property.splash_property import SplashProperty
from ats_utilities.splasher.splash_keys import SplashKeys

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashPropertyTest(unittest.TestCase):
    '''
        Defines class SplashPropertyTest with attribute(s) and method(s).
        Tests SplashProperty validations and property management.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests successful initialization.
                | test_getter_setter - Tests property getter and setter.
                | test_setter_invalid - Tests setter with invalid values/types.
                | test_validates - Tests validation checks.
                | test_str - Tests __str__ method.
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

    def test_init(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        sp = SplashProperty(context_bundle)
        self.assertEqual(sp.splash_keys, {})

    def test_getter_setter(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        sp = SplashProperty(context_bundle)
        prop = self._get_valid_prop()
        sp.splash_keys = prop
        expected = prop.copy()
        del expected["enabled"]
        self.assertEqual(sp.splash_keys, expected)

    def test_setter_invalid(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        sp = SplashProperty(context_bundle)

        # Invalid type
        with self.assertRaises(ATSTypeError):
            sp.splash_keys = "not a mapping"  # type: ignore

        # Missing key
        invalid_prop = self._get_valid_prop()
        del invalid_prop[SplashKeys.ATS_NAME]
        with self.assertRaises(ATSValueError):
            sp.splash_keys = invalid_prop

    def test_validates(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        sp = SplashProperty(context_bundle)

        # Uninitialized validation exception (decorator @has_attrs)
        with self.assertRaises(ATSValueError):
            sp.validates()

        # Enabled validation
        sp.splash_keys = self._get_valid_prop()
        self.assertTrue(sp.validates())

        # Disabled validation
        sp.splash_keys = {"enabled": False}
        self.assertTrue(sp.validates())

    def test_str(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        sp = SplashProperty(context_bundle)
        self.assertIn("SplashProperty", str(sp))


if __name__ == "__main__":
    unittest.main()
