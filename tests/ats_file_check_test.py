# -*- coding: UTF-8 -*-

'''
Module
    ats_file_check_test.py
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
    Defines classes FileCheckTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of FileCheck.
Execute
    python3 -m unittest -v ats_file_check_test
'''

from unittest import TestCase, main, mock
from os.path import dirname
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.exceptions import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


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


class FileCheckUnitTestCase(TestCase):
    '''
        Unit tests for IFileCheck interface using mocks.

        It defines:
            :methods:
                | setUp - Set up test environment with mocks.
                | test_mock_check_path - Test mock interaction for check_path.
                | test_mock_check_format - Test mock interaction for check_format.
                | test_mock_check_mode - Test mock interaction for check_mode.
                | test_mock_is_file_ok - Test mock interaction for is_file_ok.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.mock_file_check = mock.MagicMock(spec=IFileCheck)

    def test_mock_check_path(self) -> None:
        '''Test mock interaction for check_path.'''
        file_path = '/path/to/file.txt'
        self.mock_file_check.check_path(file_path)
        self.mock_file_check.check_path.assert_called_once_with(file_path)

    def test_mock_check_format(self) -> None:
        '''Test mock interaction for check_format.'''
        file_path = '/path/to/file.json'
        file_format = 'json'
        self.mock_file_check.check_format(file_path, file_format)
        self.mock_file_check.check_format.assert_called_once_with(file_path, file_format)

    def test_mock_check_mode(self) -> None:
        '''Test mock interaction for check_mode.'''
        mode = 'r'
        self.mock_file_check.check_mode(mode)
        self.mock_file_check.check_mode.assert_called_once_with(mode)

    def test_mock_is_file_ok(self) -> None:
        '''Test mock interaction for is_file_ok.'''
        self.mock_file_check.is_file_ok.return_value = True
        result = self.mock_file_check.is_file_ok()
        self.assertTrue(result)
        self.mock_file_check.is_file_ok.assert_called_once()

    def test_mock_is_file_not_ok(self) -> None:
        '''Test mock interaction for is_file_ok returning False.'''
        self.mock_file_check.is_file_ok.return_value = False
        result = self.mock_file_check.is_file_ok()
        self.assertFalse(result)
        self.mock_file_check.is_file_ok.assert_called_once()


if __name__ == '__main__':
    main()
