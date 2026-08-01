# -*- coding: UTF-8 -*-

'''
Module
    ireporter.py
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
    Defines the abstract class IReporter with method(s).
    Provides an interface for the reporting of messages.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IReporter[ConfigType, MessageType](Protocol):
    '''
        Defines the abstract class IReporter with method(s).
        Provides an interface for the reporting of messages.

        It defines:

            :methods:
                | get_bundle - Gets the current reporter configuration bundle.
                | update_bundle - Updates the reporter configuration bundle.
                | verbose - Reports a verbose message.
                | success - Reports a success message.
                | warning - Reports a warning message.
                | error - Reports an error message.
                | set_level - Sets the message reporting level.
                | is_initialized - Checks if the reporter is initialized.
                | __str__ - Returns the reporter as a string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets the current reporter configuration bundle.

            :return: Reporter configuration bundle.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates the reporter configuration bundle.

            :param bundle: The reporter configuration bundle to be updated with.
            :return: True if the update was successful, otherwise False.
        '''
        ...

    def verbose(self, is_verbose: bool, message: MessageType) -> None:
        '''
            Reports a verbose message.

            :param is_verbose: Enable/Disable verbose option.
            :param message: Message content.
        '''
        ...

    def success(self, message: MessageType) -> None:
        '''
            Reports a success message.

            :param message: Message content.
        '''
        ...

    def warning(self, message: MessageType) -> None:
        '''
            Reports a warning message.

            :param message: Message content.
        '''
        ...

    def error(self, message: MessageType) -> None:
        '''
            Reports an error message.

            :param message: Message content.
        '''
        ...

    def set_level(self, level: int) -> None:
        '''
            Sets the message reporting level.

            :param level: The message reporting level.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if the reporter is initialized.

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the reporter as a string representation.

            :return: The reporter as a string representation.
        '''
        ...
