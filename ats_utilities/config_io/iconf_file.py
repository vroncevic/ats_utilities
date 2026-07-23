# -*- coding: UTF-8 -*-

'''
Module
    iconf_file.py
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
    Defines abstract class IConfFile with method(s).
    Creates an interface for configuration file context manager.
    0th level of configuration loader/storer interface.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
from io import TextIOBase
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Optional bytes, str IO type
type File = TextIOBase | None


class IConfFile(ABC):
    '''
        Defines abstract class IConfFile with method(s).
        Creates an interface for configuration file context manager.
        0th level of configuration loader/storer interface.

        It defines:

            :methods:
                | __enter__ - Opens configuration context manager and opens the file.
                | __exit__ - Closes configuration context manager and closes the file.
                | __str__ - Returns the file context manager instance as string representation.
    '''

    @abstractmethod
    def __enter__(self) -> File | None:
        '''
            Opens configuration context manager and opens the file.

            :return: File IO object | None.
            :rtype: <File | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __exit__(self, *args: tuple[Any, ...], **kwargs: Mapping[Any, Any]) -> None:
        '''
            Closes configuration context manager and closes the file.

            :param args: Tuple of arguments.
            :type args: tuple[Any, ...]  
            :param kwargs: Mapping of arguments.
            :type kwargs: Mapping[Any, Any]
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the IConfFile as string representation.

            :return: The IConfFile as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
