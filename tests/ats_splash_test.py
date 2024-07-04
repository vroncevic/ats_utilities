# -*- coding: UTF-8 -*-

'''
Module
    ats_splash_test.py
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
    Defines class ATSSplashTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of termanl properties.
Execute
    python3 -m unittest -v ats_splash_test
'''

import sys
from typing import List
from os.path import dirname
from unittest import TestCase, main

try:
    from ats_utilities.splash import Splash
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSSplashTestCase(TestCase):
    '''
        Defines class ATSSplashTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of termanl properties.
        Splash unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_splash_with_none_property - Test splash with None.
                | test_create - Test for create (not None).
                | test_create_with_ext - Test for create with external.
                | test_wrong_parameter_center - Test for wrong center param.
                | test_empty_parameter_center - Test for empty center param.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_splash_with_none_property(self) -> None:
        '''Test splash with None'''
        with self.assertRaises(ATSTypeError):
            Splash(None)  # type: ignore

    def test_create(self) -> None:
        '''Test for create (not None)'''
        splash: Splash = Splash(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': f'{dirname(__file__)}/config/app.logo',
                'ats_use_github_infrastructure': 'yes'
            }
        )
        self.assertIsNotNone(splash)

    def test_create_with_ext(self) -> None:
        '''Test for create with external'''
        splash: Splash = Splash(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': f'{dirname(__file__)}/config/app.logo',
                'ats_use_github_infrastructure': False
            }
        )
        self.assertIsNotNone(splash)

    def test_wrong_parameter_center(self) -> None:
        '''Test for wrong center param'''
        splash: Splash = Splash(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': f'{dirname(__file__)}/config/app.logo',
                'ats_use_github_infrastructure': False
            }
        )
        with self.assertRaises(ATSTypeError):
            splash.center(120, 20, None)

    def test_empty_parameter_center(self) -> None:
        '''Test for empty center param'''
        splash: Splash = Splash(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example',
                'ats_name': 'appexample',
                'ats_logo_path': f'{dirname(__file__)}/config/app.logo',
                'ats_use_github_infrastructure': False
            }
        )
        with self.assertRaises(ATSValueError):
            splash.center(120, 20, '')


if __name__ == '__main__':
    main()
