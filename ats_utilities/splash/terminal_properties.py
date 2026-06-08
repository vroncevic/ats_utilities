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
from typing import Any, ClassVar, List, Tuple, Optional
from fcntl import ioctl
from termios import TIOCGWINSZ
from struct import unpack, pack
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.checker import IATSChecker, ATSChecker, ErrorChecker
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from .iterminal_properties import ITerminalProperties

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
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
                | ERRORS - Error checker.
                | __checker - Error checker.
                | __reporter - ATSReporter for outputting messages.
                | __verbose - Enable/Disable verbose option.
                | __window_size - Terminal window size.
            :methods:
                | __init__ - Initials TerminalProperties constructor.
                | ioctl_get_window_size - Gets size for descriptor.
                | ioctl_for_all_descriptors - Gets size for all descriptors.
                | size - Gets size of terminal window.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials TerminalProperties constructor.

            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for outputting messages | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__window_size: Tuple[Any, ...]
        self.__reporter.verbose(self.__verbose, ['init terminal properties'])

    def ioctl_get_window_size(self, file_descriptor: int, verbose: bool = False) -> Tuple[Any, ...]:
        '''
            Gets size for descriptor.

            :param file_descriptor: file descriptor.
            :type file_descriptor: <int>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Window size of terminal.
            :rtype: <Tuple[Any, ...]>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('int:file_descriptor', file_descriptor)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        if file_descriptor < 0:
            raise ATSValueError(error_msg)

        self.__window_size = unpack('HHHH', ioctl(file_descriptor, TIOCGWINSZ, pack('HHHH', 0, 0, 0, 0)))
        self.__reporter.verbose(self.__verbose or verbose, [f'terminal window size {self.__window_size}'])
        return self.__window_size

    def ioctl_for_all_descriptors(self, verbose: bool = False) -> None:
        '''
            Gets size for all descriptors.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (window size checked) else false
            :rtype: <bool>
            :exceptions: None
        '''
        std_in: Tuple[Any, ...] = self.ioctl_get_window_size(0)
        std_out: Tuple[Any, ...] = self.ioctl_get_window_size(1)
        std_err: Tuple[Any, ...] = self.ioctl_get_window_size(2)
        self.__window_size = std_in or std_out or std_err
        self.__reporter.verbose(self.__verbose or verbose, [f'terminal window size {self.__window_size}'])

    def size(self, verbose: bool = False) -> Tuple[Any, ...]:
        '''
            Gets size of terminal window.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Window size
            :rtype: <Tuple[Any, ...]>
            :exceptions: None
        '''
        self.ioctl_for_all_descriptors()
        file_descriptor: int = os.open(os.ctermid(), os.O_RDONLY)
        self.__window_size = self.ioctl_get_window_size(file_descriptor)
        os.close(file_descriptor)
        self.__reporter.verbose(self.__verbose or verbose, [f'terminal window size {self.__window_size}'])
        return self.__window_size
