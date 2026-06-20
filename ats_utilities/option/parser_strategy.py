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

from typing import Any, Dict, List, Optional
from argparse import ArgumentParser
from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.option.arg_parser import ArgParser
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.option.option_namespace import KnownArgs
from ats_utilities.info.info_keys import ATSInfoKeys
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ParserStrategy(IParserStrategy):
    '''
        Defines class ParserStrategy with attribute(s) and method(s).
        Default built-in strategy using Python's standard argparse module.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __shared_bundle - Bundle with checker, reporter and verbose (default ContextBundle).
                | __parser - Options parser (default None).
            :methods:
                | __init__ - Initials ParserStrategy constructor.
                | setup - Initializes the underlying parser with metadata parameters.
                | add_argument - Adds an operational argument/flag to the parser.
                | add_version - Adds a version display option to the parser.
                | parse - Parses the input arguments and returns an OptionNamespace.
                | __str__ - Returns the string representation of ParserStrategy.
    '''

    def __init__(self, context_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initializes ParserStrategy constructor.

            :param context_bundle: Context bundle for parser strategy | None.
            :type context_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, context_bundle)
        self.__shared_bundle: ContextBundle = ContextBundle(
            checker=get_private_attr(self, 'checker'),
            reporter=get_private_attr(self, 'reporter'),
            verbose=get_private_attr(self, 'verbose')
        )
        self.__parser: Optional[ArgumentParser] = None

    @validator([('dict:parameters', None)])
    def setup(self, parameters: Dict[str, str]) -> None:
        '''
            Initializes the underlying parser with metadata parameters.

            :param parameters: Parameters for logger.
            :type parameters: <Dict[str, str]>
            :exceptions: ATSTypeError, ATSValueError, RuntimeError, AttributeError
        '''
        self.__parser = make_component(None, ArgParser, {
            'context_bundle': self.__shared_bundle,
            'prog': f'{parameters.get(ATSInfoKeys.ATS_NAME)} {parameters.get(ATSInfoKeys.ATS_VERSION)}',
            'epilog': f'{parameters.get(ATSInfoKeys.ATS_NAME)} copyright (c) {parameters.get(ATSInfoKeys.ATS_LICENCE)}',
            'description': f'{parameters.get(ATSInfoKeys.ATS_NAME)} build date {parameters.get(ATSInfoKeys.ATS_BUILD_DATE)}'
        })
        validate_component(self.__parser, type(self.__parser), type(self.__parser).__name__)

    def add_argument(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an operational argument/flag to the parser.

            :param args: List of flags for the ATS.
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <Any>
            :exceptions: None
        '''
        if self.__parser:
            self.__parser.add_argument(*args, **kwargs)

    def add_version(self, version: Optional[str]) -> None:
        '''
            Adds a version display option to the parser.

            :param version: The ATS version | None.
            :type version: <Optional[str]>
            :exceptions: None
        '''
        if self.__parser and version:
            self.__parser.add_argument('--version', action='version', version=version)

    def parse(self, arguments: OptArgs, known_only: bool = False) -> OptionNamespace:
        '''
            Parses the input arguments and returns an OptionNamespace.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :param known_only: Parse only known arguments (default False).
            :type known_only: <bool>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions: RuntimeError
        '''
        if not self.__parser:
            raise RuntimeError('Parser strategy is not initialized.')

        if known_only:
            known_args: KnownArgs = self.__parser.parse_known_args(arguments)
            return known_args[0]
        return self.__parser.parse_args(arguments)

    def __str__(self) -> str:
        '''
            Returns the string representation of ParserStrategy.

            :return: The ParserStrategy as string representation.
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
