# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Provides an API for getting context information for method(s) and function(s).
'''

from __future__ import annotations

from collections.abc import Sequence
from inspect import FrameInfo, stack
from typing import Final

from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ContextProvider:
    '''
        Defines class ContextProvider with attribute(s) and method(s).
        Provides an API for getting context information for method(s) and function(s).

        It defines:

            :attributes:
                | DEFAULT_STACK_INDEX_CALLER - Default index in the call stack to identify the caller.
                | _stack_index_caller - Index in the call stack to identify the caller.
            :methods:
                | __init__ - Initializes context provider.
                | set_stack_index_caller - Sets the index in the call stack to identify the caller.
                | get_stack_index_caller - Returns the index in the call stack to identify the caller.
                | get_context - Returns the calling context.
                | __str__ - Returns context provider as string representation.
    '''

    DEFAULT_STACK_INDEX_CALLER: Final[int] = 2
    _stack_index_caller: int | None

    def __init__(self, stack_index_caller: int | None = None) -> None:
        '''
            Initializes context provider.

            :param stack_index_caller: Index in the call stack to identify the caller | None.
            :exceptions:
                | ATSTypeError: Stack index caller must be an integer.
        '''
        if stack_index_caller is not None:
            ctx: str = 'context_provider::init(...)'
            msg_stack_index_caller_istype: str = 'stack index caller must be an integer'

            istype(stack_index_caller, int, ctx, msg_stack_index_caller_istype)

            self._stack_index_caller = stack_index_caller
        else:
            self._stack_index_caller = self.DEFAULT_STACK_INDEX_CALLER

    def set_stack_index_caller(self, stack_index_caller: int) -> None:
        '''
            Sets the index in the call stack to identify the caller.

            :param stack_index_caller: Index in the call stack to identify the caller.
            :exceptions:
                | ATSValueError: Stack index caller must be provided.
                | ATSTypeError:  Stack index caller must be an integer.
        '''
        ctx: str = 'context_provider::set_stack_index_caller(...)'
        msg_stack_index_caller_none: str = 'stack index caller must be provided'
        msg_stack_index_caller_istype: str = 'stack index caller must be an integer'

        not_none(stack_index_caller, ctx, msg_stack_index_caller_none)
        istype(stack_index_caller, int, ctx, msg_stack_index_caller_istype)

        self._stack_index_caller = stack_index_caller

    def get_stack_index_caller(self) -> int:
        '''
            Returns the index in the call stack to identify the caller.

            :return: Index in the call stack to identify the caller.
            :exceptions: None.
        '''
        return self._stack_index_caller

    def get_context(self) -> str:
        '''
            Returns the calling context.

            :return: The calling context information.
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

    def __str__(self) -> str:
        '''
            Returns context provider as string representation.

            :return: Context provider as string representation.
            :exceptions: None.
        '''
        return to_str(self)
