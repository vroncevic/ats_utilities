# -*- coding: UTF-8 -*-

'''
Module
    ats_info_test.py
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
    Defines classes ATSInfoTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSInfo.
Execute
    python3 -m unittest -v ats_info_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.info import ATSInfo
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfoTestCase(TestCase):
    '''
        Defines classes ATSInfoTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSInfo.
        ATSInfo unit tests.

        It defines:

            :attributes:
                | base_info - Dict with base info.
                | ats_info - API for base info.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_show_base_info - Test for base info.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.base_info: dict[str, str] = {
            'ats_name': 'Simple Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'GPLv3',
            'ats_build_date': 'Sun 25 Apr 2021 08:12:40 PM CEST'
        }
        self.ats_info = ATSInfo(self.base_info)

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create_with_wrong_argument(self) -> None:
        '''Test wrong argument type'''
        with self.assertRaises(ATSTypeError):
            ATSInfo(None)  # type: ignore

    def test_create_with_wrong_arguments(self) -> None:
        '''Test wrong argument types'''
        info: ATSInfo = ATSInfo({
            'ats_name': None,
            'ats_version': None,
            'ats_licence': None,
            'ats_build_date': None
        })
        self.assertFalse(info.ats_info_ok)

    def test_create_with_extra_arguments(self) -> None:
        '''Test wrong argument types'''
        info: ATSInfo = ATSInfo({
            'ats_name': 'App',
            'ats_version': 'ver.1.0.0',
            'ats_licence': 'GPLv3',
            'ats_build_date': '02. Dec. 2023.',
            'ats_test': 'test'
        })
        self.assertFalse(info.ats_info_ok)

    def test_info_set_name_none(self) -> None:
        '''Test wrong argument types'''
        with self.assertRaises(ATSTypeError):
            self.ats_info.name = None

    def test_info_set_version_none(self) -> None:
        '''Test wrong argument types'''
        with self.assertRaises(ATSTypeError):
            self.ats_info.version = None

    def test_info_set_licence_none(self) -> None:
        '''Test wrong argument types'''
        with self.assertRaises(ATSTypeError):
            self.ats_info.licence = None

    def test_info_set_build_date_none(self) -> None:
        '''Test wrong argument types'''
        with self.assertRaises(ATSTypeError):
            self.ats_info.build_date = None

    def test_info_set_status_none(self) -> None:
        '''Test wrong argument types'''
        with self.assertRaises(ATSTypeError):
            self.ats_info.ats_info_ok = None  # type: ignore

    def test_info_name_not_none(self) -> None:
        '''Test info name not None'''
        self.assertTrue(self.ats_info.is_name_not_none())

    def test_info_licence_not_none(self) -> None:
        '''Test info licence not None'''
        self.assertTrue(self.ats_info.is_licence_not_none())

    def test_info_version_not_none(self) -> None:
        '''Test info version not None'''
        self.assertTrue(self.ats_info.is_version_not_none())

    def test_info_build_date_not_none(self) -> None:
        '''Test info build date not None'''
        self.assertTrue(self.ats_info.is_build_date_not_none())

    def test_show_base_info(self) -> None:
        '''Test base info.'''
        self.ats_info.show_base_info()


if __name__ == '__main__':
    main()
