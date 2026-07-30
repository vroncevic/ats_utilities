# -*- coding: UTF-8 -*-

'''
Module
    ibase.py
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
    Defines abstract class IBase with method(s).
    Interface for ATS base setup.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable
from collections.abc import Sequence

from ats_utilities.option.setup.types import OptionNamespace

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'

# Optional string sequence type
type ArgSeq = Sequence[str] | None


@runtime_checkable
class IBase[ContextEnvironment](Protocol):
    '''
        Defines abstract class IBase with method(s).
        Interface for ATS base setup.

        It defines:

            :methods:
                | get_context - Returns the context.
                | is_initialized - Checks if App/Tool/Script base engine is initialized.
                | add_new_option - Adds a new option for App/Tool/Script.
                | parse_args - Parses App/Tool/Script arguments.
                | process - Processes and runs App/Tool/Script (Abstract).
                | __str__ - Returns the App/Tool/Script base as string representation.
    '''
    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: Context.
            :exceptions: None.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if App/Tool/Script base engine is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        ...

    def add_new_option(self, *args: str, **kwargs: object) -> None:
        '''
            Adds a new option for App/Tool/Script.

            :param args: Arguments in string format.
            :param kwargs: Arguments in object format.
            :exceptions: None.
        '''
        ...

    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses App/Tool/Script arguments.

            :param argv: Sequence of arguments.
            :return: Options and arguments | None
            :exceptions: None.
        '''
        ...

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs App/Tool/Script (Abstract).

            :param verbose: Enable/Disable verbose option (default False).
            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the App/Tool/Script base as string representation.

            :return: The App/Tool/Script base as string representation.
            :exceptions: None.
        '''
        ...
