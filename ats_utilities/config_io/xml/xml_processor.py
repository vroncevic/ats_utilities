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
    Defines class XMLProcessor with attribute(s) and method(s).
    Default implementation for processing XML content.
'''

from __future__ import annotations

from typing import override
import xml.etree.ElementTree as ET

from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.factory_class import to_str

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class XMLProcessor(IXMLProcessor):
    '''
        Defines class XMLProcessor with attribute(s) and method(s).
        Default implementation for processing XML content.

        It defines:

            :attributes:
                | _NAME - Option name for ATS configuration.
                | _VERSION - Option version for ATS configuration.
                | _BUILD_DATE - Option build date for ATS configuration.
                | _LICENCE - Option licence for ATS configuration.
                | _root - Root element of the XML document.
            :methods:
                | __init__ - Initializes XMLProcessor constructor.
                | from_string - Loads XML content from string.
                | to_string - Converts XML content to string.
                | to_dict - Gets ATS information from XML.
                | _get_val - Internal helper for getting tag value.
                | __str__ - Returns the XMLProcessor as string representation.
    '''

    _NAME: str = 'ats_name'
    _VERSION: str = 'ats_version'
    _BUILD_DATE: str = 'ats_build_date'
    _LICENCE: str = 'ats_licence'

    def __init__(self) -> None:
        '''
            Initializes XMLProcessor constructor.

            :exceptions: None.
        '''
        self._root = None

    @override
    def from_string(self, xml_content: str) -> bool:
        '''
            Loads XML content from string.

            :param xml_content: XML content as string.
            :type xml_content: <str>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        self._root = ET.fromstring(xml_content)

        return True

    @override
    def to_string(self) -> str:
        '''
            Converts XML content to string.

            :return: XML content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        if self._root is not None:
            return ET.tostring(self._root, encoding='utf-8').decode('utf-8')

        return ""

    @override
    def to_dict(self) -> dict[str, str]:
        '''
            Gets ATS information from XML.

            :return: Dictionary with ATS information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        if self._root is None:
            return {}

        ats_info: dict[str, str] = {
            self._NAME: self._get_val(self._NAME),
            self._VERSION: self._get_val(self._VERSION),
            self._BUILD_DATE: self._get_val(self._BUILD_DATE),
            self._LICENCE: self._get_val(self._LICENCE)
        }

        return ats_info

    def _get_val(self, tag: str) -> str:
        '''
            Internal helper for getting tag value.

            :param tag: XML tag name.
            :type tag: <str>
            :return: Tag value or empty string.
            :rtype: <str>
            :exceptions: None.
        '''
        if self._root is None:
            return ""

        node = self._root.find(tag)

        if node is None:
            return ""

        return node.text if node.text is not None else ""

    @override
    def __str__(self) -> str:
        '''
            Returns the XMLProcessor as string representation.

            :return: The XMLProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
