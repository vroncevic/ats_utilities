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
        Validator for context bundle instance.

        It defines:

            :methods:
                | validate - Validates context bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: ContextBundle) -> None:
        '''
            Validates context bundle instance.

            :param bundle: Context bundle instance to be validated.
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSValueError: Verbose must be provided.
                | ATSTypeError:  Bundle must be an instance of ContextBundle.
                | ATSTypeError:  Checker must be an instance of IChecker.
                | ATSTypeError:  Logger must be an instance of ILogger.
                | ATSTypeError:  Reporter must be an instance of IReporter.
                | ATSTypeError:  Verbose must be a boolean.
        '''
        ctx: str = 'context_validator::validate(...)'

        not_none(bundle, ctx, 'bundle must be provided')
        istype(bundle, ContextBundle, ctx, 'bundle must be an instance of ContextBundle')

        not_none(bundle.checker, ctx, 'checker must be provided')
        not_none(bundle.logger, ctx, 'logger must be provided')
        not_none(bundle.reporter, ctx, 'reporter must be provided')
        not_none(bundle.verbose, ctx, 'verbose must be provided')

        istype(bundle.checker, IChecker, ctx, 'checker must be an instance of IChecker')
        istype(bundle.logger, ILogger, ctx, 'logger must be an instance of ILogger')
        istype(bundle.reporter, IReporter, ctx, 'reporter must be an instance of IReporter')
        istype(bundle.verbose, bool, ctx, 'verbose must be a boolean')
