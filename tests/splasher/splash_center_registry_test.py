# -*- coding: UTF-8 -*-

'''
Module
    splash_center_registry_test.py
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
    Unit tests for SplashCenterRegistry class.
'''

from __future__ import annotations

import unittest

from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle
from ats_utilities.splasher.splash_center_registry import SplashCenterRegistry

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashCenterRegistryTest(unittest.TestCase):
    '''
        Defines class SplashCenterRegistryTest with attribute(s) and method(s).
        Tests SplashCenterRegistry static/class factory.

        It defines:

            :attributes: None.
            :methods:
                | test_create_splash_center_bundle - Tests successful creation.
    '''

    def test_create_splash_center_bundle(self) -> None:
        bundle = SplashCenterRegistry.create_splash_center_bundle(80, 2)
        self.assertIsInstance(bundle, SplashCenterBundle)
        self.assertEqual(bundle.columns, 80)
        self.assertEqual(bundle.additional_shifter, 2)


if __name__ == "__main__":
    unittest.main()
