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

from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.option.arg_parser import ArgParser
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.option.option_namespace import KnownArgs
from ats_utilities.option.ioption_command import IOptionCommand
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import has_attrs, to_str

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ParserStrategy(IParserStrategy):
    '''
        Defines class ParserStrategy with attribute(s) and method(s).
        Default built-in strategy using Python's standard argparse module.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _parser - Options parser (default None).
            :methods:
                | __init__ - Initials ParserStrategy constructor.
                | setup - Initializes the underlying parser with metadata parameters.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
                | register_commands - Registers a list of commands with the parser.
                | parse_command - Parses the input arguments and returns command name and parameters.
                | is_initialized - Checks if the parser strategy is initialized.
                | __str__ - Returns the string representation of ParserStrategy.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _parser: ArgParser | None

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes ParserStrategy constructor.

            :param context_bundle: Context bundle for parser strategy | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._parser = None

    @vcheck([('Mapping:parameters', None)])
    @override
    def setup(self, parameters: Mapping[str, str]) -> None:
        '''
            Initializes the underlying parser with metadata parameters.

            :param parameters: Metadata parameters in mapping format (read only data).
            :type parameters: <Mapping[str, str]>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._parser = make_component(None, ArgParser, {
            'context_bundle': ContextBundle(checker=self._checker, reporter=self._reporter, verbose=self._verbose),
            'prog': f'{parameters.get(InfoKeys.ATS_NAME)} {parameters.get(InfoKeys.ATS_VERSION)}',
            'epilog': f'{parameters.get(InfoKeys.ATS_NAME)} copyright (c) {parameters.get(InfoKeys.ATS_LICENCE)}',
            'description': f'{parameters.get(InfoKeys.ATS_NAME)} build date {parameters.get(InfoKeys.ATS_BUILD_DATE)}'
        })
        validate_component(self._parser, ArgParser)

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
                dest="command", required=True, help="Available commands"
            )

        for cmd in commands:
            cmd_parser = self._subparsers.add_parser(cmd.name, help=cmd.help_text)

            for opt in cmd.options:
                kwargs: dict[str, Any] = {}

                if getattr(opt, 'action', None) is not None:
                    kwargs["action"] = opt.action
                else:
                    if opt.choices is not None:
                        kwargs["choices"] = opt.choices

                    if getattr(opt, 'nargs', None) is not None:
                        kwargs["nargs"] = opt.nargs

                if opt.default is not None:
                    kwargs["default"] = opt.default

                if opt.required:
                    kwargs["required"] = opt.required

                kwargs["help"] = opt.help_text
                cmd_parser.add_argument(opt.name, **kwargs)

    @has_attrs('_parser')
    @override
    def parse_command(self, arguments: OptArgs = None) -> tuple[str, dict[str, Any]]:
        '''
            Parses the input arguments and returns command name and parameters.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Tuple containing command name and parsed parameters.
            :rtype: <tuple[str, dict[str, Any]]>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_parser'.
        '''
        if arguments is None:
            arguments: OptArgs = sys.argv[1:]

        option_namespace: OptionNamespace = self._parser.parse_args(arguments)
        params: dict[str, Any] = vars(option_namespace)
        command_name: str = params.pop("command", "")

        return command_name, params

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if parser strategy component is ok.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        return True if self._parser is not None else False

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ParserStrategy.

            :return: The ParserStrategy as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
