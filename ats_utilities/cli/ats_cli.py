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

from typing import Any, List, Optional, Union
from os.path import basename
from abc import abstractmethod
from ats_utilities.config_io import IFileCheck, IRead, IWrite
from ats_utilities.config_io.cfg import CfgBase
from ats_utilities.config_io.ini import IniBase
from ats_utilities.config_io.json import JsonBase
from ats_utilities.config_io.xml import XmlBase
from ats_utilities.config_io.yaml import YamlBase
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.checker import IATSChecker, ATSChecker
from ats_utilities.option import ATSOptionParser, OptionNamespace, IATSArgParseStrategy
from .icli import IATSCli, ArgSeq

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Optional configuration type
Config = Optional[Union[CfgBase, IniBase, JsonBase, XmlBase, YamlBase]]


class ATSCli(IATSCli):
    '''
        Defines class ATSCli with attribute(s) and method(s).
        Creates an API for checks and loads an information argument parser.
        Command-line interface configuration.

        It defines:

            :attributes:
                | __config - CLI configuration object.
                | __operational - Status for tool | generator (default False).
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials ATSCli constructor.
                | _builder - Builds ATS cli configuration.
                | is_operational - Checks is tool | generator operational.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations (Abstract).
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        config2object: Optional[IRead] = None,
        object2config: Optional[IWrite] = None,
        options_parser: Optional[ATSOptionParser] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        strategy: Optional[IATSArgParseStrategy] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSCli constructor.

            :param info_file: Information file path | None
            :type info_file: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__config2object: Optional[IRead] = config2object
        self.__object2config: Optional[IWrite] = object2config
        self.__file_checker: Optional[IFileCheck] = file_checker
        self.__options_parser: Optional[ATSOptionParser] = options_parser
        self.__strategy: Optional[IATSArgParseStrategy] = strategy
        self.__operational: bool = False
        self.__config: Config = self._builder(info_file, verbose)
        self.__reporter.verbose(self.__verbose, ['init ATS CFG cli'])

    def _builder(self, info_file: Optional[str], verbose: bool = False) -> Config:
        '''
            Builds ATS cli configuration.

            :param info_file: Information file path | None
            :type info_file: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: CLI configuration object | None
            :rtype: <Config>
            :exceptions: None
        '''
        cli_config: Config = None
        if not info_file:
            return cli_config
        file_format: str = basename(info_file).split('.')[1]
        match file_format:
            case 'cfg':
                cli_config = CfgBase(
                    info_file,
                    self.__config2object,
                    self.__object2config,
                    self.__options_parser,
                    self.__checker,
                    self.__reporter,
                    self.__file_checker,
                    self.__strategy,
                    verbose
                )
            case 'ini':
                cli_config = IniBase(
                    info_file,
                    self.__config2object,
                    self.__object2config,
                    self.__options_parser,
                    self.__checker,
                    self.__reporter,
                    self.__file_checker,
                    self.__strategy,
                    verbose
                )
            case 'json':
                cli_config = JsonBase(
                    info_file,
                    self.__config2object,
                    self.__object2config,
                    self.__options_parser,
                    self.__checker,
                    self.__reporter,
                    self.__file_checker,
                    self.__strategy,
                    verbose
                )
            case 'xml':
                cli_config = XmlBase(
                    info_file,
                    self.__config2object,
                    self.__object2config,
                    self.__options_parser,
                    self.__checker,
                    self.__reporter,
                    self.__file_checker,
                    self.__strategy,
                    verbose
                )
            case 'yaml':
                cli_config = YamlBase(
                    info_file,
                    self.__config2object,
                    self.__object2config,
                    self.__options_parser,
                    self.__checker,
                    self.__reporter,
                    self.__file_checker,
                    self.__strategy,
                    verbose
                )
            case _:
                cli_config = None
        return cli_config

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
        if self.__config:
            self.__config.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: ArgSeq) -> Optional[OptionNamespace]:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None
            :type argv: <ArgSeq>
            :return: Options and arguments
            :rtype: <Optional[Namespace]>
            :exceptions: ATSTypeError
        '''
        if self.__config:
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
            :exception: TypeError
        '''
        raise NotImplementedError("Subclasses must implement process method")
