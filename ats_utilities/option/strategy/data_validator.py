# -*- coding: UTF-8 -*-

'''
Module
    data_validator.py
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
    Validator for StrategyData class.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.validation.check_value import not_none, not_satisfied
from ats_utilities.validation.check_type import istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class StrategyDataValidator(IDataValidator[StrategyData]):
    '''
        Validator for StrategyData class.

        It defines:

            :methods:
                | validate - Validates StrategyData instance.
    '''

    @classmethod
    @override
    def validate(cls, data: StrategyData) -> None:
        '''
            Validates StrategyData instance.

            :param data: StrategyData instance to be validated.
            :type data: StrategyData
            :exceptions:
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Parser class must be provided.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Parser class must be a type subclassing IArgParser.
        '''
        ctx: str = r'strategy_data_validator::validate(...)'
        not_none(data, ctx, r'strategy data must be provided')
        istype(data, StrategyData, ctx, r'strategy data must be an instance of StrategyData')

        not_none(data.parameters, ctx, r'parameters must be provided')
        not_none(data.context_bundle, ctx, r'context bundle must be provided')
        not_none(data.parser_class, ctx, r'parser class must be provided')

        istype(data.parameters, Mapping, ctx, r'parameters must be a Mapping[str, str] instance')
        istype(data.context_bundle, ContextBundle, ctx, r'context bundle must be a ContextBundle instance')
        istype(data.parser_class, type, ctx, r'parser class must be a type')

        not_satisfied(
            not issubclass(data.parser_class, IArgParser),
            ctx, r'parser class must be a class implementing IArgParser'
        )
