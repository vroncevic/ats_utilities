# -*- coding: UTF-8 -*-

'''
Module
    ats_info_test.py
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
    Defines classes InfoManagerTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of InfoManager.
Execute
    python3 -m unittest -v ats_info_test
'''

from typing import List
from unittest import TestCase, main
from ats_utilities.info.engine import InfoManager
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class InfoManagerTestCase(TestCase):
    '''
        Defines classes InfoManagerTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of InfoManager.
        InfoManager unit tests.

        It defines:

            :attributes:
                | base_info - Dict with base info.
                | manager - API for base info.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_create_with_wrong_argument - Test wrong argument type.
                | test_create_with_wrong_arguments - Test wrong argument types.
                | test_info_set_name_none - Test setting name to None.
                | test_info_set_version_none - Test setting version to None.
                | test_info_set_licence_none - Test setting licence to None.
                | test_info_set_build_date_none - Test setting build date to None.
                | test_info_set_name_wrong_type - Test wrong type for name.
                | test_info_set_version_wrong_type - Test wrong type for version.
                | test_info_set_licence_wrong_type - Test wrong type for licence.
                | test_info_set_build_date_wrong_type - Test wrong type for build date.
                | test_info_properties_not_none - Test properties are not None.
                | test_info_optional_properties - Test setting/getting optional properties.
                | test_info_optional_properties_wrong_types - Test wrong types for optional properties.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.base_info: dict[str, str] = {
            'ats_name': 'Simple Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'GPLv3',
            'ats_build_date': 'Sun 25 Apr 2021 08:12:40 PM CEST'
        }
        self.manager = InfoManager()
        self.manager.set_info(self.base_info)

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create_with_wrong_argument(self) -> None:
        '''Test wrong argument type.'''
        with self.assertRaises(AttributeError):
            InfoManager("wrong")  # type: ignore

    def test_create_with_wrong_arguments(self) -> None:
        '''Test wrong argument types.'''
        manager = InfoManager()
        manager.set_info({
            'ats_name': None,
            'ats_version': None,
            'ats_licence': None,
            'ats_build_date': None
        })
        self.assertFalse(manager.info_ok)

    def test_info_set_name_none(self) -> None:
        '''Test setting name to None.'''
        self.manager.name = None
        self.assertIsNone(self.manager.name)
        self.assertFalse(self.manager.info_ok)

    def test_info_set_version_none(self) -> None:
        '''Test setting version to None.'''
        self.manager.version = None
        self.assertIsNone(self.manager.version)
        self.assertFalse(self.manager.info_ok)

    def test_info_set_licence_none(self) -> None:
        '''Test setting licence to None.'''
        self.manager.licence = None
        self.assertIsNone(self.manager.licence)
        self.assertFalse(self.manager.info_ok)

    def test_info_set_build_date_none(self) -> None:
        '''Test setting build date to None.'''
        self.manager.build_date = None
        self.assertIsNone(self.manager.build_date)
        self.assertFalse(self.manager.info_ok)

    def test_info_set_name_wrong_type(self) -> None:
        '''Test wrong type for name.'''
        with self.assertRaises(ATSTypeError):
            self.manager.name = 123  # type: ignore

    def test_info_set_version_wrong_type(self) -> None:
        '''Test wrong type for version.'''
        with self.assertRaises(ATSTypeError):
            self.manager.version = 123  # type: ignore

    def test_info_set_licence_wrong_type(self) -> None:
        '''Test wrong type for licence.'''
        with self.assertRaises(ATSTypeError):
            self.manager.licence = 123  # type: ignore

    def test_info_set_build_date_wrong_type(self) -> None:
        '''Test wrong type for build date.'''
        with self.assertRaises(ATSTypeError):
            self.manager.build_date = 123  # type: ignore

    def test_info_properties_not_none(self) -> None:
        '''Test properties are not None.'''
        self.assertTrue(self.manager.info_ok)
        self.assertEqual(self.manager.name, 'Simple Tool')
        self.assertEqual(self.manager.version, '1.0.0')
        self.assertEqual(self.manager.licence, 'GPLv3')
        self.assertEqual(self.manager.build_date, 'Sun 25 Apr 2021 08:12:40 PM CEST')

    def test_info_optional_properties(self) -> None:
        '''Test setting/getting optional properties.'''
        self.manager.repository = 'my-repo'
        self.manager.organization = 'my-org'
        self.manager.use_github = True
        self.manager.logo_path = '/path/to/logo.png'

        self.assertEqual(self.manager.repository, 'my-repo')
        self.assertEqual(self.manager.organization, 'my-org')
        self.assertEqual(self.manager.use_github, True)
        self.assertEqual(self.manager.logo_path, '/path/to/logo.png')

    def test_info_optional_properties_wrong_types(self) -> None:
        '''Test wrong types for optional properties.'''
        with self.assertRaises(ATSTypeError):
            self.manager.repository = 123  # type: ignore
        with self.assertRaises(ATSTypeError):
            self.manager.organization = 123  # type: ignore
        with self.assertRaises(ATSTypeError):
            self.manager.use_github = 'true'  # type: ignore
        with self.assertRaises(ATSTypeError):
            self.manager.logo_path = 123  # type: ignore


if __name__ == '__main__':
    main()
