# -*- coding: UTF-8 -*-

'''
Module
    ioption_parser.py
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
    Defines abstract class IATSOptionParser with attribute(s) and method(s).
    Creates an interfaces for ATS option parsing.
'''

from abc import ABC, abstractmethod
from typing import Any, List, Optional
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IATSOptionParser(ABC):
    '''
        Defines abstract class IATSOptionParser with attribute(s) and method(s).
        Creates an interfaces for ATS option parsing.

        It defines:

            :attributes: None
            :methods:
                | add_operation - Adds an option to the ATS parser.
                | add_version_operation - Adds version option to the ATS parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
    '''

    @abstractmethod
    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the ATS parser.

            :param args: List of flags for the ATS
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <Any>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method add_operation() must be implemented.")

    @abstractmethod
    def add_version_operation(self, version: Optional[str]) -> None:
        '''
            Adds version option to the ATS parser.

            :param version: The ATS version
            :type version: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method add_version_operation() must be implemented.")

    @abstractmethod
    def parse_input_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :return: option namespace object
            :rtype: <OptionNamespace>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method parse_input_args() must be implemented.")

    @abstractmethod
    def parse_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method parse_args() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS option parser.

            :return: The ATS option parser as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
