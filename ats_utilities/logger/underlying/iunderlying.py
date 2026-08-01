# -*- coding: UTF-8 -*-

'''
Module
    iunderlying.py
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
    Defines the abstract class IUnderlyingLogger with method(s).
    Provides an interface for the underlying logger.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class IUnderlyingLogger[MessageType, LogFileType, LogLevelType](Protocol):
    '''
        Defines the abstract class IUnderlyingLogger with method(s).
        Provides an interface for the underlying logger.

        It defines:

            :methods:
                | log - Logs a message with a specific level.
                | set_level - Sets the logging level.
                | has_handlers - Checks if the logger has any handlers.
                | add_file_handler - Adds a file handler for logging.
                | add_stdout_handler - Adds a stdout handler for logging.
                | __str__ - Returns the logger adapter as a string representation.
    '''

    def log(self, level: LogLevelType, message: MessageType) -> None:
        '''
            Logs a message with a specific level.
        
            :param level: The logging level.
            :param message: The message to log.
        '''
        ...

    def set_level(self, level: LogLevelType) -> None:
        '''
            Sets the logging level.
            
            :param level: The logging level.
        '''
        ...

    def has_handlers(self) -> bool:
        '''
            Checks if the logger has any handlers.
            
            :return: True if the logger has any handlers, otherwise False.
        '''
        ...

    def add_file_handler(self, log_file: LogFileType) -> bool:
        '''
            Adds a file handler for logging.
            
            :param log_file: The log file path.
            :return: True if successful, otherwise False.
        '''
        ...

    def add_stdout_handler(self) -> bool:
        '''
            Adds a stdout handler for logging.
            
            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the logger adapter as a string representation.

            :return: The logger adapter as a string representation.
        '''
        ...
