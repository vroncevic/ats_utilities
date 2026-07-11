# -*- coding: UTF-8 -*-

'''
Module
    ats_splash_center_bundle_test.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates test cases for checking SplashCenterBundle.
Execute
    python3 -m unittest -v tests/splasher/ats_splash_center_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashCenterBundleTestCase(TestCase):
    '''Test cases for SplashCenterBundle.'''

    def test_splash_center_bundle(self) -> None:
        '''Test SplashCenterBundle methods.'''
        bundle1 = SplashCenterBundle()
        bundle2 = SplashCenterBundle(columns=80, additional_shifter=2, text='Welcome')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.columns, 80)
        self.assertEqual(bundle1.additional_shifter, 2)
        self.assertEqual(bundle1.text, 'Welcome')

        # Test merge when other fields are None (covers 123->120 branch)
        bundle3 = SplashCenterBundle()
        bundle3.columns = None
        bundle3.additional_shifter = None
        bundle3.text = None
        bundle2.merge(bundle3)
        self.assertEqual(bundle2.columns, 80) # should remain unchanged

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['text'], 'Welcome')

    def test_splash_center_bundle_validation_errors(self) -> None:
        '''Test SplashCenterBundle validation exceptions.'''
        # columns negative value in post init gets set to 0
        b_neg_cols = SplashCenterBundle(columns=-1)
        self.assertEqual(b_neg_cols.columns, 0)

        # additional_shifter negative value in post init gets set to 0
        b_neg_shift = SplashCenterBundle(additional_shifter=-1)
        self.assertEqual(b_neg_shift.additional_shifter, 0)

        # columns type error
        with self.assertRaises(ATSTypeError):
            SplashCenterBundle(columns='not_int', additional_shifter=2, text='ok')

        # columns value error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='ok')
        bundle.columns = -1
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # additional_shifter type error
        with self.assertRaises(ATSTypeError):
            SplashCenterBundle(columns=80, additional_shifter='not_int', text='ok')

        # additional_shifter value error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='ok')
        bundle.additional_shifter = -1
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # text type error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text=123)  # type: ignore
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        # text value error (empty string)
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='   ')
        with self.assertRaises(ATSValueError):
            bundle.validate()

    def test_splash_center_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a SplashCenterBundle.'''
        bundle = SplashCenterBundle()
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_splash_center_bundle")


if __name__ == '__main__':
    main()
