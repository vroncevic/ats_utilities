# -*- coding: UTF-8 -*-

'''
Module
    ats_splash_property_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.splash import SplashProperty
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


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
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test for create'''
        splash: SplashProperty = SplashProperty(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': '',
                'ats_use_github_infrastructure': ''
            }
        )
        self.assertIsNotNone(splash)

    def test_crete_with_none_property(self) -> None:
        '''Test create with None property'''
        with self.assertRaises(ATSTypeError):
            SplashProperty(None)  # type: ignore

    def test_property(self) -> None:
        '''Test property'''
        splash: SplashProperty = SplashProperty(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': 'app logo',
                'ats_use_github_infrastructure': 'yes'
            }
        )
        self.assertTrue(splash.validate())

    def test_wrong_property(self) -> None:
        '''Test wrong property'''
        splash: SplashProperty = SplashProperty(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': 'app logo'
            }
        )
        self.assertFalse(splash.validate())


if __name__ == '__main__':
    main()
