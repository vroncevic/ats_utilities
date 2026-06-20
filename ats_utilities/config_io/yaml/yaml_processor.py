# -*- coding: UTF-8 -*-

'''
Module
    yaml_processor.py
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
    Defines class ATSYAMLProcessor with attribute(s) and method(s).
    Provides a default implementation for processing YAML content.
'''

import yaml
from typing import Dict, List
from ats_utilities.config_io.yaml.iyaml_processor import IYAMLProcessor
from ats_utilities.exceptions.ats_error import ATSError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class ATSYAMLProcessor(IYAMLProcessor):
    '''
        Defines class ATSYAMLProcessor with attribute(s) and method(s).
        Provides a default implementation for processing YAML content.

        It defines:

            :attributes:
                | __data - Internal dictionary to store YAML data.
            :methods:
                | __init__ - Initializes ATSYAMLProcessor constructor.
                | decode - Converts raw YAML text to an internal object/structure.
                | encode - Converts an internal object/structure back to a YAML string.
                | to_dict - Returns configuration as a flat dictionary.
    '''

    def __init__(self) -> None:
        '''
            Initializes ATSYAMLProcessor constructor.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        self.__data: Dict[str, str] = {}

    def decode(self, yaml_string: str) -> bool:
        '''
            Converts raw YAML text to an internal object/structure.

            :param yaml_string: Raw YAML text.
            :type yaml_string: <str>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        try:
            self.__data = yaml.safe_load(yaml_string)
            return True
        except ATSError:
            return False

    def encode(self) -> str:
        '''
            Converts an internal object/structure back to a YAML string.

            :return: YAML content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        return yaml.safe_dump(self.__data, default_flow_style=False)

    def to_dict(self) -> Dict[str, str]:
        '''
            Returns configuration as a flat dictionary.

            :return: Dictionary with YAML information.
            :rtype: <Dict[str, str]>
            :exceptions: None.
        '''
        return self.__data
