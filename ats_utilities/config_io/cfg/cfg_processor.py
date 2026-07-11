# -*- coding: UTF-8 -*-

'''
Module
    cfg_processor.py
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
    Defines class CFGProcessor with attribute(s) and method(s).
    Default implementation for processing CFG content.
'''

from __future__ import annotations

from re import match
from typing import override

from ats_utilities.factory_class import to_str
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class CFGProcessor(ICFGProcessor):
    '''
        Defines class CFGProcessor with attribute(s) and method(s).
        Default implementation for processing CFG content.

        It defines:

            :attributes:
                | _REGEX_EXP - Regular expression for matching line.
                | _data - Dictionary with CFG information.
            :methods:
                | __init__ - Initializes CFGProcessor constructor.
                | from_lines - Loads CFG configuration from lines.
                | to_string - Converts CFG configuration to string.
                | to_dict - Converts CFG configuration to dictionary.
                | __str__ - Returns the CFGProcessor as string representation.
    '''

    _REGEX_EXP: str = r'^\s*$'
    _data: dict[str, str]

    def __init__(self) -> None:
        '''
            Initializes CFGProcessor constructor.

            :exceptions: None.
        '''
        self._data: dict[str, str] = {}

    @override
    def from_lines(self, lines: list[str]) -> bool:
        '''
            Loads CFG configuration from lines.

            :param lines: CFG content as a list of strings.
            :type lines: <list[str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        self._data.clear()

        for line in lines:
            if not match(self._REGEX_EXP, line):
                if '=' in line:
                    pairs: list[str] = line.split('=', 1)
                    self._data[pairs[0].strip()] = pairs[1].strip()

        return True

    @override
    def to_string(self) -> str:
        '''
            Converts CFG configuration to string.

            :return: CFG content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        return "".join([f"{k} = {v}\n" for k, v in self._data.items()])

    @override
    def to_dict(self) -> dict[str, str]:
        '''
            Converts CFG configuration to dictionary.

            :return: Dictionary with CFG information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        return self._data

    @override
    def __str__(self) -> str:
        '''
            Returns the CFGProcessor as string representation.

            :return: The CFGProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
