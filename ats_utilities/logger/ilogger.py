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
    Defines the abstract class ILogger with method(s).
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
class ILogger[ConfigType, LogFileType, LogLevelType, MesssageType](Protocol):
    '''
        Defines the abstract class ILogger with attribute(s) and method(s).
        Provides an interface for the logger.

        It defines:

            :methods:
                | get_bundle - Gets the current logger configuration bundle.
                | is_initialized - Checks if the logger is initialized.
                | update_bundle - Updates the logger configuration bundle.
                | set_level - Sets the log level.
                | set_log_file - Configures the output handler to output to the log file.
                | set_stdout - Configures the output handler to output to the standard output.
                | stop_buffering - Stops the log buffering.
                | write_log - Writes the message to the log output.
                | __str__ - Returns the logger as a string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets the current logger configuration bundle.

            :return: The logger configuration bundle.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if the logger is initialized.

            :return: True if successful, otherwise False.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates the logger configuration bundle.

            :param bundle: The logger configuration bundle.
            :return: True if successful, otherwise False.
        '''
        ...

    def set_level(self, level: LogLevelType) -> None:
        '''
            Sets the log level.

            :param level: The log level.
        '''
        ...

    def set_log_file(self, log_file: LogFileType) -> bool:
        '''
            Configures the output handler to output to the log file.

            :param log_file: The log file.
            :return: True if successful, otherwise False.
        '''
        ...

    def set_stdout(self) -> bool:
        '''
            Configures the output handler to output to the standard output.

            :return: True if successful, otherwise False.
        '''
        ...

    def stop_buffering(self) -> None:
        '''
            Stops log buffering.
        '''
        ...

    def write_log(self, level: LogLevelType, message: MesssageType) -> None:
        '''
            Writes the message to the log output.

            :param level: The log message level.
            :param message: The message to be logged.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the logger as a string representation.

            :return: The logger as a string representation.
        '''
        ...
