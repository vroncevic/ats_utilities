# -*- coding: UTF-8 -*-

'''
Module
    ats_object2cfg_test.py
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
    Defines classes Object2CfgTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Object2Cfg.
Execute
    python3 -m unittest -v ats_object2cfg_test
'''

from typing import List, Dict
from unittest import TestCase, main, mock
from os.path import dirname
from ats_utilities.config_io.cfg import Object2Cfg
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor as BaseICFGProcessor
from ats_utilities.exceptions import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ICFGProcessor(BaseICFGProcessor):
    '''Mock implementation of ICFGProcessor for testing.'''

    def __init__(self, is_empty: bool = False) -> None:
        self.__is_empty = is_empty
        self.to_string_mock = mock.MagicMock(return_value="")
        self.to_dict_mock = mock.MagicMock(return_value={})
        self.from_lines_mock = mock.MagicMock()

    def __bool__(self) -> bool:
        '''Mock method for truthiness.'''
        return not self.__is_empty

    def from_lines(self, lines: List[str]) -> bool:
        '''Implementation of abstract method.'''
        return self.from_lines_mock(lines)

    def to_dict(self) -> Dict[str, str]:
        '''Implementation of abstract method.'''
        return self.to_dict_mock()

    def to_string(self) -> str:
        '''Implementation of abstract method.'''
        return self.to_string_mock()


class Object2CfgTestCase(TestCase):
    '''
        Defines class Object2CfgTestCase with attribute(s) and method(s).
        Creates test cases for checking Object2Cfg interfaces.
        Object2Cfg unit tests.

        It defines:

            :attributes:
                | obj2cfg - API for checking base Object2Cfg.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Object2Cfg not None.
                | test_read_configuration - Test for read configuration.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.obj2cfg: Object2Cfg = Object2Cfg(
            f'{dirname(__file__)}/config/ats_cli_cfg_api.cfg'
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Object2Cfg'''
        self.assertIsNotNone(self.obj2cfg)

    def test_write_configuration(self) -> None:
        '''Test for read configuration'''
        mock_config = ICFGProcessor()
        mock_config.to_string_mock.return_value = "ats_name = test"
        self.assertTrue(self.obj2cfg.write_configuration(mock_config))

    def test_write_none_configuration(self) -> None:
        '''Test for read configuration'''
        with self.assertRaises(ATSTypeError):
            self.obj2cfg.write_configuration(None)  # type: ignore

    def test_write_empty_configuration(self) -> None:
        '''Test for read configuration'''
        mock_config = ICFGProcessor(is_empty=True)
        self.assertFalse(self.obj2cfg.write_configuration(mock_config))

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            Object2Cfg(None)


if __name__ == '__main__':
    main()
