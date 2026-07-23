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

from collections.abc import Mapping
from types import MappingProxyType
from typing import Final, override

from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.validation.check_value import not_none, not_satisfied
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConsoleTheme(IConsoleTheme):
    '''
        Defines class ConsoleTheme with attribute(s) and method(s).
        Implements a console theme for console styling.

        It defines:

            :attributes:
                | _DEFAULT_PALETTE_COLORS - Final default palette colors for different message types.
                | _palette - Final mapping with color codes for different message types.
            :methods:
                | __init__ - Initializes ConsoleTheme constructor.
                | get_color - Returns color code from palette.
                | __str__ - Returns the console theme as string representation.
    '''

    _DEFAULT_PALETTE_COLORS: Final[Mapping[str, str]] = MappingProxyType({
        'verbose': '\x1b[34m', # ANSI blue
        'success': '\x1b[32m', # ANSI green
        'warning': '\x1b[33m', # ANSI yellow
        'error':   '\x1b[31m', # ANSI red
        'reset':   '\x1b[0m'   # ANSI reset
    })
    _palette: Final[Mapping[str, str]]

    def __init__(self, palette: dict[str, str] | None = None) -> None:
        '''
            Initializes ConsoleTheme constructor.

            :param palette: Dictionary with color codes | None.
            :type palette: dict[str, str] | None
            :exceptions:
                | ATSTypeError: Palette must be a dictionary.
        '''
        if palette is not None:
            ctx: str = r'console_theme::init(...)',
            istype(palette, dict, ctx, r'palette must be a dictionary')

        # No dependency injection then use default ones.
        self._palette = MappingProxyType(palette) if palette is not None else self._DEFAULT_PALETTE_COLORS

    @has_attrs('_palette')
    @override
    def get_color(self, color_type: str) -> str:
        '''
            Returns color code from palette.

            :param color_type: Type of the message (key in palette).
            :type color_type: str
            :return: Color code in string format.
            :rtype: str
            :exceptions:
                | ATSValueError: Color type must be provided.
                | ATSTypeError: Color type must be a string.
                | ATSValueError: Color type not found in palette.
        '''
        ctx: str = r'console_theme::get_color(...)'
        not_none(color_type, ctx, r'color type must be provided')
        istype(color_type, str, ctx, r'color type must be a string')
        not_satisfied(
            color_type not in self._palette, ctx,
            f'color type {color_type} not found in palette'
        )

        return self._palette[color_type]

    @override
    def __str__(self) -> str:
        '''
            Returns the console theme as string representation.

            :return: The console theme as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
