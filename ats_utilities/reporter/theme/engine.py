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

from __future__ import annotations

from typing import override

from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.factory_class import has_attrs, to_str
from ats_utilities.factory_value import require_not_none, require_not_satisfied
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class ConsoleTheme(IConsoleTheme):
    '''
        Defines class ConsoleTheme with attribute(s) and method(s).
        Implements a console theme for console styling.

        It defines:

            :attributes:
                | _default_palette_colors - Default palette colors for different message types.
                | _palette - Dictionary with color codes for different message types.
            :methods:
                | __init__ - Initializes ConsoleTheme constructor.
                | get_color - Returns color code from palette.
                | __str__ - Returns the string representation of ConsoleTheme.
    '''

    _default_palette_colors: dict[str, str] = {
        'verbose': '\x1b[34m', # ANSI blue
        'success': '\x1b[32m', # ANSI green
        'warning': '\x1b[33m', # ANSI yellow
        'error':   '\x1b[31m', # ANSI red
        'reset':   '\x1b[0m'   # ANSI reset
    }
    _palette: dict[str, str]

    def __init__(self, palette: dict[str, str] | None = None) -> None:
        '''
            Initializes ConsoleTheme constructor.

            :param palette: Dictionary with color codes | None.
            :type palette: <dict[str, str] | None>
            :exceptions:
                | ATSTypeError: Palette must be a dictionary.
        '''
        if palette is not None:
            check_type(palette, dict, r'palette must be a dictionary')

        # No dependency injection then use default ones.
        self._palette = palette or self._default_palette_colors

    @has_attrs('_palette')
    @override
    def get_color(self, color_type: str) -> str:
        '''
            Returns color code from palette.

            :param color_type: Type of the message (key in palette).
            :type color_type: <str>
            :return: Color code in string format.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Color palette is not defined.
                | ATSValueError: Color type must be provided.
                | ATSTypeError: Color type must be a string.
                | ATSValueError: Color type not found in palette.
        '''
        require_not_none(color_type, r'color type must be provided')
        check_type(color_type, str, r'color type must be a string')
        require_not_satisfied(color_type not in self._palette, f"color type '{color_type}' not found in palette")

        return self._palette[color_type]

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ConsoleTheme.

            :return: The ConsoleTheme as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
