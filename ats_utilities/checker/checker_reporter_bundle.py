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
from dataclasses import dataclass, asdict
from typing import Any

from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Type alias for parameter metadata: (parameter name, expected type, actual value)
type ParamMetadata = tuple[str, str, Any]


@dataclass(slots=True, kw_only=True)
class CheckerReporterBundle:
    '''
        Defines component bundle dataclass for dependency group simplification.
        Encapsulates checker reporter parameters to minimize constructor overhead.

        It defines:

            :attributes:
                | context - Message context (default None).
                | parameters_meta - Sequence of parameter name and parameter type tuples (default None).
                | err_indices - Sequence of error indices (default None).
                | is_fmt_err - Flag indicating if format error type has been found (default False).
            :methods:
                | __post_init__ - Post-initialization hook to set up default values if not provided.
                | validate - Validates that CheckerReporterBundle is valid (can be called after merge).
                | merge - Merges non-None values from another CheckerReporterBundle instance into this one.
                | to_dict - Converts the CheckerReporterBundle instance to a dictionary.
    '''

    context: str | None = None
    parameters_meta: Sequence[ParamMetadata] | None = None
    err_indices: Sequence[int] | None = None
    is_fmt_err: bool = False

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to set up default values.
        '''
        if self.parameters_meta is None:
            self.parameters_meta = ()

        if self.err_indices is None:
            self.err_indices = ()

    def validate(self) -> None:
        '''
            Validates that CheckerReporterBundle is valid (can be called after merge).
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
        require_not_none(self.context, 'context must be provided')
        require_not_none(self.parameters_meta, 'parameters_meta must be provided')
        require_not_none(self.err_indices, 'err_indices must be provided')
        require_not_none(self.is_fmt_err, 'is_fmt_err must be provided')
        check_type(self.context, str, 'context must be a string')
        check_type(self.parameters_meta, Sequence[ParamMetadata], 'parameters_meta must be a sequence of ParamMetadata')
        check_type(self.err_indices, Sequence[int], 'err_indices must be a sequence of integers')
        check_type(self.is_fmt_err, bool, 'is_fmt_err must be a boolean')

    def merge(self, other: CheckerReporterBundle) -> None:
        '''
            Merges non-None values from another CheckerReporterBundle into this one.

            :param other: Another CheckerReporterBundle to merge into this one.
            :type other: <CheckerReporterBundle>
            :exceptions:
                | ATSTypeError: Other must be a CheckerReporterBundle instance.
        '''
        check_type(other, CheckerReporterBundle, 'other must be a CheckerReporterBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the CheckerReporterBundle instance to a dictionary.

            :return: Dictionary representation of the CheckerReporterBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
