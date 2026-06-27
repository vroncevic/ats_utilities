# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class ConsoleTheme with attribute(s) and method(s).
    Implements a console theme for console styling.
'''

from typing import override
from ats_utilities.factory_class import require_attributes, format_instance_to_string
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ConsoleTheme(IConsoleTheme):
    '''
        Defines class ConsoleTheme with attribute(s) and method(s).
        Implements a console theme for console styling.

        It defines:

            :attributes:
                | _palette - Dictionary with color codes for different message types.
            :methods:
                | __init__ - Initializes ConsoleTheme constructor.
                | get_color - Returns color code from palette.
                | __str__ - Returns the string representation of ConsoleTheme.
    '''

    _default_palete_colors: dict[str, str] = {
        'verbose': '\x1b[34m', # ANSI blue
        'success': '\x1b[32m', # ANSI green
        'warning': '\x1b[33m', # ANSI yellow
        'error':   '\x1b[31m', # ANSI red
        'reset':   '\x1b[0m'   # ANSI reset
    }

    def __init__(self, palette: dict[str, str] | None = None) -> None:
        '''
            Initializes ConsoleTheme constructor.

            :param palette: Dictionary with color codes | None.
            :type palette: <dict[str, str] | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        self._palette: dict[str, str] = palette or self._default_palete_colors

    @require_attributes('_palette')
    @override
    def get_color(self, color_type: str) -> str:
        '''
            Returns color code from palette.

            :param color_type: Type of the message (key in palette).
            :type color_type: <str>
            :return: Color code in string format.
            :rtype: <str>
            :exceptions: ATSValueError.
        '''
        return self._palette.get(color_type, '')

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ConsoleTheme.

            :return: The ConsoleTheme as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
