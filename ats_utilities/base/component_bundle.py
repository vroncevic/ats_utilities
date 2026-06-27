# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle dataclass for dependency grouping and management.
    Encapsulates base components to minimize constructor overhead.
'''

from typing import Any
from dataclasses import dataclass
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.iconfig_loader import IConfigLoader
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class BaseComponentBundle:
    '''
        Defines component bundle dataclass for dependency grouping and management.
        Encapsulates base components to minimize constructor overhead.

        It defines:

            :attributes:
                | info_file - Information file (default None).
                | config_loader - Configuration loader (default None).
                | info_manager - Information manager (default None).
                | options_parser - Options parser (default None).
                | logger_manager - Logger manager (default None).
                | splasher - Splasher (default None).
                | generator - Generator (default None).
                | use_generator - Enable/Disable generator usage (default False).
                | context_bundle - Context bundle for dependency injection (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    info_file: str | None = None
    config_loader: IConfigLoader | None = None
    info_manager: IInfoManager | None = None
    options_parser: IOptionManager | None = None
    logger_manager: ILoggerManager | None = None
    splasher: ISplasher | None = None
    generator: IGenerator | None = None
    use_generator: bool = False
    context_bundle: ContextBundle | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ValueError - Information file must be provided.
        '''
        if self.info_file is None:
            raise ValueError("information file must be provided.")

    def merge(self, other: 'BaseComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <BaseComponentBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }
