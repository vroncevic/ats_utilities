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
    Defines class ConfigLoader with attribute(s) and method(s).
    Default implementation of IConfigLoader that encapsulates factory logic.
'''

from __future__ import annotations

from typing import cast, override
from os.path import basename

from ats_utilities.config_io.iconfig_loader import IConfigLoader
from ats_utilities.config_io.iconfig_loader import IConfigProcessor, Config
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.config_loader_bundle import ConfigLoaderBundle
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
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

class ConfigLoader(IConfigLoader):
    '''
        Defines class ConfigLoader with attribute(s) and method(s).
        Default implementation of IConfigLoader that encapsulates factory logic.

        It defines:

            :attributes:
                | _info_file - Configuration file for loading process (default None).
                | _config2object - Convertor configuration to object (default None).
                | _config_bundle - ATS configuration file bundle (default None).
                | _processor - Interface for configuration processor (default None).
            :methods:
                | setup_config_loader - Setup config loader based on configuration file type.
                | __str__ - Returns the ConfigLoader as string representation.
    '''

    _info_file: str | None
    _config2object: IRead | None
    _config_bundle: ConfigFileBundle | None
    _processor: IConfigProcessor | None

    def __init__(self, config_loader_bundle: ConfigLoaderBundle | None = None) -> None:
        '''
            Initializes ConfigLoader constructor.

            :param config_loader_bundle: Configuration file for loading process | None.
            :type config_loader_bundle: <ConfigLoaderBundle | None>
            :exceptions: None.
        '''
        self._info_file = config_loader_bundle.info_file
        self._config2object = config_loader_bundle.config2object
        self._config_bundle = config_loader_bundle.config_bundle
        self._processor = config_loader_bundle.processor

    @override
    def setup_config_loader(self) -> Config:
        '''
            Setup config loader based on configuration file type.

            :return: Configuration loader object.
            :rtype: <Config>
            :exceptions: None.
        '''
        if not self._info_file:
            return None

        file_format: str = basename(self._info_file).split('.')[1]
        common_base_args = (self._info_file, self._config2object, self._config_bundle)

        match file_format:
            case 'cfg':
                return CFGLoader(*common_base_args, cast(ICFGProcessor, self._processor))
            case 'ini':
                return INILoader(*common_base_args, cast(IINIProcessor, self._processor))
            case 'json':
                return JSONLoader(*common_base_args, cast(IJSONProcessor, self._processor))
            case 'xml':
                return XMLLoader(*common_base_args, cast(IXMLProcessor, self._processor))
            case 'yaml':
                return YAMLLoader(*common_base_args, cast(IYAMLProcessor, self._processor))
            case _:
                return None

    @override
    def __str__(self) -> str:
        '''
            Returns the ConfigLoader as string representation.

            :return: The ConfigLoader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
