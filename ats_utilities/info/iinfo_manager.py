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
    Interface for the info manager mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any

from ats_utilities.context.context_bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IInfoManager(ABC):
    '''
        Defines abstract class IInfoManager with method(s).
        Interface for the info manager mechanism.
        Note: The information is read-only data (it is provided by
        configuraiton file which is loaded by config loader).

        It defines:

            :methods:
                | get_shared_context - Returns the shared context.
                | set_info - Sets the information.
                | get_info - Gets the information.
                | is_initialized - Checks if info manager is initialized.
                | refresh_status - Refreshes status for information structure.
                | __str__ - Returns the info manager as string representation.
    '''

    @abstractmethod
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def set_info(self, info: Mapping[str, Any]) -> None:
        '''
            Sets the information.

            :param info: Mapping with information.
            :type info: <Mapping[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def get_info(self) -> Mapping[str, Any]:
        '''
            Gets the information.
 
            :return: Mapping with information.
            :rtype: <Mapping[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if info manager is initialized.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def refresh_status(self) -> None:
        '''
            Refreshes status for information structure.

            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the info manager as string representation.

            :return: The info manager as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
