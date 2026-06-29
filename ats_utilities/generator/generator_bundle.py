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

from typing import Any
from dataclasses import dataclass
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class GeneratorBundle:
    '''
        Defines class GeneratorBundle with method(s).
        Encapsulates template generation parameters for simplifcation.

        It defines:

            :attributes:
                | archive_path - Path to the .tgz archive.
                | target_dir - Directory where the project will be generated.
                | template_key - Key for the template configuration.
                | scheme - Scheme configuration.
                | template_values - Template values for name case variations.
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    archive_path: str
    target_dir: str
    template_key: str
    scheme: dict[str, Any] | str
    template_values: dict[str, str]

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError: Archive_path must be set.
                | ATSValueError: Target_dir must be set.
                | ATSValueError: Template_key must be set.
                | ATSValueError: Scheme must be set.
                | ATSValueError: Template_values must be set.
                | ATSTypeError: Types of fields must be correct.
        '''
        if self.archive_path is None:
            raise ATSValueError("archive_path must be set.")
        if not isinstance(self.archive_path, str):
            raise ATSTypeError("archive_path must be a string.")

        if self.target_dir is None:
            raise ATSValueError("target_dir must be set.")
        if not isinstance(self.target_dir, str):
            raise ATSTypeError("target_dir must be a string.")

        if self.template_key is None:
            raise ATSValueError("template_key must be set.")
        if not isinstance(self.template_key, str):
            raise ATSTypeError("template_key must be a string.")

        if self.scheme is None:
            raise ATSValueError("scheme must be set.")
        if not isinstance(self.scheme, (str, dict)):
            raise ATSTypeError("scheme must be a string or a dictionary.")

        if self.template_values is None:
            raise ATSValueError("template_values must be set.")
        if not isinstance(self.template_values, dict):
            raise ATSTypeError("template_values must be a dictionary.") 

    def merge(self, other: 'GeneratorBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <GeneratorBundle>
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
