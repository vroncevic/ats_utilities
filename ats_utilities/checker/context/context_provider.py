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
    Defines class ContextProvider with attribute(s) and method(s).
    Creates an API for retrieving execution context.
'''

from __future__ import annotations

from inspect import stack
from typing import override

from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextProvider(IContextProvider):
    '''
        Defines class ContextProvider with attribute(s) and method(s).
        Retrieves context using the call stack.
        Mechanism for getting context for function or method parameters.

        It defines:

            :attributes:
                | _stack_index_caller - Index in the call stack to identify the caller (instance attribute).
            :methods:
                | __init__ - Initializes ContextProvider constructor.
                | set_stack_index_caller - Sets the index in the call stack to identify the caller.
                | get_context - Returns a string representing the calling context.
                | __str__ - Returns the context provider as string representation.
    '''

    _stack_index_caller: int

    def __init__(self, stack_index_caller: int = 2) -> None:
        '''
            Initializes ContextProvider constructor.

            :param stack_index_caller: Index in the call stack to identify the caller (default 2).
            :type stack_index_caller: int
            :exceptions: None.
        '''
        self._stack_index_caller = stack_index_caller

    @override
    def set_stack_index_caller(self, stack_index_caller: int) -> None:
        '''
            Sets the index in the call stack to identify the caller.

            :param stack_index_caller: Index in the call stack to identify the caller.
            :type stack_index_caller: int
            :exceptions:
                | ATSTypeError: Stack index caller must be an integer.
        '''
        context: str = r'context_provider::set_stack_index_caller(...)'
        istype(stack_index_caller, int, context, r'stack index caller must be an integer')
        self._stack_index_caller = stack_index_caller

    @override
    def get_context(self) -> str:
        '''
            Returns a string representing the calling context.
            It uses the instance's STACK_INDEX_CALLER to determine the correct
            frame in the call stack.

            :return: Context information in string format.
            :rtype: str
            :exceptions: None.
        '''
        current_stack = stack()
        target_index = self._stack_index_caller

        if target_index >= len(current_stack):
            target_index = len(current_stack) - 1

        caller = current_stack[target_index]
        func_name = caller.function

        if func_name == 'wrapper' and 'func' in caller.frame.f_locals:
            func_obj = caller.frame.f_locals['func']

            if hasattr(func_obj, '__name__'):
                func_name = func_obj.__name__

        return f'\nmod: {caller.filename}\n  def: {func_name}()'

    @override
    def __str__(self) -> str:
        '''
            Returns the context provider as string representation.

            :return: The context provider as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
