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
    Validator for ParserData class.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.data import ParserData
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ParserDataValidator(IDataValidator[ParserData]):
    '''
        Validator for ParserData class.

        It defines:

            :methods:
                | validate - Validates ParserData instance.
    '''

    @classmethod
    @override
    def validate(cls, data: ParserData) -> None:
        '''
            Validates ParserData instance.

            :param data: ParserData instance to be validated.
            :type data: ParserData
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
        ctx: str = r'parser_data_validator::validate(...)'
        not_none(data, ctx, r'parser data must be provided')
        istype(data, ParserData, ctx, r'parser data must be an instance of ParserData')

        not_none(data.context_bundle, ctx, r'context bundle must be provided')
        not_none(data.prog, ctx, r'prog must be provided')
        not_none(data.epilog, ctx, r'epilog must be provided')
        not_none(data.description, ctx, r'description must be provided')

        istype(data.context_bundle, ContextBundle, ctx, r'context bundle must be a ContextBundle instance')
        istype(data.prog, str, ctx, r'prog must be a string')
        istype(data.epilog, str, ctx, r'epilog must be a string')
        istype(data.description, str, ctx, r'description must be a string')
