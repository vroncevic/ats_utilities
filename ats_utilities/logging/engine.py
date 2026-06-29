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
    Defines class LoggerManager with attribute(s) and method(s).
    Creates an API for the ATS logging mechanism.
'''

from typing import override
from ats_utilities.logging.ilogger import ILogger
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.logging.logger import ATSLogger, ATSLogLevels
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import (
    get_class_name, format_instance_to_string, require_attributes
)
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_runtime_error import ATSRuntimeError
from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class LoggerManager(ILoggerManager):
    '''
        Defines class LoggerManager with attribute(s) and method(s).
        Creates an API for the ATS logging mechanism.
        ATS logger mechanism.

        It defines:

            :attributes:
                | ATS_CRITICAL - Critical log level.
                | ATS_DEBUG - Debug log level.
                | ATS_ERROR - Error log level.
                | ATS_INFO - Info log level.
                | ATS_WARNING - Warning log level.
                | _logger - Prepared logger instance or default logger.
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _shared_context - Context bundle with shared context.
                | _is_initialized - Indicates if the logger manager component is initialized (default False).
            :methods:
                | __init__ - Initials LoggerManager constructor.
                | get_shared_context - Returns the shared context.
                | get_logger - Gets logger instance.
                | write_log - Writes message to log output.
                | is_initialized - Checks if the logger manager component is initialized.
                | __str__ - Returns the string representation of ATS logger.
    '''

    ATS_CRITICAL = ATSLogLevels.ATS_LOG_CRITICAL
    ATS_DEBUG = ATSLogLevels.ATS_LOG_DEBUG
    ATS_ERROR = ATSLogLevels.ATS_LOG_ERROR
    ATS_INFO = ATSLogLevels.ATS_LOG_INFO
    ATS_WARNING = ATSLogLevels.ATS_LOG_WARNING

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, component_bundle: LoggingComponentBundle | None = None) -> None:
        '''
            Initializes LoggerManager constructor.

            :param component_bundle: Logging component bundle with parameters | None.
            :type component_bundle: <LoggingComponentBundle | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        bundle = component_bundle or LoggingComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        self._shared_context: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        log_bundle: LoggerBundle = bundle.logger_bundle or LoggerBundle()
        self._is_initialized: bool = False

        try:
            self._logger: ILogger = make_component(
                bundle.logger, ATSLogger, {'logger_bundle': log_bundle, 'context_bundle': self._shared_context}
            )
            validate_component(self._logger, ATSLogger) if not bundle.logger else None
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            self._reporter.error([f'{get_class_name(self)} {exc}'])
        except Exception as exc:
            self._reporter.error([f'{get_class_name(self)} unexpected exception: {exc}'])

    @override
    def get_shared_context(self) -> ContextBundle | None:
        '''
            Returns the shared context.

            :return: Shared context | None
            :rtype: <ContextBundle | None>
            :exceptions: None.
        '''
        return self._shared_context

    @override
    def get_logger(self) -> ILogger:
        '''
            Gets logger instance.

            :return: Logger instance.
            :rtype: <ILogger>
            :exceptions: None.
        '''
        return self._logger

    @require_attributes('_logger')
    @override
    def write_log(self, message: str | None, ctrl: int) -> bool:
        '''
            Writes message to log output.

            :param message: Log message in string format for log output | None.
            :type message: <str | None>
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_logger'.
        '''
        return self._logger.write_log(message, int(ctrl))

    @require_attributes('_logger')
    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the logger manager component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_logger'.
        '''
        return self._is_initialized and self._logger.is_initialized()

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS logger.

            :return: The ATS logger as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
