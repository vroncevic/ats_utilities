# -*- coding: UTF-8 -*-

'''
Module
    default_theme.py
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
    Defines class DefaultTheme with attribute(s) and method(s).
    Concrete implementation of IConsoleTheme preparing console styling.
'''

from typing import List, Dict, Optional
from ats_utilities.console_io.theme.iconsole_theme import IConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DefaultTheme(IConsoleTheme):
    '''
        Defines class DefaultTheme with attribute(s) and method(s).
        Concrete implementation of IConsoleTheme preparing console styling.

        It defines:

            :attributes:
                | __palette - Dictionary with color codes for different message types.
            :methods:
                | __init__ - Initializes DefaultTheme constructor.
                | get_color - Returns color code from palette.
    '''

    DEFAULT_PALETE_COLORS: Dict[str, str] = {
        'verbose': '\x1b[34m', # ANSI blue
        'success': '\x1b[32m', # ANSI green
        'warning': '\x1b[33m', # ANSI yellow
        'error':   '\x1b[31m', # ANSI red
        'reset':   '\x1b[0m'   # ANSI reset
    }

    def __init__(self, palette: Optional[Dict[str, str]] = None) -> None:
        '''
            Initials DefaultTheme constructor.

            :param palette: Dictionary with color codes
            :type palette: <Dict[str, str]>
            :exceptions: None
        '''
        self.__palette: Dict[str, str] = palette or self.DEFAULT_PALETE_COLORS

    def get_color(self, color_type: str) -> str:
        '''
            Returns color code from palette.

            :param color_type: Type of the message (key in palette)
            :type color_type: <str>
            :return: Color code
            :rtype: <str>
            :exceptions: None
        '''
        return self.__palette.get(color_type, '')
