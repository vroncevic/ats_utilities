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
    Defines abstract class IOptionManager with method(s).
    Creates an interface for ATS option parsing.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any

from ats_utilities.option.ioption_command import IOptionCommand
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IOptionManager(ABC):
    '''
        Defines abstract class IOptionManager with method(s).
        Creates an interface for ATS option parsing.

        It defines:

            :methods:
                | get_shared_context - Returns the shared context.
                | add_operation - Adds an option to the ATS parser.
                | add_version_operation - Adds version option to the ATS parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
                | register_commands - Registers a sequence of commands with the parser.
                | parse_command - Parses the input arguments and returns an OptionNamespace.
                | is_initialized - Checks if option parser component is initialized.
                | __str__ - Returns the ATS option parser as string representation.
    '''

    @abstractmethod
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the ATS parser.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: Arguments in Any form
            :type kwargs: <Any>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_version_operation(self, version: str | None) -> None:
        '''
            Adds version option to the ATS parser.

            :param version: The ATS version in string format | None
            :type version: <str | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_input_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :return: Option namespace object
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
    def parse_command(self, arguments: OptArgs = None) -> tuple[str, dict[str, Any]]:
        '''
            Parses CLI arguments for subcommands and returns command name and parameters.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Tuple containing command name and parsed parameters.
            :rtype: <tuple[str, dict[str, Any]]>
            :exceptions: None.
        '''
        pass


    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if option parser component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS option parser as string representation.

            :return: The ATS option parser as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
