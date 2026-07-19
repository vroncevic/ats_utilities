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

from __future__ import annotations

from ats_utilities.context.icontext_support import IContextSupport

from abc import ABC, abstractmethod
from collections.abc import Sequence, Mapping
from typing import Any

from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IParserStrategy(IContextSupport, ABC):
    '''
        Defines abstract class IParserStrategy with method(s).
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
                | __str__ - Returns the ATS parser strategy as string representation.
    '''

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
    def register_commands(self, commands: Sequence[IOptionCommand]) -> None:
        '''
            Register a sequence of commands with the parser.

            :param commands: Sequence of commands to register.
            :type commands: <Sequence[IOptionCommand]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_command(self, arguments: OptArgs = None) -> tuple[str, Mapping[str, Any]]:
        '''
            Parses CLI arguments for subcommands and returns command name and parameters.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Tuple containing command name and parsed parameters (read only data).
            :rtype: <tuple[str, Mapping[str, Any]]>
            :exceptions: None.
        '''
        pass


    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if parser strategy component is ok.

            :return: <True> if successful, <False> otherwise.
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
