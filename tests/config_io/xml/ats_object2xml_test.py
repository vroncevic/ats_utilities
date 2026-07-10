# -*- coding: UTF-8 -*-

'''
Module
    ats_object2xml_test.py
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
    Defines classes Object2XmlTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Object2Xml.
Execute
    python3 -m unittest -v ats_object2xml_test
'''

from unittest import TestCase, main, mock
from os.path import dirname
from ats_utilities.config_io.xml.object2xml import Object2Xml
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor as BaseIXMLProcessor
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class IXMLProcessor(BaseIXMLProcessor):
    '''Mock implementation of IXMLProcessor for testing.'''

    def __init__(self, is_empty: bool = False) -> None:
        self._is_empty = is_empty
        self.to_string_mock = mock.MagicMock(return_value="")
        self.to_dict_mock = mock.MagicMock(return_value={})
        self.from_string_mock = mock.MagicMock()
        self.get_ats_info_mock = mock.MagicMock(return_value={})

    def __bool__(self) -> bool:
        '''Mock method for truthiness.'''
        return not self._is_empty

    def from_string(self, xml_content: str) -> bool:
        return self.from_string_mock(xml_content)

    def to_dict(self) -> dict[str, str]:
        '''Implementation of abstract method.'''
        return self.to_dict_mock()

    def to_string(self) -> str:
        '''Implementation of abstract method.'''
        return self.to_string_mock()

    def get_ats_info(self) -> dict[str, str]:
        '''Implementation of abstract method.'''
        return self.get_ats_info_mock()

    def __str__(self) -> str:
        '''Implementation of abstract method.'''
        return ""


class Object2XmlTestCase(TestCase):
    '''
        Defines class Object2XmlTestCase with attribute(s) and method(s).
        Creates test cases for checking Object2Xml interfaces.
        Object2Xml unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Object2Xml not None.
                | test_write_configuration - Test for write configuration.
                | test_write_none_configuration - Write none configuration.
                | test_write_empty_configuration - Write empty configuration.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Object2Xml'''
        obj2xml: Object2Xml = Object2Xml(
            f'{dirname(__file__)}/config/ats_cli_xml_api.xml'
        )
        self.assertIsNotNone(obj2xml)

    def test_write_configuration(self) -> None:
        '''Test for write configuration'''
        obj2xml: Object2Xml = Object2Xml(
            f'{dirname(__file__)}/config/ats_cli_xml_api.xml'
        )
        mock_config = IXMLProcessor()
        mock_config.to_string_mock.return_value = "<xml></xml>"
        self.assertTrue(obj2xml.write_configuration(mock_config))

    def test_write_none_configuration(self) -> None:
        '''Test for write none configuration'''
        obj2xml: Object2Xml = Object2Xml(
            f'{dirname(__file__)}/config/ats_cli_xml_api_none.xml'
        )
        self.assertFalse(obj2xml.write_configuration(None))  # type: ignore

    def test_write_empty_configuration(self) -> None:
        '''Test for write empty configuration'''
        obj2xml: Object2Xml = Object2Xml(f'{dirname(__file__)}/config/ats_cli_xml_api_empty.xml')
        mock_config = IXMLProcessor(is_empty=True)
        self.assertFalse(obj2xml.write_configuration(mock_config))

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        writer = Object2Xml(None)
        mock_config = IXMLProcessor()
        self.assertFalse(writer.write_configuration(mock_config))


if __name__ == '__main__':
    main()

