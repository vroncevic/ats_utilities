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

from typing import Any, ClassVar, List, Dict, Optional
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.option.ioption_parser import IATSOptionParser
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.option_namespace import OptArgs
from ats_utilities.option.iparser_strategy import IATSArgParseStrategy
from ats_utilities.option.ats_parser_strategy import ATSArgParseStrategy

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
                | ERRORS - Marks error types.
                | __checker - Parameters checker instance.
                | __reporter - ATSReporter for outputting messages.
                | __verbose - Enable/Disable verbose option.
                | __opt_parser - Options parser.
            :methods:
                | __init__ - Initials ATSDefaultOptionParser constructor.
                | add_operation - Adds an option to the ATS parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        parameters: Dict[str, str],
        strategy: Optional[IATSArgParseStrategy] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSOptionParser constructor.

            :param parameters: Parameters for logger
            :type parameters: <Dict[str, str]>
            :param strategy: Strategy for argument parsing | None
            :type strategy: <Optional[IATSArgParseStrategy]>
            :param checker: Parameters checker instance | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for outputting messages | None 
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('dict:parameters', parameters)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__strategy: IATSArgParseStrategy = strategy or ATSArgParseStrategy(self.__reporter)
        self.__strategy.setup(parameters)

    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the ATS parser.

            :param args: List of flags for the ATS
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <Any>
            :exceptions: None
        '''
        self.__strategy.add_argument(*args, **kwargs)

    def add_version_operation(self, version: Optional[str], verbose: bool = False) -> None:
        '''
            Adds version option to the ATS parser.

            :param version: The ATS version
            :type version: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        if version:
            self.__strategy.add_version(version)

    def parse_input_args(self, arguments: OptArgs, verbose: bool = False) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: None
        '''
        args = self.__strategy.parse(arguments, known_only=False)
        self.__reporter.verbose(self.__verbose or verbose, [f'arguments {arguments}'])
        return args

    def parse_args(self, arguments: OptArgs, verbose: bool = False) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Option namespace object
            :rtype: <OptionNamespace>
            :exceptions: None
        '''
        args = self.__strategy.parse(arguments, known_only=True)
        self.__reporter.verbose(self.__verbose or verbose, [f'arguments {arguments}'])
        return args
