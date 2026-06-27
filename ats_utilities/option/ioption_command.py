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
    Creates an interface for ATS command with options.
'''

from abc import ABC, abstractmethod
from ats_utilities.option.command_option import CommandOption

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IOptionCommand(ABC):
    '''
        Defines abstract class IOptionCommand with method(s).
        Creates an interface for ATS command with options.

        It defines:

            :attributes: None
            :methods:
                | name - Returns the name of the command.
                | help_text - Returns the help text of the command.
                | options - Returns the list of options for the command.
                | __str__ - Returns the string representation of IOptionCommand.
    '''

    @property
    @abstractmethod
    def name(self) -> str:
        '''
            Returns the name of the command.

            :return: Name of the command.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def help_text(self) -> str:
        '''
            Returns the help text of the command.

            :return: Help text of the command.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def options(self) -> list[CommandOption]:
        '''
            Returns the list of options for the command.

            :return: List of options for the command.
            :rtype: <list[CommandOption]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of option command.

            :return: String representation of option command.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
