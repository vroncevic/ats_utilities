# -*- coding: UTF-8 -*-

'''
Module
    logger.py
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
    Defines class StandardLogger with attribute(s) and method(s).
    Creates an API for the logging mechanism.
'''

from __future__ import annotations

from collections.abc import Callable, Mapping
from types import MappingProxyType
from typing import Any, ClassVar, override
from logging import getLogger, basicConfig, Logger

from ats_utilities.logging.logger.ilogger import ILogger, LogFormats, LogLevels
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.logging.logger.logger_bundle import LoggerBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import has_attrs, to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class StandardLogger(ILogger):
    '''
        Defines class StandardLogger with attribute(s) and method(s).
        Creates an API for the logging mechanism.
        Default logger mechanism.

        It defines:

            :attributes:
                | DEBUG - Debug log level (redefinition).
                | INFO - Info log level (redefinition).
                | WARNING - Warning log level (redefinition).
                | ERROR - Error log level (redefinition).
                | CRITICAL - Critical log level (redefinition).
                | _logger_name - Logger name.
                | _log_stdout - Logging to stdout (default).
                | _log_file - Logging to file.
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _logger - Python Logger instance.
                | _log_methods - Mapping of log levels to log methods.
            :methods:
                | __init__ - Initials StandardLogger constructor.
                | write_log - Writes message to log.
                | __str__ - Returns the string representation of logger.
    '''

    LOG_FORMATS: ClassVar[type[LogFormats]] = LogFormats
    LOG_LEVELS: ClassVar[type[LogLevels]] = LogLevels
    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _logger_name: str | None
    _log_stdout: bool
    _log_file: str | None
    _logger: Logger
    _log_methods: Mapping[int, Callable[..., None]]

    def __init__(
        self, logger_bundle: LoggerBundle | None = None, context_bundle: ContextBundle | None = None
    ) -> None:
        '''
            Initializes StandardLogger constructor.

            :param logger_bundle: Logger bundle with parameters | None.
            :type logger_bundle: <LoggerBundle | None>
            :param context_bundle: Context bundle for logger | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        factory_context_bundle(self, context_bundle)
        bundle: LoggerBundle = logger_bundle or LoggerBundle()
        self._logger_name = bundle.name
        self._log_stdout = bundle.log_stdout
        self._log_file = bundle.log_file

        if bundle.configure_logging and not getLogger().hasHandlers():
            log_config: dict[str, Any] = {
                'format': self.LOG_FORMATS.MSG_FORMAT,
                'datefmt': self.LOG_FORMATS.DATE_FORMAT,
                'level': self.LOG_LEVELS.DEBUG
            }
            if self._log_stdout and self._log_file:
                # Force logging to file in case file name is provided
                self._log_stdout = False
            if self._log_file and not self._log_stdout:
                log_config['filename'] = self._log_file
            basicConfig(**log_config)

        self._logger = getLogger(self._logger_name)
        self._log_methods = MappingProxyType({
            self.LOG_LEVELS.DEBUG: self._logger.debug,
            self.LOG_LEVELS.INFO: self._logger.info,
            self.LOG_LEVELS.WARNING: self._logger.warning,
            self.LOG_LEVELS.ERROR: self._logger.error,
            self.LOG_LEVELS.CRITICAL: self._logger.critical,
        })

    @vcheck([('str:message', None), ('int:ctrl', None)])
    @override
    def write_log(self, message: str, ctrl: int) -> bool:
        '''
            Writes message to log.

            :param message: Log message in string format for log.
            :type message: <str>
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        log_call = self._log_methods.get(ctrl)

        if log_call:
            log_call(message)

            return True

        self._reporter.error([f'not supported log level [{str(ctrl)}]'])
        return False

    @has_attrs('_logger')
    @override
    def is_initialized(self) -> bool:
        '''
            Checks if logger component is ok.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_logger'.
        '''
        return self._logger.isEnabledFor(LogLevels.INFO)


    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS logger.

            :return: The ATS logger as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
