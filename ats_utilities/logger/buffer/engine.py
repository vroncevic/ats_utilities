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
    Defines the LogBuffer class for buffering early logs with attribute(s) and method(s).
    Provides an API for log buffering during early stages of logging.
'''

from __future__ import annotations

from collections.abc import Callable
from typing import Final

from ats_utilities.validation.check_type import istype
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LogBuffer:
    '''
        Defines the LogBuffer class for buffering early logs with attribute(s) and method(s).
        Provides an API for log buffering during early stages of logging.

        It defines:

            :attributes:
                | DEFAULT_LIMIT - The default limit for the buffer.
                | _buffer - The buffer for early logs.
                | _limit - The maximum number of messages to buffer.
                | _enabled - The flag indicating if buffering is enabled.
            :methods:
                | __init__ - Initializes the buffer.
                | add - Adds a message to the buffer.
                | flush - Flushes buffered messages to a writer.
                | clear - Clears the buffer.
                | is_enabled - Returns if buffering is enabled.
                | __str__ - Returns the buffer as a string representation.
    '''

    DEFAULT_LIMIT: Final[int] = 200

    def __init__(self, limit: int | None) -> None:
        '''
            Initializes the buffer.

            :param limit: The maximum number of messages to buffer.
            :exceptions:
                | ATSValueError: The limit must be an integer.
        '''
        if limit is not None:
            ctx: str = 'log_buffer::init(...)'
            msg_limit_istype: str = 'the limit must be an integer.'
            istype(limit, int, ctx, msg_limit_istype)
            self._limit = limit
        else:
            self._limit = self.DEFAULT_LIMIT

        self._buffer: list[tuple[int, str]] = []
        self._enabled = True

    def add(self, level: int, message: str) -> None:
        '''
            Adds a message to the buffer.

            :param level: The log level.
            :param message: The message to buffer.
            :exceptions: None.
        '''
        if self._enabled and len(self._buffer) < self._limit:
            self._buffer.append((level, message))

    def flush(self, writer: Callable[[int, str], None]) -> None:
        '''
            Flushes buffered messages to a writer.

            :param writer: The logging method used to write buffered logs.
            :exceptions: None.
        '''
        for level, message in self._buffer:
            writer(level, message)

        self._buffer.clear()
        self._enabled = False

    def clear(self) -> None:
        '''
            Clears the buffer.

            :exceptions: None.
        '''
        self._buffer.clear()
        self._enabled = False

    @property
    def is_enabled(self) -> bool:
        '''
            Checks if buffering is enabled.

            :return: True if buffering is enabled, otherwise False.
            :exceptions: None.
        '''
        return self._enabled

    def __str__(self) -> str:
        '''
            Returns the buffer as a string representation.

            :return: The buffer as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
