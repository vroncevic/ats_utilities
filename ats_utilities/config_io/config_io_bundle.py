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
    Defines config I/O bundle data classes for dependency group simplification.
    Encapsulates core config I/O objects to minimize constructor overhead.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, ClassVar

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class ConfigIOBundle:
    '''
        Defines config I/O bundle data classes for dependency group simplification.
        Encapsulates core config I/O objects to minimize constructor overhead.

        It defines:

            :attributes:
                | READ_MODE - Default file opening mode (class variable, default 'r').
                | WRITE_MODE - Default file opening mode (class variable, default 'w').
                | file_path - Configuration file path.
                | scheme - Configuration scheme.
                | processor - Configuration processor.
                | context_bundle - Context bundle for dependency injection.
            :methods:
                | __post_init__ - Post-initialization hook to validate config I/O bundle.
                | validate - Validates config I/O bundle.
                | to_dict - Converts the config I/O bundle instance to a dictionary.
    '''

    READ_MODE: ClassVar[str] = 'r'
    WRITE_MODE: ClassVar[str] = 'w'
    file_path: str
    scheme: Mapping[str, str]
    processor: IConfigProcessor
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate config I/O bundle.

            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Processor must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Processor must be an instance of IConfigProcessor interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates config I/O bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Processor must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Processor must be an instance of IConfigProcessor interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        not_none(self.file_path, r'file path must be provided')
        not_none(self.scheme, r'scheme must be provided')
        not_none(self.processor, r'processor must be provided')
        not_none(self.context_bundle, r'context_bundle must be provided')
        istype(self.file_path, str, r'file path must be a string')
        istype(self.scheme, Mapping, r'scheme must be an instance of Mapping interface')
        istype(self.processor, IConfigProcessor, r'processor must be an instance of IConfigProcessor interface')
        istype(self.context_bundle, ContextBundle, r'context_bundle must be an instance of ContextBundle interface')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the config I/O bundle instance to a dictionary.

            :return: Dictionary representation of the config I/O bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
