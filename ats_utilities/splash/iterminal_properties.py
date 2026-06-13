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
    Defines interface ITerminalProperties with attribute(s) and method(s).
    Interface for getting terminal properties.
'''

from abc import ABC, abstractmethod
from typing import Any, List, Tuple

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ITerminalProperties(ABC):
    '''
        Defines interface ITerminalProperties with attribute(s) and method(s).
        Interface for getting terminal properties.

        It defines:

            :attributes: None
            :methods:
                | ioctl_get_window_size - Gets size for descriptor (abstract).
                | ioctl_for_all_descriptors - Gets size for all descriptors (abstract).
                | size - Gets size of terminal window (abstract).
    '''

    @abstractmethod
    def ioctl_get_window_size(self, file_descriptor: int, verbose: bool = False) -> Tuple[Any, ...]:
        '''
            Gets size for descriptor.

            :param file_descriptor: file descriptor.
            :type file_descriptor: <int>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Window size of terminal.
            :rtype: <Tuple[Any, ...]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement ioctl_get_window_size method")

    @abstractmethod
    def ioctl_for_all_descriptors(self, verbose: bool = False) -> None:
        '''
            Gets size for all descriptors.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: None
            :rtype: <NoneType>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement ioctl_for_all_descriptors method")

    @abstractmethod
    def size(self, verbose: bool = False) -> Tuple[Any, ...]:
        '''
            Gets size of terminal window.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Window size
            :rtype: <Tuple[Any, ...]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement size method")
