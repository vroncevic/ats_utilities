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
    Defines the ParserStrategy class with attribute(s) and method(s).
    Creates an interfaces for ATS option parsing.
'''

from __future__ import annotations

from sys import argv
from collections.abc import Sequence
from types import MappingProxyType

from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.option.strategy.data_validator import StrategyDataValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.types import OptionNamespace, OptArgs, KnownArgs, ParsedCommand
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.option.underlying.iunderlying import IUnderlyingParser
from ats_utilities.utils.reflection import has_attrs, to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ParserStrategy:
    '''
        Defines the ParserStrategy class with attribute(s) and method(s).
        Default built-in strategy using Python's standard argparse module.
        Note: If extern argument parser strategy is injected this object
        is not instantiated (then the complete strategy is provided by 
        external parser strategy).

        It defines:

            :attributes:
                | _context - The shared context for components.
                | _parser - The options parser.
                | _subparsers - The subparsers.
            :methods:
                | __init__ - Initializes the ParserStrategy.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
                | register_commands - Registers a list of commands with the parser.
                | parse_command - Parses the input arguments and returns command name and parameters.
                | is_initialized - Checks if the parser strategy is initialized.
                | __str__ - Returns the string representation of ParserStrategy.
    '''

    _context: ContextBundle
    _parser: IUnderlyingParser
    _subparsers: object

    def __init__(self, strategy_data: StrategyData) -> None:
        '''
            Initializes the ParserStrategy.

            :param strategy_data: The strategy data for parser strategy.
            :exceptions:
                | ATSValueError: Strategy data must be provided.
                | ATSTypeError: Strategy data must be a StrategyData.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSValueError: Parser must be provided.
                | ATSTypeError: Parser must be an instance of IUnderlyingParser.
        '''
        StrategyDataValidator.validate(strategy_data)
        self._context = strategy_data.context_bundle
        self._parser = strategy_data.parser

    @has_attrs('_parser')
    def add_argument(self, *args: str, **kwargs: object) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: The sequence of flags for the ATS.
            :param kwargs: The arguments in shape of dictionary.
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        self._parser.add_argument(*args, **kwargs)

    @has_attrs('_parser')
    def add_version(self, version: str | None) -> None:
        '''
            Adds a version display option to the parser.

            :param version: The ATS version | None.
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        self._parser.add_argument('--version', action='version', version=version)

    @has_attrs('_parser')
    def parse(self, arguments: OptArgs, known_only: bool = False) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param arguments: Sequence of arguments | None.
            :param known_only: The parse only known arguments (default: False).
            :return: The option namespace object.
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        if known_only:
            known_args: KnownArgs = self._parser.parse_known_args(arguments)
            return known_args[0]

        return self._parser.parse_args(arguments)

    @has_attrs('_parser')
    def register_commands(self, commands: Sequence[IOptionCommand]) -> None:
        '''
            Registers the list of commands with the parser.

            :param commands: The sequence of commands to register (read only data).
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        if not hasattr(self, '_subparsers') or self._subparsers is None:
            self._subparsers = self._parser.add_subparsers(
                dest='command', required=True, help='Available commands'
            )

        for cmd in commands:
            cmd_parser = self._subparsers.add_parser(cmd.name, help=cmd.help_text)

            for opt in cmd.options:
                cmd_parser.add_argument(opt.name, **opt.to_kwargs())

    @has_attrs('_parser')
    def parse_command(self, arguments: OptArgs = None) -> ParsedCommand:
        '''
            Parses the input arguments and returns command name and parameters.

            :param arguments: Sequence of arguments | None.
            :return: The parsed command result.
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        if arguments is None:
            arguments: OptArgs = argv[1:]

        option_namespace: OptionNamespace = self._parser.parse_args(arguments)
        params: dict[str, object] = vars(option_namespace)
        command_name: str = params.pop('command')

        return command_name, MappingProxyType(params)

    def is_initialized(self) -> bool:
        '''
            Checks if the parser strategy is initialized.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return True

    def __str__(self) -> str:
        '''
            Returns the string representation of ParserStrategy.

            :return: The ParserStrategy as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
