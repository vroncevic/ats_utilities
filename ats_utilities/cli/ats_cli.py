# -*- coding: UTF-8 -*-

'''
Module
    ats_cli.py
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
    Defines class ATSCli with attribute(s) and method(s).
    Creates an API for checks and loads an information argument parser.
'''

from typing import Any, List, Optional
from abc import abstractmethod
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.cli.icli import IATSCli
from ats_utilities.cli.icli import ArgSeq
from ats_utilities.cli.iconfig_manager import IConfigManager
from ats_utilities.cli.iconfig_manager import Config
from ats_utilities.cli.config_manager import ATSConfigManager

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class ATSCli(IATSCli):
    '''
        Defines class ATSCli with attribute(s) and method(s).
        Creates an API for checks and loads an information argument parser.
        Command-line interface configuration.

        It defines:

            :attributes:
                | __config - CLI configuration object.
                | __config_manager - Manager for configuration loading.
                | __operational - Status for tool | generator (default False).
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials ATSCli constructor.
                | is_operational - Checks is tool | generator operational.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations (Abstract).
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        config_manager: Optional[IConfigManager] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSCli constructor.

            :param info_file: Information file path | None
            :type info_file: <Optional[str]>
            :param config_manager: Configuration manager | None
            :type config_manager: <Optional[IConfigManager]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose: bool = verbose
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__operational: bool = False

        # Dependency Injection of the manager or use default
        self.__config_manager: IConfigManager = config_manager or ATSConfigManager(
            reporter=self.__reporter
        )
        self.__config: Config = self.__config_manager.load_config(info_file, verbose)
        self.__reporter.verbose(self.__verbose, ['init ATS cli'])

    def is_operational(self) -> bool:
        '''
            Checks is tool | generator operational.

            :return: True (tool | generator is operational) | False
            :rtype: <bool>
            :exceptions: None
        '''
        if self.__config:
            self.__operational = self.__config.is_tool_ok()
        return self.__operational

    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: arguments in Any form
            :type kwargs: <Any>
            :exceptions: None
        '''
        if self.__config and self.__config.option_parser:
            self.__config.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: ArgSeq) -> Optional[OptionNamespace]:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None
            :type argv: <ArgSeq>
            :return: Options and arguments
            :rtype: <Optional[OptionNamespace]>
            :exceptions: ATSTypeError
        '''
        if self.__config and self.__config.option_parser:
            return self.__config.option_parser.parse_args(argv)
        return None

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations (Abstract).

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successfully finished) | False
            :rtype: <bool>
            :exceptions: TypeError
        '''
        raise NotImplementedError("Method process() must be implemented.")
