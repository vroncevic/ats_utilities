# -*- coding: utf-8 -*-

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

from typing import Any
from dataclasses import dataclass
from tarfile import TarFile, TarInfo
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
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
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    tar: TarFile
    member: TarInfo
    dest_full_path: str
    vals: dict[str, str]

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target directory must be provided.
                | ATSValueError: Source directory must be provided.
                | ATSValueError: Path replacements must be provided.
                | ATSValueError: Exclude patterns must be provided.
                | ATSValueError: Values must be provided.
        '''
        if self.tar is None:
            raise ATSValueError('tar must be provided.')

        if self.member is None:
            raise ATSValueError('member must be provided.')

        if self.dest_full_path is None:
            raise ATSValueError('dest_full_path must be provided.')

        if self.vals is None:
            raise ATSValueError('vals must be provided.')

    def merge(self, other: 'TarProcessMemberBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <TarProcessMemberBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

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
