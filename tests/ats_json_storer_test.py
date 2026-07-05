# -*- coding: UTF-8 -*-

'''
Module
    ats_json_storer_test.py
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
    Defines class JSONStorerTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of JSONStorer.
Execute
    python3 -m unittest -v ats_json_storer_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.config_io.json.json_storer import JSONStorer
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor
from ats_utilities.config_io.json.object2json import Object2Json
from ats_utilities.config_io.json.json_processor import JSONProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class JSONStorerTestCase(TestCase):
    '''
        Defines class JSONStorerTestCase with attribute(s) and method(s).
        Creates test cases for checking JSONStorer interfaces.
        JSONStorer unit tests.

        It defines:

            :methods:
                | test_not_none - Test is JSONStorer not None.
                | test_store_configuration_success - Test storing configuration successfully.
                | test_store_configuration_decode_fail - Test storing configuration when decode fails.
                | test_str - Test string representation of JSONStorer.
    '''

    def test_not_none(self) -> None:
        '''Test is JSONStorer not None.'''
        storer = JSONStorer(info_file='dummy.json')
        self.assertIsNotNone(storer)

    def test_store_configuration_success(self) -> None:
        '''Test storing configuration successfully.'''
        mock_obj2json = MagicMock(spec=Object2Json)
        mock_processor = MagicMock(spec=JSONProcessor)
        
        mock_processor.decode.return_value = True
        mock_obj2json.write_configuration.return_value = True
        
        storer = JSONStorer(
            info_file='dummy.json',
            object2json=mock_obj2json,
            json_processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertTrue(result)
        mock_processor.decode.assert_called_once()
        mock_obj2json.write_configuration.assert_called_once_with(mock_processor)

    def test_store_configuration_decode_fail(self) -> None:
        '''Test storing configuration when decode fails.'''
        mock_obj2json = MagicMock(spec=Object2Json)
        mock_processor = MagicMock(spec=JSONProcessor)
        
        mock_processor.decode.return_value = False
        
        storer = JSONStorer(
            info_file='dummy.json',
            object2json=mock_obj2json,
            json_processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertFalse(result)
        mock_processor.decode.assert_called_once()
        mock_obj2json.write_configuration.assert_not_called()

    def test_str(self) -> None:
        '''Test string representation of JSONStorer.'''
        storer = JSONStorer(info_file='dummy.json')
        self.assertIsInstance(str(storer), str)

    def test_store_configuration_serialize_fail(self) -> None:
        '''Test storing configuration when JSON serialization fails.'''
        mock_obj2json = MagicMock(spec=Object2Json)
        mock_processor = MagicMock(spec=JSONProcessor)
        storer = JSONStorer(
            info_file='dummy.json',
            object2json=mock_obj2json,
            json_processor=mock_processor
        )
        config = {'key': {1, 2, 3}}
        result = storer.store_configuration(config)
        self.assertFalse(result)


if __name__ == '__main__':
    main()

