# -*- coding: UTF-8 -*-

'''
Module
    parser_bundle.py
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
    Defines class ParserBundle with attribute(s) and method(s).
    Encapsulates core parser components for simplification of ParserBundle creation.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class ParserBundle:
    '''
        Encapsulates core parser components for simplification of ParserBundle creation.

        It defines:

            :attributes:
                | context_bundle - Context bundle for dependency injection.
                | prog - Program name.
                | epilog - Epilog text.
                | description - Description text.
            :methods:
                | __post_init__ - Post-initialization hook to validate parser bundle.
                | validate - Validates parser bundle.
                | to_dict - Converts parser bundle to dictionary.
    '''

    prog: str
    epilog: str
    description: str
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate parser bundle.

            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Prog must be provided.
                | ATSValueError: Epilog must be provided.
                | ATSValueError: Description must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Prog must be a string.
                | ATSTypeError: Epilog must be a string.
                | ATSTypeError: Description must be a string.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates parser bundle.
            Performs validation of all bundle attributes.
        '''
        not_none(self.context_bundle, r'context bundle must be provided')
        not_none(self.prog, r'prog must be provided')
        not_none(self.epilog, r'epilog must be provided')
        not_none(self.description, r'description must be provided')
        istype(self.context_bundle, ContextBundle, r'context bundle must be a ContextBundle instance')
        istype(self.prog, str, r'prog must be a string')
        istype(self.epilog, str, r'epilog must be a string')
        istype(self.description, str, r'description must be a string')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts parser bundle to dictionary.

            :return: Dictionary representation of parser bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
