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
                | __post_init__ - Post-initialization hook to validate tar process bundle.
                | validate - Validates tar process bundle.
                | to_dict - Converts the tar process bundle into a dictionary.
    '''

    archive_path: str
    target_dir: str
    source_dir: str
    path_replacements: Mapping[str, str]
    exclude_patterns: Sequence[str]
    vals: Mapping[str, str]

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate tar process bundle.

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
        self.validate()

    def validate(self) -> None:
        '''
            Validates tar processor bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

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
        not_none(
            self.archive_path,
            r'tar_process_bundle::validate(...)',
            r'archive_path must be provided.'
        )
        not_none(
            self.target_dir,
            r'tar_process_bundle::validate(...)',
            r'target_dir must be provided.'
        )
        not_none(
            self.source_dir,
            r'tar_process_bundle::validate(...)',
            r'source_dir must be provided.'
        )
        not_none(
            self.path_replacements,
            r'tar_process_bundle::validate(...)',
            r'path_replacements must be provided.'
        )
        not_none(
            self.exclude_patterns,
            r'tar_process_bundle::validate(...)',
            r'exclude_patterns must be provided.'
        )
        not_none(
            self.vals,
            r'tar_process_bundle::validate(...)',
            r'vals must be provided.'
        )
        istype(
            self.archive_path, str,
            r'tar_process_bundle::validate(...)',
            r'archive_path must be a string.'
        )
        istype(
            self.target_dir, str,
            r'tar_process_bundle::validate(...)',
            r'target_dir must be a string.'
        )
        istype(
            self.source_dir, str,
            r'tar_process_bundle::validate(...)',
            r'source_dir must be a string.'
        )
        istype(
            self.path_replacements, Mapping,
            r'tar_process_bundle::validate(...)',
            r'path_replacements must be a mapping.'
        )
        istype(
            self.exclude_patterns, Sequence,
            r'tar_process_bundle::validate(...)',
            r'exclude_patterns must be a sequence of strings.'
        )
        istype(
            self.vals, Mapping,
            r'tar_process_bundle::validate(...)',
            r'vals must be a mapping.'
        )

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts tar process bundle into a dictionary.

            :return: Dictionary representation of tar process bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
