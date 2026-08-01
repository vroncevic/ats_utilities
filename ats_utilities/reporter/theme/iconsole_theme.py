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
    Defines the abstract class IConsoleTheme with method(s).
    Provides an interface for the console styling.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IConsoleTheme(Protocol):
    '''
        Defines the abstract class IConsoleTheme with method(s).
        Provides an interface for the console styling.

        It defines:

            :methods:
                | get_color - Returns the color code based on type.
                | __str__ - Returns the console theme as a string representation.
    '''

    def get_color(self, color_type: str) -> str:
        '''
            Returns the color code based on the type.

            :param color_type: Type of the console message (e.g. error, success).
            :return: The color code.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the console theme as a string representation.

            :return: The console theme as a string representation.
        '''
        ...
