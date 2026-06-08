# -*- coding: UTF-8 -*-

'''
Module
    default_context_provider.py
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
    Defines class DefaultContextProvider with attribute(s) and method(s).
    Creates an API for retrieving execution context.
'''

from inspect import stack
from typing import List, Final
from .icontext_provider import IContextProvider

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DefaultContextProvider(IContextProvider):
    '''
        Defines class DefaultContextProvider with attribute(s) and method(s).
        Retrieves context using the call stack.
        Mechanism for getting context for function or method parameters.

        It defines:

            :attributes:
                | STACK_INDEX_CALLER - Index in the call stack to identify the caller.
            :methods:
                | get_context - Returns a string representing the calling context.
    '''

    STACK_INDEX_CALLER: Final[int] = 2

    def get_context(self) -> str:
        '''
            Returns a string representing the calling context.

            :return: Context information string
            :rtype: <str>
            :exceptions: None
        '''
        caller = stack()[self.STACK_INDEX_CALLER]
        return f'\nmod: {caller.filename}\n  def: {caller.function}()'
