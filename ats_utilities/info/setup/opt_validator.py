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
    Validator for info options.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.utils.setup.iopt_validator import IOptionsValidator
from ats_utilities.info.setup.options import InfoOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
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


class InfoOptionsValidator(IOptionsValidator[InfoOptions]):
    '''
        Validator for info options.

        It defines:

            :methods:
                | validate - Validates info options instance.
    '''

    @classmethod
    @override
    def validate(cls, options: InfoOptions) -> None:
        '''
            Validates info options instance.

            :param options: Info options instance to be validated.
            :type options: InfoOptions
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a Mapping.
                | ATSTypeError: Info must be a Mapping.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Checker must be an instance of IChecker.
                | ATSTypeError: Logger must be an instance of ILogger.
                | ATSTypeError: Reporter must be an instance of IReporter.
                | ATSTypeError: Verbose must be a boolean.
        '''
        ctx: str = r'info_options_validator::validate(...)'

        not_none(options, ctx, r'options must be provided')
        istype(options, Mapping, ctx, r'options must be a Mapping')

        info = options.get('info')

        if info is not None:
            istype(info, Mapping, ctx, r'info must be a Mapping')

        context_bundle = options.get('context_bundle')

        if context_bundle is not None:
            istype(context_bundle, ContextBundle, ctx, r'context bundle must be an instance of ContextBundle')
            ContextValidator.validate(context_bundle)
