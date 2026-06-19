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
    Implements an API for reporting messages to the console.
'''

from typing import Any, List, Optional
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.component_bundle import ReporterComponentBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.reporter.theme.engine import ATSConsoleTheme
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component

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
        Implements an API for reporting messages to the console.

        It defines:

            :attributes:
                | __checker - Parameters checker (default ATSChecker).
                | __theme - Theme for styling messages (default ATSConsoleTheme).
            :methods:
                | __init__ - Initializes ATSReporter constructor.
                | __report - Utility method for reporting messages to console.
                | error - Reports error message to console.
                | success - Reports success message to console.
                | verbose - Reports verbose message to console.
                | warning - Reports warning message to console.
                | __str__ - Returns the string representation of ATSReporter.
    '''

    def __init__(self, component_bundle: Optional[ReporterComponentBundle] = None) -> None:
        '''
            Initializes ATSReporter constructor.

            :param component_bundle: Reporter component bundle | None
            :type component_bundle: <Optional[ReporterComponentBundle]>
            :exceptions: ATSTypeError
        '''
        # No dependency injection then use default ones.
        bundle: ReporterComponentBundle = component_bundle or ReporterComponentBundle()
        self.__checker: IChecker = make_component(bundle.checker, ATSChecker, None)
        validate_component(self.__checker, type(self.__checker), type(self.__checker).__name__)
        self.__theme: IConsoleTheme = make_component(bundle.theme, ATSConsoleTheme, None)
        validate_component(self.__theme, type(self.__theme), type(self.__theme).__name__)

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
            Reports verbose message to console.

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
            Reports success message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('success'))

    @validator([('list:message', None)])
    def warning(self, message: List[Any]) -> None:
        '''
            Reports warning message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('warning'))

    @validator([('list:message', None)])
    def error(self, message: List[Any]) -> None:
        '''
            Reports error message to console.

            :param messages: List with message components
            :type messages: <List[Any]>
            :exceptions: None
        '''
        self.__report(message, self.__theme.get_color('error'))

    def __str__(self) -> str:
        '''
            Returns the string representation of ATSReporter.

            :return: The ATSReporter as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
