
# -*- coding: UTF-8 -*-

'''
Module
    iini_processor.py
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
    Defines abstract class IINIProcessor with attribute(s) and method(s).
    Creates an interface for processing INI content.
'''
from abc import ABC, abstractmethod
from typing import Any, Dict

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IINIProcessor(ABC):
    '''
        Defines interface IINIProcessor with attribute(s) and method(s).
        Interface for processing INI content.

        It defines:

            :attributes: None
            :methods:
                | from_stream - Loads INI configuration from a stream (abstract).
                | to_stream - Converts INI configuration to a stream (abstract).
                | to_dict - Converts INI configuration to dictionary (abstract).
                | __str__ - Returns the string representation of INI processor (abstract).
    '''

    @abstractmethod
    def from_stream(self, stream: Any) -> bool:
        '''
            Loads INI configuration from a stream.

            :param stream: INI content stream
            :type stream: <Any>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method from_stream() must be implemented.")

    @abstractmethod
    def to_stream(self, stream: Any) -> bool:
        '''
            Converts INI configuration to a stream.

            :param stream: INI content stream
            :type stream: <Any>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method to_stream() must be implemented.")

    @abstractmethod
    def to_dict(self) -> Dict[str, str]:
        '''
            Converts INI configuration to dictionary.

            :return: Dictionary with ATS information
            :rtype: <Dict[str, str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method to_dict() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of INI processor.

            :return: INI processor as string representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
