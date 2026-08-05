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
    Defines the Reporter class with attribute(s) and method(s).
    Implements an API for the reporting of messages.
'''

from __future__ import annotations

from collections.abc import Sequence
from logging import DEBUG, INFO, WARNING, ERROR

from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.validator import ReporterBundleValidator
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
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class Reporter:
    '''
        Defines the Reporter class with attribute(s) and method(s).
        Implements an API for the reporting of messages.

        It defines:

            :attributes:
                | _checker - The parameters checker.
                | _theme - The theme for the styling of messages.
                | _logger - The logger for the reporting of messages.
                | _is_initialized - The indication of whether the reporter is initialized.
            :methods:
                | __init__ - Initializes the reporter.
                | get_bundle - Gets the current reporter configuration bundle.
                | update_bundle - Updates the reporter configuration bundle.
                | _apply_bundle - Applies the bundle configuration to the instance attributes.
                | _report - Utility method for the reporting of messages.
                | verbose - Reports a verbose message.
                | success - Reports a success message.
                | warning - Reports a warning message.
                | error - Reports an error message.
                | set_level - Sets the message reporting level.
                | is_initialized - Checks if the reporter is initialized.
                | __str__ - Returns the reporter as a string representation.
    '''

    _checker: IChecker
    _theme: IConsoleTheme
    _logger: ILogger
    _is_initialized: bool

    def __init__(self, own: ReporterBundle) -> None:
        '''
            Initializes the reporter.

            :param own: The reporter bundle.
            :exceptions:
                | ATSValueError: Reporter bundle must be provided and have proper values.
                | ATSTypeError:  Reporter bundle must be an instance of ReporterBundle
                |                and its attributes must be instances of their
                |                respective types.
        '''
        self._is_initialized = False
        ReporterBundleValidator.validate(own)
        self._apply_bundle(own)
        self._is_initialized = True

    def get_bundle(self) -> ReporterBundle:
        '''
            Gets the current reporter configuration bundle.

            :return: The ReporterBundle containing the current reporter setup.
            :exceptions: None.
        '''
        return ReporterBundle(
            checker=self._checker,
            theme=self._theme,
            logger=self._logger
        )

    def update_bundle(self, bundle: ReporterBundle) -> bool:
        '''
            Updates the reporter configuration using a reporter bundle.

            :param bundle: The reporter bundle with reporter and reporting parameters.
            :return: True if the configuration was successfully updated, otherwise False.
            :exceptions: None.
        '''
        try:
            ReporterBundleValidator.validate(bundle)
            self._apply_bundle(bundle)
            self._is_initialized = True

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: ReporterBundle) -> None:
        '''
            Applies the bundle configuration to the instance attributes.

            :param bundle: The reporter bundle with reporter and reporting parameters.
            :exceptions: None.
        '''
        self._checker = bundle.checker
        self._theme = bundle.theme
        self._logger = bundle.logger

    def _report(self, message: Sequence[object], color: str, ctrl: int) -> None:
        '''
            Utility method for the reporting of the message to the log and console.

            :param message: The sequence with the message components.
            :param color: The theme color for the message.
            :param ctrl: The log control flag.
            :exceptions: None.
        '''
        message_out: str = ' '.join([str(item) for item in message])

        if message_out:
            reset: str = self._theme.get_color(MessageKey.RESET)
            self._logger.write_log(ctrl, f'{color}{message_out}{reset}')

    @mcheck([('bool:is_verbose', None), ('Sequence:message', None)])
    def verbose(self, is_verbose: bool, message: Sequence[object]) -> None:
        '''
            Reports a verbose message to the console.

            :param is_verbose: The Enable/Disable the verbose option.
            :param message: The sequence with the message components.
            :exceptions:
                | ATSTypeError:      The parameter type validation failed.
                | ATSValueError:     The parameter format validation failed.
                | ATSRuntimeError:   The decorator was used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        if is_verbose:
            self._report(message, self._theme.get_color(MessageKey.VERBOSE), DEBUG)

    @mcheck([('Sequence:message', None)])
    def success(self, message: Sequence[object]) -> None:
        '''
            Reports a success message to the console.

            :param message: The sequence with the message components.
            :exceptions:
                | ATSTypeError:      The parameter type validation failed.
                | ATSValueError:     The parameter format validation failed.
                | ATSRuntimeError:   The decorator was used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color(MessageKey.SUCCESS), INFO)

    @mcheck([('Sequence:message', None)])
    def warning(self, message: Sequence[object]) -> None:
        '''
            Reports a warning message to the console.

            :param message: The sequence with the message components.
            :exceptions:
                | ATSTypeError:      The parameter type validation failed.
                | ATSValueError:     The parameter format validation failed.
                | ATSRuntimeError:   The decorator was used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color(MessageKey.WARNING), WARNING)

    @mcheck([('Sequence:message', None)])
    def error(self, message: Sequence[object]) -> None:
        '''
            Reports an error message to the console.

            :param message: The sequence with the message components.
            :exceptions:
                | ATSTypeError:      The parameter type validation failed.
                | ATSValueError:     The parameter format validation failed.
                | ATSRuntimeError:   The decorator was used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._report(message, self._theme.get_color(MessageKey.ERROR), ERROR)

    @mcheck([('int:level', None)])
    def set_level(self, level: int) -> None:
        '''
            Sets the log level.

            :param level: The log level.
            :exceptions:
                | ATSTypeError:      The parameter type validation failed.
                | ATSValueError:     The parameter format validation failed.
                | ATSRuntimeError:   The decorator was used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        if hasattr(self._logger, 'set_level'):
            self._logger.set_level(level)
        elif hasattr(self._logger, 'setLevel'):
            self._logger.setLevel(level)

    def is_initialized(self) -> bool:
        '''
            Checks if the reporter is initialized.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    def __str__(self) -> str:
        '''
            Returns the reporter as a string representation.

            :return: The reporter as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
