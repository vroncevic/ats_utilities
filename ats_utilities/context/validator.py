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
    Validator for the context bundle.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ContextValidator:
    '''
        Validator for the context bundle.

        It defines:

            :methods:
                | validate - Validates the context bundle.
    '''

    @classmethod
    def validate(cls, bundle: ContextBundle) -> None:
        '''
            Validates the context bundle.

            :param bundle: The context bundle to be validated.
            :exceptions:
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
        '''
        ctx: str = 'context_validator::validate(...)'
        msg_bundle_none: str = 'the bundle must be provided'
        msg_bundle_istype: str = 'the bundle must be an instance of ContextBundle'
        msg_checker_none: str = 'the checker must be provided'
        msg_logger_none: str = 'the logger must be provided'
        msg_reporter_none: str = 'the reporter must be provided'
        msg_verbose_none: str = 'the verbose flag must be provided'
        msg_checker_istype: str = 'the checker must be an instance of IChecker'
        msg_logger_istype: str = 'the logger must be an instance of ILogger'
        msg_reporter_istype: str = 'the reporter must be an instance of IReporter'
        msg_verbose_istype: str = 'the verbose flag must be a boolean'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, ContextBundle, ctx, msg_bundle_istype)

        not_none(bundle.checker, ctx, msg_checker_none)
        not_none(bundle.logger, ctx, msg_logger_none)
        not_none(bundle.reporter, ctx, msg_reporter_none)
        not_none(bundle.verbose, ctx, msg_verbose_none)

        istype(bundle.checker, IChecker, ctx, msg_checker_istype)
        istype(bundle.logger, ILogger, ctx, msg_logger_istype)
        istype(bundle.reporter, IReporter, ctx, msg_reporter_istype)
        istype(bundle.verbose, bool, ctx, msg_verbose_istype)
