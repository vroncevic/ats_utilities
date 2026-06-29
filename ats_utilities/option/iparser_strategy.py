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
    Defines abstract class IParserStrategy with method(s).
    Creates an interface for ATS option parsing.
'''

from abc import ABC, abstractmethod
from typing import Any
from ats_utilities.option.ioption_command import IOptionCommand
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IParserStrategy(ABC):
    '''
        Defines abstract class IParserStrategy with method(s).
        Interface for concrete parsing engines (Strategy Pattern).
        Allows third-party parsers to be injected from the outside.

        It defines:

            :attributes: None
            :methods:
                | setup - Initializes the underlying parser with metadata parameters.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
                | register_commands - Registers a list of commands with the parser.
                | parse_command - Parses the input arguments and returns an OptionNamespace.
                | ok - Checks if parser strategy component is ok.
                | __str__ - Returns the ATS parser strategy as string representation.
    '''

    @abstractmethod
    def setup(self, parameters: dict[str, str]) -> None:
        '''
            Initializes the underlying parser with metadata parameters.

            :param parameters: Parameters for logger in dict format.
            :type parameters: <dict[str, str]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_argument(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: Arguments in string format.
            :type args: <str>
            :param kwargs: Arguments in Any form
            :type kwargs: <Any>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_version(self, version: str | None) -> None:
        '''
            Adds a version display option to the parser.

            :param version: The ATS version in string format | None.
            :type version: <str | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse(self, arguments: OptArgs, known_only: bool = False) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :param known_only: Parse only known arguments.
            :type known_only: <bool>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def register_commands(self, commands: list[IOptionCommand]) -> None:
        '''
            Register a list of commands with the parser.

            :param commands: List of commands to register.
            :type commands: <list[IOptionCommand]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_command(self, arguments: OptArgs = None) -> tuple[str, dict]:
        '''
            Parses CLI arguments for subcommands and returns command name and parameters.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Tuple containing command name and parsed parameters.
            :rtype: <tuple[str, dict]>
            :exceptions: None.
        '''
        pass


    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if parser strategy component is ok.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS parser strategy as string representation.

            :return: The ATS parser strategy as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
