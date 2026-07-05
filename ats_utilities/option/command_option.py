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
from dataclasses import dataclass, asdict
from typing import Any

from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'

@dataclass(slots=True)
class CommandOption:
    '''
        Represents metadata for a command line option.

        It defines:

            :attributes:
                | name - The command line option name.
                | help_text - Help text for this option.
                | action - Optional action for this option.
                | default - Optional default value for this option.
                | required - True if this option is required.
                | choices - Optional choices for this option.
                | nargs - Optional number of arguments for this option.
            :methods:
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
        require_not_none(self.name, "name must be provided")
        require_not_none(self.help_text, "help text must be provided")
        require_not_none(self.action, "action must be provided")
        require_not_none(self.default, "default must be provided")
        require_not_none(self.required, "required must be provided")
        require_not_none(self.choices, "choices must be provided")
        require_not_none(self.nargs, "nargs must be provided")
        check_type(self.required, bool, "required must be a boolean")
        check_type(self.choices, Sequence, "choices must be a sequence")
        check_type(self.nargs, (str, int), "nargs must be a string or an integer")

    def merge(self, other: CommandOption) -> None:
        '''
            Merges non-None values from another CommandOption into this one.

            :param other: Another CommandOption to merge into this one.
            :type other: <CommandOption>
            :exceptions:
                | ATSTypeError: Other must be a CommandOption instance.
        '''
        check_type(other, CommandOption, 'other must be a CommandOption instance')

        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the CommandOption instance to a dictionary.

            :return: Dictionary representation of the CommandOption instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
