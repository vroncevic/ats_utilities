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
    Defines interface IInfoManager with attribute(s) and method(s).
    Interface for the ATS info manager mechanism.
'''

from abc import ABC, abstractmethod
from typing import List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IInfoManager(ABC):
    '''
        Defines interface IInfoManager with attribute(s) and method(s).
        Interface for the ATS info manager mechanism.

        It defines:

            :attributes: None.
            :methods:
                | info_ok - Checks is ATS information structure ok (abstract).
                | refresh_status - Refresh status for ATS information structure (abstract).
                | __str__ - Returns the string representation of ATS info manager (abstract).
    '''

    @property
    @abstractmethod
    def info_ok(self) -> bool:
        '''
            Checks is ATS information structure ok.
        
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method info_ok() must be implemented.")

    @abstractmethod
    def refresh_status(self) -> None:
        '''
            Refresh status for ATS information structure.

            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method refresh_status() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS info manager.

            :return: The ATS info manager string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
