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

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.setup.validator import LoggerValidator
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class Logger:
    '''
        Defines class Logger with attribute(s) and method(s).
        Provides an API for the logging functionality.

        It defines:

            :attributes:
                | _logger - Logger instance.
                | _formatter - Formatter for log messages.
                | _buffer - Buffer for early logs.
                | _handler_manager - Manager for log output handlers.
                | _has_file_handler - Flag indicating if logger has a file handler.
                | _is_initialized - Indicates if logger is initialized.
            :methods:
                | __init__ - Initializes Logger constructor.
                | get_bundle - Gets current logger configuration bundle.
                | is_initialized - Checks if logger is initialized.
                | update_bundle - Updates logger configuration bundle.
                | _apply_bundle - Applies bundle configuration to instance attributes.
                | set_level - Sets log level.
                | _flush_buffer - Flushes log buffer.
                | set_log_file - Configures output handler.
                | set_stdout - Configures output handler.
                | stop_buffering - Stops log buffering.
                | write_log - Writes message to log output.
                | __str__ - Returns logger as string representation.
    '''

    _logger: IUnderlyingLogger
    _formatter: ILogFormatter
    _buffer: ILogBuffer
    _handler_manager: ILogHandlerManager
    _message_processor: IMessageProcessor
    _has_file_handler: bool
    _is_initialized: bool

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
        self._apply_bundle(own)

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

    def is_initialized(self) -> bool:
        '''
            Checks if logger is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    def update_bundle(self, bundle: LoggerBundle) -> bool:
        '''
            Updates logger configuration using a logger bundle.

            :param bundle: Logger bundle with logger and logging parameters.
            :return: True if configuration was successfully updated, False otherwise.
            :exceptions: None.
        '''
        try:
            LoggerValidator.validate(bundle)
            self._apply_bundle(bundle)

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: LoggerBundle) -> None:
        '''
            Applies bundle configuration to instance attributes.

            :param bundle: Logger bundle with logger and logging parameters.
            :exceptions: None.
        '''
        self._logger = bundle.logger
        self._formatter = bundle.formatter
        self._buffer = bundle.buffer
        self._handler_manager = bundle.handler_manager
        self._message_processor = bundle.message_processor
        self._has_file_handler = bundle.has_file_handler
        self._is_initialized = self._logger.has_handlers()

    def set_level(self, level: int) -> None:
        '''
            Sets log level.

            :param level: Log level.
            :exceptions: None.
        '''
        self._logger.set_level(level)

    def _flush_buffer(self) -> None:
        '''
            Flushes buffered messages to the logger.

            :exceptions: None.
        '''
        if self._has_file_handler and self._buffer.is_enabled:
            self._buffer.flush(lambda level, message: self._logger.log(level, message))

    def set_log_file(self, log_file: str) -> bool:
        '''
            Sets log file.

            :param log_file: Log file path.
            :exceptions: None.
        '''
        if self._handler_manager.set_log_file(log_file):
            self._has_file_handler = True
            self._flush_buffer()

            return True

        return False

    def set_stdout(self) -> bool:
        '''
            Sets log output to standard output (stdout).

            :exceptions: None.
        '''
        if self._handler_manager.set_stdout():
            self._has_file_handler = True
            self._flush_buffer()

            return True

        return False

    def stop_buffering(self) -> None:
        '''
            Stops log buffering.

            :exceptions: None.
        '''
        self._flush_buffer()
        self._buffer.clear()
        self._has_file_handler = True

    def write_log(self, level: int, message: str) -> None:
        '''
            Writes message to log.

            :param level: Log level.
            :param message: Log message in string format for log.
            :exceptions: None.
        '''
        if not message or not isinstance(message, str):
            return

        processed_message: str = self._message_processor.process(message)

        if not self._has_file_handler and self._buffer.is_enabled:
            self._buffer.add(processed_message, level)

        self._logger.log(level, processed_message)

    def __str__(self) -> str:
        '''
            Returns the logger as string representation.

            :return: The logger as string representation.
            :exceptions: None.
        '''
        return to_str(self)
