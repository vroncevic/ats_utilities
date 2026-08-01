# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
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
    Unit tests for SplashKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.splash.setup.keys import SplashKeys


class SplashKeysTest(unittest.TestCase):
    '''
        Defines class SplashKeysTest with attribute(s) and method(s).
        Tests SplashKeys configuration model.
    '''

    def test_keys(self) -> None:
        self.assertEqual(SplashKeys.DEPENDENCY_SPLASH_PROPERTY, 'splash_property')
        self.assertEqual(SplashKeys.DEPENDENCY_TERMINAL_PROPERTY, 'terminal_property')
        self.assertEqual(SplashKeys.DEPENDENCY_EXT, 'ext')
        self.assertEqual(SplashKeys.DEPENDENCY_PB, 'pb')
        self.assertEqual(SplashKeys.DEPENDENCY_CONTEXT_BUNDLE, 'context_bundle')

        self.assertEqual(SplashKeys.OPTION_PROP, 'prop')
        self.assertEqual(SplashKeys.OPTION_CONTEXT_BUNDLE, 'context_bundle')

    def test_get_dependency_to_type(self) -> None:
        mapping = SplashKeys.get_dependency_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(SplashKeys.DEPENDENCY_SPLASH_PROPERTY, mapping)

    def test_get_option_to_type(self) -> None:
        mapping = SplashKeys.get_option_to_type()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertIn(SplashKeys.OPTION_PROP, mapping)


if __name__ == "__main__":
    unittest.main()
