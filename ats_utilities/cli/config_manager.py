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
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.cfg.cfg_loader import CfgLoader
from ats_utilities.config_io.ini.inibase import IniBase
from ats_utilities.config_io.json.jsonbase import JsonBase
from ats_utilities.config_io.xml.xmlbase import XmlBase
from ats_utilities.config_io.yaml.yamlbase import YamlBase
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.option.iparser_strategy import IArgParserStrategy
from ats_utilities.cli.iconfig_manager import IConfigManager
from ats_utilities.cli.iconfig_manager import Config

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
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
                | __info_manager - Information manager.
                | __strategy - Strategy for argument parsing.
                | __options_parser - Option parser for CLI arguments.
                | __checker - Checker for parameter validation.
                | __reporter - Reporter for console output.
                | __file_checker - Checker for file operations.
            :methods:
                | load_config - Loads the appropriate configuration base based on file type.
    '''

    def __init__(
        self,
        config2object: Optional[IRead] = None,
        object2config: Optional[IWrite] = None,
        info_manager: Optional[IInfoManager] = None,
        strategy: Optional[IArgParserStrategy] = None,
        options_parser: Optional[IOptionManager] = None,
        checker: Optional[IChecker] = None,
        reporter: Optional[IReporter] = None,
        file_checker: Optional[IFileCheck] = None,
    ) -> None:
        '''
            Initializes ATSConfigManager constructor.

            :param config2object: Object for converting configuration to object | None
            :type config2object: <Optional[IRead]>
            :param object2config: Object for converting object to configuration | None
            :type object2config: <Optional[IWrite]>
            :param info_manager: Information manager | None
            :type info_manager: <Optional[IInfoManager]>
            :param strategy: Strategy for argument parsing | None
            :type strategy: <Optional[IArgParserStrategy]>
            :param options_parser: Option parser for CLI arguments | None
            :type options_parser: <Optional[IOptionManager]>
            :param checker: Checker for parameter validation | None
            :type checker: <Optional[IChecker]>
            :param reporter: Reporter for console output | None
            :type reporter: <Optional[IReporter]>
            :param file_checker: Checker for file operations | None
            :type file_checker: <Optional[IFileCheck]>
            :exceptions: None
        '''
        self.__config2object = config2object
        self.__object2config = object2config
        self.__info_manager = info_manager
        self.__strategy = strategy
        self.__options_parser = options_parser
        self.__checker = checker
        self.__reporter = reporter
        self.__file_checker = file_checker

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
            self.__info_manager,
            self.__strategy,
            self.__options_parser,
            self.__checker,
            self.__reporter,
            self.__file_checker,
            verbose
        )

        match file_format:
            case 'cfg':
                return CfgLoader(*common_base_args)
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
