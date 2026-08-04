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
    Validator for the reporter bundle.
'''

from __future__ import annotations

from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ReporterBundleValidator:
    '''
        Validator for the reporter bundle.

        It defines:

            :methods:
                | validate - Validates the reporter bundle.
    '''

    @classmethod
    def validate(cls, bundle: ReporterBundle) -> None:
        '''
            Validates the reporter bundle.

            :param bundle: The reporter bundle to be validated.
            :exceptions:
                | ATSValueError: The reporter bundle must be provided and have proper values.
                | ATSTypeError:  The reporter bundle must be an instance of ReporterBundle
                |                and its attributes must be instances of their respective types.
        '''
        ctx: str = 'reporter_bundle_validator::validate(...)'
        msg_bundle_none: str = f'the reporter bundle must be provided'
        msg_bundle_istype: str = f'the reporter bundle must be an instance of ReporterBundle'
        msg_checker_none: str = f'the checker must be provided'
        msg_checker_istype: str = f'the checker must be an instance of IChecker interface'
        msg_theme_none: str = f'the theme must be provided'
        msg_theme_istype: str = f'the theme must be an instance of IConsoleTheme interface'
        msg_logger_none: str = f'the logger must be provided'
        msg_logger_istype: str = f'the logger must be an instance of ILogger interface'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, ReporterBundle, ctx, msg_bundle_istype)

        not_none(bundle.checker, ctx, msg_checker_none)
        not_none(bundle.theme, ctx, msg_theme_none)
        not_none(bundle.logger, ctx, msg_logger_none)

        istype(bundle.checker, IChecker, ctx, msg_checker_istype)
        istype(bundle.theme, IConsoleTheme, ctx, msg_theme_istype)
        istype(bundle.logger, ILogger, ctx, msg_logger_istype)
