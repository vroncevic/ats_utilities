# -*- coding: UTF-8 -*-

'''
Module
    ioption_manager.py
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
    Defines abstract class IOptionManager with method(s).
    Provides an interface for option parsing.
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
class IOptionManager[ContextEnvironment, Strategy](Protocol):
    '''
        Defines abstract class IOptionManager with method(s).
        Provides an interface for option parsing.

        It defines:

            :methods:
                | get_context - Returns the context.
                | strategy - Returns the parser strategy.
                | is_initialized - Checks if option manager is initialized.
                | __str__ - Returns option manager as string representation.
    '''

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: Context.
        '''
        ...

    @property
    def strategy(self) -> Strategy:
        '''
            Returns the parser strategy.

            :return: Parser strategy.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if option manager is initialized.

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns option manager as string representation.

            :return: Option manager as string representation.
        '''
        ...
