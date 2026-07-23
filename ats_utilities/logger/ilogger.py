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
    Interface for the logger mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'1.0.0'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ILogger(ABC):
    '''
        Defines abstract class ILogger with attribute(s) and method(s).
        Interface for the logger mechanism.

        It defines:

            :methods:
                | write_log - Writes message to log output.
                | is_initialized - Checks if logger is initialized.
                | set_level - Sets log level.
                | set_log_file - Sets log file.
                | set_stdout - Sets log output to standard output (stdout).
                | set_stderr - Sets log output to standard error (stderr).
                | stop_buffering - Stops log buffering.
                | __str__ - Returns the logger as string representation.
    '''

    @abstractmethod
    def write_log(self, message: str, ctrl: int) -> None:
        '''
            Writes message to log output.

            :param message: Log message.
            :type message: str
            :param ctrl: Log control flag.
            :type ctrl: int
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if logger is initialized.

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def set_level(self, level: int) -> None:
        '''
            Sets log level.

            :param level: Log level.
            :type level: int
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def set_log_file(self, log_file: str) -> None:
        '''
            Sets log file.

            :param log_file: Log file path.
            :type log_file: str
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def set_stdout(self) -> None:
        '''
            Sets log output to standard output (stdout).

            :exceptions: None.
        '''
        pass

    @abstractmethod
    def set_stderr(self) -> None:
        '''
            Sets log output to standard error (stderr).

            :exceptions: None.
        '''
        pass

    @abstractmethod
    def stop_buffering(self) -> None:
        '''
            Stops log buffering.

            :exceptions: None.
        '''
        pass

    def __str__(self) -> str:
        '''
            Returns the logger as string representation.

            :return: The logger as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
