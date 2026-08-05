# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    Logger dependencies for the logger bundle.
'''

from __future__ import annotations

from typing import TypedDict

from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LoggerBundleDependencies(TypedDict):
    '''
        Logger dependencies for the logger bundle.

        It defines:

            :attributes:
                | logger - The logger for the logger bundle.
                | has_file_handler - The flag indicating if the logger has a file handler for the logger bundle.
                | formatter - The formatter for log messages for the logger bundle.
                | buffer - The buffer for early log messages for the logger bundle.
                | handler_manager - The handler manager for log outputs for the logger bundle.
                | message_processor - The message processor for log messages for the logger bundle.
    '''

    logger: IUnderlyingLogger
    has_file_handler: bool
    formatter: ILogFormatter
    buffer: ILogBuffer
    handler_manager: ILogHandlerManager
    message_processor: IMessageProcessor
