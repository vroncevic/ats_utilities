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

from ats_utilities.utils.reflection import instance_to_dict

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class TarData:
    '''
        Encapsulates tar archive processing runtime data.

        It defines:

            :attributes:
                | archive_path - The path to the .tgz archive containing templates.
                | target_dir - The target directory where output should be written.
                | source_dir - The source directory in tar to extract.
                | path_replacements - The string replacements mapping.
                | exclude_patterns - The patterns of files/directories to exclude.
                | vals - The computed template values for substitution.
            :methods:
                | to_dict - Converts the tar process data to a dictionary.
    '''

    archive_path: str
    target_dir: str
    source_dir: str
    path_replacements: Mapping[str, str]
    exclude_patterns: Sequence[str]
    vals: Mapping[str, str]

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the tar process data to a dictionary.

            :return: The dictionary representation of the tar process data.
            :exceptions: None.
        '''
        return instance_to_dict(self)


@dataclass(slots=True, frozen=True, kw_only=True)
class TarMemberData:
    '''
        Encapsulates single tar archive member data.

        It defines:

            :attributes:
                | tar - The open tar archive.
                | member - The member info to process.
                | dest_full_path - The absolute destination file path.
                | vals - The computed template values for substitution.
            :methods:
                | to_dict - Converts the tar member data to a dictionary.
    '''

    tar: TarFile
    member: TarInfo
    dest_full_path: str
    vals: Mapping[str, str]

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the tar member data to a dictionary.

            :return: The dictionary representation of the tar member data.
            :exceptions: None.
        '''
        return instance_to_dict(self)
