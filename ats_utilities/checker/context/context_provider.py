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

from collections.abc import Sequence
from inspect import FrameInfo, stack
from typing import override

from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextProvider(IContextProvider):
    '''
        Defines class ContextProvider with attribute(s) and method(s).
        Retrieves context using the call stack.

        It defines:

            :attributes:
                | _stack_index_caller - Index in the call stack to identify the caller.
            :methods:
                | __init__ - Initializes context provider.
                | set_stack_index_caller - Sets the index in the call stack to identify the caller.
                | get_context - Returns a string representing the calling context.
                | __str__ - Returns the context provider as string representation.
    '''

    _stack_index_caller: int

    def __init__(self, stack_index_caller: int = 2) -> None:
        '''
            Initializes context provider.

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
                | ATSValueError: Stack index caller must be provided.
                | ATSTypeError: Stack index caller must be an integer.
        '''
        ctx: str = r'context_provider::set_stack_index_caller(...)'
        not_none(stack_index_caller, ctx, r'stack index caller must be provided')
        istype(stack_index_caller, int, ctx, r'stack index caller must be an integer')
        self._stack_index_caller = stack_index_caller

    @override
    def get_context(self) -> str:
        '''
            Returns a string representing the calling context.
            It uses the instance's STACK_INDEX_CALLER to determine the correct
            frame in the call stack.

            :return: Context information in form of a string.
            :rtype: str
            :exceptions: None.
        '''
        current_stack: Sequence[FrameInfo] = stack()
        target_index: int = self._stack_index_caller

        if target_index >= len(current_stack):
            target_index = len(current_stack) - 1

        caller: FrameInfo = current_stack[target_index]
        func_name: str = caller.function

        if func_name == 'wrapper' and 'func' in caller.frame.f_locals:
            func_obj: object = caller.frame.f_locals['func']

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
