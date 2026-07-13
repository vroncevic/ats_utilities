# -*- coding: UTF-8 -*-

'''
Module
    tar_process_bundle.py
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

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
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
class TarProcessBundle:
    '''
        Defines class TarProcessBundle with method(s).
        Encapsulates tar processing parameters for simplifcation.

        It defines:

            :attributes:
                | archive_path - Path to the .tgz archive containing templates.
                | target_dir - Target directory where output should be written.
                | source_dir - Source directory in tar to extract.
                | path_replacements - String replacements mapping.
                | exclude_patterns - Patterns of files/directories to exclude.
                | vals - Computed template values for substitution.
            :methods:
                | validate - Validates that TarProcessBundle is valid (can be called after merge).
                | merge - Merges non-None values from another TarProcessBundle into this one.
                | to_dict - Converts the TarProcessBundle instance to a dictionary.
    '''

    archive_path: str
    target_dir: str
    source_dir: str
    path_replacements: Mapping[str, str]
    exclude_patterns: Sequence[str]
    vals: Mapping[str, str]

    def validate(self) -> None:
        '''
            Validates that TarProcessBundle is valid (can be called after merge).
            Performs validation of archive_path, target_dir, source_dir,
            path_replacements, exclude_patterns and vals attributes.
            Archive path must be non-None and a string.
            Target dir must be non-None and a string.
            Source dir must be non-None and a string.
            Path replacements must be non-None and a mapping.
            Exclude patterns must be non-None and a sequence.
            Vals must be non-None and a mapping.

            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSValueError: Target directory must be provided.
                | ATSTypeError: Target directory must be a string.
                | ATSValueError: Source directory must be provided.
                | ATSTypeError: Source directory must be a string.
                | ATSValueError: Path replacements must be provided.
                | ATSTypeError: Path replacements must be a mapping.
                | ATSValueError: Exclude patterns must be provided.
                | ATSTypeError: Exclude patterns must be a sequence.
                | ATSValueError: Values must be provided.
                | ATSTypeError: Values must be a mapping.
        '''
        require_not_none(self.archive_path, r'archive_path must be provided.')
        require_not_none(self.target_dir, r'target_dir must be provided.')
        require_not_none(self.source_dir, r'source_dir must be provided.')
        require_not_none(self.path_replacements, r'path_replacements must be provided.')
        require_not_none(self.exclude_patterns, r'exclude_patterns must be provided.')
        require_not_none(self.vals, r'vals must be provided.')
        check_type(self.archive_path, str, r'archive_path must be a string.')
        check_type(self.target_dir, str, r'target_dir must be a string.')
        check_type(self.source_dir, str, r'source_dir must be a string.')
        check_type(self.path_replacements, Mapping, r'path_replacements must be a mapping.')
        check_type(self.exclude_patterns, Sequence, r'exclude_patterns must be a sequence of strings.')
        check_type(self.vals, Mapping, r'vals must be a mapping.')

    def merge(self, other: TarProcessBundle) -> None:
        '''
            Merges non-None values from another TarProcessBundle into this one.

            :param other: Another TarProcessBundle to merge into this one.
            :type other: <TarProcessBundle>
            :exceptions:
                | ATSValueError: Other TarProcessBundle must be provided.
                | ATSTypeError: Other must be a TarProcessBundle.
        '''
        require_not_none(other, r'other TarProcessBundle must be provided')
        check_type(other, TarProcessBundle, r'other must be a TarProcessBundle.')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the TarProcessBundle instance to a dictionary.

            :return: Dictionary representation of the TarProcessBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
