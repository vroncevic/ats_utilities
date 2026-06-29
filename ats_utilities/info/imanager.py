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
    Defines abstract class IInfoManager with method(s).
    Interface for the ATS info manager mechanism.
'''

from typing import Any
from abc import ABC, abstractmethod
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IInfoManager(ABC):
    '''
        Defines abstract class IInfoManager with method(s).
        Interface for the ATS info manager mechanism.

        It defines:

            :attributes: None.
            :methods:
                | get_shared_context - Returns the shared context.
                | set_info - Sets the ATS information.
                | get_info - Gets the ATS information.
                | info_ok - Checks if ATS information structure is ok.
                | refresh_status - Refreshes status for ATS information structure.
                | __str__ - Returns the ATS info manager as string representation.
    '''

    @abstractmethod
    def get_shared_context(self) -> ContextBundle | None:
        '''
            Returns the shared context.

            :return: Shared context | None.
            :rtype: <ContextBundle | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def set_info(self, info: dict[str, Any]) -> None:
        '''
            Sets the ATS information.

            :param info: Dictionary with ATS information
            :type info: <dict[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def get_info(self) -> dict[str, Any]:
        '''
            Gets the ATS information.

            :return: Dictionary with ATS information.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if ATS information structure is ok.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def refresh_status(self) -> None:
        '''
            Refreshes status for ATS information structure.

            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS info manager as string representation.

            :return: The ATS info manager as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
