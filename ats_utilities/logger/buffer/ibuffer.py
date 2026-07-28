# -*- coding: UTF-8 -*-

'''
Module
    ibuffer.py
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
    Defines abstract class ILogBuffer with method(s).
    Provides an interface for log buffer during early stages of logging.
'''

from __future__ import annotations

from collections.abc import Callable
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
class ILogBuffer[MessageType, LevelType](Protocol):
    '''
        Defines abstract class ILogBuffer with method(s).
        Provides an interface for log buffer during early stages of logging.

        It defines:

            :methods:
                | add - Adds a message to the buffer.
                | flush - Flushes buffered messages to a writer.
                | clear - Clears the buffer.
                | __str__ - Returns buffer as string representation.
            
    '''

    def add(self, level: LevelType, message: MessageType) -> None:
        '''
            Adds a message to the buffer.

            :param level: Log level.
            :param message: The message to buffer.
        '''
        ...

    def flush(self, writer: Callable[[LevelType, MessageType], None]) -> None:
        '''
            Flushes buffered messages to a writer.

            :param writer: The logging method to write buffered logs.
        '''
        ...

    def clear(self) -> None:
        '''
            Clears the buffer.
        '''
        ...

    @property
    def is_enabled(self) -> bool:
        '''
            Checks if buffering is enabled.

            :return: True if buffering is enabled, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns buffer as string representation.

            :return: Buffer as string representation.
        '''
        ...
