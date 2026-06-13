# -*- coding: UTF-8 -*-

'''
Module
    iparser_strategy.py
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
from typing import Any, Dict, List, Optional
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


class IATSArgParseStrategy(ABC):
    '''
        Defines abstract class IATSArgParseStrategy with attribute(s) and method(s).
        Interface for concrete parsing engines (Strategy Pattern).
        Allows third-party parsers to be injected from the outside.

        It defines:

            :attributes: None
            :methods:
                | setup - Initializes the underlying parser with metadata parameters.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
    '''

    @abstractmethod
    def setup(self, parameters: Dict[str, str]) -> None:
        '''
            Initializes the underlying parser with metadata parameters.

            :param parameters: Parameters for logger
            :type parameters: <Dict[str, str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method setup() must be implemented.")

    @abstractmethod
    def add_argument(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: List of flags for the ATS
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <Any>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method add_argument() must be implemented.")

    @abstractmethod
    def add_version(self, version: Optional[str]) -> None:
        '''
            Adds a version display option to the parser.

            :param version: The ATS version
            :type version: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method add_version() must be implemented.")

    @abstractmethod
    def parse(self, arguments: OptArgs, known_only: bool = False) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :param known_only: Parse only known arguments
            :type known_only: <bool>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method parse() must be implemented.")
