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
    Defines the ITerminalProperties abstract class with method(s).
    Interface for getting terminal properties.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class ITerminalProperties[FileDescriptorType, WindowSizeType](Protocol):
    '''
        Defines the ITerminalProperties abstract class with method(s).
        Interface for getting terminal properties.

        It defines:

            :methods:
                | ioctl_get_window_size - Gets size for file descriptor.
                | ioctl_for_all_descriptors - Sets size for all file descriptors.
                | size - Gets terminal window size.
                | __str__ - Returns the terminal properties as a string representation.
    '''

    def ioctl_get_window_size(self, file_descriptor: FileDescriptorType) -> WindowSizeType:
        '''
            Gets size for file descriptor.

            :param file_descriptor: The file descriptor.
            :return: The window size of terminal.
        '''
        ...

    def ioctl_for_all_descriptors(self) -> None:
        '''
            Sets size for all file descriptors.
        '''
        ...

    def size(self) -> WindowSizeType:
        '''
            Gets terminal window size.

            :return: The terminal window size.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the terminal properties as a string representation.

            :return: The Terminal properties as a string representation.
        '''
        ...
