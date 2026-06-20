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
    Defines class OptionManager with attribute(s) and method(s).
    Creates an option parser based on the argparse argument processor.
'''

from typing import Any, List, Optional
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.option.parser_strategy import ParserStrategy
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class OptionManager(IOptionManager):
    '''
        Defines class OptionManager with attribute(s) and method(s).
        Creates an option parser based on the argparse argument processor.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __strategy - Strategy for argument parsing (default ParserStrategy).
            :methods:
                | __init__ - Initials OptionManager constructor.
                | add_operation - Adds an option to the ATS parser.
                | add_version_operation - Adds version option to the ATS parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
                | __str__ - Returns the string representation of OptionManager.
    '''

    def __init__(self, component_bundle: Optional[OptionComponentBundle] = None) -> None:
        '''
            Initializes OptionManager constructor.

            :param component_bundle: Bundle with components for option manager | None.
            :type component_bundle: <Optional[OptionComponentBundle]>
            :exceptions: ATSTypeError
        '''
        # No dependency injection then use default ones.
        bundle: OptionComponentBundle = component_bundle or OptionComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        shared_bundle: ContextBundle = ContextBundle(
            checker=get_private_attr(self, 'checker'),
            reporter=get_private_attr(self, 'reporter'),
            verbose=get_private_attr(self, 'verbose')
        )
        self.__strategy: IParserStrategy = make_component(
            bundle.strategy, ParserStrategy, {'context_bundle': shared_bundle}
        )
        validate_component(
            self.__strategy, type(self.__strategy), type(self.__strategy).__name__
        )
        self.__strategy.setup(bundle.parameters)

    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the ATS parser.

            :param args: List of flags for the ATS.
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <Any>
            :exceptions: None
        '''
        self.__strategy.add_argument(*args, **kwargs)

    @validator([('Optional[str]:version', None)])
    @vreporter('add version {version}')
    def add_version_operation(self, version: Optional[str]) -> None:
        '''
            Adds version option to the ATS parser.

            :param version: The ATS version in string format | None.
            :type version: <Optional[str]>
            :exceptions: ATSTypeError, ATSValueError, RuntimeError, AttributeError
        '''
        if version:
            self.__strategy.add_version(version)

    @vreporter('parse inout args arguments {arguments}')
    def parse_input_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions: RuntimeError, AttributeError
        '''
        args = self.__strategy.parse(arguments, known_only=False)
        return args

    @vreporter('parse args arguments {arguments}')
    def parse_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions: RuntimeError, AttributeError
        '''
        args = self.__strategy.parse(arguments, known_only=True)
        return args

    def __str__(self) -> str:
        '''
            Returns the string representation of OptionManager.

            :return: The ATS option parser as string representation.
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
