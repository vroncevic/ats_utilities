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
    Defines option data used to define command line options.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from collections.abc import Sequence

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
class OptionData:
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
                | __post_init__ - Post-initializes option data instance.
                | to_dict - Converts the option data instance to a dictionary.
    '''

    name: str
    help_text: str
    action: str | None
    default: Any | None
    required: bool
    choices: Sequence[Any] | None
    nargs: str | int | None

    def __post_init__(self) -> None:
        '''
            Post-initializes option data instance.
            Converts choices sequence to an immutable tuple.
        '''
        if self.choices is not None:
            object.__setattr__(self, 'choices', tuple(self.choices))

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the option data instance to a dictionary.

            :return: Dictionary representation of the option data instance.
        '''
        return instance_to_dict(self)
