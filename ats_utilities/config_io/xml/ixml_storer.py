# -*- coding: UTF-8 -*-

'''
Module
    ixml_storer.py
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
    Defines interface IXMLStorer with attribute(s) and method(s).
    Interface for storing the ATS configuration.
'''

from abc import ABC, abstractmethod
from typing import Dict, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IXMLStorer(ABC):
    '''
        Defines interface IXMLStorer with attribute(s) and method(s).
        Interface for storing the ATS configuration.

        It defines:

            :attributes: None
            :methods:
                | store_configuration - Stores the ATS configuration from dictionary (abstract).
                | __str__ - Returns the string representation of XML storer (abstract).
    '''

    @abstractmethod
    def store_configuration(self, config: Dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with XML information
            :type config: <Dict[str, str]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method store_configuration() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of XML storer component.

            :return: The XML storer component as string representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
