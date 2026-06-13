# -*- coding: UTF-8 -*-

'''
Module
    xml_processor.py
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
    Defines class ATSXmlProcessor with attribute(s) and method(s).
    Default implementation for processing XML content.
'''

import xml.etree.ElementTree as ET
from typing import Dict, List
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSXmlProcessor(IXMLProcessor):
    '''
        Defines class ATSXmlProcessor with attribute(s) and method(s).
        Default implementation for processing XML content.

        It defines:

            :attributes:
                | __root - Root element of the XML document.
            :methods:
                | __init__ - Initials ATSXmlProcessor constructor.
                | from_string - Load XML content from string.
                | to_string - Convert XML content to string.
                | get_ats_info - Get ATS information from XML.
    '''

    def __init__(self):
        '''
            Initials ATSXmlProcessor constructor.
        '''
        self.__root = None

    def from_string(self, xml_content: str) -> bool:
        '''
            Load XML content from string.

            :param xml_content: XML content as string
            :type xml_content: <str>
            :return: True (content loaded) | False
            :rtype: <bool>
            :exceptions: None
        '''
        self.__root = ET.fromstring(xml_content)

        return True

    def to_string(self) -> str:
        '''
            Convert XML content to string.

            :return: XML content as string
            :rtype: <str>
            :exceptions: None
        '''
        if self.__root is not None:
            return ET.tostring(self.__root, encoding='utf-8').decode('utf-8')

        return ""

    def get_ats_info(self) -> Dict[str, str]:
        '''
            Get ATS information from XML.

            :return: Dictionary with ATS information
            :rtype: <Dict[str, str]>
            :exceptions: None
        '''
        if self.__root is None:
            return {}

        ats_info: Dict[str, str] = {
            'ats_name': self.__get_val('ats_name'),
            'ats_version': self.__get_val('ats_version'),
            'ats_build_date': self.__get_val('ats_build_date'),
            'ats_licence': self.__get_val('ats_licence')
        }

        return ats_info

    def __get_val(self, tag: str) -> str:
        '''
            Internal helper for getting tag value.

            :param tag: XML tag name
            :type tag: <str>
            :return: Tag value or empty string
            :rtype: <str>
        '''
        if self.__root is None:
            return ""

        node = self.__root.find(tag)

        if node is None:
            return ""

        return node.text if node.text is not None else ""
