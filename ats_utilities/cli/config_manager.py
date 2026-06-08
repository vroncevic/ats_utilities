# -*- coding: UTF-8 -*-

'''
Module
    config_manager.py
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
    Defines class ATSConfigManager with attribute(s) and method(s).
    Default implementation of IConfigManager that encapsulates factory logic.
'''

from typing import List, Optional
from os.path import basename
from ats_utilities.config_io import IFileCheck, IRead, IWrite
from ats_utilities.config_io.cfg import CfgBase
from ats_utilities.config_io.ini import IniBase
from ats_utilities.config_io.json import JsonBase
from ats_utilities.config_io.xml import XmlBase
from ats_utilities.config_io.yaml import YamlBase
from ats_utilities.console_io import IATSReporter
from ats_utilities.checker import IATSChecker
from ats_utilities.option import IATSOptionParser, IATSArgParseStrategy
from .iconfig_manager import IConfigManager, Config

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class ATSConfigManager(IConfigManager):
    '''
        Default implementation of IConfigManager that encapsulates factory logic.

        It defines:

            :attributes:
                | __config2object - Object for converting configuration to object.
                | __object2config - Object for converting object to configuration.
                | __options_parser - Option parser for CLI arguments.
                | __checker - Checker for parameter validation.
                | __reporter - Reporter for console output.
                | __file_checker - Checker for file operations.
                | __strategy - Strategy for argument parsing.
            :methods:
                | load_config - Loads the appropriate configuration base based on file type.
    '''

    def __init__(
        self,
        config2object: Optional[IRead] = None,
        object2config: Optional[IWrite] = None,
        options_parser: Optional[IATSOptionParser] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        strategy: Optional[IATSArgParseStrategy] = None
    ) -> None:
        '''
            Initializes ATSConfigManager constructor.

            :param config2object: Object for converting configuration to object | None
            :type config2object: :class:`~ats_utilities.config_io.iread.IRead`
            :param object2config: Object for converting object to configuration | None
            :type object2config: :class:`~ats_utilities.config_io.iwrite.IWrite`
            :param options_parser: Option parser for CLI arguments | None
            :type options_parser: :class:`~ats_utilities.option.iatsoptionparser.IATSOptionParser`
            :param checker: Checker for parameter validation | None
            :type checker: :class:`~ats_utilities.checker.IATSChecker`
            :param reporter: Reporter for console output | None
            :type reporter: :class:`~ats_utilities.console_io.iats_reporter.IATSReporter`
            :param file_checker: Checker for file operations | None
            :type file_checker: :class:`~ats_utilities.config_io.ifile_check.IFileCheck`
            :param strategy: Strategy for argument parsing | None
            :type strategy: :class:`~ats_utilities.option.iats_arg_parse_strategy.IATSArgParseStrategy`
            :exceptions: None
        '''
        self.__config2object = config2object
        self.__object2config = object2config
        self.__options_parser = options_parser
        self.__checker = checker
        self.__reporter = reporter
        self.__file_checker = file_checker
        self.__strategy = strategy

    def load_config(self, info_file: Optional[str], verbose: bool = False) -> Config:
        '''
            Loads the appropriate configuration base based on file type.

            :param info_file: Path to information file.
            :type info_file: <Optional[str]>
            :param verbose: Verbose flag.
            :type verbose: <bool>
            :return: Configuration object.
            :rtype: <Config>
            :exceptions: None
        '''
        if not info_file:
            return None

        file_format = basename(info_file).split('.')[1]

        common_base_args = (
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

        match file_format:
            case 'cfg':
                return CfgBase(*common_base_args)
            case 'ini':
                return IniBase(*common_base_args)
            case 'json':
                return JsonBase(*common_base_args)
            case 'xml':
                return XmlBase(*common_base_args)
            case 'yaml':
                return YamlBase(*common_base_args)
            case _:
                return None
