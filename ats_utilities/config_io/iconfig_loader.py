# -*- coding: UTF-8 -*-

'''
Module
    iconfig_loader.py
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
    Defines interface IConfigLoader with attribute(s) and method(s).
    Interface for managing configuration loading.
'''

from abc import ABC, abstractmethod
from typing import List, Optional, Union
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

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Optional configuration type
Config = Optional[Union[CFGLoader, INILoader, JSONLoader, XMLLoader, YAMLLoader]]

# Optional configuration interface type
IConfigProcessor = Optional[Union[ICFGProcessor, IINIProcessor, IJSONProcessor, IXMLProcessor, IYAMLProcessor]]

class IConfigLoader(ABC):
    '''
        Defines interface IConfigLoader with attribute(s) and method(s).
        Interface for managing CLI configuration loading.

        It defines:

            :attributes: None
            :methods:
                | setup_config_loader - Loads the appropriate configuration base based on file type (abstract).
                | __str__ - Returns the string representation of configuration loader (abstract).
    '''

    @abstractmethod
    def setup_config_loader(self) -> Config:
        '''
            Setup config loader based on configuration file type.

            :return: Configuration loaader object.
            :rtype: <Config>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method setup_config_loader() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of configuration loader.

            :return: The configuration loader as string representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
