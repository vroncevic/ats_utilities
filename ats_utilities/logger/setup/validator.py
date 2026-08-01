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
    A validator for the logger bundle instance.
'''

from __future__ import annotations

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor
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


class LoggerValidator:
    '''
        A validator for the logger bundle instance.

        It defines:

            :methods:
                | validate - Validates the logger bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: LoggerBundle) -> None:
        '''
            Validates the logger bundle instance.

            :param bundle: The logger bundle to be validated.
            :exceptions:
                | ATSValueError: The bundle must be provided and have proper values.
                | ATSTypeError:  The bundle must be an instance of LoggerBundle and its attributes
                |                must be instances of their respective types.
        '''
        ctx: str = 'logger_validator::validate(...)'

        msg_bundle_none: str = 'the bundle must be provided'
        msg_bundle_istype: str = 'the bundle must be an instance of LoggerBundle'
        msg_logger_none: str = 'the logger must be provided'
        msg_logger_istype: str = 'the logger must be an instance of IUnderlyingLogger'
        msg_has_file_handler_none: str = 'the has file handler flag must be provided'
        msg_has_file_handler_istype: str = 'the has file handler flag must be a boolean instance'
        msg_formatter_none: str = 'the formatter must be provided'
        msg_formatter_istype: str = 'the formatter must be an instance of ILogFormatter'
        msg_buffer_none: str = 'the buffer must be provided'
        msg_buffer_istype: str = 'the buffer must be an instance of ILogBuffer'
        msg_handler_manager_none: str = 'the handler manager must be provided'
        msg_handler_manager_istype: str = 'the handler manager must be an instance of ILogHandlerManager'
        msg_message_processor_none: str = 'the message processor must be provided'
        msg_message_processor_istype: str = 'the message processor must be an instance of IMessageProcessor'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, LoggerBundle, ctx, msg_bundle_istype)

        not_none(bundle.logger, ctx, msg_logger_none)
        not_none(bundle.has_file_handler, ctx, msg_has_file_handler_none)
        not_none(bundle.formatter, ctx, msg_formatter_none)
        not_none(bundle.buffer, ctx, msg_buffer_none)
        not_none(bundle.handler_manager, ctx, msg_handler_manager_none)
        not_none(bundle.message_processor, ctx, msg_message_processor_none)

        istype(bundle.logger, IUnderlyingLogger, ctx, msg_logger_istype)
        istype(bundle.has_file_handler, bool, ctx, msg_has_file_handler_istype)
        istype(bundle.formatter, ILogFormatter, ctx, msg_formatter_istype)
        istype(bundle.buffer, ILogBuffer, ctx, msg_buffer_istype)
        istype(bundle.handler_manager, ILogHandlerManager, ctx, msg_handler_manager_istype)
        istype(bundle.message_processor, IMessageProcessor, ctx, msg_message_processor_istype)
