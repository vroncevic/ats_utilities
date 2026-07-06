# -*- coding: UTF-8 -*-

'''
Module
    ilogger.py
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
    Defines abstract class ILogger with attribute(s) and method(s).
    Interface for the logging mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar
from enum import Enum, EnumMeta

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class LogFormats(str, Enum):
    '''
        Defines class LogFormats with attribute(s).
        Log formats for the logging mechanism.

        It defines:

            :attributes:
                | MSG_FORMAT - Log message format.
                | DATE_FORMAT - Log date format.
    '''

    MSG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'


class LogLevels(int, Enum):
    '''
        Defines class LogLevels with attribute(s).
        Log levels for the logging mechanism.

        It defines:

            :attributes:
                | DEBUG - Debug log level.
                | INFO - Info log level.
                | WARNING - Warning log level.
                | ERROR - Error log level.
                | CRITICAL - Critical log level.
    '''

    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class ILogger(ABC):
    '''
        Defines abstract class ILogger with attribute(s) and method(s).
        Interface for the logger mechanism.

        It defines:

            :attributes:
                | LOG_FORMATS - Log formats.
                | LOG_LEVELS - Log levels.
            :methods:
                | write_log - Writes message to log output.
                | is_initialized - Checks if logger component is initialized.
                | __str__ - Returns the logger as string representation.
    '''

    LOG_FORMATS: ClassVar[EnumMeta] = LogFormats
    LOG_LEVELS: ClassVar[EnumMeta] = LogLevels

    @abstractmethod
    def write_log(self, message: str, ctrl: int) -> bool:
        '''
            Writes message to log output.

            :param message: Log message.
            :type message: <str>
            :param ctrl: Log control flag.
            :type ctrl: <int>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if logger component is initialized.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the logger as string representation.

            :return: The logger as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
