# -*- coding: UTF-8 -*-

'''
Module
    config_loader.py
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
    Defines class ATSConfigLoader with attribute(s) and method(s).
    Default implementation of IConfigLoader that encapsulates factory logic.
'''

from typing import List, Optional, cast
from os.path import basename
from ats_utilities.config_io.iconfig_loader import IConfigLoader
from ats_utilities.config_io.iconfig_loader import IConfigProcessor, Config
from ats_utilities.config_io.config_loader_bundle import ATSConfigLoaderBundle
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.config_io.cfg.cfg_loader import CFGLoader
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
from ats_utilities.config_io.ini.ini_loader import INILoader
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor
from ats_utilities.config_io.json.json_loader import JSONLoader
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.config_io.xml.xml_loader import XMLLoader
from ats_utilities.config_io.yaml.iyaml_processor import IYAMLProcessor
from ats_utilities.config_io.yaml.yaml_loader import YAMLLoader
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class ATSConfigLoader(IConfigLoader):
    '''
        Defines class ATSConfigLoader with attribute(s) and method(s).
        Default implementation of IConfigLoader that encapsulates factory logic.

        It defines:

            :attributes:
                | __info_file - Configuration file for loading process (default None).
                | __config2object - Convertor configuration to object (default None).
                | __config_bundle - ATS configuration file bundle (default None).
                | __processor - Interface for configuration processor (default None).
            :methods:
                | setup_config_loader - Setup config loader based on configuration file type.
                | __str__ - Returns the ATSConfigLoader as string representation.
    '''

    def __init__(self, config_loader_bundle: Optional[ATSConfigLoaderBundle] = None) -> None:
        '''
            Initializes ATSConfigLoader constructor.

            :param config_loader_bundle: Configuration file for loading process | None.
            :type config_loader_bundle: <Optional[ATSConfigLoaderBundle]>
            :exceptions: None.
        '''
        self.__info_file = config_loader_bundle.info_file
        self.__config2object = config_loader_bundle.config2object
        self.__config_bundle = config_loader_bundle.config_bundle
        self.__processor = config_loader_bundle.processor

    def setup_config_loader(self) -> Config:
        '''
            Setup config loader based on configuration file type.

            :return: Configuration loader object.
            :rtype: <Config>
            :exceptions: None.
        '''
        if not self.__info_file:
            return None

        file_format: str = basename(self.__info_file).split('.')[1]
        common_base_args = (self.__info_file, self.__config2object, self.__config_bundle)

        match file_format:
            case 'cfg':
                return CFGLoader(*common_base_args, cast(ICFGProcessor, self.__processor))
            case 'ini':
                return INILoader(*common_base_args, cast(IINIProcessor, self.__processor))
            case 'json':
                return JSONLoader(*common_base_args, cast(IJSONProcessor, self.__processor))
            case 'xml':
                return XMLLoader(*common_base_args, cast(IXMLProcessor, self.__processor))
            case 'yaml':
                return YAMLLoader(*common_base_args, cast(IYAMLProcessor, self.__processor))
            case _:
                return None

    def __str__(self) -> str:
        '''
            Returns the ATSConfigLoader as string representation.

            :return: The ATSConfigLoader as string representation.
            :rtype: <str>
            :exceptions: NotImplementedError.
        '''
        return format_instance_to_string(self)
