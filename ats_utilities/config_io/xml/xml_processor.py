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
    Defines class ATSXMLProcessor with attribute(s) and method(s).
    Default implementation for processing XML content.
'''

import xml.etree.ElementTree as ET
from typing import Dict, List
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSXMLProcessor(IXMLProcessor):
    '''
        Defines class ATSXMLProcessor with attribute(s) and method(s).
        Default implementation for processing XML content.

        It defines:

            :attributes:
                | __NAME - Option name for ATS configuration.
                | __VERSION - Option version for ATS configuration.
                | __BUILD_DATE - Option build date for ATS configuration.
                | __LICENCE - Option licence for ATS configuration.
                | __root - Root element of the XML document.
            :methods:
                | __init__ - Initializes ATSXMLProcessor constructor.
                | from_string - Loads XML content from string.
                | to_string - Converts XML content to string.
                | to_dict - Gets ATS information from XML.
                | __get_val - Internal helper for getting tag value.
                | __str__ - Returns the ATSXMLProcessor as string representation.
    '''

    __NAME: str = 'ats_name'
    __VERSION: str = 'ats_version'
    __BUILD_DATE: str = 'ats_build_date'
    __LICENCE: str = 'ats_licence'

    def __init__(self) -> None:
        '''
            Initializes ATSXMLProcessor constructor.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        self.__root = None

    def from_string(self, xml_content: str) -> bool:
        '''
            Loads XML content from string.

            :param xml_content: XML content as string.
            :type xml_content: <str>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        self.__root = ET.fromstring(xml_content)

        return True

    def to_string(self) -> str:
        '''
            Converts XML content to string.

            :return: XML content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        if self.__root is not None:
            return ET.tostring(self.__root, encoding='utf-8').decode('utf-8')

        return ""

    def to_dict(self) -> Dict[str, str]:
        '''
            Gets ATS information from XML.

            :return: Dictionary with ATS information.
            :rtype: <Dict[str, str]>
            :exceptions: None.
        '''
        if self.__root is None:
            return {}

        ats_info: Dict[str, str] = {
            self.__NAME: self.__get_val(self.__NAME),
            self.__VERSION: self.__get_val(self.__VERSION),
            self.__BUILD_DATE: self.__get_val(self.__BUILD_DATE),
            self.__LICENCE: self.__get_val(self.__LICENCE)
        }

        return ats_info

    def __get_val(self, tag: str) -> str:
        '''
            Internal helper for getting tag value.

            :param tag: XML tag name.
            :type tag: <str>
            :return: Tag value or empty string.
            :rtype: <str>
            :exceptions: None.
        '''
        if self.__root is None:
            return ""

        node = self.__root.find(tag)

        if node is None:
            return ""

        return node.text if node.text is not None else ""

    def __str__(self) -> str:
        '''
            Returns the ATSXMLProcessor as string representation.

            :return: The ATSXMLProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
