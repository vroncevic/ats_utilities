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
    Validator for logger bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.utils.ivalidator import IValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LoggerValidator(IValidator[LoggerBundle]):
    '''
        Validator for logger bundle instance.

        It defines:

            :methods:
                | validate - Validates logger bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: LoggerBundle) -> None:
        '''
            Validates logger bundle instance.

            :param bundle: Logger bundle instance to be validated.
            :type bundle: LoggerBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Log file must be provided.
                | ATSValueError: Log level must be provided.
                | ATSTypeError: Bundle must be an instance of LoggerBundle.
                | ATSTypeError: Log file must be a str instance.
                | ATSTypeError: Log level must be an int instance.
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
        '''
        ctx: str = r'logger_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, LoggerBundle, ctx, r'bundle must be an instance of LoggerBundle')

        not_none(bundle.logger, ctx, r'logger must be provided')
        not_none(bundle.log_file, ctx, r'log file must be provided')
        not_none(bundle.log_level, ctx, r'log level must be provided')

        istype(bundle.log_file, str, ctx, r'log file must be a str instance')
        istype(bundle.log_level, int, ctx, r'log level must be an int instance')

        not_satisfied(
            not (hasattr(bundle.logger, 'info') or hasattr(bundle.logger, 'write_log')), ctx,
            r'logger must be an ILogger instance or a standard logging.Logger instance'
        )
