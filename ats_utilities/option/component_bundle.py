# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle data classe for dependency group simplification.
    Encapsulates option components to minimize constructor overhead.
'''

from typing import Any
from dataclasses import dataclass
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class OptionComponentBundle:
    '''
        Defines component bundle data classe for dependency group simplification.
        Encapsulates option components to minimize constructor overhead.

        It defines:

            :attributes:
                | parameters - Configuration parameters (default None).
                | strategy - Strategy for argument parsing (default None).
                | context_bundle - Context bundle for dependency injection (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    parameters: dict[str, str] | None = None
    strategy: IParserStrategy | None = None
    context_bundle: ContextBundle | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError - Parameters must be provided.
                | ATSValueError - Strategy must be provided.
                | ATSValueError - Context bundle must be provided.
        '''
        if self.parameters is None:
            raise ATSValueError("parameters is required.")

        if self.strategy is None:
            raise ATSValueError("strategy is required.")

        if self.context_bundle is None:
            raise ATSValueError("context bundle is required.")

    def merge(self, other: 'OptionComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <OptionComponentBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

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
