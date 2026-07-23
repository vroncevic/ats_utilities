# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    Validator for option bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.utils.ivalidator import IValidator
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


class OptionValidator(IValidator[OptionBundle]):
    '''
        Validator for option bundle instance.

        It defines:

            :methods:
                | validate - Validates option bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: OptionBundle) -> None:
        '''
            Validates option bundle instance.

            :param bundle: Option bundle instance to be validated.
            :type bundle: OptionBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of OptionBundle.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        ctx: str = r'option_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, OptionBundle, ctx, r'bundle must be an instance of OptionBundle')

        not_none(bundle.parameters, ctx, r'parameters must be provided')
        not_none(bundle.strategy, ctx, r'strategy must be provided')
        not_none(bundle.context_bundle, ctx, r'context bundle must be provided')

        istype(bundle.parameters, Mapping[str, str], ctx, r'parameters must be a Mapping[str, str] instance')
        istype(bundle.strategy, IParserStrategy, ctx, r'strategy must be an IParserStrategy instance')
        istype(bundle.context_bundle, ContextBundle, ctx, r'context bundle must be a ContextBundle instance')
