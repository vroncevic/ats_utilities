# -*- coding: UTF-8 -*-

'''
Module
    ats_pro_config_test.py
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
    Defines classes ProConfigTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ProConfig.
Execute
    python3 -m unittest -v ats_pro_config_test
'''

from typing import Any, Dict, List
from unittest import TestCase, main
from ats_utilities.pro_config import ProConfig
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.exceptions import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseProConfig(ProConfig):
    '''Simple Class for checking ProConfig.'''

    def __init__(self, reporter: IATSReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        super().__init__()
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS pro config'])

    def is_tool_ok(self) -> bool:
        '''
            Check is pro config operational.

            :return: Is pro config operational
            :rtype: <bool>
        '''
        return bool(self.config)


class ProConfigTestCase(TestCase):
    '''
        Defines class ProConfigTestCase with attribute(s) and method(s).
        Creates test cases for checking ProConfig interfaces.
        ProConfig unit tests.

        It defines:

            :attributes:
                | ats_base_pro_config - API for checking base ProConfig.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseProConfig not None.
                | test_tool_operational - Test is tool operational.
                | test_set_config_empty - Sets empty configuration.
                | test_set_config_none - Sets None configuration.
                | test_set_config - Sets simple configuration.
                | test_get_config - Gets simple configuration.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_pro_config: ATSBaseProConfig = ATSBaseProConfig()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create ProConfig'''
        self.assertIsNotNone(self.ats_base_pro_config)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertFalse(self.ats_base_pro_config.is_tool_ok())

    def test_set_config_empty(self) -> None:
        '''Sets empty configuration'''
        empty_config: Dict[Any, Any] | None = {}
        self.ats_base_pro_config.config = empty_config
        self.assertFalse(self.ats_base_pro_config.is_tool_ok())

    def test_set_config_none(self) -> None:
        '''Sets None configuration'''
        none_config: Dict[Any, Any] | None = None
        with self.assertRaises(ATSTypeError):
            self.ats_base_pro_config.config = none_config

    def test_set_config(self) -> None:
        '''Sets simple configuration'''
        test_config: dict[str, str | bool] = {
            'simple_path': '/home/test/',
            'used': True
        }
        self.ats_base_pro_config.config = test_config
        self.assertTrue(self.ats_base_pro_config.is_tool_ok())

    def test_get_config(self) -> None:
        '''Gets simple configuration'''
        test_config: dict[str, str | bool] = {
            'simple_path': '/home/test/',
            'used': True
        }
        self.ats_base_pro_config.config = test_config
        self.assertIsNotNone(self.ats_base_pro_config.config)


if __name__ == '__main__':
    main()
