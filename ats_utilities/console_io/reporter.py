# -*- coding: utf-8 -*-

'''
Module
    reporter.py
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
    Defines class ATSReporter with attribute(s) and method(s).
    Creates an API for reporting messages.
'''

from typing import Any, List, Optional
from ats_utilities.checker import IATSChecker, ATSChecker
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.console_io.theme import IConsoleTheme, DefaultTheme
from .ireporter import IATSReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSReporter(IATSReporter):
    '''
        Defines class ATSReporter with attribute(s) and method(s).
        Creates an API for reporting messages.
        Reports status messages to the console.

        It defines:

            :attributes: None
            :methods:
                | error - Report error message to console.
                | success - Report success message to console.
                | verbose - Report verbose message to console.
                | warning - Report warning message to console.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        theme: Optional[IConsoleTheme] = None
    ) -> None:
        '''
            Initializes ATSReporter constructor.

            :param checker: Checker for parameter validation | None
            :type checker: <Optional[IATSChecker]>
            :param theme: Theme for styling | None
            :type theme: <Optional[IConsoleTheme]>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__theme: IConsoleTheme = theme or DefaultTheme()

    def __report(self, message: List[Any], color: str) -> None:
        '''
            Utility method for reporting message to console.

            :param message: List with message components
            :type message: <List[Any]>
            :param color: Theme color for the message
            :type color: <str>
            :exceptions: ATSTypeError
        '''
        error_msg, error_id = self.__checker.validate_parameters([('list:message', message)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        message_out: str = ' '.join([str(item) for item in message])

        if message_out:
            print(f"{color}{message_out}{self.__theme.get_color('reset')}")

    def verbose(self, is_verbose: bool, message: List[Any]) -> None:
        '''
            Report verbose message to console.

            :param is_verbose: Enable/Disable verbose option
            :type is_verbose: <bool>
            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        if is_verbose:
            self.__report(message, self.__theme.get_color('verbose'))

    def success(self, message: List[Any]) -> None:
        '''
            Report success message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('success'))

    def warning(self, message: List[Any]) -> None:
        '''
            Report warning message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('warning'))

    def error(self, message: List[Any]) -> None:
        '''
            Report error message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('error'))
