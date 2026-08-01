# -*- coding: UTF-8 -*-

'''
Module
    iformatter.py
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
    Defines the abstract class ILogFormatter with method(s).
    Provides an interface for log formatting.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class ILogFormatter[LogFormatType, LogDateFormatType, MessageType](Protocol):
    '''
        Defines the abstract class ILogFormatter with method(s).
        Provides an interface for log formatting.

        It defines:

            :methods:
                | set_format - Sets the log format.
                | get_format - Gets the log format.
                | set_date_format - Sets the log date format.
                | get_date_format - Gets the log date format.
                | __str__ - Returns the log formatter as a string representation.
    '''

    def set_format(self, log_format: LogFormatType) -> None:
        '''
            Sets the log format.

            :param log_format: The log format.
        '''
        ...

    def get_format(self) -> LogFormatType:
        '''
            Gets the log format.

            :return: The log format.
        '''
        ...

    def set_date_format(self, log_datefmt: LogDateFormatType) -> None:
        '''
            Sets the log date format.

            :param log_datefmt: The log date format.
        '''
        ...

    def get_date_format(self) -> LogDateFormatType:
        '''
            Gets the log date format.

            :return: The log date format.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the log formatter as a string representation.

            :return: The log formatter as a string representation.
        '''
        ...
