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

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.option.option_namespace import OptionNamespace

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Optional string sequence type
type ArgSeq = Sequence[str] | None


class IBase(ABC):
    '''
        Defines abstract class IBase with method(s).
        Interface for ATS base setup.

        It defines:

            :methods:
                | get_shared_context - Returns the shared context.
                | is_initialized - Checks if App/Tool/Script base engine is initialized.
                | add_new_option - Adds a new option for App/Tool/Script.
                | parse_args - Parses App/Tool/Script arguments.
                | process - Processes and runs App/Tool/Script (Abstract).
                | __str__ - Returns the App/Tool/Script base as string representation.
    '''

    @abstractmethod
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if App/Tool/Script base engine is initialized.

            :return: <True> if successful else <False>.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for App/Tool/Script.

            :param args: Arguments in string format.
            :type args: <str>
            :param kwargs: Arguments in Any format.
            :type kwargs: <Any>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses App/Tool/Script arguments.

            :param argv: Sequence of arguments.
            :type argv: <ArgSeq>
            :return: Options and arguments | None
            :rtype: <OptionNamespace | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs App/Tool/Script (Abstract).

            :param verbose: Enable/Disable verbose option (default False).
            :type verbose: <bool>
            :return: <True> if successful else <False>.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the App/Tool/Script base as string representation.

            :return: The App/Tool/Script base as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
