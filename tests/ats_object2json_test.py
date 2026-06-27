# -*- coding: UTF-8 -*-

'''
Module
    ats_object2json_test.py
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
    Defines classes Object2JsonTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Object2Json.
Execute
    python3 -m unittest -v ats_object2json_test
'''

from unittest import TestCase, main, mock
from os.path import dirname
from ats_utilities.config_io.json.json2object import Json2Object
from ats_utilities.config_io.json.object2json import Object2Json
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor as BaseIJSONProcessor
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IJSONProcessor(BaseIJSONProcessor):
    '''Mock implementation of IJSONProcessor for testing.'''

    def __init__(self, is_empty: bool = False) -> None:
        self._is_empty = is_empty
        self.encode_mock = mock.MagicMock(return_value="")
        self.to_dict_mock = mock.MagicMock(return_value={})
        self.decode_mock = mock.MagicMock()
        self.from_string_mock = mock.MagicMock()


    def __bool__(self) -> bool:
        '''Mock method for truthiness.'''
        return not self._is_empty

    def decode(self, json_string: str) -> bool:
        '''Implementation of abstract method.'''
        return self.decode_mock(json_string)

    def to_dict(self) -> dict[str, str]:
        '''Implementation of abstract method.'''
        return self.to_dict_mock()

    def encode(self) -> str:
        '''Implementation of abstract method.'''
        return self.encode_mock()

    def __str__(self) -> str:
        '''Implementation of abstract method.'''
        return ""



class Object2JsonTestCase(TestCase):
    '''
        Defines class Object2JsonTestCase with attribute(s) and method(s).
        Creates test cases for checking Object2Json interfaces.
        Object2Json unit tests.

        It defines:

            :attributes:
                | obj2json - API for checking base Object2Json.
                | json2obj - API for checking base Json2Object.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Object2Json not None.
                | test_read_configuration - Test for read configuration.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.json2obj: Json2Object = Json2Object(
            f'{dirname(__file__)}/config/ats_cli_json_api.json'
        )
        self.obj2json: Object2Json = Object2Json(
            f'{dirname(__file__)}/config/ats_cli_json_api.json'
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Object2Json'''
        self.assertIsNotNone(self.obj2json)

    def test_write_configuration(self) -> None:
        '''Test for write configuration'''
        mock_config = IJSONProcessor()
        mock_config.encode_mock.return_value = "{}"
        self.assertTrue(self.obj2json.write_configuration(mock_config))

    def test_write_none_configuration(self) -> None:
        '''Test for write none configuration'''
        self.assertFalse(self.obj2json.write_configuration(None))  # type: ignore

    def test_write_empty_configuration(self) -> None:
        '''Test for write empty configuration'''
        mock_config = IJSONProcessor(is_empty=True)
        self.assertFalse(self.obj2json.write_configuration(mock_config))

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        writer = Object2Json(None)
        mock_config = IJSONProcessor()
        self.assertFalse(writer.write_configuration(mock_config))


if __name__ == '__main__':
    main()

