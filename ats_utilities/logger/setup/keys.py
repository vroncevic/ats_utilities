# -*- coding: UTF-8 -*-

'''
Module
    keys.py
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
    Runtime components and interface constraints for the logger bundle.
'''

from __future__ import annotations

from typing import ClassVar
from re import Pattern
from types import MappingProxyType

from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LoggerBundleKeys:
    '''
        Runtime components and interface constraints for the logger bundle.

        It defines:

            :attributes:
                | DEPENDENCY_LOGGER - The logger interface constant for the logger bundle.
                | DEPENDENCY_HAS_FILE_HANDLER - The has file handler flag interface constant for the logger bundle.
                | DEPENDENCY_FORMATTER - The formatter interface constant for the logger bundle.
                | DEPENDENCY_BUFFER - The buffer interface constant for the logger bundle.
                | DEPENDENCY_HANDLER_MANAGER - The handler manager interface constant for the logger bundle.
                | DEPENDENCY_MESSAGE_PROCESSOR - The message processor interface constant for the logger bundle.
                | OPTION_LOG_FILE - The log file path option constant for the logger bundle.
                | OPTION_LOG_LEVEL - The log level option constant for logger bundle.
                | OPTION_LOG_FORMAT - The format string for the log messages option constant for logger bundle.
                | OPTION_LOG_DATEFMT - The date format string for the log messages option constant for logger bundle.
                | OPTION_LOG_BUFFER_SIZE - The buffer size option constant for logger bundle.
                | OPTION_LOG_MESSAGE_PATTERN - The message pattern option constant for logger bundle.
            :methods:
                | get_dependency_to_type - Returns the mapping of the logger bundle dependencies to their types.
                | get_option_to_type - Returns the mapping of the logger bundle options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_LOGGER: ClassVar[str] = 'logger'
    DEPENDENCY_HAS_FILE_HANDLER: ClassVar[str] = 'has_file_handler'
    DEPENDENCY_FORMATTER: ClassVar[str] = 'formatter'
    DEPENDENCY_BUFFER: ClassVar[str] = 'buffer'
    DEPENDENCY_HANDLER_MANAGER: ClassVar[str] = 'handler_manager'
    DEPENDENCY_MESSAGE_PROCESSOR: ClassVar[str] = 'message_processor'

    # Option Keys
    OPTION_LOG_FILE: ClassVar[str] = 'log_file'
    OPTION_LOG_LEVEL: ClassVar[str] = 'log_level'
    OPTION_LOG_FORMAT: ClassVar[str] = 'log_format'
    OPTION_LOG_DATEFMT: ClassVar[str] = 'log_datefmt'
    OPTION_LOG_BUFFER_SIZE: ClassVar[int] = 'log_buffer_size'
    OPTION_LOG_MESSAGE_PATTERN: ClassVar[str] = 'message_pattern'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the logger bundle dependencies to their types.

            :return: The mapping of the logger bundle dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_LOGGER: object,
            cls.DEPENDENCY_HAS_FILE_HANDLER: bool,
            cls.DEPENDENCY_FORMATTER: ILogFormatter,
            cls.DEPENDENCY_BUFFER: ILogBuffer,
            cls.DEPENDENCY_HANDLER_MANAGER: ILogHandlerManager,
            cls.DEPENDENCY_MESSAGE_PROCESSOR: IMessageProcessor,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the logger bundle options to their types.

            :return: The mapping of the logger bundle options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_LOG_FILE: str,
            cls.OPTION_LOG_LEVEL: int,
            cls.OPTION_LOG_FORMAT: str,
            cls.OPTION_LOG_DATEFMT: str,
            cls.OPTION_LOG_BUFFER_SIZE: int,
            cls.OPTION_LOG_MESSAGE_PATTERN: Pattern[str],
        })
