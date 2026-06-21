# -*- coding: UTF-8 -*-

'''
Module
    ats_object2ini_test.py
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
    Defines classes Object2IniTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Object2Ini.
Execute
    python3 -m unittest -v ats_object2ini_test
'''

from typing import Any
from unittest import TestCase, main, mock
from os.path import dirname
from ats_utilities.config_io.ini.ini2object import Ini2Object
from ats_utilities.config_io.ini.object2ini import Object2Ini
from ats_utilities.config_io.ini.iini_processor import IINIProcessor as BaseIINIProcessor
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IINIProcessor(BaseIINIProcessor):
    '''Mock implementation of IINIProcessor for testing.'''

    def __init__(self, is_empty: bool = False) -> None:
        self._is_empty = is_empty
        self.to_stream_mock = mock.MagicMock(return_value=True)
        self.to_dict_mock = mock.MagicMock(return_value={})
        self.from_stream_mock = mock.MagicMock()
        self.get_ats_info_mock = mock.MagicMock(return_value={})

    def __bool__(self) -> bool:
        '''Mock method for truthiness.'''
        return not self._is_empty

    def from_stream(self, stream: Any) -> bool:
        '''Implementation of abstract method.'''
        return self.from_stream_mock(stream)

    def to_dict(self) -> dict[str, str]:
        '''Implementation of abstract method.'''
        return self.to_dict_mock()

    def to_stream(self, stream: Any) -> bool:
        '''Implementation of abstract method.'''
        return self.to_stream_mock(stream)

    def get_ats_info(self) -> dict[str, str]:
        '''Implementation of abstract method.'''
        return self.get_ats_info_mock()

    def __str__(self) -> str:
        '''Implementation of abstract method.'''
        return ""



class Object2IniTestCase(TestCase):
    '''
        Defines class Object2IniTestCase with attribute(s) and method(s).
        Creates test cases for checking Object2Ini interfaces.
        Object2Ini unit tests.

        It defines:

            :attributes:
                | obj2ini - API for checking base Object2Ini.
                | ini2obj - API for checking base Ini2Object.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Object2Ini not None.
                | test_read_configuration - Test for read configuration.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ini2obj: Ini2Object = Ini2Object(
            f'{dirname(__file__)}/config/ats_cli_ini_api.ini'
        )
        self.obj2ini: Object2Ini = Object2Ini(
            f'{dirname(__file__)}/config/ats_cli_ini_api.ini'
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Object2Ini'''
        self.assertIsNotNone(self.obj2ini)

    def test_write_configuration(self) -> None:
        '''Test for read configuration'''
        mock_config = IINIProcessor()
        mock_config.to_stream_mock.return_value = True
        self.assertTrue(self.obj2ini.write_configuration(mock_config))

    def test_write_none_configuration(self) -> None:
        '''Test for read configuration'''
        self.assertFalse(self.obj2ini.write_configuration(None))  # type: ignore

    def test_write_empty_configuration(self) -> None:
        '''Test for read configuration'''
        mock_config = IINIProcessor(is_empty=True)
        self.assertFalse(self.obj2ini.write_configuration(mock_config))

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        writer = Object2Ini(None)
        mock_config = IINIProcessor()
        self.assertFalse(writer.write_configuration(mock_config))


if __name__ == '__main__':
    main()

