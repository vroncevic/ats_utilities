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
    Validator for strategy data.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.option.underlying.iunderlying import IUnderlyingParser
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class StrategyDataValidator:
    '''
        Validator for strategy data.

        It defines:

            :methods:
                | validate - Validates strategy data.
    '''

    @classmethod
    def validate(cls, data: StrategyData) -> None:
        '''
            Validates strategy data instance.

            :param data: StrategyData instance to be validated.
            :exceptions:
                | ATSValueError: Strategy data must be provided and have proper values.
                | ATSTypeError:  Strategy data must be an instance of StrategyData and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'strategy_data_validator::validate(...)'
        msg_data_none: str = 'strategy data must be provided'
        msg_data_istype: str = 'strategy data must be an instance of StrategyData'
        msg_context_bundle_none: str = 'context bundle must be provided'
        msg_parser_none: str = 'parser must be provided'
        msg_context_bundle_istype: str = 'context bundle must be a ContextBundle instance'
        msg_parser_istype: str = 'parser must be an instance of IUnderlyingParser'

        not_none(data, ctx, msg_data_none)
        not_none(data.context_bundle, ctx, msg_context_bundle_none)
        not_none(data.parser, ctx, msg_parser_none)

        istype(data, StrategyData, ctx, msg_data_istype)
        istype(data.context_bundle, ContextBundle, ctx, msg_context_bundle_istype)
        istype(data.parser, IUnderlyingParser, ctx, msg_parser_istype)

        ContextValidator.validate(data.context_bundle)
