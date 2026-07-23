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
    Interface for splash screen.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splasher.data import CenterData

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ISplasher(ABC):
    '''
        Defines abstract class ISplasher with method(s).
        Interface for splash screen.

        It defines:

            :methods:
                | get_context - Returns the context.
                | center - Centers console line.
                | is_initialized - Checks if splasher is initialized.
                | __str__ - Returns the splash screen as string representation.
    '''

    @abstractmethod
    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :rtype: ContextBundle
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def center(self, center_data: CenterData, text: str) -> None:
        '''
            Centers console line with given text.

            :param center_data: Center data for centering console output.
            :type center_data: <CenterData>
            :param text: Text to center.
            :type text: str
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if splasher is initialized.

            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the splash screen as string representation.

            :return: The splash screen as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
