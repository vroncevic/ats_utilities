# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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

import sys
from typing import Any, List, Optional, Sequence, TypeAlias, Union
from os.path import basename
from argparse import Namespace
from abc import abstractmethod

try:
    from ats_utilities.config_io.cfg import CfgBase
    from ats_utilities.config_io.ini import IniBase
    from ats_utilities.config_io.json import JsonBase
    from ats_utilities.config_io.xml import XmlBase
    from ats_utilities.config_io.yaml import YamlBase
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

# Optional string sequence type
ArgSeq: TypeAlias = Optional[Sequence[str]]

# Optional configuration type
Config = Optional[Union[CfgBase, IniBase, JsonBase, XmlBase, YamlBase]]


class ATSCli:
    '''
        Defines class ATSCli with attribute(s) and method(s).
        Creates an API for checks and loads an information argument parser.
        Command-line interface configuration.

        It defines:

            :attributes:
                | _config - CLI configuration object.
                | _operational - Status for tool | generator (default False).
                | _verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials ATSCli constructor.
                | _builder - Builds ATS cli configuration.
                | is_operational - Checks is tool | generator operational.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations (Abstract).
    '''

    def __init__(
        self, info_file: Optional[str], verbose: bool = False
    ) -> None:
        '''
            Initials ATSCli constructor.

            :param info_file: Information file path | None
            :type info_file: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self._operational: bool = False
        self._config: Config = self._builder(info_file, verbose)
        self._verbose: bool = verbose
        verbose_message(self._verbose, ['init ATS CFG cli'])

    def _builder(
        self, info_file: Optional[str], verbose: bool = False
    ) -> Config:
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
                cli_config = CfgBase(info_file, verbose)
            case 'ini':
                cli_config = IniBase(info_file, verbose)
            case 'json':
                cli_config = JsonBase(info_file, verbose)
            case 'xml':
                cli_config = XmlBase(info_file, verbose)
            case 'yaml':
                cli_config = YamlBase(info_file, verbose)
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
        if self._config:
            self._operational = self._config.tool_operational
        return self._operational

    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: arguments in Any form
            :type kwargs: <Any>
            :exceptions: None
        '''
        if self._config:
            self._config.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: ArgSeq) -> Optional[Namespace]:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None
            :type argv: <ArgSeq>
            :return: Options and arguments
            :rtype: <Optional[Namespace]>
            :exceptions: ATSTypeError
        '''
        if self._config:
            return self._config.option_parser.parse_args(argv)
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
