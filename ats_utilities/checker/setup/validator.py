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
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class CheckerValidator:
    '''
        Validator for checker bundle instance.

        It defines:

            :methods:
                | validate - Validates checker bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: CheckerBundle) -> None:
        '''
            Validates checker bundle instance.

            :param bundle: Checker bundle instance to be validated.
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format validator must be provided.
                | ATSValueError: Type validator must be provided.
                | ATSTypeError:  Bundle must be an instance of CheckerBundle.
                | ATSTypeError:  Context provider must be an instance of IContextProvider.
                | ATSTypeError:  Check reporter must be an instance of ICheckReporter.
                | ATSTypeError:  Format validator must be an instance of IFormatValidator.
                | ATSTypeError:  Type validator must be an instance of ITypeValidator.
        '''
        ctx: str = 'checker_validator::validate(...)'

        msg_bundle_none: str = 'bundle must be provided'
        msg_bundle_istype: str = 'bundle must be an instance of CheckerBundle'
        msg_context_provider_none: str = 'context provider must be provided'
        msg_check_reporter_none: str = 'check reporter must be provided'
        msg_format_validator_none: str = 'format validator must be provided'
        msg_type_validator_none: str = 'type validator must be provided'
        msg_context_provider_istype: str = 'context provider must be an instance of IContextProvider'
        msg_check_reporter_istype: str = 'check reporter must be an instance of ICheckReporter'
        msg_format_validator_istype: str = 'format validator must be an instance of IFormatValidator'
        msg_type_validator_istype: str = 'type validator must be an instance of ITypeValidator'

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
