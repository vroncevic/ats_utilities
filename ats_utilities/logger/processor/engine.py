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
    Defines the MessageProcessor class with attribute(s) and method(s).
    Provides an API for processing/sanitizing log messages.
'''

from __future__ import annotations

from os import environ
from re import compile, Pattern
from typing import Final
from sys import stdout

from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class MessageProcessor:
    '''
        Defines the MessageProcessor class with attribute(s) and method(s).
        Provides an API for processing/sanitizing log messages.

        :attributes:
            | NO_COLOR - The environment variable for disabling colored output.
            | FORCE_COLOR - The environment variable for forcing colored output.
            | DEFAULT_ESCAPE - The regex pattern for ANSI escape codes.
            | _pattern - The regex pattern for message processing.
        :methods:
            | __init__ - Initializes a message processor.
            | get_pattern - Gets a regex pattern for message processing.
            | set_pattern - Sets a regex pattern for message processing.
            | process - Processes a log message.
            | __str__ - Returns the message processor as a string representation.
    '''

    NO_COLOR: Final[str] = 'NO_COLOR'
    FORCE_COLOR: Final[str] = 'FORCE_COLOR'
    DEFAULT_ESCAPE: Final[Pattern[str]] = compile(r'\x1B(?:[@-Z\\-_]|[\[0-?]*[ -/]*[@-~])')
    _pattern: Pattern[str]

    def __init__(self, pattern: Pattern[str] | None = None) -> None:
        '''
            Initializes a message processor.
            :param pattern: A regex pattern for message processing.
            :exceptions:
                | ATSValueError: The pattern must be provided.
                | ATSTypeError:  The pattern must be a compiled regex pattern.
        '''
        if pattern is not None:
            ctx: str = 'message_processor::init(...)'
            msg_pattern_none: str = 'the pattern must be provided'
            msg_pattern_istype: str = 'the pattern must be a compiled regex pattern'

            not_none(pattern, ctx, msg_pattern_none)
            istype(pattern, Pattern[str], ctx, msg_pattern_istype)

            self._pattern = pattern
        else:
            self._pattern = self.DEFAULT_ESCAPE

    def get_pattern(self) -> Pattern[str]:
        '''
            Gets a regex pattern for message processing.
            :return: A regex pattern for message processing.
            :exceptions: None.
        '''
        return self._pattern

    def set_pattern(self, pattern: Pattern[str]) -> None:
        '''
            Sets a regex pattern for message processing.
            :param pattern: A regex pattern for message processing.
            :exceptions:
                | ATSValueError: The pattern must be provided.
                | ATSTypeError:  The pattern must be a compiled regex pattern.
        '''
        ctx: str = 'message_processor::set_pattern(...)'
        msg_pattern_none: str = 'the pattern must be provided'
        msg_pattern_istype: str = 'the pattern must be a compiled regex pattern'

        not_none(pattern, ctx, msg_pattern_none)
        istype(pattern, Pattern[str], ctx, msg_pattern_istype)

        self._pattern = pattern

    def process(self, message: str) -> str:
        '''
            Processes a log message.

            :param message: A log message to process.
            :return: A processed log message.
            :exceptions: None.
        '''
        no_color: bool = self.NO_COLOR in environ
        force_color: bool = self.FORCE_COLOR in environ
        is_terminal: bool = stdout.isatty()

        if no_color or (not is_terminal and not force_color):
            message = self._pattern.sub('', message)

        return message

    def __str__(self) -> str:
        '''
            Returns the message processor as a string representation.

            :return: The message processor as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
