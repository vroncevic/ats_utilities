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
    Creates test cases for checking functionalities of XMLStorer.
Execute
    python3 -m unittest -v ats_xml_storer_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.config_io.xml.xml_storer import XMLStorer
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.config_io.xml.object2xml import Object2Xml
from ats_utilities.config_io.xml.xml_processor import XMLProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class XMLStorerTestCase(TestCase):
    '''
        Defines class XMLStorerTestCase with attribute(s) and method(s).
        Creates test cases for checking XMLStorer interfaces.
        XMLStorer unit tests.

        It defines:

            :methods:
                | test_not_none - Test is XMLStorer not None.
                | test_store_configuration_success - Test storing configuration successfully.
                | test_store_configuration_from_string_fail - Test storing configuration when from_string fails.
                | test_str - Test string representation of XMLStorer.
    '''

    def test_not_none(self) -> None:
        '''Test is XMLStorer not None.'''
        storer = XMLStorer(info_file='dummy.xml')
        self.assertIsNotNone(storer)

    def test_store_configuration_success(self) -> None:
        '''Test storing configuration successfully.'''
        mock_obj2xml = MagicMock(spec=Object2Xml)
        mock_processor = MagicMock(spec=XMLProcessor)
        
        mock_processor.from_string.return_value = True
        mock_obj2xml.write_configuration.return_value = True
        
        storer = XMLStorer(
            info_file='dummy.xml',
            object2xml=mock_obj2xml,
            xml_processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertTrue(result)
        mock_processor.from_string.assert_called_once()
        mock_obj2xml.write_configuration.assert_called_once_with(mock_processor)

    def test_store_configuration_from_string_fail(self) -> None:
        '''Test storing configuration when from_string fails.'''
        mock_obj2xml = MagicMock(spec=Object2Xml)
        mock_processor = MagicMock(spec=XMLProcessor)
        
        mock_processor.from_string.return_value = False
        
        storer = XMLStorer(
            info_file='dummy.xml',
            object2xml=mock_obj2xml,
            xml_processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertFalse(result)
        mock_processor.from_string.assert_called_once()
        mock_obj2xml.write_configuration.assert_not_called()

    def test_str(self) -> None:
        '''Test string representation of XMLStorer.'''
        storer = XMLStorer(info_file='dummy.xml')
        self.assertIsInstance(str(storer), str)

    def test_store_configuration_serialize_fail(self) -> None:
        '''Test storing configuration when XML serialization fails.'''
        mock_obj2xml = MagicMock(spec=Object2Xml)
        mock_processor = MagicMock(spec=XMLProcessor)
        storer = XMLStorer(
            info_file='dummy.xml',
            object2xml=mock_obj2xml,
            xml_processor=mock_processor
        )
        config = {123: 'value'}
        result = storer.store_configuration(config)
        self.assertFalse(result)


if __name__ == '__main__':
    main()

