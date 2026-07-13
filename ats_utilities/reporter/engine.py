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
    Defines class Reporter with attribute(s) and method(s).
    Implements an API for reporting messages to the console.
'''

from __future__ import annotations

from collections.abc import Sequence
from logging import DEBUG, INFO, WARNING, ERROR
from sys import stderr
from typing import Any, override

from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.component_bundle import ReporterComponentBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.factory_class import cls_name, to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Reporter(IReporter):
    '''
        Defines class Reporter with attribute(s) and method(s).
        Implements an API for reporting messages to the console.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _theme - Injected theme for styling messages (default ConsoleTheme).
                | _logger - Injected logger for reporting messages (default Logger).
                | _is_initialized -  Indicates if the reporter is initialized (default False).
            :methods:
                | __init__ - Initializes Reporter.
                | _report - Utility method for reporting messages to console.
                | verbose - Reports verbose message to console.
                | success - Reports success message to console.
                | warning - Reports warning message to console.
                | error - Reports error message to console.
                | set_level - Sets log level.
                | is_initialized - Checks if reporter is initialized.
                | __str__ - Returns the string representation of Reporter.
    '''

    _checker: IChecker
    _theme: IConsoleTheme
    _logger: ILogger
    _is_initialized: bool

    def __init__(self, component_bundle: ReporterComponentBundle | None = None) -> None:
        '''
            Initializes Reporter.

            :param component_bundle: Reporter component bundle | None.
            :type component_bundle: <ReporterComponentBundle | None>
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            # No dependency injection then use default ones.
            bundle: ReporterComponentBundle = component_bundle or ReporterComponentBundle()
            self._checker = bundle.checker
            self._theme = bundle.theme
            self._logger = bundle.logger

            # All components initialized successfully.
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            stderr.write(f'\x1b[31m{cls_name(self)} {exc}\x1b[0m\n')

        except Exception as exc:
            stderr.write(f'\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m\n')

    def _report(self, message: Sequence[Any], color: str, ctrl: int) -> None:
        '''
            Utility method for reporting message to log/console.

            :param message: Sequence with message components.
            :type message: <Sequence[Any]>
            :param color: Theme color for the message.
            :type color: <str>
            :param ctrl: Log control flag.
            :type ctrl: <int>
            :exceptions: None.
        '''
        message_out: str = ' '.join([str(item) for item in message])

        if message_out:
            reset: str = self._theme.get_color('reset')
            self._logger.write_log(f'{color}{message_out}{reset}', ctrl)

    @vcheck([('bool:is_verbose', None), ('Sequence:message', None)])
    @override
    def verbose(self, is_verbose: bool, message: Sequence[Any]) -> None:
        '''
            Reports verbose message to console.

            :param is_verbose: Enable/Disable verbose option.
            :type is_verbose: <bool>
            :param message: Sequence with message components.
            :type message: <Sequence[Any]>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        if is_verbose:
            self._report(message, self._theme.get_color('verbose'), DEBUG)

    @vcheck([('Sequence:message', None)])
    @override
    def success(self, message: Sequence[Any]) -> None:
        '''
            Reports success message to console.

            :param message: Sequence with message components.
            :type message: <Sequence[Any]>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color('success'), INFO)

    @vcheck([('Sequence:message', None)])
    @override
    def warning(self, message: Sequence[Any]) -> None:
        '''
            Reports warning message to console.

            :param message: Sequence with message components.
            :type message: <Sequence[Any]>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color('warning'), WARNING)

    @vcheck([('Sequence:message', None)])
    @override
    def error(self, message: Sequence[Any]) -> None:
        '''
            Reports error message to console.

            :param message: Sequence with message components.
            :type message: <Sequence[Any]>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color('error'), ERROR)

    @vcheck([('int:level', None)])
    @override
    def set_level(self, level: int) -> None:
        '''
            Sets log level.

            :param level: Log level.
            :type level: <int>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        if hasattr(self._logger, 'set_level'):
            self._logger.set_level(level)
        elif hasattr(self._logger, 'setLevel'):
            self._logger.setLevel(level)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if reporter is initialized.

            :return: <True> if successful else <False>.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of Reporter.

            :return: The Reporter as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
