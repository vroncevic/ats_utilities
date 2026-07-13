# -*- coding: UTF-8 -*-

'''
Module
    file_bundle.py
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
    Encapsulates file configuration and processor utilities to minimize constructor overhead.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ats_utilities.factory_value import require_not_empty, require_not_none
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
class FileBundle:
    '''
        Defines class FileBundle with attribute(s) and method(s).
        Encapsulates file configuration and processor utilities to minimize constructor overhead.
        Acts as a Parameter Object to clean up highly repetitive constructor arguments.

        It defines:

            :attributes:
                | file_path - File path (default None).
                | file_mode - File mode (default None).
                | file_format - File format (default None).
            :methods:
                | validate - Validates that the FileBundle is valid (can be called after merge).
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    file_path: str | None = None
    file_mode: str | None = None
    file_format: str | None = None

    def validate(self) -> None:
        '''
            Validates that FileBundle is valid (can be called after merge).
            Performs validation of file path, file mode and file format attributes.
            File path must be non-None and a string.
            File mode must be non-None and a string.
            File format must be non-None and a string.

            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: File mode must be provided.
                | ATSValueError: File format must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: File mode must be a string.
                | ATSTypeError: File format must be a string.
        '''
        require_not_empty(self.file_path, r'file path must be provided')
        require_not_empty(self.file_mode, r'file mode must be provided')
        require_not_empty(self.file_format, r'file format must be provided')
        check_type(self.file_path, str, r'file path must be a string')
        check_type(self.file_mode, str, r'file mode must be a string')
        check_type(self.file_format, str, r'file format must be a string')

    def merge(self, other: FileBundle) -> None:
        '''
            Merges non-None values from another FileBundle instance into this one.

            :param other: Another FileBundle instance to merge into this one.
            :type other: <FileBundle>
            :exceptions:
                | ATSValueError: Other FileBundle must be provided.
                | ATSTypeError: Other must be a FileBundle instance.
        '''
        require_not_none(other, r'other FileBundle must be provided')
        check_type(other, FileBundle, r'other must be a FileBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the FileBundle instance to a dictionary.

            :return: Dictionary representation of the FileBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
