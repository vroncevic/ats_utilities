# -*- coding: UTF-8 -*-

'''
Module
    ats_pro_config_test.py
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
    Defines classes ProConfigTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ProConfig.
Execute
    python3 -m unittest -v ats_pro_config_test
'''

import sys
from typing import Any, List, Dict
from unittest import TestCase, main

try:
    from ats_utilities.pro_config import ProConfig
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProConfigTestCase(TestCase):
    '''
        Defines class ProConfigTestCase with attribute(s) and method(s).
        Creates test cases for checking ProConfig interfaces.
        ProConfig unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default create.
                | test_set_config_empty - Sets empty configuration.
                | test_set_config_none - Sets None configuration.
                | test_set_config - Sets simple configuration.
                | test_get_config - Gets simple configuration.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default create'''
        pro_config: ProConfig = ProConfig()
        self.assertIsNotNone(pro_config)

    def test_set_config_empty(self) -> None:
        '''Sets empty configuration'''
        pro_config: ProConfig = ProConfig()
        empty_config: Dict[Any, Any] | None = {}
        pro_config.config = empty_config
        self.assertFalse(pro_config.is_config_ok())

    def test_set_config_none(self) -> None:
        '''Sets None configuration'''
        pro_config: ProConfig = ProConfig()
        none_config: Dict[Any, Any] | None = None
        with self.assertRaises(ATSTypeError):
            pro_config.config = none_config

    def test_set_config(self) -> None:
        '''Sets simple configuration'''
        pro_config: ProConfig = ProConfig()
        test_config: dict[str, str | bool] = {
            'simple_path': '/home/test/',
            'used': True
        }
        pro_config.config = test_config
        self.assertTrue(pro_config.is_config_ok())

    def test_get_config(self) -> None:
        '''Gets simple configuration'''
        pro_config: ProConfig = ProConfig()
        test_config: dict[str, str | bool] = {
            'simple_path': '/home/test/',
            'used': True
        }
        pro_config.config = test_config
        self.assertIsNotNone(pro_config.config)


if __name__ == '__main__':
    main()
