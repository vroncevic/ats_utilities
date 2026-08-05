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
    Validator for the checker bundle.
'''

from __future__ import annotations

from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class CheckerBundleValidator:
    '''
        Validator for the checker bundle.

        It defines:

            :methods:
                | validate - Validates the checker bundle.
    '''

    @classmethod
    def validate(cls, bundle: CheckerBundle) -> None:
        '''
            Validates the checker bundle.

            :param bundle: The checker bundle to be validated.
            :exceptions:
                | ATSValueError: The checker bundle must be provided and have proper values.
                | ATSTypeError:  The checker bundle must be an instance of CheckerBundle
                |                and its attributes must be instances of their respective types.
        '''
        ctx: str = 'checker_bundle_validator::validate(...)'
        msg_bundle_none: str = 'the checker bundle must be provided'
        msg_bundle_istype: str = 'the checker bundle must be an instance of CheckerBundle'
        msg_context_provider_none: str = 'the checker context provider must be provided'
        msg_check_reporter_none: str = 'the checker check reporter must be provided'
        msg_format_validator_none: str = 'the checker format validator must be provided'
        msg_type_validator_none: str = 'the checker type validator must be provided'
        msg_context_provider_istype: str = 'the checker context provider must be an instance of IContextProvider'
        msg_check_reporter_istype: str = 'the checker check reporter must be an instance of ICheckReporter'
        msg_format_validator_istype: str = 'the checker format validator must be an instance of IFormatValidator'
        msg_type_validator_istype: str = 'the checker type validator must be an instance of ITypeValidator'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, CheckerBundle, ctx, msg_bundle_istype)

        not_none(bundle.context_provider, ctx, msg_context_provider_none)
        not_none(bundle.check_reporter, ctx, msg_check_reporter_none)
        not_none(bundle.format_validator, ctx, msg_format_validator_none)
        not_none(bundle.type_validator, ctx, msg_type_validator_none)

        istype(bundle.context_provider, IContextProvider, ctx, msg_context_provider_istype)
        istype(bundle.check_reporter, ICheckReporter, ctx, msg_check_reporter_istype)
        istype(bundle.format_validator, IFormatValidator, ctx, msg_format_validator_istype)
        istype(bundle.type_validator, ITypeValidator, ctx, msg_type_validator_istype)
