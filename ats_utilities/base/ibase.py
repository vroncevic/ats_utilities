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
from typing import Any, TypeAlias
from ats_utilities.option.option_namespace import OptionNamespace

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Optional string sequence type
ArgSeq: TypeAlias = Sequence[str] | None


class IBase(ABC):
    '''
        Defines abstract class IBase with method(s).
        Interface for ATS base setup.

        It defines:

            :attributes: None
            :methods:
                | is_operational - Checks if ATS is operational.
                | add_new_option - Adds a new option for the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations.
                | __str__ - Returns the ATS base as string representation.
    '''

    @abstractmethod
    def is_operational(self) -> bool:
        '''
            Checks if ATS is operational.

            :return: True (operational) | False (not operational)
            :rtype: <bool>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method is_operational() must be implemented.")

    @abstractmethod
    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: Arguments in Any form
            :type kwargs: <Any>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method add_new_option() must be implemented.")

    @abstractmethod
    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None
            :type argv: <ArgSeq>
            :return: Options and arguments | None
            :rtype: <OptionNamespace | None>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method parse_args() must be implemented.")

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations.

            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method process() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS base as string representation.

            :return: The ATS base as string representation.
            :rtype: <str>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
