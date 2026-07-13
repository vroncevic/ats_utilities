# -*- coding: UTF-8 -*-

'''
Module
    tar_process_member_bundle.py
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
    Defines parameter bundle dataclass for component dependency management.
    Encapsulates core runtime components for simplifcation.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from tarfile import TarFile, TarInfo
from typing import Any

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
class TarProcessMemberBundle:
    '''
        Defines class TarProcessMemberBundle with method(s).
        Encapsulates tar member processing parameters for simplifcation.

        It defines:

            :attributes:
                | tar - The open tar archive instance.
                | member - The member info to process.
                | dest_full_path - Absolute destination file path.
                | vals - Computed template values for substitution.
            :methods:
                | validate - Validates that TarProcessMemberBundle is valid (can be called after merge).
                | merge - Merges non-None values from another TarProcessMemberBundle into this one.
                | to_dict - Converts the TarProcessMemberBundle instance to a dictionary.
    '''

    tar: TarFile
    member: TarInfo
    dest_full_path: str
    vals: Mapping[str, str]

    def validate(self) -> None:
        '''
            Validates that TarProcessMemberBundle is valid (can be called after merge).
            Performs validation of tar, member, dest_full_path and vals attributes.
            Tar must be non-None and a TarFile instance.
            Member must be non-None and a TarInfo instance.
            Dest full path must be non-None and a string.
            Vals must be non-None and a mapping.

            :exceptions:
                | ATSValueError: tar must be provided.
                | ATSValueError: member must be provided.
                | ATSValueError: dest_full_path must be provided.
                | ATSValueError: vals must be provided.
                | ATSTypeError: tar must be a TarFile instance.
                | ATSTypeError: member must be a TarInfo instance.
                | ATSTypeError: dest_full_path must be a string.
                | ATSTypeError: vals must be a mapping.
        '''
        require_not_none(self.tar, r'tar must be provided.')
        require_not_none(self.member, r'member must be provided.')
        require_not_none(self.dest_full_path, r'dest_full_path must be provided.')
        require_not_none(self.vals, r'vals must be provided.')
        check_type(self.tar, TarFile, r'tar must be a TarFile instance.')
        check_type(self.member, TarInfo, r'member must be a TarInfo instance.')
        check_type(self.dest_full_path, str, r'dest_full_path must be a string.')
        check_type(self.vals, Mapping, r'vals must be a mapping.')

    def merge(self, other: TarProcessMemberBundle) -> None:
        '''
            Merges non-None values from another TarProcessMemberBundle into this one.

            :param other: Another TarProcessMemberBundle to merge into this one.
            :type other: <TarProcessMemberBundle>
            :exceptions:
                | ATSValueError: Other TarProcessMemberBundle must be provided.
                | ATSTypeError: Other must be a TarProcessMemberBundle.
        '''
        require_not_none(other, r'other TarProcessMemberBundle must be provided')
        check_type(other, TarProcessMemberBundle, r'other must be a TarProcessMemberBundle.')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the TarProcessMemberBundle instance to a dictionary.

            :return: Dictionary representation of the TarProcessMemberBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
