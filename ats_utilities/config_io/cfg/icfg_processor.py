# -*- coding: UTF-8 -*-

'''
Module
    icfg_processor.py
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
    Defines abstract class ICFGProcessor with attribute(s) and method(s).
    Creates an interface for processing CFG content.
'''

from abc import ABC, abstractmethod
from typing import Any, Dict, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ICFGProcessor(ABC):
    '''
        Defines interface ICFGProcessor with attribute(s) and method(s).
        Interface for processing CFG content.

        It defines:

            :attributes: None
            :methods:
                | from_lines - Load CFG content from lines (abstract).
                | to_string - Convert CFG content to string (abstract).
                | to_dict - Convert CFG content to dictionary (abstract).
    '''

    @abstractmethod
    def from_lines(self, lines: list[str]) -> bool:
        '''
            Load CFG content from lines.

            :param lines: CFG content as a list of strings
            :type lines: <list[str]>
            :return: True (content loaded) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement from_lines method")

    @abstractmethod
    def to_string(self) -> str:
        '''
            Convert CFG content to string.

            :return: CFG content as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement to_string method")

    @abstractmethod
    def to_dict(self) -> Dict[Any, Any]:
        '''
            Convert CFG content to dictionary.

            :return: Dictionary with CFG information
            :rtype: <Dict[Any, Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement to_dict method")
