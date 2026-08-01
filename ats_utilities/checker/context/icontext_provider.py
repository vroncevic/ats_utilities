# -*- coding: UTF-8 -*-

'''
Module
    icontext_provider.py
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
    Defines the abstract class IContextProvider with method(s).
    Provides an interface for getting the context information for method(s) and function(s).
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
class IContextProvider[StackIndexCallerType, ContextFormatType](Protocol):
    '''
        Defines the abstract class IContextProvider with method(s).
        Provides an interface for getting the context information for method(s) and function(s).

        It defines:

            :methods:
                | set_stack_index_caller - Sets the index in the call stack to identify the caller.
                | get_stack_index_caller - Returns the index in the call stack to identify the caller.
                | get_context - Returns the calling context.
                | __str__ - Returns the context provider as a string representation.
    '''

    def set_stack_index_caller(self, stack_index_caller: StackIndexCallerType) -> None:
        '''
            Sets the index in the call stack to identify the caller.

            :param stack_index_caller: The index in the call stack to identify the caller.
        '''
        ...

    def get_stack_index_caller(self) -> StackIndexCallerType:
        '''
            Returns the index in the call stack to identify the caller.

            :return: The index in the call stack to identify the caller.
        '''
        ...

    def get_context(self) -> ContextFormatType:
        '''
            Returns the calling context.

            :return: The calling context information.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the context provider as a string representation.

            :return: The context provider as a string representation.
        '''
        ...
