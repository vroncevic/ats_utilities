# -*- coding: UTF-8 -*-

'''
Module
    default_logger.py
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

from typing import Any, ClassVar, List, Dict, Optional, Callable, Protocol
from enum import Enum
from logging import (
    getLogger, basicConfig, Logger, DEBUG, WARNING, CRITICAL, ERROR, INFO
)
from ats_utilities.checker.ichecker import IATSChecker, ErrorChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.logging.ilogger import IATSLogger, LogFormats

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSLogLevels(int, Enum):
    '''
        Defines class ATSLogLevels with attribute(s) and method(s).
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


class LoggerLevelsProtocol(Protocol):
    '''
        Defines class LoggerLevelsProtocol with attribute(s) and method(s).
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


class ATSLogger(IATSLogger):
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
                | __logger_name - ATS name.
                | __log_stdout - Logging to stdout (default).
                | __log_file - Logging to file.
                | __checker - Checker for parameter validation.
                | __reporter - Formatter for error reports.
                | __logger - Python Logger instance.
                | __verbose - Enable/Disable verbose option.
                | 
            :methods:
                | __init__ - Initials ATSLogger constructor.
                | write_log - Writes message to log file.
    '''

    LOG_FORMATS: ClassVar[type[LogFormats]] = LogFormats
    LOG_LEVELS: ClassVar[type[ATSLogLevels]] = ATSLogLevels
    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        ats_name: Optional[str] = None,
        ats_log_stdout: bool = True,
        ats_log_file: Optional[str] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        configure_logging: bool = True,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSLogger constructor.

            :param ats_name: ATS name | None
            :type ats_name: <Optional[str]>
            :param ats_log_stdout: Log to stdout (default True)
            :type ats_log_stdout: <bool>
            :param ats_log_file: Log to file (default None)
            :type ats_log_file: <Optional[str]>
            :param checker: Checker for parameter validation | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for verbose output | None
            :type reporter: <Optional[IATSReporter]>
            :param configure_logging: Configure logging | True
            :type configure_logging: <bool>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__logger_name: Optional[str] = ats_name
        self.__log_stdout: bool = ats_log_stdout
        self.__log_file: Optional[str] = ats_log_file

        if configure_logging and not getLogger().hasHandlers():
            log_config: Dict[str, Any] = {
                'format': self.LOG_FORMATS.ATS_LOG_MSG_FORMAT,
                'datefmt': self.LOG_FORMATS.ATS_LOG_DATE_FORMAT,
                'level': DEBUG
            }
            if self.__log_stdout and self.__log_file:
                # Force logging to file in case file name is provided
                self.__log_stdout = False
            if self.__log_file and not self.__log_stdout:
                log_config['filename'] = ats_log_file
            basicConfig(**log_config)

        self.__logger: Logger = getLogger(self.__logger_name)
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__reporter.verbose(self.__verbose, ['init default ATS logger'])
        self.__log_methods: Dict[int, Callable[..., None]] = {
            self.LOG_LEVELS.ATS_LOG_DEBUG: self.__logger.debug,
            self.LOG_LEVELS.ATS_LOG_INFO: self.__logger.info,
            self.LOG_LEVELS.ATS_LOG_WARNING: self.__logger.warning,
            self.LOG_LEVELS.ATS_LOG_ERROR: self.__logger.error,
            self.LOG_LEVELS.ATS_LOG_CRITICAL: self.__logger.critical,
        }

    def write_log(self, message: Optional[str], ctrl: int, verbose: bool = False) -> bool:
        '''
            Writes message to log file.

            :param message: Log message for log file | None
            :type message: <Optional[str]>
            :param ctrl: Control flag (debug, warning, critical, errors, info)
            :type ctrl: <int>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successfully logged message) | False
            :rtype: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('str:message', message)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__reporter.verbose(self.__verbose or verbose, [f'log message: {message} {str(ctrl)}'])
        log_call = self.__log_methods.get(ctrl)

        if log_call:
            log_call(message)
            return True

        self.__reporter.error([f'not supported log level [{str(ctrl)}]'])
        return False
