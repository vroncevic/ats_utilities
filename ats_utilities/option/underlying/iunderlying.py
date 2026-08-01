# -*- coding: UTF-8 -*-

'''
Module
    iunderlying.py
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
    Defines the IUnderlyingParser abstract class with method(s).
    Provides an interface for the underlying parser.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class IUnderlyingParser[NamespaceType, ArgsType, ActionType, SubparsersActionType, KnownArgsType](Protocol):
    '''
        Defines the IUnderlyingParser abstract class with method(s).
        Provides an interface for the underlying parser.

        It defines:

            :methods:
                | add_argument - Adds an operational argument/flag to the parser.
                | add_subparsers - Adds subparsers to the parser.
                | parse_args - Parses the input arguments.
                | parse_known_args - Parses known input arguments.
    '''

    def add_argument(self, *args: str, **kwargs: object) -> ActionType:
        '''
            Adds an operational argument/flag to the parser.

            :param args: The flags/arguments.
            :param kwargs: The arguments as dictionary.
            :return: The added argument/flag.
        '''
        ...

    def add_subparsers(self, **kwargs: object) -> SubparsersActionType:
        '''
            Adds subparsers to the parser.

            :param kwargs: The arguments as dictionary.
            :return: The added subparsers container.
        '''
        ...

    def parse_args(self, args: ArgsType) -> NamespaceType:
        '''
            Parses the input arguments.

            :param args: The sequence of arguments.
            :return: The container with parsed arguments.
        '''
        ...

    def parse_known_args(self, args: ArgsType) -> KnownArgsType:
        '''
            Parses known input arguments.
 
            :param args: The sequence of arguments.
            :return: The container with parsed known arguments.
        '''
        ...
