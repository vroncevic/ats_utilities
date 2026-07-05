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
    Defines abstract class ICFGProcessor with method(s).
    Creates an interface for processing CFG content.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ICFGProcessor(ABC):
    '''
        Defines abstract class ICFGProcessor with method(s).
        Interface for processing CFG content.

        It defines:

            :methods:
                | from_lines - Loads CFG configuration from lines.
                | to_string - Converts CFG configuration to string.
                | to_dict - Converts CFG configuration to dictionary.
                | __str__ - Returns the CFG processor as string representation.
    '''

    @abstractmethod
    def from_lines(self, lines: list[str]) -> bool:
        '''
            Loads CFG configuration from lines.

            :param lines: CFG content as a list of strings
            :type lines: <list[str]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def to_string(self) -> str:
        '''
            Converts CFG configuration to string.

            :return: CFG content as string
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        '''
            Converts CFG configuration to dictionary.

            :return: Dictionary with ATS information
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the CFG processor as string representation.

            :return: The CFG processor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
