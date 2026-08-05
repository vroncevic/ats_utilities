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
    Defines the ConsoleTheme class with attribute(s) and method(s).
    Provides the console theme for the console styling.
'''

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

from ats_utilities.reporter.theme.types import MessageKey
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.validation.check_value import not_none, not_satisfied
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ConsoleTheme:
    '''
        Defines the ConsoleTheme class with attribute(s) and method(s).
        Provides the console theme for the console styling.

        It defines:

            :attributes:
                | DEFAULT_PALETTE_COLORS - The final default palette colors for different message types.
                | _palette - The final mapping with color codes for different message types.
            :methods:
                | __init__ - Initializes the ConsoleTheme.
                | get_color - Returns the color code from the palette.
                | __str__ - Returns the console theme as a string representation.
    '''

    DEFAULT_PALETTE_COLORS: Final[MappingProxyType[str, str]] = MappingProxyType({
        MessageKey.VERBOSE: '\x1b[34m', # ANSI blue
        MessageKey.SUCCESS: '\x1b[32m', # ANSI green
        MessageKey.WARNING: '\x1b[33m', # ANSI yellow
        MessageKey.ERROR:   '\x1b[31m', # ANSI red
        MessageKey.RESET:   '\x1b[0m'   # ANSI reset
    })

    _palette: Final[Mapping[str, str]]

    def __init__(self, palette: Mapping[str, str] | None = None) -> None:
        '''
            Initializes the ConsoleTheme.

            :param palette: The mapping with color codes or None.
            :exceptions:
                | ATSTypeError: The palette must be a mapping.
        '''
        if palette is not None:
            ctx: str = 'console_theme::init(...)'
            msg_pallete_istype: str = 'the palette must be a mapping'

            istype(palette, Mapping, ctx, msg_pallete_istype)

            self._palette = MappingProxyType(palette)
        else:
            # No dependency injection then use default ones.
            self._palette = self.DEFAULT_PALETTE_COLORS

    @has_attrs('_palette')
    def get_color(self, color_type: str) -> str:
        '''
            Returns the color code from the palette.

            :param color_type: The type of the message (key in palette).
            :return: The color code in string format.
            :exceptions:
                | ATSValueError: The color type must be provided.
                | ATSTypeError:  The color type must be a string.
                | ATSValueError: The color type not found in palette.
        '''
        ctx: str = 'console_theme::get_color(...)'
        msg_color_type_none: str = 'the color type must be provided'
        msg_color_type_istype: str = 'the color type must be a string'
        msg_color_type_not_found: str = f'the color type {color_type} not found in palette'

        not_none(color_type, ctx, msg_color_type_none)
        istype(color_type, str, ctx, msg_color_type_istype)
        not_satisfied(color_type not in self._palette, ctx, msg_color_type_not_found)

        return self._palette[color_type]

    def __str__(self) -> str:
        '''
            Returns the console theme as a string representation.

            :return: The console theme as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
