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
    Defines abstract class IContextProvider with method(s).
    Creates an interface for getting context for method(s) and function(s).
'''

from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IContextProvider(ABC):
    '''
        Defines abstract class IContextProvider with method(s).
        Creates an interface for getting context for method(s) and function(s).

        It defines:

            :attributes: None
            :methods:
                | set_stack_index_caller - Sets the index in the call stack to identify the caller.
                | get_context - Returns a string representing the calling context.
                | __str__ - Returns the context provider as string representation.
    '''

    @abstractmethod
    def set_stack_index_caller(self, stack_index_caller: int) -> None:
        '''
            Sets the index in the call stack to identify the caller.

            :param stack_index_caller: Index in the call stack to identify the caller.
            :type stack_index_caller: <int>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def get_context(self) -> str:
        '''
            Returns a string representing the calling context.

            :return: Context information string
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the context provider as string representation.

            :return: The context provider as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

