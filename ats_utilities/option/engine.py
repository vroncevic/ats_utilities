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

from typing import Any
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.option.parser_strategy import ParserStrategy
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_runtime_error import ATSRuntimeError
from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_class_name, format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
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
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _is_initialized - Indicates if the option manager component is initialized (default False).
                | _strategy - Strategy for argument parsing (default ParserStrategy).
            :methods:
                | __init__ - Initials OptionManager constructor.
                | add_operation - Adds an option to the ATS parser.
                | add_version_operation - Adds version option to the ATS parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
                | is_initialized - Checks if the option manager component is initialized.
                | __str__ - Returns the string representation of OptionManager.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, component_bundle: OptionComponentBundle | None = None) -> None:
        '''
            Initializes OptionManager constructor.

            :param component_bundle: Bundle with components for option manager | None.
            :type component_bundle: <OptionComponentBundle | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        bundle: OptionComponentBundle = component_bundle or OptionComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        shared_bundle: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        self._is_initialized: bool = False

        try:
            self._strategy: IParserStrategy = make_component(
                bundle.strategy, ParserStrategy, {'context_bundle': shared_bundle}
            )
            validate_component(self._strategy, ParserStrategy) if not bundle.strategy else None
            self._strategy.setup(bundle.parameters)
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            self._reporter.error([f"{get_class_name(self)} - error during initialization: {exc}"])

    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the ATS parser.

            :param args: List of flags for the ATS.
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <Any>
            :exceptions: None.
        '''
        self._strategy.add_argument(*args, **kwargs)

    @validator([('str | None:version', None)])
    @vreporter('add version {version}')
    def add_version_operation(self, version: str | None) -> None:
        '''
            Adds version option to the ATS parser.

            :param version: The ATS version in string format | None.
            :type version: <str | None>
            :exceptions: ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError.
        '''
        if version:
            self._strategy.add_version(version)

    @vreporter('parse inout args arguments {arguments}')
    def parse_input_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        args = self._strategy.parse(arguments, known_only=False)
        return args

    @vreporter('parse args arguments {arguments}')
    def parse_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        args = self._strategy.parse(arguments, known_only=True)
        return args

    def is_initialized(self) -> bool:
        '''
            Checks if option parser component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized and self._strategy.is_initialized()

    def __str__(self) -> str:
        '''
            Returns the string representation of OptionManager.

            :return: The ATS option parser as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
