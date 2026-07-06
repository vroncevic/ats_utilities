# -*- coding: UTF-8 -*-

'''
Module
    ats_splash_property_test.py
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
    Defines class ATSSplashPropTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of termanl properties.
Execute
    python3 -m unittest -v ats_splash_property_test
'''

from unittest import TestCase, main
from ats_utilities.splasher.property.splash_property import SplashProperty
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSSplashPropTestCase(TestCase):
    '''
        Defines class ATSSplashPropTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of termanl properties.
        SplashProperty unit tests.

        It defines:

            :attributes:
                | None.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_create - Test for create.
                | test_crete_with_none_property - Create with None property.
                | test_property - Test property.
                | test_wrong_property - Test wrong property.
                | test_str - Test string representation.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.splash_data = {
            'ats_organization': 'App Example',
            'ats_repository': 'app_example',
            'ats_name': 'appexample',
            'ats_logo_path': '',
            'ats_use_github_infrastructure': ''
        }

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test for create'''
        splash = SplashProperty()
        splash.splash_keys = self.splash_data
        self.assertIsNotNone(splash)

    def test_crete_with_none_property(self) -> None:
        '''Test create with None property'''
        splash = SplashProperty()
        with self.assertRaises(ATSTypeError):
            splash.splash_keys = None  # type: ignore

    def test_property(self) -> None:
        '''Test property'''
        splash = SplashProperty()
        splash.splash_keys = {
            'ats_organization': 'App Example',
            'ats_repository': 'app_example',
            'ats_name': 'appexample',
            'ats_logo_path': 'app logo',
            'ats_use_github_infrastructure': 'yes'
        }
        self.assertTrue(splash.validates())

    def test_wrong_property(self) -> None:
        '''Test wrong property'''
        splash = SplashProperty()
        with self.assertRaises(ATSValueError):
            splash.splash_keys = {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': 'app logo'
            }

    def test_get_splash_property(self) -> None:
        '''Test getter for splash_property.'''
        splash = SplashProperty()
        self.assertEqual(splash.splash_keys, {})
        splash.splash_keys = self.splash_data
        self.assertEqual(splash.splash_keys, self.splash_data)

    def test_str(self) -> None:
        '''Test string representation of SplashProperty.'''
        splash = SplashProperty()
        splash.splash_keys = self.splash_data
        self.assertIsInstance(str(splash), str)


if __name__ == '__main__':
    main()
