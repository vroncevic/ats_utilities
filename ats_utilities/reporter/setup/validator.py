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
    Validator for reporter bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
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


class ReporterValidator(IValidator[ReporterBundle]):
    '''
        Validator for reporter bundle instance.

        It defines:

            :methods:
                | validate - Validates reporter bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: ReporterBundle) -> None:
        '''
            Validates reporter bundle instance.

            :param bundle: Reporter bundle instance to be validated.
            :type bundle: ReporterBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Theme must be provided.
                | ATSValueError: Logger must be provided.
                | ATSTypeError: Bundle must be an instance of ReporterBundle.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Theme must be an instance of IConsoleTheme interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        ctx: str = r'reporter_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, ReporterBundle, ctx, r'bundle must be an instance of ReporterBundle')

        not_none(bundle.checker, ctx, r'checker must be provided')
        not_none(bundle.theme, ctx, r'theme must be provided')
        not_none(bundle.logger, ctx, r'logger must be provided')

        istype(bundle.checker, IChecker, ctx, r'checker must be an IChecker instance')
        istype(bundle.theme, IConsoleTheme, ctx, r'theme must be an IConsoleTheme instance')
        istype(bundle.logger, ILogger, ctx, r'logger must be an ILogger instance')
