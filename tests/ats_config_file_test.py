# -*- coding: UTF-8 -*-

'''
Module
    ats_config_file_test.py
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
    Defines classes ConfigFileTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ConfFile.
Execute
    python3 -m unittest -v ats_config_file_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.config_io import ConfFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ConfigFileTestCase(TestCase):
    '''
        Defines class ConfigFileTestCase with attribute(s) and method(s).
        Creates test cases for checking ConfFile interfaces.
        ConfFile unit tests.

        It defines:

            :attributes:
                | file_path - File path for checking ConfFile.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_config_path - Test for file path.
                | test_none_file - Test for None file.
                | test_wrong_path_file - Test for wrong file path.
                | test_empty_path_file - Test for missing file path.
                | test_empty_type_file - Test for missing file format.
                | test_empty_mode_file - Test for missing file mode.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.file_path: str = f'{dirname(__file__)}/config/Makefile'

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_config_path(self) -> None:
        '''Test for file path'''
        with ConfFile(self.file_path, 'r', 'Makefile') as cfg:
            self.assertIsNotNone(cfg)

    def test_none_file(self) -> None:
        '''Test for None file'''
        with self.assertRaises(ATSTypeError):
            with ConfFile(None, 'r', 'Makefile'):
                pass

    def test_wrong_path_file(self) -> None:
        '''Test for wrong file path'''
        with ConfFile('test', 'r', 'Makefile') as cfg:
            self.assertIsNone(cfg)

    def test_empty_path_file(self) -> None:
        '''Test for missing file path'''
        with self.assertRaises(ATSValueError):
            with ConfFile('', 'r', 'Makefile') as cfg:
                self.assertIsNone(cfg)

    def test_empty_type_file(self) -> None:
        '''Test for missing file format'''
        with self.assertRaises(ATSValueError):
            with ConfFile('test', 'r', '') as cfg:
                self.assertIsNone(cfg)

    def test_empty_mode_file(self) -> None:
        '''Test for missing file mode'''
        with self.assertRaises(ATSValueError):
            with ConfFile('test', '', 'Makefile') as cfg:
                self.assertIsNone(cfg)


if __name__ == '__main__':
    main()
