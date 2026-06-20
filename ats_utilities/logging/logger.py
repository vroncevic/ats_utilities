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

from typing import Any, ClassVar, List, Dict, Optional, Callable, Protocol
from enum import Enum
from logging import (
    getLogger, basicConfig, Logger, DEBUG, WARNING, CRITICAL, ERROR, INFO
)
from ats_utilities.logging.ilogger import ILogger, LogFormats
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
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


class LoggerLevelsProtocol(Protocol):
    '''
        Defines class LoggerLevelsProtocol with attribute(s).
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
                | __logger_name - ATS name.
                | __log_stdout - Logging to stdout (default).
                | __log_file - Logging to file.
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __logger - Python Logger instance.
                | 
            :methods:
                | __init__ - Initials ATSLogger constructor.
                | write_log - Writes message to log.
                | _reporter - Property method for getting the internal reporter instance.
                | __str__ - Returns the string representation of ATS logger.
    '''

    LOG_FORMATS: ClassVar[type[LogFormats]] = LogFormats
    LOG_LEVELS: ClassVar[type[ATSLogLevels]] = ATSLogLevels

    def __init__(
        self, logger_bundle: Optional[LoggerBundle] = None, context_bundle: Optional[ContextBundle] = None
    ) -> None:
        '''
            Initializes ATSLogger constructor.

            :param logger_bundle: Logger bundle with parameters | None.
            :type logger_bundle: <Optional[LoggerBundle]>
            :param context_bundle: Context bundle for logger | None.
            :type context_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        factory_context_bundle(self, context_bundle)
        bundle: LoggerBundle = logger_bundle or LoggerBundle()
        self.__logger_name: Optional[str] = bundle.name
        self.__log_stdout: bool = bundle.log_stdout
        self.__log_file: Optional[str] = bundle.log_file

        if bundle.configure_logging and not getLogger().hasHandlers():
            log_config: Dict[str, Any] = {
                'format': self.LOG_FORMATS.ATS_LOG_MSG_FORMAT,
                'datefmt': self.LOG_FORMATS.ATS_LOG_DATE_FORMAT,
                'level': DEBUG
            }
            if self.__log_stdout and self.__log_file:
                # Force logging to file in case file name is provided
                self.__log_stdout = False
            if self.__log_file and not self.__log_stdout:
                log_config['filename'] = self.__log_file
            basicConfig(**log_config)

        self.__logger: Logger = getLogger(self.__logger_name)
        self.__log_methods: Dict[int, Callable[..., None]] = {
            self.LOG_LEVELS.ATS_LOG_DEBUG: self.__logger.debug,
            self.LOG_LEVELS.ATS_LOG_INFO: self.__logger.info,
            self.LOG_LEVELS.ATS_LOG_WARNING: self.__logger.warning,
            self.LOG_LEVELS.ATS_LOG_ERROR: self.__logger.error,
            self.LOG_LEVELS.ATS_LOG_CRITICAL: self.__logger.critical,
        }

    @validator([('Optional[str]:message', None), ('int:ctrl', None)])
    def write_log(self, message: Optional[str], ctrl: int) -> bool:
        '''
            Writes message to log.

            :param message: Log message in string format for log | None.
            :type message: <Optional[str]>
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError by validates_parameters
        '''
        log_call = self.__log_methods.get(ctrl)

        if log_call:
            log_call(message)
            return True

        self._reporter.error([f'not supported log level [{str(ctrl)}]'])
        return False

    def ok(self) -> bool:
        '''
            Checks if logger component is ok.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        return self.__logger.isEnabledFor(INFO)

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format.
            :rtype: <IReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS logger.

            :return: The ATS logger as string representation.
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
