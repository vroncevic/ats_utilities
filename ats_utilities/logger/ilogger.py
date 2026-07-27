# -*- coding: UTF-8 -*-

'''
Module
    ilogger.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines abstract class ILogger with attribute(s) and method(s).
    Provides an interface for the logger.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class ILogger[ConfigType, MesssageType, LogLevelType](Protocol):
    '''
        Defines abstract class ILogger with attribute(s) and method(s).
        Provides an interface for the logger.

        It defines:

            :methods:
                | get_bundle - Gets current logger configuration bundle.
                | update_bundle - Updates logger configuration bundle.
                | write_log - Writes message to log output.
                | is_initialized - Checks if logger is initialized.
                | stop_buffering - Stops log buffering.
                | __str__ - Returns logger as string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets current logger configuration bundle.

            :return: Logger configuration bundle.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates logger configuration bundle.

            :param bundle: Logger configuration bundle.
        '''
        ...

    def write_log(self, message: MesssageType, level: LogLevelType) -> None:
        '''
            Writes message to log output.

            :param message: Message to be logged.
            :param level: Log message level.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if logger is initialized.

            :return: True if successfully, otherwise False.
        '''
        ...

    def stop_buffering(self) -> None:
        '''
            Stops log buffering.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns logger as string representation.

            :return: Logger as string representation.
        '''
        ...
