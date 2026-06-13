# -*- coding: UTF-8 -*-

'''
Module
    icli.py
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
    Defines interface IATSCli with attribute(s) and method(s).
    Interface for command-line interface configuration.
'''

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Sequence, TypeAlias
from ats_utilities.option.option_namespace import OptionNamespace

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Optional string sequence type
ArgSeq: TypeAlias = Optional[Sequence[str]]


class IATSCli(ABC):
    '''
        Defines interface IATSCli with attribute(s) and method(s).
        Interface for command-line interface configuration.

        It defines:

            :attributes: None
            :methods:
                | is_operational - Checks is tool | generator operational.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations.
    '''

    @abstractmethod
    def is_operational(self) -> bool:
        '''
            Checks is tool | generator operational.

            :return: True (tool | generator is operational) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_operational() must be implemented.")

    @abstractmethod
    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: arguments in Any form
            :type kwargs: <Any>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method add_new_option() must be implemented.")

    @abstractmethod
    def parse_args(self, argv: ArgSeq) -> Optional[OptionNamespace]:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None
            :type argv: <ArgSeq>
            :return: Options and arguments | None
            :rtype: <Optional[OptionNamespace]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method parse_args() must be implemented.")

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successfully finished) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method process() must be implemented.")
