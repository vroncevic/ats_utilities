# -*- coding: UTF-8 -*-

'''
Module
    iterminal_properties.py
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
    Defines abstract class ITerminalProperties with method(s).
    Interface for getting terminal properties.
'''

from abc import ABC, abstractmethod
from typing import Any

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ITerminalProperties(ABC):
    '''
        Defines abstract class ITerminalProperties with method(s).
        Interface for getting terminal properties.

        It defines:

            :attributes: None
            :methods:
                | ioctl_get_window_size - Gets size for file descriptor.
                | ioctl_for_all_descriptors - Sets size for all file descriptors.
                | size - Gets terminal window size.
                | __str__ - Returns the terminal properties as string representation.
    '''

    @abstractmethod
    def ioctl_get_window_size(self, file_descriptor: int) -> tuple[Any, ...]:
        '''
            Gets size for file descriptor.

            :param file_descriptor: File descriptor.
            :type file_descriptor: <int>
            :return: Window size of terminal.
            :rtype: <tuple[Any, ...]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def ioctl_for_all_descriptors(self) -> None:
        '''
            Sets size for all file descriptors.

            :exceptions: None.
        '''
        pass

    @abstractmethod
    def size(self) -> tuple[Any, ...]:
        '''
            Gets terminal window size.

            :return: Terminal window size.
            :rtype: <tuple[Any, ...]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the terminal properties as string representation.

            :return: The terminal properties as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
