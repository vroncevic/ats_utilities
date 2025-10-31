# -*- coding: UTF-8 -*-

'''
Module
    ats_object2xml_test.py
Copyright
    Copyright (C) 2017 - 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
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

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname

try:
    from bs4 import BeautifulSoup
    from ats_utilities.config_io.xml.xml2object import Xml2Object
    from ats_utilities.config_io.xml.object2xml import Object2Xml
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2025, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


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
        xlm2obj: Xml2Object = Xml2Object(
            f'{dirname(__file__)}/config/ats_cli_xml_api.xml'
        )
        obj2xml: Object2Xml = Object2Xml(
            f'{dirname(__file__)}/config/ats_cli_xml_api.xml'
        )
        configuration: BeautifulSoup | None = xlm2obj.read_configuration()
        self.assertTrue(obj2xml.write_configuration(configuration))

    def test_write_none_configuration(self) -> None:
        '''Test for write none configuration'''
        obj2xml: Object2Xml = Object2Xml(
            f'{dirname(__file__)}/config/ats_cli_xml_api_none.xml'
        )
        with self.assertRaises(ATSTypeError):
            obj2xml.write_configuration(None)  # type: ignore

    def test_write_empty_configuration(self) -> None:
        '''Test for write empty configuration'''
        obj2xml: Object2Xml = Object2Xml(
            f'{dirname(__file__)}/config/ats_cli_xml_api_empty.xml'
        )
        self.assertFalse(obj2xml.write_configuration(BeautifulSoup()))

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            Object2Xml(None)


if __name__ == '__main__':
    main()
