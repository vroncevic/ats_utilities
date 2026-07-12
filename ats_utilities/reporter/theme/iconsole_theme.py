# -*- coding: UTF-8 -*-

'''
Module
    iconsole_theme.py
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
    Defines abstract class IConsoleTheme with method(s).
    Defines interface for console styling.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IConsoleTheme(ABC):
    '''
        Defines abstract class IConsoleTheme with method(s).
        Defines interface for console styling.

        It defines:

            :methods:
                | get_color - Returns color code based on type.
                | __str__ - Returns the console theme as string representation.
    '''

    @abstractmethod
    def get_color(self, color_type: str) -> str:
        '''
            Returns color code based on type.

            :param color_type: Type of the message (error, success, etc.).
            :type color_type: <str>
            :return: Color code.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the console theme as string representation.

            :return: The console theme as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
