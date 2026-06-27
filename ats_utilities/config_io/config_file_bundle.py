# -*- coding: UTF-8 -*-

'''
Module
    config_file_bundle.py
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
    Encapsulates file check configuration to minimize constructor overhead.
'''

from dataclasses import dataclass
from typing import Any
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.ifile_check import IFileCheck

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ATSConfigFileBundle:
    '''
        Defines class ATSConfigFileBundle with attribute(s) and method(s).
        Encapsulates file check configuration to minimize constructor overhead.

        It defines:

            :attributes:
                | context - Context bundle for checker, reporter and verbose (default None).
                | file_checker - Parameters checker implementation (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    context: ContextBundle | None = None
    file_checker: IFileCheck | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: File check implementation must be provided.
        '''
        if self.context is None:
            raise ATSValueError("context bundle must be provided.")

        if self.file_checker is None:
            raise ATSValueError("file checker implementation must be provided.")

    def merge(self, other: 'ATSConfigFileBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <ATSConfigFileBundle>
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

