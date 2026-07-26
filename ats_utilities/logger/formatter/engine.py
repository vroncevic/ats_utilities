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
    Defines class LogFormatter with attribute(s) and method(s).
    Provides an API for log formatting (removing color codes, etc.).
'''

from __future__ import annotations

from os import environ
from re import compile, Pattern
from sys import stdout

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LogFormatter:
    '''
        Defines class LogFormatter with attribute(s) and method(s).
        Provides an API for log formatting (removing color codes, etc.).

        It defines:

            :attributes:
                | _ANSI_ESCAPE - Regex pattern for ANSI escape codes.
            :methods:
                | format_message - Formats the log message.
    '''

    _ANSI_ESCAPE: Pattern[str] = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    def format_message(self, message: str) -> str:
        '''
            Formats the log message by checking the environment.
            Stripping ANSI color codes if output is redirected or disabled.

            :param message: The original log message.
            :return: The formatted log message.
            :exceptions: None.
        '''
        no_color: bool = 'NO_COLOR' in environ
        force_color: bool = 'FORCE_COLOR' in environ
        is_terminal: bool = stdout.isatty()

        if no_color or (not is_terminal and not force_color):
            message = self._ANSI_ESCAPE.sub('', message)

        return message
