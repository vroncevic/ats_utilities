# -*- coding: UTF-8 -*-

'''
Module
    parser_strategy_bundle.py
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
    Defines class ParserStrategyBundle with attribute(s) and method(s).
    Creates an interfaces for ATS option parsing.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.engine import ArgParser
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class ParserStrategyBundle:
    '''
        Encapsulates core strategy components for ParserStrategy.

        It defines:

            :attributes:
                | parameters - Configuration parameters.
                | context_bundle - Context bundle for strategy.
                | parser_class - Injected parser class type.
            :methods:
                | __post_init__ - Post-initialization hook to validate strategy bundle.
                | validate - Validates strategy bundle.
                | to_dict - Converts strategy bundle to dictionary.
    '''

    parameters: Mapping[str, str]
    context_bundle: ContextBundle
    parser_class: type[IArgParser] = ArgParser

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate strategy bundle.

            :exceptions:
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Parser class must be provided.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Parser class must be a type subclassing IArgParser.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates strategy bundle.
            Performs validation of all bundle attributes.
        '''
        context: str = r'parser_strategy_bundle::validate(...)'
        not_none(self.parameters, context, r'parameters must be provided')
        not_none(self.context_bundle, context, r'context bundle must be provided')
        not_none(self.parser_class, context, r'parser class must be provided')
        istype(self.parameters, Mapping[str, str], context, r'parameters must be a Mapping[str, str] instance')
        istype(self.context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')
        istype(self.parser_class, type, context, r'parser class must be a type')
        not_satisfied(
            not isinstance(self.parser_class, type) and not issubclass(self.parser_class, IArgParser),
            context, r'parser class must be provided'
        )
        istype(self.parameters, Mapping, context, r'parameters must be a Mapping[str, str] instance')
        istype(self.context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')
        not_satisfied(
            not isinstance(self.parser_class, type) and not issubclass(self.parser_class, IArgParser),
            context, r'parser class must be a class implementing IArgParser'
        )

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts strategy bundle to dictionary.

            :return: Dictionary representation of strategy bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
