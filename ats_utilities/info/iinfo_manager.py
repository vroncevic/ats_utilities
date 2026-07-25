# -*- coding: UTF-8 -*-

'''
Module
    iinfo_manager.py
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
    Defines abstract class IInfoManager with method(s).
    Provides an interface for the info management.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IInfoManager[InfoStructure, ContextEnvironment](ABC):
    '''
        Defines abstract class IInfoManager with method(s).
        Provides an interface for the info management.
        Note: The information is read-only data (it is consumed from
        configuration file loaded by config loader).

        It defines:

            :methods:
                | get_context - Returns the context.
                | set_info - Sets the information structure.
                | get_info - Gets the information structure.
                | is_initialized - Checks if info manager is initialized.
                | refresh_status - Refreshes status for information structure.
                | __str__ - Returns info manager as string representation.
    '''

    @abstractmethod
    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: Context.
        '''
        pass

    @abstractmethod
    def set_info(self, info: InfoStructure) -> None:
        '''
            Sets the information structure.

            :param info: Info structure.
        '''
        pass

    @abstractmethod
    def get_info(self) -> InfoStructure:
        '''
            Gets the information structure.
 
            :return: Info structure.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if info manager is initialized.

            :return: True if successfully, otherwise False.
        '''
        pass

    @abstractmethod
    def refresh_status(self) -> None:
        '''
            Refreshes status for information structure.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns info manager as string representation.

            :return: Info manager as string representation.
        '''
        pass
