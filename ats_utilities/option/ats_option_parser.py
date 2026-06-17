# -*- coding: utf-8 -*-

'''
Module
    ats_option_parser.py
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
    Defines class ATSDefaultOptionParser with attribute(s) and method(s).
    Creates an option parser based on the argparse argument processor.
'''

from typing import Any, List, Dict, Optional
from ats_utilities.factory_class import inject, get_private_attr, format_instance_to_string
from ats_utilities.option.ioption_parser import IATSOptionParser
from ats_utilities.option.iparser_strategy import IATSArgParseStrategy
from ats_utilities.option.ats_parser_strategy import ATSArgParseStrategy
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSOptionParser(IATSOptionParser):
    '''
        Defines class ATSDefaultOptionParser with attribute(s) and method(s).
        Creates an option parser based on the argparse argument processor.
        Mechanism for application, tool, or script option parser.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __strategy - Strategy for argument parsing (default ATSArgParseStrategy).
            :methods:
                | __init__ - Initials ATSDefaultOptionParser constructor.
                | add_operation - Adds an option to the ATS parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
                | add_version_operation - Adds version option to the ATS parser.
                | _strategy - Property method for getting the internal strategy instance.
                | __str__ - Returns the string representation of ATSOptionParser.
    '''

    def __init__(
        self,
        parameters: Dict[str, str],
        strategy: Optional[IATSArgParseStrategy] = None,
        checker: Optional[IChecker] = None,
        reporter: Optional[IReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSOptionParser constructor.

            :param parameters: Parameters for logger
            :type parameters: <Dict[str, str]>
            :param strategy: Strategy for argument parsing | None
            :type strategy: <Optional[IATSArgParseStrategy]>
            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IChecker]>
            :param reporter: ATSReporter for outputting messages | None 
            :type reporter: <Optional[IReporter]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions: ATSTypeError by validates_parameters
        '''
        # No dependency injection then use default ones.
        inject(
            self,
            ('checker', checker, ATSChecker, None),
            ('reporter', reporter, ATSReporter, ['checker']),
            ('verbose', verbose, False, None),
            ('strategy', strategy, ATSArgParseStrategy, ['checker', 'reporter', 'verbose'])
        )
        self._strategy.setup(parameters)

    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the ATS parser.

            :param args: List of flags for the ATS
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <Any>
            :exceptions: None
        '''
        self._strategy.add_argument(*args, **kwargs)

    @validator([('Optional[str]:version', None)])
    @vreporter('add version {version}')
    def add_version_operation(self, version: Optional[str]) -> None:
        '''
            Adds version option to the ATS parser.

            :param version: The ATS version in string format | None
            :type version: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        if version:
            self._strategy.add_version(version)

    @vreporter('parse inout args arguments {arguments}')
    def parse_input_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        args = self._strategy.parse(arguments, known_only=False)
        return args

    @vreporter('parse args arguments {arguments}')
    def parse_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        args = self._strategy.parse(arguments, known_only=True)
        return args

    @property
    def _strategy(self) -> IATSArgParseStrategy:
        '''
            Property method for getting the internal strategy instance.

            :return: The strategy instance in IATSArgParseStrategy format
            :rtype: <IATSArgParseStrategy>
            :exceptions: None
        '''
        return get_private_attr(self, 'strategy')

    def __str__(self) -> str:
        '''
            Returns the string representation of ATSOptionParser.

            :return: The ATS option parser as string
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
