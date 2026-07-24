# -*- coding: UTF-8 -*-

'''
Module
    buffer.py
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
    Buffer for early logs.
'''

from __future__ import annotations

from collections.abc import Callable
from typing import override

from ats_utilities.logger.ibuffer import ILogBuffer

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
        Buffer for early logs.

        It defines:

            :methods:
                | add - Adds a message to the buffer.
                | flush - Flushes buffered messages to a writer.
                | clear - Clears the buffer.
            :properties:
                | is_enabled - Checks if buffering is enabled.
    '''

    def __init__(self, limit: int = 200) -> None:
        self._buffer: list[tuple[str, int]] = []
        self._limit = limit
        self._enabled = True

    @override
    def add(self, message: str, level: int) -> None:
        '''
            Adds a message to the buffer.

            :param message: The message to buffer.
            :type message: str
            :param level: Log level.
            :type level: int
        '''
        if self._enabled and len(self._buffer) < self._limit:
            self._buffer.append((message, level))

    @override
    def flush(self, writer: Callable[[str, int], None]) -> None:
        '''
            Flushes buffered messages to a writer.

            :param writer: The logging method to write buffered logs.
            :type writer: Callable[[str, int], None]
        '''
        for msg, lvl in self._buffer:
            writer(msg, lvl)
        self._buffer.clear()
        self._enabled = False

    @override
    def clear(self) -> None:
        '''
            Clears the buffer.
        '''
        self._buffer.clear()
        self._enabled = False

    @property
    @override
    def is_enabled(self) -> bool:
        '''
            Checks if buffering is enabled.

            :return: True if buffering is enabled, otherwise False.
            :rtype: bool
        '''
        return self._enabled
