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
    Defines class ATSLoggerManager with attribute(s) and method(s).
    Creates an API for the ATS logging mechanism.
'''

from typing import List, Optional
from ats_utilities.logging.ilogger import ILogger
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.logging.logger import ATSLogger, ATSLogLevels
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSLoggerManager(ILoggerManager):
    '''
        Defines class ATSLoggerManager with attribute(s) and method(s).
        Creates an API for the ATS logging mechanism.
        ATS logger mechanism.

        It defines:

            :attributes:
                | ATS_CRITICAL - Critical log level.
                | ATS_DEBUG - Debug log level.
                | ATS_ERROR - Error log level.
                | ATS_INFO - Info log level.
                | ATS_WARNING - Warning log level.
                | __logger - Prepared logger instance or default logger.
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials ATSLoggerManager constructor.
                | get_logger - Gets logger instance.
                | ok - Checks if logger manager component is ok.
                | write_log - Writes message to log output.
    '''

    ATS_CRITICAL = ATSLogLevels.ATS_LOG_CRITICAL
    ATS_DEBUG = ATSLogLevels.ATS_LOG_DEBUG
    ATS_ERROR = ATSLogLevels.ATS_LOG_ERROR
    ATS_INFO = ATSLogLevels.ATS_LOG_INFO
    ATS_WARNING = ATSLogLevels.ATS_LOG_WARNING

    def __init__(self, component_bundle: Optional[LoggingComponentBundle] = None) -> None:
        '''
            Initializes ATSLoggerManager constructor.

            :param component_bundle: Logging component bundle with parameters | None.
            :type component_bundle: <Optional[LoggingComponentBundle]>
            :exceptions: ATSTypeError
        '''
        # No dependency injection then use default ones.
        bundle = component_bundle or LoggingComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        shared_bundle: ContextBundle = ContextBundle(
            checker=get_private_attr(self, 'checker'),
            reporter=get_private_attr(self, 'reporter'),
            verbose=get_private_attr(self, 'verbose')
        )
        log_bundle: LoggerBundle = bundle.logger_bundle or LoggerBundle()
        self.__logger: ILogger = make_component(
            bundle.logger, ATSLogger, {'logger_bundle': log_bundle, 'context_bundle': shared_bundle}
        )
        validate_component(self.__logger, type(self.__logger), type(self.__logger).__name__)

    def get_logger(self) -> ILogger:
        '''
            Gets logger instance.

            :return: Logger instance.
            :rtype: <ILogger>
            :exceptions: None
        '''
        return self.__logger

    def write_log(self, message: Optional[str], ctrl: int) -> bool:
        '''
            Writes message to log output.

            :param message: Log message in string format for log output | None.
            :type message: <Optional[str]>
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__logger.write_log(message, ctrl)

    def ok(self) -> bool:
        '''
            Checks if logger component is ok.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        return self.__logger.ok()

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS logger.

            :return: The ATS logger as string representation.
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
