# -*- coding: UTF-8 -*-

'''
Module
    ioption.py
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
    Defines the IOption abstract class with method(s).
    Provides an interface for command options.
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
class IOption(Protocol):
    '''
        Defines the IOption abstract class with method(s).
        Provides an interface for command options.

        It defines:

            :methods:
                | name - Returns the command line option name.
                | help_text - Returns the command line option help text.
                | action - Returns the optional action for this option.
                | default - Returns the optional default value for this option.
                | required - Returns whether this option is required.
                | choices - Returns the optional choices for this option.
                | nargs - Returns the optional number of arguments for this option.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command line option name.

            :return: The option name.
        '''
        ...

    @property
    def help_text(self) -> str:
        '''
            Returns the command line option help text.

            :return: The option help text.
        '''
        ...

    @property
    def action(self) -> str | None:
        '''
            Returns the optional action for this option.

            :return: The option action.
        '''
        ...

    @property
    def default(self) -> object | None:
        '''
            Returns the optional default value for this option.

            :return: The option default value.
        '''
        ...

    @property
    def required(self) -> bool:
        '''
            Returns whether this option is required.

            :return: True if required, otherwise False.
        '''
        ...

    @property
    def choices(self) -> Sequence[object] | None:
        '''
            Returns the optional choices for this option.

            :return: The option choices.
        '''
        ...

    @property
    def nargs(self) -> str | int | None:
        '''
            Returns the optional number of arguments for this option.

            :return: The option nargs.
        '''
        ...

    def to_kwargs(self) -> dict[str, object]:
        '''
            Converts option properties to a dictionary of parser keyword arguments.

            :return: The dictionary of parser keyword arguments.
        '''
        ...
