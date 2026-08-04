# -*- coding: UTF-8 -*-

'''
Module
    imanager.py
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
    Defines the IInfoManager abstract class with method(s).
    Provides an interface for the info management.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IInfoManager[ConfigType, InfoStructure, ContextEnvironment](Protocol):
    '''
        Defines the IInfoManager abstract class with method(s).
        Provides an interface for the info management.
        Note: The information is read-only data (it is consumed from
        configuration file loaded by config loader).

        It defines:

            :methods:
                | get_bundle - Gets current info configuration bundle.
                | update_bundle - Updates info configuration bundle.
                | get_context - Returns the context.
                | set_info - Sets the information structure.
                | get_info - Gets the information structure.
                | is_initialized - Checks if the info manager is initialized.
                | refresh_status - Refreshes the status for the information structure.
                | __str__ - Returns the info manager as a string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets current info configuration bundle.

            :return: The info configuration bundle.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates info configuration bundle.

            :param bundle: The info configuration bundle.
        '''
        ...

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: The context.
        '''
        ...

    def set_info(self, info: InfoStructure) -> None:
        '''
            Sets the information structure.

            :param info: The info structure.
        '''
        ...

    def get_info(self) -> InfoStructure:
        '''
            Gets the information structure.
 
            :return: The info structure.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if the info manager is initialized.

            :return: True if successful, otherwise False.
        '''
        ...

    def refresh_status(self) -> None:
        '''
            Refreshes the status for the information structure.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the info manager as a string representation.

            :return: The Info manager as a string representation.
        '''
        ...
