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

from unittest import TestCase, main, mock
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.build_date import BuildDate
from ats_utilities.info.licence import Licence
from ats_utilities.info.logo import Logo
from ats_utilities.info.name import Name
from ats_utilities.info.organization import Organization
from ats_utilities.info.repository import Repository
from ats_utilities.info.use_github import UseGitHub
from ats_utilities.info.version import Version
from ats_utilities.info.info_ok import InfoOk
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
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
                | test_is_initialized - Test is info manager initialized.
                | test_initialization_failure - Test info manager initialization failure.
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
                | test_str - Test string representation of InfoManager.
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

    def test_is_initialized(self) -> None:
        '''Test is_initialized method.'''
        self.assertTrue(self.manager.is_initialized())

    @mock.patch('ats_utilities.info.engine.make_component')
    def test_initialization_failure(self, mock_make_component) -> None:
        '''Test info manager initialization failure.'''
        mock_make_component.side_effect = ATSTypeError('Failed to initialize component')
        invalid_manager = InfoManager()
        self.assertFalse(invalid_manager.is_initialized())

    def test_str(self) -> None:
        '''Test string representation of InfoManager.'''
        self.assertIsInstance(str(self.manager), str)

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

    def test_getattr_invalid_attribute(self) -> None:
        '''Test getattr with an invalid attribute raises AttributeError.'''
        with self.assertRaises(AttributeError):
            _ = self.manager.non_existent_attribute


class InfoComponentsTestCase(TestCase):
    '''
        Defines class InfoComponentsTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of individual info components.
        Info components unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_build_date_component - Tests build date component.
                | test_licence_component - Tests licence component.
                | test_logo_component - Tests logo component.
                | test_name_component - Tests name component.
                | test_organization_component - Tests organization component.
                | test_repository_component - Tests repository component.
                | test_use_github_component - Tests use GitHub component.
                | test_version_component - Tests version component.
                | test_info_ok_component - Tests info ok component.
    '''

    def test_build_date_component(self) -> None:
        '''
            Tests build date component.

            :exceptions: None.
        '''
        component = BuildDate()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.build_date)
        component.build_date = 'Sun 25 Apr 2021 08:12:40 PM CEST'
        self.assertTrue(component.not_none())
        self.assertEqual(component.build_date, 'Sun 25 Apr 2021 08:12:40 PM CEST')
        self.assertIsInstance(str(component), str)

    def test_licence_component(self) -> None:
        '''
            Tests licence component.

            :exceptions: None.
        '''
        component = Licence()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.licence)
        component.licence = 'GPLv3'
        self.assertTrue(component.not_none())
        self.assertEqual(component.licence, 'GPLv3')
        self.assertIsInstance(str(component), str)

    def test_logo_component(self) -> None:
        '''
            Tests logo component.

            :exceptions: None.
        '''
        component = Logo()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.logo_path)
        component.logo_path = '/path/to/logo.png'
        self.assertTrue(component.not_none())
        self.assertEqual(component.logo_path, '/path/to/logo.png')
        self.assertIsInstance(str(component), str)

    def test_name_component(self) -> None:
        '''
            Tests name component.

            :exceptions: None.
        '''
        component = Name()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.name)
        component.name = 'Simple Tool'
        self.assertTrue(component.not_none())
        self.assertEqual(component.name, 'Simple Tool')
        self.assertIsInstance(str(component), str)

    def test_organization_component(self) -> None:
        '''
            Tests organization component.

            :exceptions: None.
        '''
        component = Organization()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.organization)
        component.organization = 'my-org'
        self.assertTrue(component.not_none())
        self.assertEqual(component.organization, 'my-org')
        self.assertIsInstance(str(component), str)

    def test_repository_component(self) -> None:
        '''
            Tests repository component.

            :exceptions: None.
        '''
        component = Repository()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.repository)
        component.repository = 'my-repo'
        self.assertTrue(component.not_none())
        self.assertEqual(component.repository, 'my-repo')
        self.assertIsInstance(str(component), str)

    def test_use_github_component(self) -> None:
        '''
            Tests use GitHub component.

            :exceptions: None.
        '''
        component = UseGitHub()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.use_github)
        component.use_github = True
        self.assertTrue(component.not_none())
        self.assertEqual(component.use_github, True)
        self.assertIsInstance(str(component), str)

    def test_version_component(self) -> None:
        '''
            Tests version component.

            :exceptions: None.
        '''
        component = Version()
        self.assertFalse(component.not_none())
        self.assertIsNone(component.version)
        component.version = '1.0.0'
        self.assertTrue(component.not_none())
        self.assertEqual(component.version, '1.0.0')
        self.assertIsInstance(str(component), str)

    def test_info_ok_component(self) -> None:
        '''
            Tests info ok component.

            :exceptions: None.
        '''
        component = InfoOk()
        self.assertFalse(component.info_ok)
        component.info_ok = True
        self.assertTrue(component.info_ok)
        self.assertIsInstance(str(component), str)


if __name__ == '__main__':
    main()
