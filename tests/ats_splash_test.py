# -*- coding: UTF-8 -*-

'''
Module
    ats_splash_test.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
from os.path import dirname
from unittest import TestCase, main

try:
    from ats_utilities.splash import Splash
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSSplashTestCase(TestCase):
    '''
        Defines class ATSSplashTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of termanl properties.
        Terminal properties unittests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_splash_with_none_property - Test splash with None.
                | test_size - Test for size.
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
        '''Test for create'''
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
        '''Test for create'''
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


if __name__ == '__main__':
    main()
