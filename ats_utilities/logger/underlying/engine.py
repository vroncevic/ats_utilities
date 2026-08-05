# -*- coding: UTF-8 -*-

'''
Module
    engine.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines the LoggerAdapter class with attribute(s) and method(s).
    Provides an API for the logger adapter.
'''

from __future__ import annotations

from sys import stdout
from logging import Logger as Logger, FileHandler, StreamHandler, Formatter

from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LoggerAdapter:
    '''
        Defines the LoggerAdapter class with attribute(s) and method(s).
        Provides an API for the logger adapter.

        Note: Implements a wrapper for the standard Python logging.Logger class.
        This class acts as an adapter, providing the IUnderlyingLogger interface
        for the standard Python logging infrastructure.

        It defines:

            :attributes:
                | _logger - The underlying logger.
                | _formatter - The formatter.
            :methods:
                | __init__ - Initializes the logger adapter.
                | log - Logs a message with a specific log level.
                | set_level - Sets the logging level.
                | has_handlers - Checks if the logger has any handler.
                | add_file_handler - Adds a file handler for logging.
                | add_stdout_handler - Adds a stdout handler for logging.
                | __str__ - Returns the logger adapter as a string representation.
    '''

    def __init__(self, logger: Logger, formatter: ILogFormatter) -> None:
        '''
            Initializes the logger adapter.

            :param logger: The underlying logger.
            :param formatter: The formatter.
            :exceptions:
                | ATSValueError: The logger must be provided.
                | ATSValueError: The formatter must be provided.
                | ATSTypeError:  The logger must be an instance of Logger.
                | ATSTypeError:  The formatter must be an instance of ILogFormatter.
        '''
        ctx: str = 'logger_adapter::init(...)'
        msg_logger_none: str = 'the logger must be provided'
        msg_formatter_none: str = 'the formatter must be provided'
        msg_logger_istype: str = 'the logger must be an instance of Logger'
        msg_formatter_istype: str = 'the formatter must be an instance of ILogFormatter'

        not_none(logger, ctx, msg_logger_none)
        not_none(formatter, ctx, msg_formatter_none)

        istype(logger, Logger, ctx, msg_logger_istype)
        istype(formatter, ILogFormatter, ctx, msg_formatter_istype)

        self._logger = logger
        self._formatter = formatter

    def log(self, level: int, message: str) -> None:
        '''
            Logs a message with a specific log level.

            :param level: The log level.
            :param message: The message to log.
            :exceptions: None.
        '''
        self._logger.log(level, message)

    def set_level(self, level: int) -> None:
        '''
            Sets the logging level.

            :param level: The log level.
            :exceptions: None.
        '''
        self._logger.setLevel(level)

    def has_handlers(self) -> bool:
        '''
            Checks if the logger has any handler.

            :return: True if the logger has any handler, otherwise False.
            :exceptions: None.
        '''
        return self._logger.hasHandlers()

    def add_file_handler(self, log_file: str) -> bool:
        '''
            Adds a file handler for logging.

            :param log_file: The log file path.
            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        try:
            file_handler = FileHandler(log_file)
            file_handler.setFormatter(
                fmt=Formatter(
                    fmt=self._formatter.get_format(),
                    datefmt=self._formatter.get_date_format()
                )
            )
            self._logger.addHandler(file_handler)

            return True

        except Exception:
            return False

    def add_stdout_handler(self) -> bool:
        '''
            Adds a stdout handler for logging.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        try:
            stdout_handler = StreamHandler(stdout)
            stdout_handler.setFormatter(
                fmt=Formatter(
                    fmt=self._formatter.get_format(),
                    datefmt=self._formatter.get_date_format()
                )
            )
            self._logger.addHandler(stdout_handler)

            return True

        except Exception:
            return False

    def __str__(self) -> str:
        '''
            Returns the logger adapter as a string representation.

            :return: The logger adapter as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
