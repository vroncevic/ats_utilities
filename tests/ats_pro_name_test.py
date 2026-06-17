# -*- coding: UTF-8 -*-

'''
Module
    ats_pro_name_test.py
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
    Defines classes ProNameTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ProName.
Execute
    python3 -m unittest -v ats_pro_name_test
'''

from typing import List, Optional
from unittest import TestCase, main
from ats_utilities.pro_config.pro_name import ProName
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseProName(ProName):
    '''Simple Class for checking ProName.'''

    def __init__(self, reporter: IReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        super().__init__()
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init project name'])

    def is_tool_ok(self) -> bool:
        '''
            Check is project name operational.

            :return: Is project name operational
            :rtype: <bool>
        '''
        return bool(self.pro_name)


class ProNameTestCase(TestCase):
    '''
        Defines class ProNameTestCase with attribute(s) and method(s).
        Creates test cases for checking ProName interfaces.
        ProName unit tests.

        It defines:

            :attributes:
                | ats_base_pro_name - API for checking base ProName.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseProName not None.
                | test_tool_operational - Test is tool operational.
                | test_set_pro_name_empty - Sets empty project name.
                | test_set_pro_name_none - Sets None project name.
                | test_set_pro_name - Sets simple project name.
                | test_get_pro_name - Gets simple project name.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_pro_name: ATSBaseProName = ATSBaseProName()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create ProName'''
        self.assertIsNotNone(self.ats_base_pro_name)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertFalse(self.ats_base_pro_name.is_tool_ok())

    def test_set_pro_name_empty(self) -> None:
        '''Sets empty name'''
        empty_name: Optional[str] = ""
        self.ats_base_pro_name.pro_name = empty_name
        self.assertFalse(self.ats_base_pro_name.is_tool_ok())

    def test_set_pro_name_none(self) -> None:
        '''Sets None name'''
        none_name: Optional[str] = None
        with self.assertRaises(ATSTypeError):
            self.ats_base_pro_name.pro_name = none_name

    def test_set_pro_name(self) -> None:
        '''Sets simple project name'''
        test_name: Optional[str] = "app_example"
        self.ats_base_pro_name.pro_name = test_name
        self.assertTrue(self.ats_base_pro_name.is_tool_ok())

    def test_get_pro_name(self) -> None:
        '''Gets simple project name'''
        test_name: Optional[str] = "app_example"
        self.ats_base_pro_name.pro_name = test_name
        self.assertIsNotNone(self.ats_base_pro_name.pro_name)


if __name__ == '__main__':
    main()
