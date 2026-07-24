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
    Provides an interface for splash screen.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ISplasher[PositionData](ABC):
    '''
        Defines abstract class ISplasher with method(s).
        Provides an interface for splash screen.

        It defines:

            :methods:
                | get_context - Returns the context.
                | center - Centers console line and places text.
                | is_initialized - Checks if splasher is initialized.
                | __str__ - Returns the splash screen as string representation.
    '''

    @abstractmethod
    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :rtype: ContextBundle
        '''
        pass

    @abstractmethod
    def center(self, position: PositionData, text: str) -> None:
        '''
            Centers console line and places text.

            :param position: Position data for console output.
            :type position: PositionData
            :param text: Text to be centered.
            :type text: str
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if splasher is initialized.

            :return: True if successfully, otherwise False.
            :rtype: bool
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the splash screen as string representation.

            :return: The splash screen as string representation.
            :rtype: str
        '''
        pass
