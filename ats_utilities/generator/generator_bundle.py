# -*- coding: UTF-8 -*-

'''
Module
    generator_bundle.py
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
from dataclasses import dataclass, asdict
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
class GeneratorBundle:
    '''
        Defines class GeneratorBundle with method(s).
        Encapsulates template generation parameters for simplifcation.

        It defines:

            :attributes:
                | archive_path - Path to the .tgz archive.
                | target_dir - Directory where the project will be generated.
                | template_key - Key for the template configuration.
                | scheme - Scheme configuration file path.
                | template_values - Template values for name case variations.
            :methods:
                | validate - Validates that GeneratorBundle is valid (can be called after merge).
                | merge - Merges non-None values from another GeneratorBundle instance into this one.
                | to_dict - Converts the GeneratorBundle instance to a dictionary.
    '''

    archive_path: str
    target_dir: str
    template_key: str
    scheme: str | Mapping[str, Any]
    template_values: Mapping[str, str]

    def validate(self) -> None:
        '''
            Validates that GeneratorBundle is valid (can be called after merge).
            Performs validation of archive_path, target_dir, template_key, scheme and template_values attributes.
            Archive path must be non-None and a string.
            Target dir must be non-None and a string.
            Template key must be non-None and a string.
            Scheme must be non-None and a string or a mapping.
            Template values must be non-None and a mapping.

            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSValueError: Target dir must be provided.
                | ATSTypeError: Target dir must be a string.
                | ATSValueError: Template key must be provided.
                | ATSTypeError: Template key must be a string.
                | ATSValueError: Scheme must be provided.
                | ATSTypeError: Scheme must be a string or a mapping.
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Template values must be a mapping.
        '''
        require_not_none(self.archive_path, r'archive_path must be provided')
        check_type(self.archive_path, str, r'archive_path must be a string')
        require_not_none(self.target_dir, r'target_dir must be provided')
        check_type(self.target_dir, str, r'target_dir must be a string')
        require_not_none(self.template_key, r'template_key must be provided')
        check_type(self.template_key, str, r'template_key must be a string')
        require_not_none(self.scheme, r'scheme must be provided')
        check_type(self.scheme, (str, Mapping), r'scheme must be a string or a mapping')
        require_not_none(self.template_values, r'template_values must be provided')
        check_type(self.template_values, Mapping, r'template_values must be a mapping')

    def merge(self, other: GeneratorBundle) -> None:
        '''
            Merges non-None values from another GeneratorBundle instance into this one.

            :param other: Another GeneratorBundle instance to merge into this one.
            :type other: <GeneratorBundle>
            :exceptions:
                | ATSTypeError: Other must be a GeneratorBundle.
        '''
        check_type(other, GeneratorBundle, r'other must be a GeneratorBundle')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the GeneratorBundle instance to a dictionary.

            :return: Dictionary representation of the GeneratorBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
