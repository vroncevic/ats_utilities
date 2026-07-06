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
    Creates an API for the logging mechanism.
'''

from __future__ import annotations

from typing import Any, override

from ats_utilities.logging.logger.ilogger import ILogger
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import cls_name, to_str, has_attrs
from ats_utilities.factory_context_error import raise_context_error
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_runtime_error import ATSRuntimeError
from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class LoggerManager(ILoggerManager):
    '''
        Defines class LoggerManager with attribute(s) and method(s).
        Creates an API for the logging mechanism.

        It defines:

            :attributes:
                | CRITICAL - Critical log level.
                | DEBUG - Debug log level.
                | ERROR - Error log level.
                | INFO - Info log level.
                | WARNING - Warning log level.
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
                | __str__ - Returns the string representation of LoggerManager.
    '''

    CRITICAL: int
    DEBUG: int
    ERROR: int
    INFO: int
    WARNING: int

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _shared_context: ContextBundle
    _is_initialized: bool
    _logger: ILogger

    def __init__(self, component_bundle: LoggingComponentBundle | None = None) -> None:
        '''
            Initializes LoggerManager constructor.

            :param component_bundle: Logging component bundle with parameters | None.
            :type component_bundle: <LoggingComponentBundle | None>
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            bundle = component_bundle or LoggingComponentBundle()
            factory_context_bundle(self, bundle.context_bundle)
            self._shared_context = bundle.context_bundle
            self._logger = bundle.logger

            self.CRITICAL = self._logger.LOG_LEVELS.CRITICAL
            self.DEBUG = self._logger.LOG_LEVELS.DEBUG
            self.ERROR = self._logger.LOG_LEVELS.ERROR
            self.INFO = self._logger.LOG_LEVELS.INFO
            self.WARNING = self._logger.LOG_LEVELS.WARNING

            # All components initialized successfully.
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            print(f"\x1b[31m{cls_name(self)} {exc}\x1b[0m")

        except Exception as exc:
            print(f"\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m")

    @override
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
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

    @has_attrs('_logger')
    @override
    def write_log(self, message: str, ctrl: int) -> bool:
        '''
            Writes message to log output.

            :param message: Log message in string format for log output.
            :type message: <str>
            :param ctrl: Control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_logger'.
        '''
        return self._logger.write_log(message, ctrl)

    @has_attrs('_logger')
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

    def __setattr__(self, name: str, value: Any) -> None:
        '''
            Sets attribute to instance components, blocking modification of log levels.

            :param name: Name of the attribute to set.
            :type name: <str>
            :param value: Value to assign to the attribute.
            :type value: <Any>
            :exceptions:
                | ATSAttributeError: If attempting to modify a log level attribute.
        '''
        if getattr(self, '_is_initialized', False) and name in (
            'CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'WARNING'
        ):
            raise_context_error(
                cls_name(self),
                f"attribute '{name}' of '{type(self).__name__}' object is read-only",
                exception_class=ATSAttributeError
            )
        super().__setattr__(name, value)

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of LoggerManager.

            :return: The LoggerManager as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
