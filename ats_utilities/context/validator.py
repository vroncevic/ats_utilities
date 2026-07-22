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
    Validator for context bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.ivalidator import IValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextValidator(IValidator[ContextBundle]):
    '''
        Validator for context bundle instance.

        It defines:

            :methods:
                | validate - Validates context bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: ContextBundle) -> None:
        '''
            Validates context bundle instance.

            :param bundle: Context bundle instance to be validated.
            :type bundle: ContextBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Bundle must be an instance of ContextBundle.
                | ATSTypeError: Checker must be an instance of IChecker.
                | ATSTypeError: Logger must be an instance of ILogger.
                | ATSTypeError: Reporter must be an instance of IReporter.
                | ATSTypeError: Verbose must be a boolean.
        '''
        ctx: str = r'context_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, ContextBundle, ctx, r'bundle must be an instance of ContextBundle')

        not_none(bundle.checker, ctx, r'checker must be provided')
        not_none(bundle.logger, ctx, r'logger must be provided')
        not_none(bundle.reporter, ctx, r'reporter must be provided')
        not_none(bundle.verbose, ctx, r'verbose must be provided')

        istype(bundle.checker, IChecker, ctx, r'checker must be an instance of IChecker')
        istype(bundle.logger, ILogger, ctx, r'logger must be an instance of ILogger')
        istype(bundle.reporter, IReporter, ctx, r'reporter must be an instance of IReporter')
        istype(bundle.verbose, bool, ctx, r'verbose must be a boolean')
