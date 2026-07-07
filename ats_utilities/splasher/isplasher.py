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
    Defines abstract class ISplasher with method(s).
    Interface for splash screen component.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class ISplasher(ABC):
    '''
        Defines abstract class ISplasher with method(s).
        Interface for splash screen component.

        It defines:

            :methods:
                | get_shared_context - Returns the shared context.
                | center - Centers console line.
                | is_initialized - Checks if splasher component is initialized.
                | __str__ - Returns the splash screen component as string representation.
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
    def center(self, splash_center_bundle: SplashCenterBundle | None = None) -> None:
        '''
            Centers console line.

            :param splash_center_bundle: Splash center bundle for centering console output | None.
            :type splash_center_bundle: <SplashCenterBundle | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if splasher component is initialized.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the splash screen component as string representation.

            :return: The splash screen component as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
