# -*- coding: UTF-8 -*-

'''
Module
    ats_logo_test.py
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
    Defines classes LogoTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Logo.
Execute
    python3 -m unittest -v ats_logo_test
'''

from unittest import TestCase, main

from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.info.logo.engine import Logo
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class LogoTestCase(TestCase):
    '''
        Defines classes LogoTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Logo.
        Logo unit tests.

        It defines:

            :attributes:
                | instance - API for logo.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that Logo instance is not None.
                | test_logo_value_is_none_by_default - Test that logo value is None by default.
                | test_logo_try_to_set_none - Test setting logo to None.
                | test_logo_try_to_set_wrong_type - Test wrong type for logo.
                | test_logo_set_to_value - Test setting logo with value.
                | test_logo_set_twice - Test setting logo twice.
                | test_logo_set_then_changed - Test setting logo then changing it.
                | test_logo_not_none_after_set - Test that logo is not None after setting it.
                | test_logo_string_after_set - Test that logo is a string after setting it.
                | test_logo_str_representation - Test string representation of logo.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = Logo()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default Logo instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, ILogo)

    def test_logo_value_is_none_by_default(self) -> None:
        '''Test logo value is None by default.'''
        self.assertIsNone(self.instance.logo)
        self.assertFalse(self.instance.not_none())

    def test_logo_try_to_set_none(self) -> None:
        '''Test setting logo to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.logo = None

    def test_logo_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for logo.'''
        with self.assertRaises(ATSTypeError):
            self.instance.logo = True

        with self.assertRaises(ATSTypeError):
            self.instance.logo = 123

        with self.assertRaises(ATSTypeError):
            self.instance.logo = [r'GPLv2']

        with self.assertRaises(ATSTypeError):
            self.instance.logo = (r'GPLv2',)

        with self.assertRaises(ATSTypeError):
            self.instance.logo = {'logo': r'GPLv2'}

    def test_logo_set_to_value(self) -> None:
        '''Test setting logo with value.'''
        self.instance.logo = r'GPLv2'
        self.assertEqual(self.instance.logo, r'GPLv2')

    def test_logo_set_twice(self) -> None:
        '''Test setting logo twice.'''
        self.instance.logo = r'GPLv2'
        self.instance.logo = r'GPLv2'
        self.assertEqual(self.instance.logo, r'GPLv2')

    def test_logo_set_then_changed(self) -> None:
        '''Test setting logo then changing it.'''
        self.instance.logo = r'GPLv2'
        self.assertEqual(self.instance.logo, r'GPLv2')
        self.instance.logo = r'MIT'
        self.assertEqual(self.instance.logo, r'MIT')

    def test_logo_not_none_after_set(self) -> None:
        '''Test that logo is not None after setting it.'''
        self.instance.logo = r'MIT'
        self.assertTrue(self.instance.not_none())

    def test_logo_string_after_set(self) -> None:
        '''Test that logo is a string after setting it.'''
        self.instance.logo = r'MIT'
        self.assertIsInstance(self.instance.logo, str)

    def test_logo_str_representation(self) -> None:
        '''Test string representation of logo.'''
        self.instance.logo = r'MIT'
        self.assertIsInstance(str(self.instance.logo), str)
        self.assertEqual(str(self.instance.logo), r'MIT')
        self.assertNotEqual(str(self.instance.logo), r'GPLv2')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
