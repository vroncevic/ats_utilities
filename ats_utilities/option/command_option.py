# -*- coding: UTF-8 -*-

'''
Module
    command_option.py
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
    Defines class CommandOption with attributes.
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
class CommandOption:
    '''
        Defines class CommandOption with attribute(s) and method(s).

        It defines:

            :attributes:
                | name - The name of the option.
                | help_text - The help description.
                | default - Default value (default None).
                | required - Is this option required (default False).
                | choices - List of possible choices (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another CommandOption into this one.
                | to_dict - Converts the CommandOption attributes to a dictionary.
    '''

    name: str
    help_text: str
    default: Any = None
    required: bool = False
    choices: list[Any] | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError - Name must be provided.
                | ATSValueError - Help text must be provided.
                | ATSValueError - Default must be provided.
                | ATSValueError - Required must be provided.
                | ATSValueError - Choices must be provided.
        '''
        if self.name is None:
            raise ATSValueError("name must be provided.")

        if self.help_text is None:
            raise ATSValueError("help text is required.")

        if self.default is None:
            raise ATSValueError("default is required.")

        if self.required is None:
            raise ATSValueError("required is required.")

        if self.choices is None:
            raise ATSValueError("choices is required.")

    def merge(self, other: 'CommandOption') -> None:
        '''
            Merges non-None values from another CommandOption into this one.

            :param other: Another CommandOption to merge into this one.
            :type other: <CommandOption>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the CommandOption attributes to a dictionary.

            :return: Dictionary representation of the CommandOption attributes.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }
