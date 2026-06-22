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
    Defines class ATSLogger with attribute(s) and method(s).
    Creates an API for the ATS logging mechanism.
'''

from collections.abc import Callable
from typing import Any, ClassVar
from enum import Enum
from logging import (
    getLogger, basicConfig, Logger, DEBUG, WARNING, CRITICAL, ERROR, INFO
)
from ats_utilities.logging.ilogger import ILogger, LogFormats
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSLogLevels(int, Enum):
    '''
        Defines class ATSLogLevels with attribute(s).
        Log levels for the ATS default logging mechanism.
        It defines:

            :attributes:
                | ATS_LOG_DEBUG - Debug log level from logging module.
                | ATS_LOG_INFO - Info log level from logging module.
                | ATS_LOG_WARNING - Warning log level from logging module.
                | ATS_LOG_ERROR - Error log level from logging module.
                | ATS_LOG_CRITICAL - Critical log level from logging module.
            :methods: None
    '''
    ATS_LOG_DEBUG = DEBUG
    ATS_LOG_INFO = INFO
    ATS_LOG_WARNING = WARNING
    ATS_LOG_ERROR = ERROR
    ATS_LOG_CRITICAL = CRITICAL


class ATSLogger(ILogger):
    '''
        Defines class ATSLogger with attribute(s) and method(s).
        Creates an API for the ATS logging mechanism.
        Default logger mechanism.

        It defines:

            :attributes:
                | ATS_LOG_DEBUG - Debug log level (redefinition).
                | ATS_LOG_INFO - Info log level (redefinition).
                | ATS_LOG_WARNING - Warning log level (redefinition).
                | ATS_LOG_ERROR - Error log level (redefinition).
                | ATS_LOG_CRITICAL - Critical log level (redefinition).
                | _logger_name - ATS name.
                | _log_stdout - Logging to stdout (default).
                | _log_file - Logging to file.
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _logger - Python Logger instance.
            :methods:
                | __init__ - Initials ATSLogger constructor.
                | write_log - Writes message to log.
                | __str__ - Returns the string representation of ATS logger.
    '''

    LOG_FORMATS: ClassVar[type[LogFormats]] = LogFormats
    LOG_LEVELS: ClassVar[type[ATSLogLevels]] = ATSLogLevels

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self, logger_bundle: LoggerBundle | None = None, context_bundle: ContextBundle | None = None
    ) -> None:
        '''
            Initializes ATSLogger constructor.

            :param logger_bundle: Logger bundle with parameters | None.
            :type logger_bundle: <LoggerBundle | None>
            :param context_bundle: Context bundle for logger | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        factory_context_bundle(self, context_bundle)
        bundle: LoggerBundle = logger_bundle or LoggerBundle()
        self._logger_name: str | None = bundle.name
        self._log_stdout: bool = bundle.log_stdout
        self._log_file: str | None = bundle.log_file

        if bundle.configure_logging and not getLogger().hasHandlers():
            log_config: dict[str, Any] = {
                'format': self.LOG_FORMATS.ATS_LOG_MSG_FORMAT,
                'datefmt': self.LOG_FORMATS.ATS_LOG_DATE_FORMAT,
                'level': self.LOG_LEVELS.ATS_LOG_DEBUG
            }
            if self._log_stdout and self._log_file:
                # Force logging to file in case file name is provided
                self._log_stdout = False
            if self._log_file and not self._log_stdout:
                log_config['filename'] = self._log_file
            basicConfig(**log_config)

        self._logger: Logger = getLogger(self._logger_name)
        self._log_methods: dict[int, Callable[..., None]] = {
            self.LOG_LEVELS.ATS_LOG_DEBUG: self._logger.debug,
            self.LOG_LEVELS.ATS_LOG_INFO: self._logger.info,
            self.LOG_LEVELS.ATS_LOG_WARNING: self._logger.warning,
            self.LOG_LEVELS.ATS_LOG_ERROR: self._logger.error,
            self.LOG_LEVELS.ATS_LOG_CRITICAL: self._logger.critical,
        }

    @validator([('str | None:message', None), ('int:ctrl', None)])
    def write_log(self, message: str | None, ctrl: int) -> bool:
        '''
            Writes message to log.

            :param message: Log message in string format for log | None.
            :type message: <str | None>
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError by validates_parameters
        '''
        log_call = self._log_methods.get(ctrl)

        if log_call:
            log_call(message)
            return True

        self._reporter.error([f'not supported log level [{str(ctrl)}]'])
        return False

    def is_initialized(self) -> bool:
        '''
            Checks if logger component is ok.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None..
        '''
        return self._logger.isEnabledFor(INFO)


    def __str__(self) -> str:
        '''
            Returns the string representation of ATS logger.

            :return: The ATS logger as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
