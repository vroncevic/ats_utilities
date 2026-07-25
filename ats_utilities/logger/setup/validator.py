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
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.utils.setup.ivalidator import IValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
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
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Has file handler flag must be provided.
                | ATSValueError: Formatter must be provided.
                | ATSValueError: Buffer must be provided.
                | ATSValueError: Handler manager must be provided.
                | ATSTypeError: Bundle must be an instance of LoggerBundle.
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
                | ATSTypeError: Has file handler flag must be a boolean instance.
                | ATSTypeError: Formatter must be an instance of ILogFormatter.
                | ATSTypeError: Buffer must be an instance of ILogBuffer.
                | ATSTypeError: Handler manager must be an instance of ILogHandlerManager.
        '''
        ctx: str = r'logger_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, LoggerBundle, ctx, r'bundle must be an instance of LoggerBundle')

        not_none(bundle.logger, ctx, r'logger must be provided')
        not_none(bundle.has_file_handler, ctx, r'has file handler flag must be provided')
        not_none(bundle.formatter, ctx, r'formatter must be provided')
        not_none(bundle.buffer, ctx, r'buffer must be provided')
        not_none(bundle.handler_manager, ctx, r'handler manager must be provided')

        istype(bundle.has_file_handler, bool, ctx, r'has file handler flag must be a boolean instance')
        istype(bundle.formatter, ILogFormatter, ctx, r'formatter must be an instance of ILogFormatter')
        istype(bundle.buffer, ILogBuffer, ctx, r'buffer must be an instance of ILogBuffer')
        istype(bundle.handler_manager, ILogHandlerManager, ctx, r'handler manager must be an instance of ILogHandlerManager')

        not_satisfied(
            not (hasattr(bundle.logger, 'info') or hasattr(bundle.logger, 'write_log')), ctx,
            r'logger must be an ILogger instance or a standard logging.Logger instance'
        )
