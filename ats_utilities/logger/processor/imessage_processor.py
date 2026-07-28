# -*- coding: UTF-8 -*-

'''
Module
    imessage_processor.py
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
    Defines abstract class IMessageProcessor with method(s).
    Provides an interface for processing/sanitizing log messages.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IMessageProcessor[PatternType, MessageType](Protocol):
    '''
        Defines abstract class IMessageProcessor with method(s).
        Provides an interface for processing/sanitizing log messages.

        :methods:
            | get_pattern - Gets a regex pattern for message processing.
            | set_pattern - Sets a regex pattern for message processing.
            | process - Processes a log message.
            | __str__ - Returns message processor as string representation.
    '''

    def get_pattern(self) -> PatternType:
        '''
            Gets a regex pattern for message processing.
            :return: A regex pattern for message processing.
        '''
        ...

    def set_pattern(self, pattern: PatternType) -> None:
        '''
            Sets a regex pattern for message processing.
            :param pattern: A regex pattern for message processing.
        '''
        ...

    def process(self, message: MessageType) -> MessageType:
        '''
            Processes a log message.

            :param message: A log message to process.
            :return: A processed log message.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns message processor as string representation.

            :return: Message processor as string representation.
        '''
        ...
