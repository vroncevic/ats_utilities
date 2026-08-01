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
    Defines the IConfFile abstract class with method(s).
    Provides an interface for configuration file context manager.
    0th level of configuration loader/storer interface.
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
class IConfFile[FileType, ArgType, KwargType](Protocol):
    '''
        Defines the IConfFile abstract class with method(s).
        Provides an interface for configuration file context manager.
        0th level of configuration loader/storer interface.

        It defines:

            :methods:
                | __enter__ - Opens configuration context manager.
                | __exit__ - Closes configuration context manager.
                | __str__ - Returns the configuration context manager as a string representation.
    '''

    def __enter__(self) -> FileType:
        '''
            Opens configuration context manager.

            :return: The file type.
        '''
        ...

    def __exit__(self, *args: ArgType, **kwargs: KwargType) -> None:
        '''
            Closes configuration context manager.

            :param args: The tuple of arguments.
            :param kwargs: The mapping of arguments.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the configuration context manager as a string representation.

            :return: The Configuration context manager as a string representation.
        '''
        ...
