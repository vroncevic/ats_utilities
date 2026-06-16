# -*- coding: UTF-8 -*-

'''
Module
    context_provider.py
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
    Defines class ATSContextProvider with attribute(s) and method(s).
    Creates an API for retrieving execution context.
'''

from inspect import stack
from typing import List
from ats_utilities.factory import format_instance_to_string
from ats_utilities.checker.icontext_provider import IATSContextProvider

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSContextProvider(IATSContextProvider):
    '''
        Defines class ATSContextProvider with attribute(s) and method(s).
        Retrieves context using the call stack.
        Mechanism for getting context for function or method parameters.

        It defines:

            :attributes:
                | __stack_index_caller - Index in the call stack to identify the caller (instance attribute).
            :methods:
                | __init__ - Initializes ATSContextProvider.
                | set_stack_index_caller - Sets the index in the call stack to identify the caller.
                | get_context - Returns a string representing the calling context.
                | __str__ - Returns the string representation of ATSContextProvider.
    '''

    def __init__(self, stack_index_caller: int = 2) -> None:
        '''
            Initializes ATSContextProvider.

            :param stack_index_caller: Index in the call stack to identify the caller.
            :type stack_index_caller: <int>
            :exceptions: None
        '''
        self.__stack_index_caller: int = stack_index_caller

    def set_stack_index_caller(self, stack_index_caller: int) -> None:
        '''
            Sets the index in the call stack to identify the caller.

            :param stack_index_caller: Index in the call stack to identify the caller.
            :type stack_index_caller: <int>
            :exceptions: None
        '''
        self.__stack_index_caller = stack_index_caller

    def get_context(self) -> str:
        '''
            Returns a string representing the calling context.
            It uses the instance's STACK_INDEX_CALLER to determine the correct
            frame in the call stack.

            :return: Context information string
            :rtype: <str>
            :exceptions: None
        '''
        current_stack = stack()
        target_index = self.__stack_index_caller
        if target_index >= len(current_stack):
            target_index = len(current_stack) - 1
        caller = current_stack[target_index]
        return f'\nmod: {caller.filename}\n  def: {caller.function}()'

    def __str__(self) -> str:
        '''
            Returns the string representation of ATSContextProvider.

            :return: String representation of ATSContextProvider
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
