# -*- coding: UTF-8 -*-

'''
Module
    iparser_strategy.py
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
    Defines the IParserStrategy abstract class with method(s).
    Provides an interface for ATS option parsing.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable
from collections.abc import Sequence

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IParserStrategy[CommandType, NamespaceType, ArgsType, ParsedCommandType](Protocol):
    '''
        Defines the IParserStrategy abstract class with method(s).
        Interface for concrete parsing engines (Strategy Pattern).
        Allows third-party parsers to be injected from the outside.

        It defines:

            :methods:
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
                | register_commands - Registers a sequence of commands with the parser.
                | parse_command - Parses the input arguments and returns an OptionNamespace.
                | ok - Checks if parser strategy component is ok.
                | __str__ - Returns the ATS parser strategy as a string representation.
    '''

    def add_argument(self, *args: str, **kwargs: object) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: The arguments in string format.
            :param kwargs: Arguments in object form
        '''
        ...

    def add_version(self, version: str | None) -> None:
        '''
            Adds a version display option to the parser.

            :param version: The ATS version in string format | None.
        '''
        ...

    def parse(self, arguments: ArgsType, known_only: bool = False) -> NamespaceType:
        '''
            Parses the input arguments and returns a NamespaceType.

            :param arguments: The sequence of arguments.
            :param known_only: The parse only known arguments.
            :return: The option namespace object.
        '''
        ...

    def register_commands(self, commands: Sequence[CommandType]) -> None:
        '''
            Register a sequence of commands with the parser.

            :param commands: The sequence of commands to register.
        '''
        ...

    def parse_command(self, arguments: ArgsType = ...) -> ParsedCommandType:
        '''
            Parses CLI arguments for subcommands and returns command name and parameters.

            :param arguments: The sequence of arguments.
            :return: The parsed command result.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if parser strategy component is ok.

            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the ATS parser strategy as a string representation.

            :return: The ATS parser strategy as a string representation.
        '''
        ...
