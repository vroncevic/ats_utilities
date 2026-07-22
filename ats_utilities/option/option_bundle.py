# -*- coding: UTF-8 -*-

'''
Module
    option_bundle.py
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
    Encapsulates core runtime components for simplification of OptionBundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
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


@dataclass(slots=True, frozen=True, kw_only=True)
class OptionBundle:
    '''
        Encapsulates core runtime components for simplification of OptionBundle creation.

        It defines:

            :attributes:
                | parameters - Configuration parameters.
                | strategy - Strategy for argument parsing.
                | context_bundle - Context bundle for dependency injection.
            :methods:
                | __post_init__ - Post-initialization hook to validate option bundle.
                | validate - Validates option bundle.
                | to_dict - Converts option bundle to dictionary.
    '''

    parameters: Mapping[str, str]
    strategy: IParserStrategy
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate option bundle.

            :exceptions:
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates option bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        context: str = r'option_bundle::validate(...)'
        not_none(self.parameters, context, r'parameters must be provided')
        not_none(self.strategy, context, r'strategy must be provided')
        not_none(self.context_bundle, context, r'context bundle must be provided')
        istype(self.parameters, Mapping[str, str], context, r'parameters must be a Mapping[str, str] instance')
        istype(self.strategy, IParserStrategy, context, r'strategy must be an IParserStrategy instance')
        istype(self.context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts option bundle to dictionary.

            :return: Dictionary representation of option bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
