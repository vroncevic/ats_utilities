# -*- coding: UTF-8 -*-

'''
Module
    parser_strategy.py
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

from ats_utilities.option.strategy.parser_strategy_bundle import ParserStrategyBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.parser_registry import ParserRegistry
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.option.option_namespace import KnownArgs
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.context.context_bundle_inject import inject_context_bundle
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ParserStrategy(IParserStrategy):
    '''
        Defines class ParserStrategy with attribute(s) and method(s).
        Default built-in strategy using Python's standard argparse module.
        Note: If extern argument parser strategy is injected this object
              is not instantiated (then the complete strategy is provided
              by external parser strategy).

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _shared_context - Shared context for components.
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

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _shared_context: ContextBundle
    _parser: IArgParser
    _parser_class: type[IArgParser]
    _subparsers: Any

    def __init__(self, component_bundle: ParserStrategyBundle) -> None:
        '''
            Initializes ParserStrategy constructor.

            :param parameters: Metadata parameters in mapping format (read only data).
            :type parameters: <Mapping[str, str]>
            :param context_bundle: Context bundle for parser strategy.
            :type context_bundle: <ContextBundle>
            :param parser_class: Injected parser class type.
            :type parser_class: <type[IArgParser]>
            :exceptions: None.
        '''
        not_none(component_bundle, r'component_bundle must be provided')
        istype(component_bundle, ParserStrategyBundle, r'component_bundle must be a ParserStrategyBundle instance')
        self._shared_context = component_bundle.context_bundle
        inject_context_bundle(self, self._shared_context)
        self._parser_class = component_bundle.parser_class
        bundle = ParserRegistry.create_parser_bundle_from_dict(component_bundle.parameters, self._shared_context)
        self._parser = self._parser_class(component_bundle=bundle)
        istype(self._parser, IArgParser, r'parser must be an IArgParser instance')

    @has_attrs('_parser')
    @override
    def add_argument(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: List of flags for the ATS.
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <Any>
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
            :type version: <str | None>
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
            :type arguments: <OptArgs>
            :param known_only: Parse only known arguments (default False).
            :type known_only: <bool>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
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
            :type commands: <Sequence[IOptionCommand]>
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
            :type arguments: <OptArgs>
            :return: Tuple containing command name and parsed parameters (read only data).
            :rtype: <tuple[str, Mapping[str, Any]]>
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

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return True

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ParserStrategy.

            :return: The ParserStrategy as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
