# -*- coding: UTF-8 -*-

'''
Module
    ijson_processor.py
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
    Defines abstract class IJSONProcessor with method(s).
    Creates an interface for processing JSON content.
'''
from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class IJSONProcessor(ABC):
    '''
        Defines abstract class IJSONProcessor with method(s).
        Interface for processing JSON content.

        It defines:

            :attributes: None
            :methods:
                | decode - Converts raw JSON text to an internal object/structure.
                | encode - Converts an internal object/structure back to a JSON string.
                | to_dict - Converts data as a flat dictionary.
                | __str__ - Returns the JSON processor as string representation.
    '''

    @abstractmethod
    def decode(self, json_string: str) -> bool:
        '''
            Converts raw JSON text to an internal object/structure.

            :param json_string: Raw JSON text in string format
            :type json_string: <str>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def encode(self) -> str:
        '''
            Converts an internal object/structure back to a JSON string.

            :return: JSON content in string format
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        '''
            Converts data as a flat dictionary.

            :return: Dictionary with JSON configuration
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the JSON processor as string representation.

            :return: The JSON processor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
