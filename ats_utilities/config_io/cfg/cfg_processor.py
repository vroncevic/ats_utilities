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
    Defines class ATSCFGProcessor with attribute(s) and method(s).
    Default implementation for processing CFG content.
'''

from re import match
from typing import Dict, List
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
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
                | from_lines - Loads CFG configuration from lines.
                | to_string - Converts CFG configuration to string.
                | to_dict - Converts CFG configuration to dictionary.
                | __str__ - Returns the ATSCFGProcessor as string representation.
    '''

    __REGEX_EXP: str = r'^\s*$'

    def __init__(self) -> None:
        '''
            Initializes ATSCFGProcessor constructor.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        self.__data: Dict[str, str] = {}

    def from_lines(self, lines: List[str]) -> bool:
        '''
            Loads CFG configuration from lines.

            :param lines: CFG content as a list of strings.
            :type lines: <List[str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        self.__data.clear()

        for line in lines:
            if not match(self.__REGEX_EXP, line):
                if '=' in line:
                    pairs: List[str] = line.split('=', 1)
                    self.__data[pairs[0].strip()] = pairs[1].strip()

        return True

    def to_string(self) -> str:
        '''
            Converts CFG configuration to string.

            :return: CFG content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        return "".join([f"{k} = {v}\n" for k, v in self.__data.items()])

    def to_dict(self) -> Dict[str, str]:
        '''
            Converts CFG configuration to dictionary.

            :return: Dictionary with CFG information.
            :rtype: <Dict[str, str]>
            :exceptions: None.
        '''
        return self.__data

    def __str__(self) -> str:
        '''
            Returns the ATSCFGProcessor as string representation.

            :return: The ATSCFGProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
