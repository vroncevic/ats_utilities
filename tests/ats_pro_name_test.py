# -*- coding: UTF-8 -*-

'''
Module
    ats_pro_name_test.py
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
    Defines classes ProNameTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ProName.
Execute
    python3 -m unittest -v ats_pro_name_test
'''

import sys
from typing import List, Optional
from unittest import TestCase, main

try:
    from ats_utilities.pro_config.pro_name import ProName
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProNameTestCase(TestCase):
    '''
        Defines class ProNameTestCase with attribute(s) and method(s).
        Creates test cases for checking ProName interfaces.
        ProName unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default create.
                | test_set_pro_name_empty - Sets empty project name.
                | test_set_pro_name_none - Sets None project name.
                | test_set_pro_name - Sets simple project name.
                | test_get_pro_name - Gets simple project name.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default create'''
        pro_name: ProName = ProName()
        self.assertIsNotNone(pro_name)

    def test_set_pro_name_empty(self) -> None:
        '''Sets empty name'''
        pro_name: ProName = ProName()
        empty_name: Optional[str] = ""
        pro_name.pro_name = empty_name
        self.assertFalse(pro_name.is_pro_name_ok())

    def test_set_pro_name_none(self) -> None:
        '''Sets None name'''
        pro_name: ProName = ProName()
        none_name: Optional[str] = None
        with self.assertRaises(ATSTypeError):
            pro_name.pro_name = none_name

    def test_set_pro_name(self) -> None:
        '''Sets simple project name'''
        pro_name: ProName = ProName()
        test_name: Optional[str] = "app_example"
        pro_name.pro_name = test_name
        self.assertTrue(pro_name.is_pro_name_ok())

    def test_get_pro_name(self) -> None:
        '''Gets simple project name'''
        pro_name: ProName = ProName()
        test_name: Optional[str] = "app_example"
        pro_name.pro_name = test_name
        self.assertIsNotNone(pro_name.pro_name)


if __name__ == '__main__':
    main()
