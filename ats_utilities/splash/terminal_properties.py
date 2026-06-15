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
from typing import Any, List, Tuple, Optional
from fcntl import ioctl
from termios import TIOCGWINSZ
from struct import unpack, pack
from ats_utilities.splash.iterminal_properties import ITerminalProperties
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.console_io.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TerminalProperties(ITerminalProperties):
    '''
        Defines class TerminalProperties with attribute(s) and method(s).
        Creates an API for getting terminal properties.
        API for terminal properties.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __window_size - Terminal window size.
            :methods:
                | __init__ - Initials TerminalProperties constructor.
                | ioctl_get_window_size - Gets size for descriptor.
                | ioctl_for_all_descriptors - Sets size for all descriptors.
                | size - Gets size of terminal window.
                | __str__ - Returns the string representation of terminal properties.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials TerminalProperties constructor.

            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter(checker=self.__checker)
        self.__verbose: bool = verbose
        self.__window_size: Tuple[Any, ...]

    @validator([('int:file_descriptor', None)])
    @vreporter('ioctl get window size {window_size}')
    def ioctl_get_window_size(self, file_descriptor: int) -> Tuple[Any, ...]:
        '''
            Gets size for descriptor.

            :param file_descriptor: file descriptor.
            :type file_descriptor: <int>
            :return: Window size of terminal.
            :rtype: <Tuple[Any, ...]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__window_size = unpack('HHHH', ioctl(file_descriptor, TIOCGWINSZ, pack('HHHH', 0, 0, 0, 0)))

        return self.__window_size

    @vreporter('ioctl for all descriptors {window_size}')
    def ioctl_for_all_descriptors(self) -> None:
        '''
            Sets size for all descriptors.

            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        std_in: Tuple[Any, ...] = self.ioctl_get_window_size(0)
        std_out: Tuple[Any, ...] = self.ioctl_get_window_size(1)
        std_err: Tuple[Any, ...] = self.ioctl_get_window_size(2)
        self.__window_size = std_in or std_out or std_err

    @vreporter('size {window_size}')
    def size(self) -> Tuple[Any, ...]:
        '''
            Gets size of terminal window.

            :return: Window size
            :rtype: <Tuple[Any, ...]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        self.ioctl_for_all_descriptors()
        file_descriptor: int = os.open(os.ctermid(), os.O_RDONLY)
        self.__window_size = self.ioctl_get_window_size(file_descriptor)
        os.close(file_descriptor)

        return self.__window_size

    def __str__(self) -> str:
        '''
            Returns the string representation of terminal properties.

            :return: The terminal properties as string
            :rtype: <str>
            :exceptions: None
        '''
        window_size = str(self.__window_size).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    window_size={window_size},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
