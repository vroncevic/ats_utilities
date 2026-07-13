# -*- coding: UTF-8 -*-

'''
Module
    ilog_file.py
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
    Defines abstract class ILogFile with method(s).
    Interface for the log file path mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ILogFile(ABC):
    '''
        Defines abstract class ILogFile with method(s).
        Interface for the log file path mechanism.
        Note: Log file path is only prepared when it is set by user (not None).

        It defines:

            :methods:
                | log_file - Property methods for set/get operations.
                | not_none - Checks if log file path is not None.
                | __str__ - Returns the log file as string representation.
    '''

    @property
    @abstractmethod
    def log_file(self) -> str | None:
        '''
            Property method for getting log file path.
            Note: Log file path is only prepared when it is set by user (not None).

            :return: The log file path in string format | None.
            :rtype: <str | None>
            :exceptions: None.
        '''
        pass

    @log_file.setter
    @abstractmethod
    def log_file(self, log_file: str) -> None:
        '''
            Property method for setting log file path.
            Note: Log file path is only prepared when it is set by user (not None).

            :param log_file: The log file path in string format.
            :type log_file: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if log file path is not None.
            Note: Log file path is only prepared when it is set by user (not None).

            :return: True (Not None) | False (None).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the LogFile as string representation.

            :return: The LogFile as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
