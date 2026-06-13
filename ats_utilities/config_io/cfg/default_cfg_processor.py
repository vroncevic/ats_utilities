# -*- coding: UTF-8 -*-

'''
Module
    default_cfg_processor.py
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
    Defines class ATSCFGProcessor with attribute(s) and method(s).
    Default implementation for processing CFG content.
'''

from re import match
from typing import Any, Dict, List
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSCFGProcessor(ICFGProcessor):
    '''
        Defines class ATSCFGProcessor with attribute(s) and method(s).
        Default implementation for processing CFG content.

        It defines:

            :attributes:
                | __REGEX_EXP - Regular expression for matching line.
                | __data - Dictionary with CFG information.
            :methods:
                | __init__ - Initializes ATSCFGProcessor constructor.
                | from_lines - Load CFG content from lines.
                | to_string - Convert CFG content to string.
                | to_dict - Convert CFG content to dictionary.
    '''

    __REGEX_EXP: str = r'^\s*$'

    def __init__(self) -> None:
        '''
            Initializes ATSCFGProcessor constructor.
        '''
        self.__data: Dict[Any, Any] = {}

    def from_lines(self, lines: list[str]) -> bool:
        '''
            Load CFG content from lines.

            :param lines: CFG content as a list of strings
            :type lines: <list[str]>
            :return: True (content loaded) | False
            :rtype: <bool>
            :exceptions: None
        '''
        self.__data.clear()
        for line in lines:
            if not match(self.__REGEX_EXP, line):
                if '=' in line:
                    pairs = line.split('=', 1)
                    self.__data[pairs[0].strip()] = pairs[1].strip()
        return True

    def to_string(self) -> str:
        '''
            Convert CFG content to string.

            :return: CFG content as string
            :rtype: <str>
            :exceptions: None
        '''
        return "".join([f"{k} = {v}\n" for k, v in self.__data.items()])

    def to_dict(self) -> Dict[Any, Any]:
        '''
            Convert CFG content to dictionary.

            :return: Dictionary with CFG information
            :rtype: <Dict[Any, Any]>
            :exceptions: None
        '''
        return self.__data
