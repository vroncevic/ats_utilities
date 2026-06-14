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
    Defines interface IATSInfoManager with attribute(s) and method(s).
    Interface for the ATS info manager mechanism.
'''

from abc import ABC, abstractmethod
from typing import Any, Dict, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IATSInfoManager(ABC):
    '''
        Defines interface IATSInfoManager with attribute(s) and method(s).
        Interface for the ATS info manager mechanism.

        It defines:

            :attributes: None.
            :methods:
                | pre_setup - Property method for getting ATS pre-setup status.
                | show_base_info - Shows ATS information.
                | base_info_is_ok - Checks base information structure.
                | __str__ - Returns the string representation of ATS info manager.
    '''

    @property
    @abstractmethod
    def pre_setup(self) -> bool:
        '''
            Property method for getting ATS pre-setup status.

            :return: The ATS pre-setup status
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement pre_setup getter")

    @abstractmethod
    def show_base_info(self) -> None:
        '''
            Shows ATS information.

            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement show_base_info method")

    @abstractmethod
    def base_info_is_ok(self, info: Dict[Any, Any]) -> bool:
        '''
            Checks base information structure.

            :param info: The ATS base information
            :type info: <Dict[Any, Any]>
            :return: True (all info params are ok) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement base_info_is_ok method")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS info manager.

            :return: The ATS info manager string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement __str__ method")
