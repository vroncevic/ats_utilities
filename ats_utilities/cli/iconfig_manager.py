# -*- coding: UTF-8 -*-

'''
Module
    iconfig_manager.py
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
    Defines interface IConfigManager with attribute(s) and method(s).
    Interface for managing CLI configuration loading.
'''

from abc import ABC, abstractmethod
from typing import List, Optional, Union
from ats_utilities.config_io.cfg.cfg_initializer import CfgInitializer
from ats_utilities.config_io.ini.inibase import IniBase
from ats_utilities.config_io.json.jsonbase import JsonBase
from ats_utilities.config_io.xml.xmlbase import XmlBase
from ats_utilities.config_io.yaml.yamlbase import YamlBase

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Optional configuration type
Config = Optional[Union[CfgInitializer, IniBase, JsonBase, XmlBase, YamlBase]]

class IConfigManager(ABC):
    '''
        Defines interface IConfigManager with attribute(s) and method(s).
        Interface for managing CLI configuration loading.

        It defines:

            :attributes: None
            :methods:
                | load_config - Loads the appropriate configuration base based on file type (abstract).
                | __str__ - Returns the string representation of configuration manager (abstract).
    '''

    @abstractmethod
    def load_config(self, info_file: Optional[str], verbose: bool = False) -> Config:
        '''
            Loads the appropriate configuration base based on file type.

            :param info_file: Path to information file.
            :type info_file: <Optional[str]>
            :param verbose: Verbose flag.
            :type verbose: <bool>
            :return: Configuration object.
            :rtype: <Config>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method load_config() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of configuration manager.

            :return: The configuration manager as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
