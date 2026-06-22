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

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


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
            :methods: None
    '''

    def __init__(
        self,
        name: str,
        help_text: str,
        default: Any = None,
        required: bool = False,
        choices: list[Any] | None = None
    ) -> None:
        '''
            Initializes CommandOption constructor.

            :param name: Name of the option.
            :type name: <str>
            :param help_text: Help description.
            :type help_text: <str>
            :param default: Default value.
            :type default: <Any>
            :param required: Is this option required.
            :type required: <bool>
            :param choices: List of possible choices.
            :type choices: <list[Any] | None>
            :exceptions: None.
        '''
        self.name: str = name
        self.help_text: str = help_text
        self.default: Any = default
        self.required: bool = required
        self.choices: list[Any] | None = choices
