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

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.iconfig_loader import IConfigProcessor
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class ConfigLoaderBundle:
    '''
        Defines class ConfigLoaderBundle with attribute(s) and method(s).
        Encapsulates the core system tracking, verification, and configuration components.
        Acts as a Parameter Object to clean up highly repetitive logger and vcheck arguments.

        It defines:

            :attributes:
                | info_file - Configuration file for loading process (default None).
                | config2object - Convertor configuration to object (default None).
                | config_bundle - ATS configuration file bundle (default None).
                | processor - Configuration processor implementation (default None).
            :methods:
                | validate - Validates that ConfigLoaderBundle is valid (can be called after merge).
                | merge - Merges non-None values from ConfigLoaderBundle instance into this one.
                | to_dict - Converts the ConfigLoaderBundle instance to a dictionary.
    '''

    info_file: str | None = None
    config2object: IRead | None = None
    config_bundle: ConfigFileBundle | None = None
    processor: IConfigProcessor | None = None

    def validate(self) -> None:
        '''
            Validates that ConfigLoaderBundle is valid (can be called after merge).
            Performs validation of info_file, config2object, config_bundle and processor attributes.
            Info file must be non-None and an instance of str.
            Config2object must be non-None and an instance of IRead interface.
            Config_bundle must be non-None and an instance of ConfigFileBundle interface.
            Processor must be non-None and an instance of IConfigProcessor interface.

            :exceptions:
                | ATSValueError: Info file must be provided.
                | ATSValueError: Config2object must be provided.
                | ATSValueError: Configuration bundle must be provided.
                | ATSValueError: Configuration processor must be provided.
                | ATSTypeError: Info file must be a string.
                | ATSTypeError: Config2object must be an instance of IRead interface.
                | ATSTypeError: Config_bundle must be an instance of ConfigFileBundle interface.
                | ATSTypeError: Processor must be an instance of IConfigProcessor interface.
        '''
        require_not_none(self.info_file, r'info file must be provided')
        check_type(self.info_file, str, r'info file must be a string')
        require_not_none(self.config2object, r'config2object must be provided')
        check_type(self.config2object, IRead, r'config2object must be an instance of IRead interface')
        require_not_none(self.config_bundle, r'configuration bundle must be provided')
        check_type(self.config_bundle, ConfigFileBundle, r'configuration bundle must be an instance of ConfigFileBundle interface')
        require_not_none(self.processor, r'configuration processor must be provided')
        check_type(self.processor, IConfigProcessor, r'configuration processor must be an instance of IConfigProcessor interface')

    def merge(self, other: ConfigLoaderBundle) -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <ConfigLoaderBundle>
            :exceptions:
                | ATSValueError: Other ConfigLoaderBundle must be provided.
                | ATSTypeError: Other must be an ConfigLoaderBundle instance.
        '''
        require_not_none(other, r'other ConfigLoaderBundle must be provided')
        check_type(other, ConfigLoaderBundle, r'other must be an ConfigLoaderBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the ConfigLoaderBundle instance to a dictionary.

            :return: Dictionary representation of the ConfigLoaderBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
