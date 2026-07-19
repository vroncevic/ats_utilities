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

from __future__ import annotations

from fcntl import ioctl
from os import open, ctermid, close, O_RDONLY
from typing import Any, override
from termios import TIOCGWINSZ
from struct import unpack, pack

from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TerminalProperties(ContextSupport, ITerminalProperties):
    '''
        Defines class TerminalProperties with attribute(s) and method(s).
        Creates an API for getting terminal properties.

        It defines:

            :attributes:
                | _window_size - Terminal window size (default None).
            :methods:
                | __init__ - Initials TerminalProperties constructor.
                | ioctl_get_window_size - Gets size for file descriptor.
                | ioctl_for_all_descriptors - Tries to get and set terminal window size.
                | size - Gets terminal window size.
                | __str__ - Returns the string representation of TerminalProperties.
    '''

    _window_size: tuple[Any, ...] | None

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initials TerminalProperties constructor.

            :param context_bundle: Context bundle for terminal properties | None
            :type context_bundle: <ContextBundle | None>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        ContextSupport.__init__(self, context_bundle)
        self._window_size = None

    @mcheck([('int:file_descriptor', None)])
    @vreport('ioctl get window size {window_size}')
    @override
    def ioctl_get_window_size(self, file_descriptor: int) -> tuple[Any, ...]:
        '''
            Gets size for file descriptor.

            :param file_descriptor: File descriptor.
            :type file_descriptor: <int>
            :return: Window size of terminal.
            :rtype: <tuple[Any, ...]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._window_size = unpack('HHHH', ioctl(file_descriptor, TIOCGWINSZ, pack('HHHH', 0, 0, 0, 0)))

        return self._window_size

    @vreport('ioctl for all descriptors {window_size}')
    @override
    def ioctl_for_all_descriptors(self) -> None:
        '''
            Tries to get and set terminal window size using standard file descriptors (0, 1, 2).
            It stops and returns on the first successfully queried descriptor.

            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        for fd in (0, 1, 2):
            try:
                self._window_size = self.ioctl_get_window_size(fd)

                if self._window_size:
                    return

            except (OSError, Exception):
                continue

    @vreport('size {window_size}')
    @override
    def size(self) -> tuple[Any, ...]:
        '''
            Gets terminal window size.

            :return: Terminal window size.
            :rtype: <tuple[Any, ...]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        try:
            self.ioctl_for_all_descriptors()

        except OSError:
            pass

        try:
            file_descriptor: int = open(ctermid(), O_RDONLY)

            try:
                self._window_size = self.ioctl_get_window_size(file_descriptor)
            finally:
                close(file_descriptor)

        except OSError:
            if not self._window_size:
                self._window_size = (24, 80, 0, 0)

        return self._window_size

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of TerminalProperties.

            :return: The TerminalProperties as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
