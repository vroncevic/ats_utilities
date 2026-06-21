# -*- coding: UTF-8 -*-

'''
Module
    terminal_properties.py
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
    Defines class TerminalProperties with attribute(s) and method(s).
    Creates an API for getting terminal properties.
'''

import os
from typing import Any
from fcntl import ioctl
from termios import TIOCGWINSZ
from struct import unpack, pack
from ats_utilities.splasher.iterminal_properties import ITerminalProperties
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TerminalProperties(ITerminalProperties):
    '''
        Defines class TerminalProperties with attribute(s) and method(s).
        Creates an API for getting terminal properties.

        It defines:

            :attributes:
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
                | _window_size - Terminal window size.
            :methods:
                | __init__ - Initials TerminalProperties constructor.
                | ioctl_get_window_size - Gets size for file descriptor.
                | ioctl_for_all_descriptors - Sets size for all file descriptors.
                | size - Gets terminal window size.
                | __str__ - Returns the string representation of TerminalProperties.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initials TerminalProperties constructor.

            :param context_bundle: Context bundle for terminal properties | None
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._window_size: tuple[Any, ...]

    @validator([('int:file_descriptor', None)])
    @vreporter('ioctl get window size {window_size}')
    def ioctl_get_window_size(self, file_descriptor: int) -> tuple[Any, ...]:
        '''
            Gets size for file descriptor.

            :param file_descriptor: File descriptor.
            :type file_descriptor: <int>
            :return: Window size of terminal.
            :rtype: <tuple[Any, ...]>
            :exceptions: ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError.
        '''
        self._window_size = unpack('HHHH', ioctl(file_descriptor, TIOCGWINSZ, pack('HHHH', 0, 0, 0, 0)))

        return self._window_size

    @vreporter('ioctl for all descriptors {window_size}')
    def ioctl_for_all_descriptors(self) -> None:
        '''
            Sets size for all file descriptors.

            :exceptions: ATSRuntimeError, ATSAttributeError
        '''
        std_in: tuple[Any, ...] = self.ioctl_get_window_size(0)
        std_out: tuple[Any, ...] = self.ioctl_get_window_size(1)
        std_err: tuple[Any, ...] = self.ioctl_get_window_size(2)
        self._window_size = std_in or std_out or std_err

    @vreporter('size {window_size}')
    def size(self) -> tuple[Any, ...]:
        '''
            Gets terminal window size.

            :return: Terminal window size.
            :rtype: <tuple[Any, ...]>
            :exceptions: ATSRuntimeError, ATSAttributeError
        '''
        try:
            self.ioctl_for_all_descriptors()
        except OSError:
            pass

        try:
            file_descriptor: int = os.open(os.ctermid(), os.O_RDONLY)
            self._window_size = self.ioctl_get_window_size(file_descriptor)
            os.close(file_descriptor)
        except OSError:
            # Fall back to self._window_size if set, otherwise default to (24, 80, 0, 0)
            if not hasattr(self, '_TerminalProperties__window_size') or not self._window_size:
                self._window_size = (24, 80, 0, 0)

        return self._window_size

    def __str__(self) -> str:
        '''
            Returns the string representation of TerminalProperties.

            :return: The TerminalProperties as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
