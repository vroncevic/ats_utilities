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

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

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

# Type alias for parameter metadata: (parameter name, expected type, actual value)
type ParamMetadata = tuple[str, str, Any]


@dataclass(slots=True, frozen=True, kw_only=True)
class CheckerReporterBundle:
    '''
        Defines component bundle dataclass for dependency group simplification.
        Encapsulates checker reporter parameters to minimize constructor overhead.

        It defines:

            :attributes:
                | context - Message context.
                | parameters_meta - Sequence of parameter name and parameter type tuples.
                | err_indices - Sequence of error indices.
                | is_fmt_err - Flag indicating if format error type has been found.
            :methods:
                | __post_init__ - Post-initialization hook to validate CheckerReporterBundle.
                | validate - Validates checker reporter bundle.
                | to_dict - Converts the checker reporter bundle instance to a dictionary.
    '''

    context: str
    parameters_meta: Sequence[ParamMetadata]
    err_indices: Sequence[int]
    is_fmt_err: bool

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate CheckerReporterBundle.

            :exceptions:
                | ATSValueError: Context must be provided.
                | ATSValueError: Parameters metadata must be provided.
                | ATSValueError: Error indices must be provided.
                | ATSValueError: Is format error must be provided.
                | ATSTypeError: Context must be a string.
                | ATSTypeError: Parameters metadata must be a sequence of ParamMetadata.
                | ATSTypeError: Error indices must be a sequence of integers.
                | ATSTypeError: Is format error must be a boolean.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates checker reporter bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Context must be provided.
                | ATSValueError: Parameters metadata must be provided.
                | ATSValueError: Error indices must be provided.
                | ATSValueError: Is format error must be provided.
                | ATSTypeError: Context must be a string.
                | ATSTypeError: Parameters metadata must be a sequence of ParamMetadata.
                | ATSTypeError: Error indices must be a sequence of integers.
                | ATSTypeError: Is format error must be a boolean.
        '''
        context: str = r'checker_reporter_bundle::validate(...)'
        not_none(self.context, context, r'context must be provided')
        not_none(self.parameters_meta, context, r'parameters_meta must be provided')
        not_none(self.err_indices, context, r'err_indices must be provided')
        not_none(self.is_fmt_err, context, r'is_fmt_err must be provided')
        istype(self.context, str, context, r'context must be a string')
        istype(self.parameters_meta, Sequence[ParamMetadata], context, r'parameters_meta must be a sequence of ParamMetadata')
        istype(self.err_indices, Sequence[int], context, r'err_indices must be a sequence of integers')
        istype(self.is_fmt_err, bool, context, r'is_fmt_err must be a boolean')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the checker reporter bundle instance to a dictionary.

            :return: Dictionary representation of the checker reporter bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
