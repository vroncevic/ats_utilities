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
    Defines class LogHandlerManager with attribute(s) and method(s).
    Provides an API for managing logger output handlers.
'''

from __future__ import annotations

from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
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
        Defines class LogHandlerManager with attribute(s) and method(s).
        Provides an API for managing logger output handlers.

        It defines:

            :attributes:
                | _logger - Logger to be managed.
            :methods:
                | __init__ - Initializes the log handler manager.
                | set_log_file - Configures file output handler.
                | set_stdout - Configures stdout stream handler.
                | __str__ - Returns log handler manager as string representation.
    '''

    _logger: IUnderlyingLogger

    def __init__(self, logger: IUnderlyingLogger) -> None:
        '''
            Initializes the log handler manager.

            :param logger: Logger to be managed.
            :exceptions: None.
        '''
        self._logger = logger

    def set_log_file(self, log_file: str) -> bool:
        '''
            Configures file output handler.

            :param log_file: Log file path.
            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._logger.add_file_handler(log_file)

    def set_stdout(self) -> bool:
        '''
            Configures stdout stream handler.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._logger.add_stdout_handler()

    def __str__(self) -> str:
        '''
            Returns log handler manager as string representation.

            :return: Log handler manager as string representation.
            :exceptions: None.
        '''
        return to_str(self)
