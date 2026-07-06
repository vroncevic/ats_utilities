# -*- coding: UTF-8 -*-

'''
Module
    ats_config_file_test.py
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
    Defines classes ConfigFileTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ConfFile.
Execute
    python3 -m unittest -v ats_config_file_test
'''

from unittest import TestCase, main
from os.path import dirname
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.file_bundle import FileBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


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
                | test_str - Test string representation of ConfFile.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.file_path: str = f'{dirname(__file__)}/config/Makefile'

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_config_path(self) -> None:
        '''Test for file path'''
        bundle = FileBundle(file_path=self.file_path, file_mode='r', file_format='Makefile')
        with ConfFile(bundle) as cfg:
            self.assertIsNotNone(cfg)

    def test_str(self) -> None:
        '''Test string representation of ConfFile.'''
        bundle = FileBundle(file_path=self.file_path, file_mode='r', file_format='Makefile')
        cfg = ConfFile(bundle)
        self.assertIsInstance(str(cfg), str)

    def test_none_file(self) -> None:
        '''Test for None file'''
        with self.assertRaises(ATSValueError):
            bundle = FileBundle(file_path=None, file_mode='r', file_format='Makefile')
            with ConfFile(bundle):
                pass

    def test_wrong_path_file(self) -> None:
        '''Test for wrong file path'''
        bundle = FileBundle(file_path='test', file_mode='r', file_format='Makefile')
        with ConfFile(bundle) as cfg:
            self.assertIsNone(cfg)

    def test_empty_path_file(self) -> None:
        '''Test for missing file path'''
        with self.assertRaises(ATSValueError):
            bundle = FileBundle(file_path='', file_mode='r', file_format='Makefile')
            with ConfFile(bundle):
                pass

    def test_empty_type_file(self) -> None:
        '''Test for missing file format'''
        with self.assertRaises(ATSValueError):
            bundle = FileBundle(file_path='test', file_mode='r', file_format='')
            with ConfFile(bundle):
                pass

    def test_empty_mode_file(self) -> None:
        '''Test for missing file mode'''
        with self.assertRaises(ATSValueError):
            bundle = FileBundle(file_path='test', file_mode='', file_format='Makefile')
            with ConfFile(bundle):
                pass


if __name__ == '__main__':
    main()
