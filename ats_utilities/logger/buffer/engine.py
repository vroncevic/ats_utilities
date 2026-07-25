# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class LogBuffer for early logs with attribute(s) and method(s).
    Provides an API for early logging during initialization of logger.
'''

from __future__ import annotations

from collections.abc import Callable
from typing import override

from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.utils.reflection import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LogBuffer(ILogBuffer):
    '''
        Defines class LogBuffer for early logs with attribute(s) and method(s).
        Provides an API for early logging during initialization of logger.

        It defines:

            :attributes:
                | _buffer - Buffer for early logs.
                | _limit - Maximum number of messages to buffer.
                | _enabled - Flag indicating if buffering is enabled.
            :methods:
                | __init__ - Initializes the buffer.
                | add - Adds a message to the buffer.
                | flush - Flushes buffered messages to a writer.
                | clear - Clears the buffer.
                | is_enabled - Returns if buffering is enabled.
                | __str__ - Returns buffer as string representation.
    '''

    def __init__(self, limit: int = 200) -> None:
        '''
            Initializes the buffer.

            :param limit: Maximum number of messages to buffer.
            :exceptions: None.
        '''
        self._buffer: list[tuple[str, int]] = []
        self._limit = limit
        self._enabled = True

    @override
    def add(self, message: str, level: int) -> None:
        '''
            Adds a message to the buffer.

            :param message: The message to buffer.
            :param level: Log level.
            :exceptions: None.
        '''
        if self._enabled and len(self._buffer) < self._limit:
            self._buffer.append((message, level))

    @override
    def flush(self, writer: Callable[[str, int], None]) -> None:
        '''
            Flushes buffered messages to a writer.

            :param writer: The logging method to write buffered logs.
            :exceptions: None.
        '''
        for msg, lvl in self._buffer:
            writer(msg, lvl)

        self._buffer.clear()
        self._enabled = False

    @override
    def clear(self) -> None:
        '''
            Clears the buffer.

            :exceptions: None.
        '''
        self._buffer.clear()
        self._enabled = False

    @property
    @override
    def is_enabled(self) -> bool:
        '''
            Checks if buffering is enabled.

            :return: True if buffering is enabled, otherwise False.
            :exceptions: None.
        '''
        return self._enabled

    @override
    def __str__(self) -> str:
        '''
            Returns buffer as string representation.

            :return: Buffer as string representation.
            :exceptions: None.
        '''
        return to_str(self)
