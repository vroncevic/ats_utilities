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

import sys
from typing import Any, Dict, List, Optional, NoReturn
from argparse import ArgumentParser
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.option.option_namespace import KnownArgs
from ats_utilities.option.iparser_strategy import IATSArgParseStrategy


__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class _ATSArgumentParser(ArgumentParser):
    '''
        Defines class _ATSArgumentParser with attribute(s) and method(s).
        Custom ArgumentParser to route errors to IATSReporter.

        It defines:

            :attributes:
                | __reporter - ATSReporter for outputting messages.
            :methods:
                | __init__ - Initials _ATSArgumentParser constructor.
                | error - Overrides default error handling to use IATSReporter.
    '''

    def __init__(
        self,
        reporter: Optional[IATSReporter],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        '''
            Initials _ATSArgumentParser constructor.

            :param reporter: ATSReporter for outputting messages
            :type reporter: <Optional[IATSReporter]>
            :param args: Additional positional arguments
            :type args: <Any>
            :param kwargs: Additional keyword arguments
            :type kwargs: <Any>
            :exceptions: None
        '''
        super().__init__(*args, **kwargs)
        # No dependency injection then use default ones.
        self.__reporter: IATSReporter = reporter or ATSReporter()

    def error(self, message: str) -> NoReturn:
        '''
            Overrides default error handling to use IATSReporter.

            :param message: Error message to report
            :type message: <str>
            :return: None
            :rtype: <NoReturn>
            :exceptions: None
        '''
        self.__reporter.error([f'argument error: {message}'])
        sys.exit(2)


class ATSArgParseStrategy(IATSArgParseStrategy):
    '''
        Defines class ATSArgParseStrategy with attribute(s) and method(s).
        Default built-in strategy using Python's standard argparse module.
        Requires zero external dependencies.

        It defines:

            :attributes:
                | __reporter - ATSReporter for outputting messages.
                | __parser - Options parser.
            :methods:
                | __init__ - Initials ATSArgParseStrategy constructor.
                | setup - Initializes the underlying parser with metadata parameters.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
    '''

    def __init__(self, reporter: Optional[IATSReporter]) -> None:
        '''
            Initials ATSArgParseStrategy constructor.

            :param reporter: ATSReporter for outputting messages
            :type reporter: <Optional[IATSReporter]>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        self.__reporter = reporter or ATSReporter()
        self.__parser: Optional[ArgumentParser] = None

    def setup(self, parameters: Dict[str, str]) -> None:
        '''
            Initializes the underlying parser with metadata parameters.

            :param parameters: Parameters for logger
            :type parameters: <Dict[str, str]>
            :exceptions: None
        '''
        self.__parser = _ATSArgumentParser(
            self.__reporter,
            prog=f'{parameters.get("name")} {parameters.get("version")}',
            epilog=parameters.get("epilog"),
            description=parameters.get("description")
        )

    def add_argument(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: List of flags for the ATS
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <Any>
            :exceptions: None
        '''
        if self.__parser:
            self.__parser.add_argument(*args, **kwargs)

    def add_version(self, version: Optional[str]) -> None:
        '''
            Adds a version display option to the parser.

            :param version: The ATS version
            :type version: <Optional[str]>
            :exceptions: None
        '''
        if self.__parser and version:
            self.__parser.add_argument('--version', action='version', version=version)

    def parse(self, arguments: OptArgs, known_only: bool = False) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :param known_only: Parse only known arguments
            :type known_only: <bool>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: RuntimeError
        '''
        if not self.__parser:
            raise RuntimeError("Parser strategy is not initialized.")

        if known_only:
            known_args: KnownArgs = self.__parser.parse_known_args(arguments)
            return known_args[0]
        return self.__parser.parse_args(arguments)
