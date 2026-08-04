# -*- coding: UTF-8 -*-

'''
Module
    ioption_configurator.py
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
    Defines the IOptionConfigurator abstract class with method(s).
    Provides an interface for option configuration.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable
from collections.abc import Sequence

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


@runtime_checkable
class IOptionConfigurator[CommandType](Protocol):
    '''
        Defines the IOptionConfigurator abstract class with method(s).
        Provides an interface for option configuration.

        It defines:

            :methods:
                | add_operation - Adds an option to the parser.
                | add_version_operation - Adds version option to the parser.
                | register_commands - Registers a list of commands with the parser.
    '''

    def add_operation(self, *args: str, **kwargs: object) -> None:
        '''
            Adds an option to the parser.

            :param args: The list of flags.
            :param kwargs: The arguments in shape of dictionary.
        '''
        ...

    def add_version_operation(self, version: str | None) -> None:
        '''
            Adds version option to the parser.

            :param version: The version in string format | None.
        '''
        ...

    def register_commands(self, commands: Sequence[CommandType]) -> None:
        '''
            Registers a sequence of commands with the parser.

            :param commands: The sequence of commands to register (read only data).
        '''
        ...
