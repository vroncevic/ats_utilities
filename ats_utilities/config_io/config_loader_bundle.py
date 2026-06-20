# -*- coding: UTF-8 -*-

'''
Module
    config_loader_bundle.py
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
    Defines parameter bundle data classes for dependency group simplification.
    Encapsulates core configuration and processor utilities to minimize constructor overhead.
'''

from dataclasses import dataclass, field
from typing import List, Optional
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.iconfig_loader import IConfigProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ATSConfigLoaderBundle:
    '''
        Defines class ATSConfigLoaderBundle with attribute(s) and method(s).
        Encapsulates the core system tracking, verification, and configuration components.
        Acts as a Parameter Object to clean up highly repetitive logger and validator arguments.

        It defines:

            :attributes:
                | info_file - Configuration file for loading process (default None).
                | config2object - Convertor configuration to object (default None).
                | config_bundle - ATS configuration file bundle (default ATSConfigFileBundle()).
                | processor - Configuration processor implementation (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    info_file: Optional[str] = None
    config2object: Optional[IRead] = None
    config_bundle: Optional[ATSConfigFileBundle] = field(default_factory=ATSConfigFileBundle)
    processor: Optional[IConfigProcessor] = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        pass

    def merge(self, other: 'ATSConfigLoaderBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <ATSConfigLoaderBundle>
            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)
            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }

