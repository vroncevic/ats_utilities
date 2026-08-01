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
    Defines ParserAdapter with attribute(s) and method(s).
    Provides an API for the parser adapter.
'''

from __future__ import annotations

from argparse import ArgumentParser
from ats_utilities.option.setup.types import OptionNamespace, OptArgs, KnownArgs
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ParserAdapter:
    '''
        Defines ParserAdapter with attribute(s) and method(s).
        Provides an API for the parser adapter.

        It defines:

            :attributes:
                | _parser - The underlying parser instance.
            :methods:
                | __init__ - Initializes parser adapter.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_subparsers - Adds subparsers to the parser.
                | parse_args - Parses the input arguments and returns an OptionNamespace.
                | parse_known_args - Parses known input arguments.
                | __str__ - Returns the parser adapter as a string representation.
    '''

    _parser: ArgumentParser

    def __init__(self, parser: ArgumentParser) -> None:
        '''
            Initializes parser adapter.

            :param parser: The underlying parser instance.
            :exceptions: None.
        '''
        self._parser = parser

    def add_argument(self, *args: str, **kwargs: object) -> object:
        '''
            Adds an operational argument/flag to the parser.

            :param args: The flags/arguments.
            :param kwargs: The arguments as dictionary.
            :return: The added action object.
            :exceptions: None.
        '''
        return self._parser.add_argument(*args, **kwargs)

    def add_subparsers(self, **kwargs: object) -> object:
        '''
            Adds subparsers to the parser.

            :param kwargs: The arguments as dictionary.
            :return: The subparsers action object.
            :exceptions: None.
        '''
        return self._parser.add_subparsers(**kwargs)

    def parse_args(self, args: OptArgs = None) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param args: The sequence of arguments.
            :return: The option namespace object.
            :exceptions: None.
        '''
        return self._parser.parse_args(args)

    def parse_known_args(self, args: OptArgs = None) -> KnownArgs:
        '''
            Parses known input arguments.

            :param args: The sequence of arguments.
            :return: The tuple containing option namespace and unknown arguments.
            :exceptions: None.
        '''
        return self._parser.parse_known_args(args)

    def __str__(self) -> str:
        '''
            Returns the parser adapter as a string representation.

            :return: The Parser adapter as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
