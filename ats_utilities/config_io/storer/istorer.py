# -*- coding: UTF-8 -*-

'''
Module
    istorer.py
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
    Defines abstract class IStorer with method(s).
    Provides an interface for storing the configuration to writer.
    2nd level of configuration storer interface.
'''

from __future__ import annotations

from collections.abc import Mapping
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
class IStorer[ContextEnvironment](Protocol):
    '''
        Defines abstract class IStorer with method(s).
        Provides an interface for storing the configuration to writer.
        2nd level of configuration storer interface.

        It defines:

            :methods:
                | get_context - Returns the context.
                | store_configuration - Stores configuration content from mapping to configuration file.
                | __str__ - Returns the storer instance as string representation.
    '''

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: Context.
            :exceptions: None.
        '''
        ...

    def store_configuration(self, config: Mapping[str, str]) -> bool:
        '''
            Stores configuration content from mapping to configuration file.

            :param config: Mapping with configuration information (read only data).
            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the storer instance as string representation.

            :return: The storer instance as string representation.
            :exceptions: None.
        '''
        ...
