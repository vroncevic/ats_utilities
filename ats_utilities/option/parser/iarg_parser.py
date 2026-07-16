# -*- coding: UTF-8 -*-

'''
Module
    iarg_parser.py
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
    Defines abstract class IArgParser with method(s).
    Interface for custom argument parser.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ats_utilities.option.parser.parser_bundle import ParserBundle
from ats_utilities.option.option_namespace import OptionNamespace, OptArgs, KnownArgs

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IArgParser(ABC):
    '''
        Defines abstract class IArgParser with method(s).
        Interface for custom argument parser.

        It defines:

            :methods:
                | add_argument - Adds an operational argument/flag to the parser.
                | parse_args - Parses the input arguments and returns an OptionNamespace.
                | parse_known_args - Parses the input arguments and returns an OptionNamespace and unknown arguments.
                | add_subparsers - Registers subparsers with the parser.
    '''

    @abstractmethod
    def __init__(self, component_bundle: ParserBundle | None = None) -> None:
        '''
            Initializes IArgParser.

            :param component_bundle: Bundle with components for argument parser | None.
            :type component_bundle: <ParserBundle | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_argument(self, *args: str, **kwargs: Any) -> Any:
        '''
            Adds an operational argument/flag to the parser.

            :param args: List of flags for the ATS.
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <Any>
            :return: Action/argument instance.
            :rtype: <Any>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_args(
        self,
        args: OptArgs = None,
        namespace: OptionNamespace | None = None
    ) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param args: Sequence of arguments | None.
            :type args: <OptArgs>
            :param namespace: Option namespace object | None.
            :type namespace: <OptionNamespace | None>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def parse_known_args(
        self,
        args: OptArgs = None,
        namespace: OptionNamespace | None = None
    ) -> KnownArgs:
        '''
            Parses the input arguments and returns an OptionNamespace and unknown arguments.

            :param args: Sequence of arguments | None.
            :type args: <OptArgs>
            :param namespace: Option namespace object | None.
            :type namespace: <OptionNamespace | None>
            :return: Tuple containing option namespace and unknown arguments.
            :rtype: <KnownArgs>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def add_subparsers(self, **kwargs: Any) -> Any:
        '''
            Registers subparsers with the parser.

            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <Any>
            :return: Action/subparser instance.
            :rtype: <Any>
            :exceptions: None.
        '''
        pass
