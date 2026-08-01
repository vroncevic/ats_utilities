# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines the LogHandlerManager class with attribute(s) and method(s).
    Provides an API for managing the logger output handlers.
'''

from __future__ import annotations

from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LogHandlerManager:
    '''
        Defines the LogHandlerManager class with attribute(s) and method(s).
        Provides an API for managing the logger output handlers.

        It defines:

            :attributes:
                | _logger - The logger to be managed.
            :methods:
                | __init__ - Initializes the log handler manager.
                | set_log_file - Configures the file output handler.
                | set_stdout - Configures the stdout stream handler.
                | __str__ - Returns the log handler manager as a string representation.
    '''

    _logger: IUnderlyingLogger

    def __init__(self, logger: IUnderlyingLogger) -> None:
        '''
            Initializes the log handler manager.

            :param logger: The logger to be managed.
            :exceptions:
                | ATSValueError: The logger must be provided.
                | ATSTypeError:  The logger must be an instance of IUnderlyingLogger.
        '''
        ctx: str = 'log_handler_manager::init(...)'
        msg_logger_none: str = 'the logger must be provided'
        msg_logger_istype: str = 'the logger must be an instance of IUnderlyingLogger'

        not_none(logger, ctx, msg_logger_none)
        istype(logger, ctx, IUnderlyingLogger, msg_logger_istype)

        self._logger = logger

    def set_log_file(self, log_file: str) -> bool:
        '''
            Configures the file output handler.

            :param log_file: The log file path.
            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return self._logger.add_file_handler(log_file)

    def set_stdout(self) -> bool:
        '''
            Configures the stdout stream handler.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return self._logger.add_stdout_handler()

    def __str__(self) -> str:
        '''
            Returns the log handler manager as a string representation.

            :return: The log handler manager as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
