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
    Defines class ParserStrategy with attribute(s) and method(s).
    Creates an interfaces for ATS option parsing.
'''

from __future__ import annotations

import sys
from collections.abc import Sequence, Mapping
from typing import Any, override
from types import MappingProxyType

from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.option.strategy.data_validator import StrategyDataValidator
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.data import ParserData
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.option.option_namespace import KnownArgs
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ParserStrategy(IParserStrategy):
    '''
        Defines class ParserStrategy with attribute(s) and method(s).
        Default built-in strategy using Python's standard argparse module.
        Note: If extern argument parser strategy is injected this object
        is not instantiated (then the complete strategy is provided by 
        external parser strategy).

        It defines:

            :attributes:
                | _context - Shared context for components.
                | _parser - Options parser.
                | _parser_class - Injected parser class.
                | _subparsers - Subparsers instance.
            :methods:
                | __init__ - Initials ParserStrategy constructor.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
                | register_commands - Registers a list of commands with the parser.
                | parse_command - Parses the input arguments and returns command name and parameters.
                | is_initialized - Checks if the parser strategy is initialized.
                | __str__ - Returns the string representation of ParserStrategy.
    '''

    _context: ContextBundle
    _parser: IArgParser
    _parser_class: type[IArgParser]
    _subparsers: Any

    def __init__(self, strategy_data: StrategyData) -> None:
        '''
            Initializes ParserStrategy constructor.

            :param strategy_data: Strategy data for parser strategy.
            :type strategy_data: StrategyData
            :exceptions:
                | ATSValueError: Strategy data must be provided.
                | ATSTypeError: Strategy data must be a StrategyData instance.
                | ATSTypeError: Parser class must be an IArgParser subclass.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSTypeError: Parser must be an IArgParser instance.
        '''
        context: str = r'parser_strategy::init(...)'
        StrategyDataValidator.validate(strategy_data)
        self._context = strategy_data.context_bundle
        self._parser_class = strategy_data.parser_class
        parser_data = ParserData(
            context_bundle=self._context,
            prog=f"{strategy_data.parameters.get(InfoKeys.ATS_NAME, '')} {strategy_data.parameters.get(InfoKeys.ATS_VERSION, '')}",
            epilog=f"{strategy_data.parameters.get(InfoKeys.ATS_NAME, '')} copyright (c) {strategy_data.parameters.get(InfoKeys.ATS_LICENCE, '')}",
            description=f"{strategy_data.parameters.get(InfoKeys.ATS_NAME, '')} build date {strategy_data.parameters.get(InfoKeys.ATS_BUILD_DATE, '')}"
        )
        self._parser = self._parser_class(own=parser_data)
        istype(self._parser, IArgParser, context, r'parser must be an IArgParser instance')

    @has_attrs('_parser')
    @override
    def add_argument(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: Sequence of flags for the ATS.
            :type args: Sequence[str]
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: Mapping[str, Any]
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        self._parser.add_argument(*args, **kwargs)

    @has_attrs('_parser')
    @override
    def add_version(self, version: str | None) -> None:
        '''
            Adds a version display option to the parser.

            :param version: The ATS version | None.
            :type version: str | None
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        self._parser.add_argument('--version', action='version', version=version)

    @has_attrs('_parser')
    @override
    def parse(self, arguments: OptArgs, known_only: bool = False) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param arguments: Sequence of arguments | None.
            :type arguments: OptArgs
            :param known_only: Parse only known arguments (default False).
            :type known_only: bool
            :return: Option namespace object.
            :rtype: OptionNamespace
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        if known_only:
            known_args: KnownArgs = self._parser.parse_known_args(arguments)
            return known_args[0]

        return self._parser.parse_args(arguments)

    @has_attrs('_parser')
    @override
    def register_commands(self, commands: Sequence[IOptionCommand]) -> None:
        '''
            Registers the list of commands with the parser.

            :param commands: Sequence of commands to register (read only data).
            :type commands: Sequence[IOptionCommand]
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
                kwargs: dict[str, Any] = {}

                if getattr(opt, 'action', None) is not None:
                    kwargs['action'] = opt.action
                else:
                    if opt.choices is not None:
                        kwargs['choices'] = opt.choices

                    if getattr(opt, 'nargs', None) is not None:
                        kwargs['nargs'] = opt.nargs

                if opt.default is not None:
                    kwargs['default'] = opt.default

                if opt.required:
                    kwargs['required'] = opt.required

                kwargs['help'] = opt.help_text
                cmd_parser.add_argument(opt.name, **kwargs)

    @has_attrs('_parser')
    @override
    def parse_command(self, arguments: OptArgs = None) -> tuple[str, Mapping[str, Any]]:
        '''
            Parses the input arguments and returns command name and parameters.

            :param arguments: Sequence of arguments | None.
            :type arguments: OptArgs
            :return: Tuple containing command name and parsed parameters (read only data).
            :rtype: tuple[str, Mapping[str, Any]]
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        if arguments is None:
            arguments: OptArgs = sys.argv[1:]

        option_namespace: OptionNamespace = self._parser.parse_args(arguments)
        params: dict[str, Any] = vars(option_namespace)
        command_name: str = params.pop('command')

        return command_name, MappingProxyType(params)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the parser strategy is initialized.

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        return True

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ParserStrategy.

            :return: The ParserStrategy as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
