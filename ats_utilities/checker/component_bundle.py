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
    Defines component bundle dataclass for dependency group simplification.
    Encapsulates checker components to minimize constructor overhead.
'''

from typing import Any
from dataclasses import dataclass
from ats_utilities.checker.itype_validator import ITypeValidator
from ats_utilities.checker.iformat_validator import IFormatValidator
from ats_utilities.checker.icontext_provider import IContextProvider
from ats_utilities.checker.icheck_reporter import ICheckReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class CheckerComponentBundle:
    '''
        Defines component bundle dataclass for dependency group simplification.
        Encapsulates checker components to minimize constructor overhead.

        It defines:

            :attributes:
                | format_validator - Validator for parameters format (default None).
                | type_validator - Validator for parameters type (default None).
                | context_provider - Provider for call context (default None).
                | check_reporter - Formatter for message reports (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    format_validator: IFormatValidator | None = None
    type_validator: ITypeValidator | None = None
    context_provider: IContextProvider | None = None
    check_reporter: ICheckReporter | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ValueError - Context provider must be provided.
                | ValueError - Check reporter must be provided.
                | ValueError - Format validator must be provided.
                | ValueError - Type validator must be provided.
        '''
        if self.context_provider is None:
            raise ValueError("context provider must be provided.")

        if self.check_reporter is None:
            raise ValueError("check reporter must be provided.")

        if self.format_validator is None:
            raise ValueError("format validator must be provided.")

        if self.type_validator is None:
            raise ValueError("type validator must be provided.")

    def merge(self, other: 'CheckerComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <CheckerComponentBundle>
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

