# -*- coding: UTF-8 -*-

'''
Module
    isplasher.py
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
    Defines interface ISplasher with attribute(s) and method(s).
    Interface for splash screen component.
'''

from abc import ABC, abstractmethod
from typing import List, Optional
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ISplasher(ABC):
    '''
        Defines interface ISplasher with attribute(s) and method(s).
        Interface for splash screen component.

        It defines:

            :attributes: None
            :methods:
                | center - Centers console line (abstract).
                | __str__ - Returns the string representation of splash screen component (abstract).
    '''

    @abstractmethod
    def center(self, splash_center_bundle: Optional[SplashCenterBundle] = None) -> None:
        '''
            Centers console line.

            :param splash_center_bundle: Splash center bundle for centering console output | None
            :type splash_center_bundle: <Optional[SplashCenterBundle]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method center method")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of splash screen component.

            :return: The splash screen component as string representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
