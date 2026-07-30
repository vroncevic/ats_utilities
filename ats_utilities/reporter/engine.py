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

from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.validator import ReporterValidator
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.reporter.theme.types import MessageKey
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class Reporter:
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
                | get_bundle - Gets current logger configuration bundle.
                | update_bundle - Updates logger configuration bundle.
                | _apply_bundle - Applies bundle configuration to instance attributes.
                | _report - Utility method for reporting messages to console.
                | verbose - Reports verbose message to console.
                | success - Reports success message to console.
                | warning - Reports warning message to console.
                | error - Reports error message to console.
                | set_level - Sets log level.
                | is_initialized - Checks if reporter is initialized.
                | __str__ - Returns reporter as string representation.
    '''

    _checker: IChecker
    _theme: IConsoleTheme
    _logger: ILogger
    _is_initialized: bool

    def __init__(self, own: ReporterBundle) -> None:
        '''
            Initializes Reporter.

            :param own: Reporter bundle.
            :exceptions:
                | ATSValueError: Reporter bundle must be provided and have proper values.
                | ATSTypeError:  Reporter bundle must be an instance of ReporterBundle
                |                and its attributes must be instances of their
                |                respective types.
        '''
        self._is_initialized = False
        ReporterValidator.validate(own)
        self._apply_bundle(own)
        self._is_initialized = True

    def get_bundle(self) -> ReporterBundle:
        '''
            Gets current reporter configuration bundle.

            :return: ReporterBundle containing current reporter setup.
            :exceptions: None.
        '''
        return ReporterBundle(
            checker=self._checker,
            theme=self._theme,
            logger=self._logger
        )

    def update_bundle(self, bundle: ReporterBundle) -> bool:
        '''
            Updates reporter configuration using a reporter bundle.

            :param bundle: Reporter bundle with reporter and reporting parameters.
            :return: True if configuration was successfully updated, False otherwise.
            :exceptions: None.
        '''
        try:
            ReporterValidator.validate(bundle)
            self._apply_bundle(bundle)
            self._is_initialized = True

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: ReporterBundle) -> None:
        '''
            Applies bundle configuration to instance attributes.

            :param bundle: Reporter bundle with reporter and reporting parameters.
            :exceptions: None.
        '''
        self._checker = bundle.checker
        self._theme = bundle.theme
        self._logger = bundle.logger

    def _report(self, message: Sequence[object], color: str, ctrl: int) -> None:
        '''
            Utility method for reporting message to log/console.

            :param message: Sequence with message components.
            :param color: Theme color for the message.
            :param ctrl: Log control flag.
            :exceptions: None.
        '''
        message_out: str = ' '.join([str(item) for item in message])

        if message_out:
            reset: str = self._theme.get_color(MessageKey.RESET)
            self._logger.write_log(ctrl, f'{color}{message_out}{reset}')

    @mcheck([('bool:is_verbose', None), ('Sequence:message', None)])
    def verbose(self, is_verbose: bool, message: Sequence[object]) -> None:
        '''
            Reports verbose message to console.

            :param is_verbose: Enable/Disable verbose option.
            :param message: Sequence with message components.
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        if is_verbose:
            self._report(message, self._theme.get_color(MessageKey.VERBOSE), DEBUG)

    @mcheck([('Sequence:message', None)])
    def success(self, message: Sequence[object]) -> None:
        '''
            Reports success message to console.

            :param message: Sequence with message components.
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color(MessageKey.SUCCESS), INFO)

    @mcheck([('Sequence:message', None)])
    def warning(self, message: Sequence[object]) -> None:
        '''
            Reports warning message to console.

            :param message: Sequence with message components.
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color(MessageKey.WARNING), WARNING)

    @mcheck([('Sequence:message', None)])
    def error(self, message: Sequence[object]) -> None:
        '''
            Reports error message to console.

            :param message: Sequence with message components.
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color(MessageKey.ERROR), ERROR)

    @mcheck([('int:level', None)])
    def set_level(self, level: int) -> None:
        '''
            Sets log level.

            :param level: Log level.
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

    def is_initialized(self) -> bool:
        '''
            Checks if reporter is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    def __str__(self) -> str:
        '''
            Returns reporter as string representation.

            :return: Reporter as string representation.
            :exceptions: None.
        '''
        return to_str(self)
