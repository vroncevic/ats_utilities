# -*- coding: UTF-8 -*-

'''
Module
    ats_info_engine_test.py
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
    Defines classes InfoEngineTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of InfoManager.
Execute
    python3 -m unittest -v tests/info/ats_info_engine_test.py
'''

from __future__ import annotations

from unittest import TestCase, main, mock
from typing import Any

from ats_utilities.info.imanager import IInfoManager
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class InfoEngineTestCase(TestCase):
    '''
        Defines class InfoEngineTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of InfoManager.
        InfoManager unit tests.

        It defines:

            :attributes:
                | base_info - Dict with base info.
                | manager - InfoManager for base info.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_is_not_none - Test that the instance is not None.
                | test_instance_is_not_initialized - Test that the instance is not initialized.
                | test_info_properties_default_values - Test info properties default values.
                | test_set_info_set_and_get_info - Test set_info and get_info methods.
                | test_create_with_wrong_argument - Test wrong argument type.
                | test_create_with_wrong_arguments - Test wrong argument types.
                | test_initialization_failure - Test info manager initialization failure.
                | test_initialization_unexpected_exception - Test info manager initialization unexpected exception.
                | test_to_str - Test string representation of InfoManager.
                | test_getattr_invalid_attribute - Test getattr with an invalid attribute raises AttributeError.
                | test_get_shared_context - Test get_shared_context returns ContextBundle.
                | test_info_set_valid_values - Test setting valid values on InfoManager.
                | test_info_missing_keys_failure - Test InfoManager.set_info raises ATSValueError when key is missing.
                | test_info_use_github_infrastructure_bool - Test InfoManager.set_info when ats_use_github_infrastructure is already a boolean.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.base_info: dict[str, Any] = {
            InfoKeys.ATS_NAME: 'Simple Tool',
            InfoKeys.ATS_VERSION: '1.0.0',
            InfoKeys.ATS_LICENCE: 'GPLv3',
            InfoKeys.ATS_BUILD_DATE: 'Sun 25 Apr 2021 08:12:40 PM CEST',
            InfoKeys.ATS_REPOSITORY: 'my-repo',
            InfoKeys.ATS_ORGANIZATION: 'my-org',
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False,
            InfoKeys.ATS_LOGO_PATH: '/path/to/logo.png'
        }
        self.manager: IInfoManager = InfoManager()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.manager
        del self.base_info

    def test_instance_is_not_none(self) -> None:
        '''Test that the instance is not None.'''
        self.assertIsNotNone(self.manager)
        self.assertIsInstance(self.manager, IInfoManager)

    def test_instance_is_not_initialized(self) -> None:
        '''Test that the instance is not initialized.'''
        self.assertFalse(self.manager.is_initialized())

    def test_info_properties_default_values(self) -> None:
        '''Test info properties default values.'''
        self.assertIsNone(self.manager.name)
        self.assertIsNone(self.manager.version)
        self.assertIsNone(self.manager.licence)
        self.assertIsNone(self.manager.build_date)
        self.assertIsNone(self.manager.repository)
        self.assertIsNone(self.manager.organization)
        self.assertFalse(self.manager.use_github)
        self.assertIsNone(self.manager.logo)

    def test_set_info_set_and_get_info(self) -> None:
        '''Test set_info and get_info methods.'''
        self.manager.set_info(self.base_info)
        self.assertIsNotNone(self.manager.get_info())
        self.assertEqual(self.manager.get_info(), self.base_info)
        self.assertTrue(self.manager.is_initialized())

    def test_create_with_wrong_argument(self) -> None:
        '''Test wrong argument type.'''
        invalid_manager = InfoManager("wrong")
        self.assertFalse(invalid_manager.is_initialized())

    def test_create_with_wrong_arguments(self) -> None:
        '''Test wrong argument types.'''
        manager = InfoManager()
        with self.assertRaises(ATSValueError):
            manager.set_info({
                InfoKeys.ATS_NAME: None,
                InfoKeys.ATS_VERSION: None,
                InfoKeys.ATS_LICENCE: None,
                InfoKeys.ATS_BUILD_DATE: None
            })

    @mock.patch('ats_utilities.info.component_bundle.validate_component')
    def test_initialization_failure(self, mock_validate_component) -> None:
        '''Test info manager initialization failure.'''
        mock_validate_component.side_effect = ATSTypeError('Failed to initialize component')
        invalid_manager = InfoManager()
        self.assertFalse(invalid_manager.is_initialized())

    @mock.patch('ats_utilities.info.component_bundle.validate_component')
    def test_initialization_unexpected_exception(self, mock_validate_component) -> None:
        '''Test info manager initialization unexpected exception.'''
        mock_validate_component.side_effect = Exception('Unexpected')
        invalid_manager = InfoManager()
        self.assertFalse(invalid_manager.is_initialized())

    def test_to_str(self) -> None:
        '''Test string representation of InfoManager.'''
        self.assertIsInstance(str(self.manager), str)

    def test_getattr_invalid_attribute(self) -> None:
        '''Test getattr with an invalid attribute raises AttributeError.'''
        with self.assertRaises(AttributeError):
            _ = self.manager.non_existent_attribute

    def test_get_shared_context(self) -> None:
        '''Test get_shared_context returns ContextBundle.'''
        from ats_utilities.context_bundle import ContextBundle
        context = self.manager.get_shared_context()
        self.assertIsInstance(context, ContextBundle)

    def test_info_set_valid_values(self) -> None:
        '''Test setting valid values on InfoManager.'''
        self.manager.name = "New name"
        self.assertEqual(self.manager.name, "New name")
        self.manager.version = "2.0.0"
        self.assertEqual(self.manager.version, "2.0.0")

    def test_info_missing_keys_failure(self) -> None:
        '''Test InfoManager.set_info raises ATSValueError when key is missing.'''
        with self.assertRaises(ATSValueError):
            self.manager.set_info({'ats_name': 'Simple Tool'})

    def test_info_use_github_infrastructure_bool(self) -> None:
        '''Test InfoManager.set_info when ats_use_github_infrastructure is already a boolean.'''
        info = dict(self.base_info)
        info['ats_use_github_infrastructure'] = True
        self.manager.set_info(info)
        self.assertTrue(self.manager.use_github)

    def test_info_set_attribute_missing_component(self) -> None:
        '''Test setting attribute on InfoManager when component is None.'''
        self.manager._components.logo = None
        self.manager.logo = "New logo"
        self.assertEqual(self.manager.logo, "New logo")



if __name__ == '__main__':
    main()
