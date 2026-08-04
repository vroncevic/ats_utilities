# -*- coding: UTF-8 -*-

'''
Module
    ioption_parser.py
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
    Defines the IOptionParser abstract class with method(s).
    Provides an interface for option parsing.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


@runtime_checkable
class IOptionParser[NamespaceType, ArgsType, ParsedCommandType](Protocol):
    '''
        Defines the IOptionParser abstract class with method(s).
        Provides an interface for parsing options.

        It defines:

            :methods:
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
                | parse_command - Parses arguments as a command.
    '''

    def parse_input_args(self, arguments: ArgsType) -> NamespaceType:
        '''
            Processes arguments from the start.

            :param arguments: The sequence of arguments.
            :return: The option namespace object.
        '''
        ...

    def parse_args(self, arguments: ArgsType) -> NamespaceType:
        '''
            Processes arguments from the start.

            :param arguments: The sequence of arguments.
            :return: The option namespace object.
        '''
        ...

    def parse_command(self, arguments: ArgsType = ...) -> ParsedCommandType:
        '''
            Parses arguments as a command.

            :param arguments: The sequence of arguments.
            :return: The parsed command result.
        '''
        ...
