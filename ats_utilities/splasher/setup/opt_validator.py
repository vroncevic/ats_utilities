# -*- coding: UTF-8 -*-

'''
Module
    opt_validator.py
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
    Validator for splash options.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.splasher.setup.options import SplashOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.setup.iopt_validator import IOptionsValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashOptionsValidator(IOptionsValidator[SplashOptions]):
    '''
        Validator for splash options.

        It defines:

            :methods:
                | validate - Validates splash options instance.
    '''

    @classmethod
    @override
    def validate(cls, options: SplashOptions) -> None:
        '''
            Validates splash options instance.

            :param options: Splash options instance to be validated.
            :type options: SplashOptions
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a Mapping.
                | ATSTypeError: Properties must be a Mapping.
                | ATSTypeError: Context bundle must be a ContextBundle.
        '''
        ctx: str = r'splash_options_validator::validate(...)'

        not_none(options, ctx, r'options must be provided')
        istype(options, Mapping, ctx, r'options must be a Mapping')

        prop = options.get('prop')
        if prop is not None:
            istype(prop, Mapping, ctx, r'prop must be a Mapping')

        context_bundle = options.get('context_bundle')
        not_none(context_bundle, ctx, r'context bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context bundle must be an instance of ContextBundle')
