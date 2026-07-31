# -*- coding: UTF-8 -*-

'''
Module
    iloader.py
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
    Defines abstract class ILoader with method(s).
    Provides an interface for loading the configuration from reader.
    2nd level of configuration loader interface.
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
class ILoader[ContextEnvironment, ConfigurationType](Protocol):
    '''
        Defines abstract class ILoader with method(s).
        Provides an interface for loading the configuration from configuration reader.
        2nd level of configuration loader interface.

        It defines:

            :methods:
                | get_context - Returns context.
                | load_configuration - Loads configuration from file and returns configuration.
                | __str__ - Returns loader as string representation.
    '''

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: Context.
        '''
        ...

    def load_configuration(self) -> ConfigurationType:
        '''
            Loads configuration from file and returns configuration.

            :return: Configuration.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns loader as string representation.

            :return: Loader as string representation.
        '''
        ...
