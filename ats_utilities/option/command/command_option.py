# -*- coding: UTF-8 -*-

'''
Module
    command_option.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines CommandOption used to define command line options.
'''

from __future__ import annotations

from collections.abc import Sequence
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


@dataclass(slots=True)
class CommandOption:
    '''
        Represents metadata for a command line option.

        It defines:

            :attributes:
                | name - The command line option name.
                | help_text - Help text for this option.
                | action - Optional action for this option (default None).
                | default - Optional default value for this option (default None).
                | required - True if this option is required (default False).
                | choices - Optional choices for this option (default None).
                | nargs - Optional number of arguments for this option (default None).
            :methods:
                | __post_init__ - Post-initializes CommandOption instance.
                | validate - Validates that CommandOption instance is valid (can be called after merge).
                | merge - Merges non-None values from another CommandOption instance into this one.
                | to_dict - Converts the CommandOption instance to a dictionary.
    '''

    name: str
    help_text: str
    action: str | None = None
    default: Any | None = None
    required: bool = False
    choices: Sequence[Any] | None = None
    nargs: str | int | None = None

    def __post_init__(self) -> None:
        '''
            Post-initializes CommandOption instance.
            Converts choices sequence to an immutable tuple.
        '''
        if self.choices is not None:
            self.choices = tuple(self.choices)

    def validate(self) -> None:
        '''
            Validates that CommandOption instance is valid (can be called after merge).
            Performs validation of name, help_text, action, default, required, choices and nargs attributes.
            Name must be non-None and a string.
            Help text must be non-None and a string.
            Action must be non-None and a string.
            Default must be non-None.
            Required must be non-None and a boolean.
            Choices must be non-None and a sequence.
            Nargs must be non-None and a string or an integer.

            :exceptions:
                | ATSValueError: Name must be provided.
                | ATSValueError: Help text must be provided.
                | ATSValueError: Action must be provided.
                | ATSValueError: Default must be provided.
                | ATSValueError: Required must be provided.
                | ATSTypeError: Required must be a boolean.
                | ATSValueError: Choices must be provided.
                | ATSTypeError: Choices must be a sequence.
                | ATSValueError: Nargs must be provided.
                | ATSTypeError: Nargs must be a string or an integer.
        '''
        not_none(
            self.name,
            r'command_option::validate(...)',
            r'name must be provided'
        )
        not_none(
            self.help_text,
            r'command_option::validate(...)',
            r'help text must be provided'
        )
        not_none(
            self.action,
            r'command_option::validate(...)',
            r'action must be provided'
        )
        not_none(
            self.default,
            r'command_option::validate(...)',
            r'default must be provided'
        )
        not_none(
            self.required,
            r'command_option::validate(...)',
            r'required must be provided'
        )
        not_none(
            self.choices,
            r'command_option::validate(...)',
            r'choices must be provided'
        )
        not_none(
            self.nargs,
            r'command_option::validate(...)',
            r'nargs must be provided'
        )
        istype(
            self.required, bool,
            r'command_option::validate(...)',
            r'required must be a boolean'
        )
        istype(
            self.choices, Sequence,
            r'command_option::validate(...)',
            r'choices must be a sequence'
        )
        istype(
            self.nargs, (str, int),
            r'command_option::validate(...)',
            r'nargs must be a string or an integer'
        )

    def merge(self, other: CommandOption) -> None:
        '''
            Merges non-None values from another CommandOption into this one.

            :param other: Another CommandOption to merge into this one.
            :type other: <CommandOption>
            :exceptions:
                | ATSValueError: Other CommandOption must be provided.
                | ATSTypeError: Other must be a CommandOption instance.
        '''
        not_none(
            other,
            r'command_option::merge(...)',
            r'other CommandOption must be provided'
        )
        istype(
            other, CommandOption,
            r'command_option::merge(...)',
            r'other must be a CommandOption instance'
        )

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                if field_name == 'choices':
                    other_value = tuple(other_value)
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the CommandOption instance to a dictionary.

            :return: Dictionary representation of the CommandOption instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
