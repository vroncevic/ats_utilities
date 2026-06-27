# -*- coding: UTF-8 -*-

'''
Module
    checker_reporter_bundle.py
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
    Encapsulates checker reporter parameters to minimize constructor overhead.
'''

from typing import Any
from dataclasses import dataclass

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Type alias for parameter metadata: (parameter name, expected type, actual value)
type ParamMetadata = tuple[str, str, Any]


@dataclass
class CheckerReporterBundle:
    '''
        Defines component bundle dataclass for dependency group simplification.
        Encapsulates checker reporter parameters to minimize constructor overhead.

        It defines:

            :attributes:
                | context - Message context (default None).
                | parameters_meta - parameter name and parameter type (default None).
                | err_indices - Error set (default None).
                | is_fmt_err - Check for format error type (default False).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    context: str | None = None
    parameters_meta: list[ParamMetadata] | None = None
    err_indices: list[int] | None = None
    is_fmt_err: bool = False

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ValueError - Context must be provided.
                | ValueError - Parameters metadata must be provided.
        '''
        if self.context is None:
            raise ValueError("Context must be provided.")

        if self.parameters_meta is None:
            raise ValueError("Parameters metadata must be provided.")

    def merge(self, other: 'CheckerReporterBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <CheckerReporterBundle>
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

