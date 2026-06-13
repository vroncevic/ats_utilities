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
    Defines interface IXMLProcessor with attribute(s) and method(s).
    Interface for processing XML content.
'''

from abc import ABC, abstractmethod
from typing import List, Dict

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IXMLProcessor(ABC):
    '''
        Defines interface IXMLProcessor with attribute(s) and method(s).
        Interface for processing XML content.

        It defines:

            :attributes: None
            :methods:
                | from_string - Load XML content from string (abstract).
                | to_string - Convert XML content to string (abstract).
                | get_ats_info - Get ATS information from XML (abstract).
    '''

    @abstractmethod
    def from_string(self, xml_content: str) -> bool:
        '''
            Load XML content from string.

            :param xml_content: XML content as string
            :type xml_content: <str>
            :return: True (content loaded) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method from_string() must be implemented.")

    @abstractmethod
    def to_string(self) -> str:
        '''
            Convert XML content to string.

            :return: XML content as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method to_string() must be implemented.")

    @abstractmethod
    def get_ats_info(self) -> Dict[str, str]:
        '''
            Get ATS information from XML.

            :return: Dictionary with ATS information
            :rtype: <Dict[str, str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method get_ats_info() must be implemented.")
