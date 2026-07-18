# -*- coding: UTF-8 -*-

'''
Module
    splash_center_bundle_test.py
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
    Unit tests for SplashCenterBundle class.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashCenterBundleTest(unittest.TestCase):
    '''
        Defines class SplashCenterBundleTest with attribute(s) and method(s).
        Tests SplashCenterBundle validations.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful creation.
                | test_init_invalid_none - Tests creation with None values.
                | test_init_invalid_type - Tests creation with invalid types.
                | test_init_invalid_value - Tests creation with negative values.
                | test_to_dict - Tests dictionary serialization.
    '''

    def test_init_valid(self) -> None:
        bundle = SplashCenterBundle(columns=80, additional_shifter=2)
        self.assertEqual(bundle.columns, 80)
        self.assertEqual(bundle.additional_shifter, 2)

    def test_init_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            SplashCenterBundle(columns=None, additional_shifter=2)  # type: ignore

        with self.assertRaises(ATSValueError):
            SplashCenterBundle(columns=80, additional_shifter=None)  # type: ignore

    def test_init_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            SplashCenterBundle(columns="80", additional_shifter=2)  # type: ignore

        with self.assertRaises(ATSTypeError):
            SplashCenterBundle(columns=80, additional_shifter="2")  # type: ignore

    def test_init_invalid_value(self) -> None:
        with self.assertRaises(ATSValueError):
            SplashCenterBundle(columns=-10, additional_shifter=2)

        with self.assertRaises(ATSValueError):
            SplashCenterBundle(columns=80, additional_shifter=-2)

    def test_to_dict(self) -> None:
        bundle = SplashCenterBundle(columns=80, additional_shifter=2)
        self.assertEqual(bundle.to_dict(), {"columns": 80, "additional_shifter": 2})


if __name__ == "__main__":
    unittest.main()
