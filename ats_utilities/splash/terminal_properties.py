# -*- coding: UTF-8 -*-

'''
Module
    terminal_properties.py
Copyright
    Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines API for getting terminal properties.
'''

import sys
import os
from typing import Any
from fcntl import ioctl
from termios import TIOCGWINSZ
from struct import unpack, pack

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TerminalProperties(ATSChecker):
    '''
        Defined class TerminalProperties with attribute(s) and method(s).
        Defined API for getting terminal properties.
        API for terminal properties.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _window_size - Terminal window size.
            :methods:
                | __init__ - Initial TerminalProperties constructor.
                | _ioctl_get_window_size - Size for descriptor.
                | _ioctl_for_all_descriptors - Size for all descriptors.
                | size - Gets size of terminal window.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._window_size: tuple[Any, ...]
        verbose_message(self._verbose, ['init terminal properties'])

    def _ioctl_get_window_size(
        self, file_descriptor: int, verbose: bool = False
    ) -> tuple[Any, ...]:
        '''
            Check window size for descriptor.

            :param file_descriptor: file descriptor.
            :type file_descriptor: <int>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: window size of terminal.
            :rtype: <tupple>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('int:file_descriptor', file_descriptor)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._window_size = unpack(
            'HH', ioctl(file_descriptor, TIOCGWINSZ, pack('HHHH', 0, 0, 0, 0))
        )
        verbose_message(
            self._verbose or verbose,
            [f'terminal window size {self._window_size}']
        )
        return self._window_size

    def _ioctl_for_all_descriptors(self, verbose: bool = False) -> None:
        '''
            Check window size for all descriptors.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (window size checked) else false
            :rtype: <bool>
            :exceptions: None
        '''
        std_in: tuple[Any, ...] = self._ioctl_get_window_size(0)
        std_out: tuple[Any, ...] = self._ioctl_get_window_size(1)
        std_err: tuple[Any, ...] = self._ioctl_get_window_size(2)
        self._window_size = std_in or std_out or std_err
        verbose_message(
            self._verbose or verbose,
            [f'terminal window size {self._window_size}']
        )

    def size(self, verbose: bool = False) -> tuple[Any, ...]:
        '''
            Center console line.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Window size
            :rtype: <tuple>
            :exceptions: None
        '''
        self._ioctl_for_all_descriptors()
        file_descriptor: int = os.open(os.ctermid(), os.O_RDONLY)
        self._window_size = self._ioctl_get_window_size(file_descriptor)
        os.close(file_descriptor)
        verbose_message(
            self._verbose or verbose,
            [f'terminal window size {self._window_size}']
        )
        return self._window_size
