# -*- coding: UTF-8 -*-

'''
Module
    ixml_processor.py
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
    Defines abstract class IXMLProcessor with method(s).
    Interface for processing XML content.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IXMLProcessor(ABC):
    '''
        Defines abstract class IXMLProcessor with method(s).
        Interface for processing XML content.

        It defines:

            :methods:
                | from_string - Loads XML content from string.
                | to_string - Converts XML content to string.
                | to_dict - Gets ATS information from XML.
                | __str__ - Returns the XML processor as string representation.
    '''

    @abstractmethod
    def from_string(self, xml_content: str) -> bool:
        '''
            Loads XML content from string.

            :param xml_content: XML content as string
            :type xml_content: <str>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def to_string(self) -> str:
        '''
            Converts XML content to string.

            :return: XML content as string
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        '''
            Gets ATS information from XML.

            :return: Dictionary with ATS information
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the XML processor as string representation.

            :return: The XML processor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
