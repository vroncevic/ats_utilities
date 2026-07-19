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
    Defines parameter bundle dataclass for tar member processing.
    Encapsulates tar member processing parameters.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from tarfile import TarFile, TarInfo
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


@dataclass(slots=True, frozen=True, kw_only=True)
class TarProcessMemberBundle:
    '''
        Defines parameter bundle dataclass for tar member processing.
        Encapsulates tar member processing parameters.

        It defines:

            :attributes:
                | tar - The open tar archive instance.
                | member - The member info to process.
                | dest_full_path - Absolute destination file path.
                | vals - Computed template values for substitution.
            :methods:
                | __post_init__ - Post-initialization hook that validates tar process member bundle.
                | validate - Validates tar process member bundle.
                | to_dict - Converts the TarProcessMemberBundle instance to a dictionary.
    '''

    tar: TarFile
    member: TarInfo
    dest_full_path: str
    vals: Mapping[str, str]

    def __post_init__(self) -> None:
        '''
            Post-initialization hook that validates tar process member bundle.

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
        self.validate()

    def validate(self) -> None:
        '''
            Validates tar process member bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

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
        not_none(
            self.tar,
            r'tar_process_member_bundle::validate(...)',
            r'tar must be provided.'
        )
        not_none(
            self.member,
            r'tar_process_member_bundle::validate(...)',
            r'member must be provided.'
        )
        not_none(
            self.dest_full_path,
            r'tar_process_member_bundle::validate(...)',
            r'dest_full_path must be provided.'
        )
        not_none(
            self.vals,
            r'tar_process_member_bundle::validate(...)',
            r'vals must be provided.'
        )
        istype(
            self.tar, TarFile,
            r'tar_process_member_bundle::validate(...)',
            r'tar must be a TarFile instance.'
        )
        istype(
            self.member, TarInfo,
            r'tar_process_member_bundle::validate(...)',
            r'member must be a TarInfo instance.'
        )
        istype(
            self.dest_full_path, str,
            r'tar_process_member_bundle::validate(...)',
            r'dest_full_path must be a string.'
        )
        istype(
            self.vals, Mapping,
            r'tar_process_member_bundle::validate(...)',
            r'vals must be a mapping.'
        )

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the TarProcessMemberBundle instance to a dictionary.

            :return: Dictionary representation of the TarProcessMemberBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
