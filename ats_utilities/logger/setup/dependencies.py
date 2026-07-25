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
    Logger dependencies for logger bundle creation.
'''

from __future__ import annotations

from typing import TypedDict, NotRequired, Any

from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LoggerDependencies(TypedDict):
    '''
        Logger dependencies for logger bundle creation.

        It defines:

            :attributes:
                | logger: Logger instance.
                | has_file_handler: Flag indicating if logger has a file handler.
                | formatter: Formatter for log messages.
                | buffer: Buffer for early logs.
                | handler_manager: Manager for log output handlers.
    '''

    logger: NotRequired[Any]
    has_file_handler: NotRequired[bool]
    formatter: NotRequired[ILogFormatter]
    buffer: NotRequired[ILogBuffer]
    handler_manager: NotRequired[ILogHandlerManager]
