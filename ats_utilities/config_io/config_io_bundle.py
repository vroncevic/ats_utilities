# -*- coding: UTF-8 -*-

'''
Module
    config_io_bundle.py
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
    Defines ConfigIOBundle data classes for dependency group simplification.
    Encapsulates core configuration and processor utilities to minimize constructor overhead.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, ClassVar

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
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
class ConfigIOBundle:
    '''
        Defines ConfigIOBundle data classes for dependency group simplification.
        Encapsulates core configuration and processor utilities to minimize constructor overhead.

        It defines:

            :attributes:
                | READ_MODE - Default file opening mode (class variable, default 'r').
                | WRITE_MODE - Default file opening mode (class variable, default 'w').
                | file_path - Configuration file path (default None).
                | scheme - Configuration scheme (default None).
                | processor - Configuration processor (default None).
                | context_bundle - Context bundle for dependency injection (default None).
            :methods:
                | __init__ - Initializes ConfigIOBundle constructor.
                | validate - Validates that ConfigIOBundle is valid (can be called after merge).
                | merge - Merges non-None values from ConfigIOBundle instance into this one.
                | to_dict - Converts the ConfigIOBundle instance to a dictionary.
    '''

    READ_MODE: ClassVar[str] = 'r'
    WRITE_MODE: ClassVar[str] = 'w'
    file_path: str | None
    scheme: Mapping[str, str] | None = None
    processor: IConfigProcessor | None = None
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Performs post-initialization operations for the ConfigIOBundle instance.

            :exceptions: None.
        '''
        if self.context_bundle is None:
            self.context_bundle = ContextBundle()

    def validate(self) -> None:
        '''
            Validates that ConfigIOBundle is valid (can be called after merge).
            Performs validation of file_path, scheme and processor attributes.
            File path must be non-None and an instance of str.
            Scheme must be non-None and an instance of Mapping interface.
            Processor must be non-None and an instance of IConfigProcessor interface.

            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Processor must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Processor must be an instance of IConfigProcessor interface.
        '''
        require_not_none(self.file_path, r'file path must be provided')
        check_type(self.file_path, str, r'file path must be a string')
        require_not_none(self.scheme, r'scheme must be provided')
        check_type(self.scheme, Mapping, r'scheme must be an instance of Mapping interface')
        require_not_none(self.processor, r'processor must be provided')
        check_type(self.processor, IConfigProcessor, r'processor must be an instance of IConfigProcessor interface')
        require_not_none(self.context_bundle, r'context_bundle must be provided')
        check_type(self.context_bundle, ContextBundle, r'context_bundle must be an instance of ContextBundle interface')

    def merge(self, other: ConfigIOBundle) -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <ConfigIOBundle>
            :exceptions:
                | ATSValueError: Other ConfigIOBundle must be provided.
                | ATSTypeError: Other must be an ConfigIOBundle instance.
        '''
        require_not_none(other, r'other ConfigIOBundle must be provided')
        check_type(other, ConfigIOBundle, r'other must be an ConfigIOBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the ConfigIOBundle instance to a dictionary.

            :return: Dictionary representation of the ConfigIOBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
