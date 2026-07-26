# -*- coding: UTF-8 -*-

'''
Module
    ioption_command.py
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
    Defines abstract class IOptionCommand with method(s).
    Provides an interface for command with options.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable
from collections.abc import Sequence

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IOptionCommand[MetaOption](Protocol):
    '''
        Defines abstract class IOptionCommand with method(s).
        Provides an interface for command with options.

        It defines:

            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of options for the command.
                | __str__ - Returns the option command as string representation.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: Command name.
        '''
        ...

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: Command help text.
        '''
        ...

    @property
    def options(self) -> Sequence[MetaOption]:
        '''
            Returns the sequence of options for the command.

            :return: Sequence of options for the command.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the string representation of option command.

            :return: String representation of option command.
        '''
        ...
