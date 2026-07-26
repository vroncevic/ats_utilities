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
    Defines class Logger with attribute(s) and method(s).
    Provides an API for the logging functionality.
'''

from __future__ import annotations

from collections.abc import Callable, Mapping
from logging import (
    getLogger, DEBUG, INFO, WARNING, ERROR, CRITICAL
)
from types import MappingProxyType
from typing import Any

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.validator import LoggerValidator
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.utils.reflection import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'1.0.0'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Logger:
    '''
        Defines class Logger with attribute(s) and method(s).
        Provides an API for the logging functionality.

        It defines:

            :attributes:
                | _logger - Logger instance.
                | _log_methods - Mapping of log levels to log methods.
                | _formatter - Formatter for log messages.
                | _buffer - Buffer for early logs.
                | _handler_manager - Manager for log output handlers.
                | _has_file_handler - Flag indicating if logger has a file handler.
            :methods:
                | __init__ - Initializes Logger constructor.
                | write_log - Writes message to log.
                | is_initialized - Checks if logger is initialized.
                | set_level - Sets log level.
                | set_log_file - Sets log file.
                | set_stdout - Sets log output to standard output (stdout).
                | set_stderr - Sets log output to standard error (stderr).
                | stop_buffering - Stops log buffering.
                | __str__ - Returns the logger as string representation.
    '''

    _logger: Any
    _log_methods: Mapping[int, Callable[..., None]]
    _formatter: ILogFormatter
    _buffer: ILogBuffer
    _handler_manager: ILogHandlerManager
    _has_file_handler: bool

    def __init__(self, own: LoggerBundle) -> None:
        '''
            Initializes Logger constructor.

            :param own: Component bundle with logger and logging parameters.
            :exceptions:
                | ATSValueError: Logger bundle must be provided and have proper values.
                | ATSTypeError:  Logger bundle must be an instance of LoggerBundle.
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        LoggerValidator.validate(own)
        self._logger = own.logger
        self._formatter = own.formatter
        self._buffer = own.buffer
        self._handler_manager = own.handler_manager
        self._has_file_handler = own.has_file_handler

        if hasattr(self._logger, 'info'):
            self._log_methods = MappingProxyType({
                DEBUG: self._logger.debug,
                INFO: self._logger.info,
                WARNING: self._logger.warning,
                ERROR: self._logger.error,
                CRITICAL: self._logger.critical,
            })
        elif hasattr(self._logger, 'write_log'):
            self._log_methods = MappingProxyType({
                DEBUG: lambda msg: self._logger.write_log(msg, DEBUG),
                INFO: lambda msg: self._logger.write_log(msg, INFO),
                WARNING: lambda msg: self._logger.write_log(msg, WARNING),
                ERROR: lambda msg: self._logger.write_log(msg, ERROR),
                CRITICAL: lambda msg: self._logger.write_log(msg, CRITICAL),
            })

    def get_bundle(self) -> LoggerBundle:
        '''
            Gets current logger configuration bundle.

            :return: LoggerBundle containing current logger setup.
            :exceptions: None.
        '''
        return LoggerBundle(
            logger=self._logger,
            formatter=self._formatter,
            buffer=self._buffer,
            handler_manager=self._handler_manager,
            has_file_handler=self._has_file_handler
        )

    def update_bundle(self, bundle: LoggerBundle) -> bool:
        '''
            Updates logger configuration using a logger bundle.

            :param bundle: Component bundle with logger and logging parameters.
            :return: True if configuration was successfully updated, False otherwise.
            :exceptions:
                | ATSValueError: Logger bundle must be provided and have proper values.
                | ATSTypeError: Logger bundle must be an instance of LoggerBundle
                |               and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        try:
            LoggerValidator.validate(bundle)
            self._logger = bundle.logger
            self._formatter = bundle.formatter
            self._buffer = bundle.buffer
            self._handler_manager = bundle.handler_manager
            self._has_file_handler = bundle.has_file_handler

            if hasattr(self._logger, 'info'):
                self._log_methods = MappingProxyType({
                    DEBUG: self._logger.debug,
                    INFO: self._logger.info,
                    WARNING: self._logger.warning,
                    ERROR: self._logger.error,
                    CRITICAL: self._logger.critical,
                })
            elif hasattr(self._logger, 'write_log'):
                self._log_methods = MappingProxyType({
                    DEBUG: lambda msg: self._logger.write_log(msg, DEBUG),
                    INFO: lambda msg: self._logger.write_log(msg, INFO),
                    WARNING: lambda msg: self._logger.write_log(msg, WARNING),
                    ERROR: lambda msg: self._logger.write_log(msg, ERROR),
                    CRITICAL: lambda msg: self._logger.write_log(msg, CRITICAL),
                })
            return True

        except (ATSValueError, ATSTypeError):
            return False

    def write_log(self, message: str, ctrl: int) -> None:
        '''
            Writes message to log.

            :param message: Log message in string format for log.
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :exceptions: None.
        '''
        if bool(message) and isinstance(message, str):
            if ctrl in self._log_methods:
                processed_message: str = self._formatter.format_message(message)

                if not self._has_file_handler and self._buffer.is_enabled:
                    self._buffer.add(processed_message, ctrl)

                self._log_methods[ctrl](processed_message)

    def is_initialized(self) -> bool:
        '''
            Checks if logger is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        if hasattr(self._logger, 'hasHandlers'):
            return bool(self._log_methods) and (
                self._logger.hasHandlers() or getLogger().hasHandlers()
            )

        return bool(self._logger and self._log_methods)

#    def set_level(self, level: int) -> None:
#        '''
#            Sets log level.
#
#            :param level: Log level.
#            :exceptions: None.
#        '''
#        if hasattr(self._logger, 'setLevel'):
#            self._logger.setLevel(level)
#        elif hasattr(self._logger, 'set_level'):
#            self._logger.set_level(level)
#
#    def _flush_buffer(self) -> None:
#        if self._has_file_handler and self._buffer.is_enabled:
#            if hasattr(self._logger, 'log'):
#                self._buffer.flush(lambda msg, lvl: self._logger.log(lvl, msg))
#            elif hasattr(self._logger, 'write_log'):
#                self._buffer.flush(lambda msg, lvl: self._logger.write_log(msg, lvl))
#            else:
#                self._buffer.clear()
#
#    def set_log_file(self, log_file: str) -> None:
#        '''
#            Sets log file.
#
#            :param log_file: Log file path.
#            :exceptions: None.
#        '''
#        if self._handler_manager.set_log_file(log_file):
#            self._has_file_handler = True
#            self._flush_buffer()
#
#    def set_stdout(self) -> None:
#        '''
#            Sets log output to standard output (stdout).
#
#            :exceptions: None.
#        '''
#        if self._handler_manager.set_stdout():
#            self._has_file_handler = True
#            self._flush_buffer()
#
#    def set_stderr(self) -> None:
#        '''
#            Sets log output to standard error (stderr).
#
#            :exceptions: None.
#        '''
#        if self._handler_manager.set_stderr():
#            self._has_file_handler = True
#            self._flush_buffer()

    def stop_buffering(self) -> None:
        '''
            Stops log buffering.

            :exceptions: None.
        '''
        if hasattr(self._logger, 'stop_buffering'):
            self._logger.stop_buffering()

        self._buffer.clear()
        self._has_file_handler = True

    def __str__(self) -> str:
        '''
            Returns the logger as string representation.

            :return: The logger as string representation.
            :exceptions: None.
        '''
        return to_str(self)
