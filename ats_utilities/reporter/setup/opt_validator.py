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
    Validator for reporter options.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.reporter.setup.options import ReporterOptions
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


class ReporterOptionsValidator(IOptionsValidator[ReporterOptions]):
    '''
        Validator for reporter options.

        It defines:

            :methods:
                | validate - Validates reporter options instance.
    '''

    @classmethod
    @override
    def validate(cls, options: ReporterOptions) -> None:
        '''
            Validates reporter options instance.

            :param options: Reporter options instance to be validated.
            :type options: ReporterOptions
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a Mapping.
                | ATSTypeError: Checker options must be a Mapping.
                | ATSTypeError: Theme options must be a Mapping.
                | ATSTypeError: Logger options must be a Mapping.
        '''
        ctx: str = r'reporter_options_validator::validate(...)'

        not_none(options, ctx, r'options must be provided')
        istype(options, Mapping, ctx, r'options must be a Mapping')

        checker = options.get('checker')

        if checker is not None:
            istype(checker, Mapping, ctx, r'checker options must be a Mapping')

        theme = options.get('theme')

        if theme is not None:
            istype(theme, Mapping, ctx, r'theme options must be a Mapping')

        logger = options.get('logger')

        if logger is not None:
            istype(logger, Mapping, ctx, r'logger options must be a Mapping')
