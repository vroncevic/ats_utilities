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

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.option.option_namespace import OptionNamespace

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Optional string sequence type
type ArgSeq = Sequence[str] | None


class IBase(ABC):
    '''
        Defines abstract class IBase with method(s).
        Interface for ATS base setup.

        It defines:

            :attributes: None
            :methods:
                | get_shared_context - Returns the shared context.
                | is_initialized - Checks if the base component is initialized.
                | add_new_option - Adds a new option for the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations.
                | __str__ - Returns the ATS base as string representation.
    '''

    @abstractmethod
    def get_shared_context(self) -> ContextBundle | None:
        '''
            Returns the shared context.

            :return: Shared context | None
            :rtype: <ContextBundle | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if the base component is initialized.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: Arguments in Any form
            :type kwargs: <Any>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None
            :type argv: <ArgSeq>
            :return: Options and arguments | None
            :rtype: <OptionNamespace | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations.

            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS base as string representation.

            :return: The ATS base as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
