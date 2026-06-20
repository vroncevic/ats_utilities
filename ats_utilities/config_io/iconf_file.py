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
'''

from abc import ABC, abstractmethod
from typing import Any, Dict, IO, Optional, Tuple, TypeAlias, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Optional bytes, str IO type
File: TypeAlias = Optional[IO[str]]


class IConfFile(ABC):
    '''
        Defines abstract class IConfFile with method(s).
        Creates an interface for configuration file context manager.

        It defines:

            :attributes: None
            :methods:
                | __enter__ - Opens configuration context manager.
                | __exit__ - Closes configuration context manager.
                | __str__ - Returns the IConfFile as string representation.
    '''

    @abstractmethod
    def __enter__(self) -> File:
        '''
            Opens configuration context manager.

            :return: File IO object | None.
            :rtype: <File>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method __enter__() must be implemented.")

    @abstractmethod
    def __exit__(self, *args: Tuple[Any, ...], **kwargs: Dict[Any, Any]) -> None:
        '''
            Closes configuration context manager.

            :param args: List of arguments.
            :type args: <Tuple[Any, ...]>
            :param kwargs: Dictionary of mapped arguments.
            :type kwargs: <Dict[Any, Any]>
            :return: None.
            :rtype: <None>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method __exit__() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the IConfFile as string representation.

            :return: The IConfFile as string representation.
            :rtype: <str>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
