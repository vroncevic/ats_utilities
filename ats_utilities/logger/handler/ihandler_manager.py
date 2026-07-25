# -*- coding: UTF-8 -*-

'''
Module
    ihandler_manager.py
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
    Defines abstract class ILogHandlerManager with method(s).
    Provides an interface for log handler manager.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ILogHandlerManager(ABC):
    '''
        Defines abstract class ILogHandlerManager with method(s).
        Provides an interface for log handler manager.

        It defines:

            :methods:
                | set_log_file - Configures file output handler.
                | set_stdout - Configures stdout stream handler.
                | set_stderr - Configures stderr stream handler.
                | __str__ - Returns log handler manager as string representation.
    '''

    @abstractmethod
    def set_log_file(self, log_file: str) -> bool:
        '''
            Configures file output handler.

            :param log_file: Log file path.
            :return: True if successfully, otherwise False.
        '''
        pass

    @abstractmethod
    def set_stdout(self) -> bool:
        '''
            Configures stdout stream handler.

            :return: True if successfully, otherwise False.
        '''
        pass

    @abstractmethod
    def set_stderr(self) -> bool:
        '''
            Configures stderr stream handler.

            :return: True if successfully, otherwise False.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns log handler manager as string representation.

            :return: Log handler manager as string representation.
        '''
        pass