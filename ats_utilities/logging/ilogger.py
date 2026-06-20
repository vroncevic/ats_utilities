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
    Interface for the ATS logging mechanism.
'''

from abc import ABC, abstractmethod
from typing import ClassVar, List, Optional, Protocol
from enum import Enum, EnumMeta

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class LogFormats(str, Enum):
    '''
        Defines class LogFormats with attribute(s).
        Log formats for the ATS logging mechanism.

        It defines:

            :attributes:
                | ATS_LOG_MSG_FORMAT - Log message format.
                | ATS_LOG_DATE_FORMAT - Log date format.
            :methods: None
    '''
    ATS_LOG_MSG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    ATS_LOG_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'


class LoggerFormatsProtocol(Protocol):
    '''
        Defines protocol LoggerFormatsProtocol with attribute(s).
        Protocol for log formats in the ATS logging mechanism.

        It defines:

            :attributes:
                | ATS_LOG_MSG_FORMAT - Log message format (string).
                | ATS_LOG_DATE_FORMAT - Log date format (string).
            :methods: None
    '''
    ATS_LOG_MSG_FORMAT: ClassVar[str]
    ATS_LOG_DATE_FORMAT: ClassVar[str]


class LogLevels(int, Enum):
    '''
        Defines class LogLevels with attribute(s).
        Log levels for the ATS logging mechanism.

        It defines:

            :attributes:
                | ATS_LOG_DEBUG - Debug log level.
                | ATS_LOG_INFO - Info log level.
                | ATS_LOG_WARNING - Warning log level.
                | ATS_LOG_ERROR - Error log level.
                | ATS_LOG_CRITICAL - Critical log level.
            :methods: None
    '''
    ATS_LOG_DEBUG = 10
    ATS_LOG_INFO = 20
    ATS_LOG_WARNING = 30
    ATS_LOG_ERROR = 40
    ATS_LOG_CRITICAL = 50


class LoggerLevelsProtocol(Protocol):
    '''
        Defines protocol LoggerLevelsProtocol with attribute(s).
        Protocol for log levels in the ATS logging mechanism.

        It defines:

            :attributes:
                | ATS_LOG_DEBUG - Debug log level.
                | ATS_LOG_INFO - Info log level.
                | ATS_LOG_WARNING - Warning log level.
                | ATS_LOG_ERROR - Error log level.
                | ATS_LOG_CRITICAL - Critical log level.
            :methods: None
    '''
    ATS_LOG_DEBUG: ClassVar[int]
    ATS_LOG_INFO: ClassVar[int]
    ATS_LOG_WARNING: ClassVar[int]
    ATS_LOG_ERROR: ClassVar[int]
    ATS_LOG_CRITICAL: ClassVar[int]


class ILogger(ABC):
    '''
        Defines abstract class ILogger with attribute(s) and method(s).
        Interface for the ATS logging mechanism.

        It defines:

            :attributes:
                | LOG_FORMATS - Log formats.
                | LOG_LEVELS - Log levels.
            :methods:
                | write_log - Writes message to log output.
                | ok - Checks if logger component is ok.
                | __str__ - Returns the ATS logger as string representation.
    '''

    LOG_FORMATS: ClassVar[EnumMeta] = LogFormats
    LOG_LEVELS: ClassVar[EnumMeta] = LogLevels

    @abstractmethod
    def write_log(self, message: Optional[str], ctrl: int) -> bool:
        '''
            Writes message to log output.

            :param message: Log message for log output | None
            :type message: <Optional[str]>
            :param ctrl: Control flag (debug, warning, critical, errors, info)
            :type ctrl: <int>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method write_log() must be implemented.")

    @abstractmethod
    def ok(self) -> bool:
        '''
            Checks if logger component is ok.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method ok() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS logger as string representation.

            :return: The ATS logger as string representation.
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
