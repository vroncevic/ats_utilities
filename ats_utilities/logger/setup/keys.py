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
    Runtime components and interface constraints for logger bundle.
'''

from __future__ import annotations

from typing import Any, ClassVar
from types import MappingProxyType

from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LoggerKeys:
    '''
        Runtime components and interface constraints for logger bundle.

        It defines:

            :attributes:
                | DEPENDENCY_LOGGER: Logger interface constant.
                | DEPENDENCY_HAS_FILE_HANDLER: Has file handler flag interface constant.
                | DEPENDENCY_FORMATTER: Formatter interface constant.
                | DEPENDENCY_BUFFER: Buffer interface constant.
                | DEPENDENCY_HANDLER_MANAGER: Handler manager interface constant.
                | OPTION_LOG_FILE: Log file path option constant.
                | OPTION_LOG_LEVEL: Log level option constant.
                | OPTION_LOG_FORMAT: Format string for the log messages option constant.
                | OPTION_LOG_DATEFMT: Date format string for the log messages option constant.
            :methods:
                | get_dependency_to_type - Returns mapping of logger dependencies to their types.
                | get_option_to_type - Returns mapping of logger options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_LOGGER: ClassVar[str] = 'logger'
    DEPENDENCY_HAS_FILE_HANDLER: ClassVar[str] = 'has_file_handler'
    DEPENDENCY_FORMATTER: ClassVar[str] = 'formatter'
    DEPENDENCY_BUFFER: ClassVar[str] = 'buffer'
    DEPENDENCY_HANDLER_MANAGER: ClassVar[str] = 'handler_manager'

    # Option Keys
    OPTION_LOG_FILE: ClassVar[str] = 'log_file'
    OPTION_LOG_LEVEL: ClassVar[str] = 'log_level'
    OPTION_LOG_FORMAT: ClassVar[str] = 'log_format'
    OPTION_LOG_DATEFMT: ClassVar[str] = 'log_datefmt'
    OPTION_LOG_BUFFER_SIZE: ClassVar[int] = 'log_buffer_size'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of logger dependencies to their types.

            :return: Mapping of logger dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_LOGGER: Any,
            cls.DEPENDENCY_HAS_FILE_HANDLER: bool,
            cls.DEPENDENCY_FORMATTER: ILogFormatter,
            cls.DEPENDENCY_BUFFER: ILogBuffer,
            cls.DEPENDENCY_HANDLER_MANAGER: ILogHandlerManager,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of logger options to their types.

            :return: Mapping of logger options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_LOG_FILE: str,
            cls.OPTION_LOG_LEVEL: int,
            cls.OPTION_LOG_FORMAT: str,
            cls.OPTION_LOG_DATEFMT: str,
            cls.OPTION_LOG_BUFFER_SIZE: int,
        })
