# -*- coding: UTF-8 -*-

'''
Module
    gen_params_bundle.py
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
    Defines parameter bundle dataclass for template generation.
    Encapsulates template generation parameters for simplifcation.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.files import check_file_exists

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class GenParamsBundle:
    '''
        Defines parameter bundle dataclass for template generation.
        Encapsulates template generation parameters for simplifcation.

        It defines:

            :attributes:
                | archive_path - Path to the .tgz archive.
                | target_dir - Directory where the project will be generated.
                | template_key - Key for the template configuration.
                | scheme - Scheme configuration file path.
                | template_values - Template values for name case variations.
            :methods:
                | __post_init__ - Post-initialization hook to validate generator parameters bundle.
                | validate - Validates generator parameters bundle.
                | to_dict - Converts generator parameters bundle to dictionary.
    '''

    archive_path: str
    target_dir: str
    template_key: str
    scheme: str | Mapping[str, Any]
    template_values: Mapping[str, str]

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate generator parameters bundle.

            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target dir must be provided.
                | ATSValueError: Template key must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSTypeError: Target dir must be a string.
                | ATSTypeError: Template key must be a string.
                | ATSTypeError: Scheme must be a string or a mapping.
                | ATSTypeError: Template values must be a mapping.
                | ATSValueError: Archive file does not exist.
                | ATSValueError: Scheme file does not exist.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates generator parameters bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target dir must be provided.
                | ATSValueError: Template key must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSTypeError: Target dir must be a string.
                | ATSTypeError: Template key must be a string.
                | ATSTypeError: Scheme must be a string or a mapping.
                | ATSTypeError: Template values must be a mapping.
                | ATSValueError: Archive file does not exist.
                | ATSValueError: Scheme file does not exist.
        '''
        not_none(self.archive_path, r'archive_path must be provided')
        not_none(self.target_dir, r'target_dir must be provided')
        not_none(self.template_key, r'template_key must be provided')
        not_none(self.scheme, r'scheme must be provided')
        not_none(self.template_values, r'template_values must be provided')
        istype(self.archive_path, str, r'archive_path must be a string')
        istype(self.target_dir, str, r'target_dir must be a string')
        istype(self.template_key, str, r'template_key must be a string')
        istype(self.scheme, (str, Mapping), r'scheme must be a string or a mapping')
        istype(self.template_values, Mapping, r'template_values must be a mapping')
        check_file_exists(self.archive_path, f'archive file does not exist: {self.archive_path}')

        if isinstance(self.scheme, str):
            check_file_exists(self.scheme, f'scheme file does not exist: {self.scheme}')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts generator parameters bundle to dictionary.

            :return: Dictionary representation of generator parameters bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
