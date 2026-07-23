# -*- coding: UTF-8 -*-

'''
Module
    data.py
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
    Encapsulates tar archive processing runtime data.
'''

from __future__ import annotations

from collections.abc import Sequence, Mapping
from dataclasses import dataclass
from tarfile import TarFile, TarInfo
from typing import Any

from ats_utilities.utils.reflection import instance_to_dict

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class TarData:
    '''
        Encapsulates tar archive processing runtime data.

        It defines:

            :attributes:
                | archive_path - Path to the .tgz archive containing templates.
                | target_dir - Target directory where output should be written.
                | source_dir - Source directory in tar to extract.
                | path_replacements - String replacements mapping.
                | exclude_patterns - Patterns of files/directories to exclude.
                | vals - Computed template values for substitution.
            :methods:
                | to_dict - Converts the tar process data to a dictionary.
    '''

    archive_path: str
    target_dir: str
    source_dir: str
    path_replacements: Mapping[str, str]
    exclude_patterns: Sequence[str]
    vals: Mapping[str, str]

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the tar process data to a dictionary.

            :return: Dictionary representation of the tar process data.
            :rtype: dict[str, Any]
            :exceptions: None.
        '''
        return instance_to_dict(self)

@dataclass(slots=True, frozen=True, kw_only=True)
class TarMemberData:
    '''
        Encapsulates single tar archive member data.

        It defines:

            :attributes:
                | tar - The open tar archive instance.
                | member - The member info to process.
                | dest_full_path - Absolute destination file path.
                | vals - Computed template values for substitution.
            :methods:
                | to_dict - Converts the tar member data to a dictionary.
    '''

    tar: TarFile
    member: TarInfo
    dest_full_path: str
    vals: Mapping[str, str]

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the tar member data to a dictionary.

            :return: Dictionary representation of the tar member data.
            :rtype: dict[str, Any]
            :exceptions: None.
        '''
        return instance_to_dict(self)