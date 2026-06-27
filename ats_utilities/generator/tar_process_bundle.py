# -*- coding: utf-8 -*-

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

from typing import Any
from dataclasses import dataclass
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
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    archive_path: str
    target_dir: str
    source_dir: str
    path_replacements: dict[str, str]
    exclude_patterns: list[str]
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
        if self.archive_path is None:
            raise ATSValueError('archive_path must be provided.')

        if self.target_dir is None:
            raise ATSValueError('target_dir must be provided.')

        if self.source_dir is None:
            raise ATSValueError('source_dir must be provided.')

        if self.path_replacements is None:
            raise ATSValueError('path_replacements must be provided.')

        if self.exclude_patterns is None:
            raise ATSValueError('exclude_patterns must be provided.')

        if self.vals is None:
            raise ATSValueError('vals must be provided.')

    def merge(self, other: 'TarProcessBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <TarProcessBundle>
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
