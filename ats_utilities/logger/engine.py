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
    Creates an API for the logging mechanism.
'''

from __future__ import annotations

from collections.abc import Callable, Mapping
from logging import getLogger, basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL
from os import environ
from re import compile, Pattern
from sys import stdout
from types import MappingProxyType
from typing import Any, override

from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.component_bundle import LoggerComponentBundle
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'1.0.0'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Logger(ILogger):
    '''
        Defines class Logger with attribute(s) and method(s).
        Creates an API for the logging mechanism.

        It defines:

            :attributes:
                | _logger - Logger instance.
                | _log_methods - Mapping of log levels to log methods.
            :methods:
                | __init__ - Initials Logger constructor.
                | _process_message - Processes the log message by checking the environment.
                | write_log - Writes message to log.
                | is_initialized - Checks if logger is initialized.
                | set_level - Sets log level.
                | __str__ - Returns the logger as string representation.
    '''

    _logger: Any
    _log_methods: Mapping[int, Callable[..., None]]

    def __init__(self, component_bundle: LoggerComponentBundle | None = None) -> None:
        '''
            Initializes Logger constructor.

            :param component_bundle: Component bundle with logger and log file.
            :type component_bundle: <LoggerComponentBundle | None>
            :exceptions: None.
        '''
        bundle: LoggerComponentBundle = component_bundle or LoggerComponentBundle()
        self._logger = bundle.logger

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

    def _process_message(self, message: str) -> str:
        '''
            Processes the log message by checking the environment.
            Stripping ANSI color codes and emojis if output is redirected or disabled.

            :param message: The original log message.
            :type message: <str>
            :return: The processed (clean or untouched) log message.
            :rtype: <str>
            :exceptions: None.
        '''
        no_color: bool = 'NO_COLOR' in environ
        force_color: bool = 'FORCE_COLOR' in environ
        is_terminal: bool = stdout.isatty()

        if no_color or (not is_terminal and not force_color):
            ansi_escape: Pattern[str] = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            message = ansi_escape.sub('', message)

        return message

    @override
    def write_log(self, message: str, ctrl: int) -> None:
        '''
            Writes message to log.

            :param message: Log message in string format for log.
            :type message: <str>
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :exceptions: None.
        '''
        if bool(message) and isinstance(message, str):
            if ctrl in self._log_methods.keys():
                processed_message: str = self._process_message(message)
                self._log_methods[ctrl](processed_message)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if logger is initialized.

            :return: <True> if logger is initialized, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        if hasattr(self._logger, 'hasHandlers'):
            return bool(self._log_methods) and (self._logger.hasHandlers() or getLogger().hasHandlers())

        return bool(self._logger and self._log_methods)

    @override
    def set_level(self, level: int) -> None:
        '''
            Sets log level.

            :param level: Log level.
            :type level: <int>
            :exceptions: None.
        '''
        if hasattr(self._logger, 'setLevel'):
            self._logger.setLevel(level)
        elif hasattr(self._logger, 'set_level'):
            self._logger.set_level(level)

    @override
    def __str__(self) -> str:
        '''
            Returns the logger as string representation.

            :return: The logger as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
