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
    Provides an interface for log buffer.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ILogBuffer(ABC):
    '''
        Provides an interface for log buffer.

        It defines:

            :methods:
                | add - Adds a message to the buffer.
                | flush - Flushes buffered messages to a writer.
                | clear - Clears the buffer.
            :properties:
                | is_enabled - Checks if buffering is enabled.
    '''

    @abstractmethod
    def add(self, message: str, level: int) -> None:
        '''
            Adds a message to the buffer.

            :param message: The message to buffer.
            :type message: str
            :param level: Log level.
            :type level: int
        '''
        pass

    @abstractmethod
    def flush(self, writer: Callable[[str, int], None]) -> None:
        '''
            Flushes buffered messages to a writer.

            :param writer: The logging method to write buffered logs.
            :type writer: Callable[[str, int], None]
        '''
        pass

    @abstractmethod
    def clear(self) -> None:
        '''
            Clears the buffer.
        '''
        pass

    @property
    @abstractmethod
    def is_enabled(self) -> bool:
        '''
            Checks if buffering is enabled.

            :return: True if buffering is enabled, otherwise False.
            :rtype: bool
        '''
        pass
