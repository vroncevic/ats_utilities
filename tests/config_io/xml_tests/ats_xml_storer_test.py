# -*- coding: UTF-8 -*-

'''
Module
    ats_xml_storer_test.py
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
    Defines class XMLStorerTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ConfigStorer.
Execute
    python3 -m unittest -v ats_xml_storer_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.config_io.storer.config_storer import ConfigStorer
from ats_utilities.config_io.storer.iwrite import IWrite
from ats_utilities.config_io.processor.ixml_processor import IXMLProcessor
from ats_utilities.config_io.storer.object2file import Object2File
from ats_utilities.config_io.processor.xml_processor import XMLProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class XMLStorerTestCase(TestCase):
    '''
        Defines class XMLStorerTestCase with attribute(s) and method(s).
        Creates test cases for checking ConfigStorer interfaces.
        ConfigStorer unit tests.

        It defines:

            :methods:
                | test_not_none - Test is ConfigStorer not None.
                | test_store_configuration_success - Test storing configuration successfully.
                | test_store_configuration_from_string_fail - Test storing configuration when from_string fails.
                | test_str - Test string representation of ConfigStorer.
    '''

    def test_not_none(self) -> None:
        '''Test is ConfigStorer not None.'''
        storer = ConfigStorer('xml', info_file='dummy.xml')
        self.assertIsNotNone(storer)

    def test_store_configuration_success(self) -> None:
        '''Test storing configuration successfully.'''
        mock_obj2xml = MagicMock(spec=Object2File)
        mock_processor = MagicMock(spec=XMLProcessor)
        
        mock_processor.from_string.return_value = True
        mock_obj2xml.write_configuration.return_value = True
        
        storer = ConfigStorer('xml', 
            info_file='dummy.xml',
            object2file=mock_obj2xml,
            processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertTrue(result)
        mock_processor.from_string.assert_called_once()
        mock_obj2xml.write_configuration.assert_called_once_with(mock_processor)

    def test_store_configuration_from_string_fail(self) -> None:
        '''Test storing configuration when from_string fails.'''
        mock_obj2xml = MagicMock(spec=Object2File)
        mock_processor = MagicMock(spec=XMLProcessor)
        
        mock_processor.from_string.return_value = False
        
        storer = ConfigStorer('xml', 
            info_file='dummy.xml',
            object2file=mock_obj2xml,
            processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertFalse(result)
        mock_processor.from_string.assert_called_once()
        mock_obj2xml.write_configuration.assert_not_called()

    def test_str(self) -> None:
        '''Test string representation of ConfigStorer.'''
        storer = ConfigStorer('xml', info_file='dummy.xml')
        self.assertIsInstance(str(storer), str)

    def test_store_configuration_serialize_fail(self) -> None:
        '''Test storing configuration when XML serialization fails.'''
        mock_obj2xml = MagicMock(spec=Object2File)
        mock_processor = MagicMock(spec=XMLProcessor)
        storer = ConfigStorer('xml', 
            info_file='dummy.xml',
            object2file=mock_obj2xml,
            processor=mock_processor
        )
        config = {123: 'value'}
        result = storer.store_configuration(config)
        self.assertFalse(result)


if __name__ == '__main__':
    main()

