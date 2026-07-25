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
    Defines abstract class ILogFormatter with method(s).
    Provides an interface for log formatting (removing color codes, etc.).
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


class ILogFormatter(ABC):
    '''
        Defines abstract class ILogFormatter with method(s).
        Provides an interface for log formatting (removing color codes, etc.).

        It defines:

            :methods:
                | format_message - Formats the log message.
    '''

    @abstractmethod
    def format_message(self, message: str) -> str:
        '''
            Formats the log message.

            :param message: The original log message.
            :return: The formatted log message.
        '''
        pass
