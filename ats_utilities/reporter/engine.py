# -*- coding: utf-8 -*-

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
    Defines class ATSReporter with attribute(s) and method(s).
    Creates an API for reporting messages.
'''

from typing import Any, List, Optional
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.reporter.theme.engine import ATSConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSReporter(IReporter):
    '''
        Defines class ATSReporter with attribute(s) and method(s).
        Creates an API for reporting messages.
        Reports status messages to the console.

        It defines:

            :attributes:
                | __checker - Parameters checker (default ATSChecker).
                | __theme - Theme for styling messages (default ATSConsoleTheme).
            :methods:
                | error - Report error message to console.
                | success - Report success message to console.
                | verbose - Report verbose message to console.
                | warning - Report warning message to console.
                | __str__ - Returns the string representation of ATSReporter.
    '''

    def __init__(self, checker: Optional[IChecker] = None, theme: Optional[IConsoleTheme] = None) -> None:
        '''
            Initializes ATSReporter constructor.

            :param checker: Parameters checker (default ATSChecker) | None
            :type checker: <Optional[IChecker]>
            :param theme: Theme for styling messages (default ATSConsoleTheme) | None
            :type theme: <Optional[IConsoleTheme]>
            :exceptions: ATSTypeError by validate_component()
        '''
        # No dependency injection then use default ones.
        self.__checker: IChecker = make_component(checker, ATSChecker, None)
        validate_component(self.__checker, ATSChecker, "ATSChecker")
        self.__theme: IConsoleTheme = make_component(theme, ATSConsoleTheme, None)
        validate_component(self.__theme, ATSConsoleTheme, "ATSConsoleTheme")

    def __report(self, message: List[Any], color: str) -> None:
        '''
            Utility method for reporting message to console.

            :param message: List with message components
            :type message: <List[Any]>
            :param color: Theme color for the message
            :type color: <str>
            :exceptions: ATSTypeError
        '''
        message_out: str = ' '.join([str(item) for item in message])

        if message_out:
            print(f"{color}{message_out}{self.__theme.get_color('reset')}")

    @validator([('bool:is_verbose', None), ('list:message', None)])
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

    @validator([('list:message', None)])
    def success(self, message: List[Any]) -> None:
        '''
            Report success message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('success'))

    @validator([('list:message', None)])
    def warning(self, message: List[Any]) -> None:
        '''
            Report warning message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('warning'))

    @validator([('list:message', None)])
    def error(self, message: List[Any]) -> None:
        '''
            Report error message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('error'))

    def __str__(self) -> str:
        '''
            Returns the string representation of ATSReporter.

            :return: ATS reporter instance as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
