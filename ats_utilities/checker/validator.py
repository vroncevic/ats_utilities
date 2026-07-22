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
    Validator for checker bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.checker.bundle import CheckerBundle
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
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


class CheckerValidator(IValidator[CheckerBundle]):
    '''
        Validator for checker bundle instance.

        It defines:

            :methods:
                | validate - Validates checker bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: CheckerBundle) -> None:
        '''
            Validates checker bundle instance.

            :param bundle: Checker bundle instance to be validated.
            :type bundle: CheckerBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format validator must be provided.
                | ATSValueError: Type validator must be provided.
                | ATSTypeError: Bundle must be an instance of CheckerBundle.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
                | ATSTypeError: Format validator must be an instance of IFormatValidator.
                | ATSTypeError: Type validator must be an instance of ITypeValidator.
        '''
        ctx: str = r'checker_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, CheckerBundle, ctx, r'bundle must be an instance of CheckerBundle')

        not_none(bundle.context_provider, ctx, r'context provider must be provided')
        not_none(bundle.check_reporter, ctx, r'check reporter must be provided')
        not_none(bundle.format_validator, ctx, r'format validator must be provided')
        not_none(bundle.type_validator, ctx, r'type validator must be provided')

        istype(bundle.context_provider, IContextProvider, ctx, r'context provider must be an instance of IContextProvider')
        istype(bundle.check_reporter, ICheckReporter, ctx, r'check reporter must be an instance of ICheckReporter')
        istype(bundle.format_validator, IFormatValidator, ctx, r'format validator must be an instance of IFormatValidator')
        istype(bundle.type_validator, ITypeValidator, ctx, r'type validator must be an instance of ITypeValidator')
