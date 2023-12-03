# -*- coding: UTF-8 -*-

'''
Module
    ats_file_check_test.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines classes FileCheckTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of FileCheck.
Execute
    python3 -m unittest -v ats_file_check_test
'''

import sys
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.config_io import FileCheck
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FileCheckTestCase(TestCase):
    '''
        Defines class FileCheckTestCase with attribute(s) and method(s).
        Creates test cases for checking FileCheck interfaces.
        FileCheck unit tests.

        It defines:

            :attributes:
                | file_check - API for checking base FileCheck.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is FileCheck not None.
                | test_default_file_not_ok - By default file it is not ok.
                | test_file - Test for file.
                | test_none_config_path - Test for None as file path.
                | test_none_config_format - Test for None as file format.
                | test_none_config_mode - Test for None as file mode.
                | test_non_file_config_path - Test for directory as file path.
                | test_non_supported_mode - Test for non supported mode.
                | test_makefile - Test for makefile.
                | test_wrong_format - Test for wrong format.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.file_check: FileCheck = FileCheck()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create FileCheck'''
        self.assertIsNotNone(self.file_check)

    def test_default_file_not_ok(self) -> None:
        '''Test for default file it is not ok'''
        self.assertFalse(self.file_check.is_file_ok())

    def test_file(self) -> None:
        '''Test for file'''
        file_path: str = f'{dirname(__file__)}/config/ats_cli_json_api.json'
        self.file_check.check_path(file_path)
        self.file_check.check_format(file_path, 'json')
        self.file_check.check_mode('r')
        self.assertTrue(self.file_check.is_file_ok())

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            self.file_check.check_path(None)

    def test_none_config_format(self) -> None:
        '''Test for None as file format'''
        file_path: str = f'{dirname(__file__)}/config/ats_cli_json_api.json'
        with self.assertRaises(ATSTypeError):
            self.file_check.check_format(file_path, None)

    def test_none_config_mode(self) -> None:
        '''Test for None as file mode'''
        with self.assertRaises(ATSTypeError):
            self.file_check.check_mode(None)

    def test_non_file_config_path(self) -> None:
        '''Test for directory as file path'''
        self.file_check.check_path(f'{dirname(__file__)}/config/')
        self.assertFalse(self.file_check.is_file_ok())

    def test_non_supported_mode(self) -> None:
        '''Test for non supported mode'''
        file_path: str = f'{dirname(__file__)}/config/ats_cli_json_api.json'
        self.file_check.check_path(file_path)
        self.file_check.check_format(file_path, 'json')
        self.file_check.check_mode('z')
        self.assertFalse(self.file_check.is_file_ok())

    def test_makefile(self) -> None:
        '''Test for Makefile'''
        file_path: str = f'{dirname(__file__)}/config/Makefile'
        self.file_check.check_path(file_path)
        self.file_check.check_format(file_path, 'makefile')
        self.file_check.check_mode('r')
        self.assertTrue(self.file_check.is_file_ok())

    def test_wrong_format(self) -> None:
        '''Test for wrong format'''
        file_path: str = f'{dirname(__file__)}/config/test.rpt'
        self.file_check.check_path(file_path)
        self.file_check.check_format(file_path, 'txt')
        self.file_check.check_mode('r')
        self.assertFalse(self.file_check.is_file_ok())


if __name__ == '__main__':
    main()
