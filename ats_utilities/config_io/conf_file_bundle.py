# -*- coding: UTF-8 -*-

'''
Module
    conf_file_bundle.py
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
    Defines ConfFile parameters bundle dataclass.
    Encapsulates parameters for ConfFile class.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class ConfFileBundle:
    '''
        Defines ConfFile parameters bundle dataclass.
        Encapsulates parameters for ConfFile class.

        It defines:

            :attributes:
                | file_path - File path (default None).
                | file_mode - File mode (default None).
                | context_bundle - Context bundle for dependency injection (default None).
            :methods:
                | __post_init__ - Post-initialization hook to set up ConfFileBundle if not provided.
                | validate - Validates that ConfFileBundle is valid (can be called after merge).
                | merge - Merges non-None values from another ConfFileBundle into this one.
                | to_dict - Converts the ConfFileBundle instance to a dictionary.
    '''

    file_path: str | None = None
    file_mode: str | None = None
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to set up ConfFileBundle if not provided.
            Initializes ContextBundle if None.

            :exceptions: None.
        '''
        if self.context_bundle is None:
            self.context_bundle = ContextBundle()

    def validate(self) -> None:
        '''
            Validates that ConfFileBundle is valid (can be called after merge).
            Performs validation of file path, file mode and context_bundle attributes.
            File path must be non-None and a string.
            File mode must be non-None and a string.
            Context bundle must be non-None and a ContextBundle instance.

            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: File mode must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: File mode must be a string.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        require_not_none(self.file_path, r'file path must be provided')
        require_not_none(self.file_mode, r'file mode must be provided')
        require_not_none(self.context_bundle, r'context bundle must be provided')
        check_type(self.file_path, str, r'file path must be a string')
        check_type(self.file_mode, str, r'file mode must be a string')
        check_type(self.context_bundle, ContextBundle, r'context bundle must be a ContextBundle instance')

    def merge(self, other: ConfFileBundle) -> None:
        '''
            Merges non-None values from another ConfFileBundle into this one.

            :param other: Another ConfFileBundle to merge into this one.
            :type other: <ConfFileBundle>
            :exceptions:
                | ATSValueError: Other ConfFileBundle must be provided.
                | ATSTypeError: Other must be a ConfFileBundle instance.
        '''
        require_not_none(other, r'other ConfFileBundle must be provided')
        check_type(other, ConfFileBundle, r'other must be a ConfFileBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the ConfFileBundle instance to a dictionary.

            :return: Dictionary representation of the ConfFileBundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
