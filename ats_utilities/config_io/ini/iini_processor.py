
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
                | from_stream - Load INI content from a stream (abstract).
                | to_stream - Write INI content to a stream (abstract).
                | get_ats_info - Get ATS information from INI (abstract).
    '''

    @abstractmethod
    def from_stream(self, stream: Any) -> bool:
        '''
            Load INI content from a stream.

            :param stream: INI content stream
            :type stream: <Any>
            :return: True (content loaded) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method from_stream() must be implemented.")

    @abstractmethod
    def to_stream(self, stream: Any) -> bool:
        '''
            Write INI content to a stream.

            :param stream: INI content stream
            :type stream: <Any>
            :return: True (content written) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method to_stream() must be implemented.")

    @abstractmethod
    def get_ats_info(self) -> Dict[str, str]:
        '''
            Get ATS information from INI.

            :return: Dictionary with ATS information
            :rtype: <Dict[str, str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method get_ats_info() must be implemented.")
