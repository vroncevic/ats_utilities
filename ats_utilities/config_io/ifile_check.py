# -*- coding: UTF-8 -*-

'''
Module
    ifile_check.py
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
    Defines abstract class IFileCheck with attribute(s) and method(s).
    Creates an interface for file checking operations.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IFileCheck(ABC):
    '''
        Defines abstract class IFileCheck with attribute(s) and method(s).
        Creates an interface for file checking operations.

        It defines:

            :attributes:
                | MODES - Mode file operations.
                | TRUSTED_EXTENSIONS - List of trusted file extensions.
            :methods:
                | check_path - Checks file path.
                | check_mode - Checks file mode.
                | check_format - Checks file format by extension.
                | is_file_ok - Returns aggregated file status.
                | __str__ - Returns the IFileCheck as string representation.
    '''

    MODES: list[str] = ['r', 'w', 'a', 'b', 'x', 't', '+']
    TRUSTED_EXTENSIONS: list[str] = ['makefile']

    @abstractmethod
    def check_path(self, file_path: str) -> None:
        '''
            Checks file path in string format.

            :param file_path: File path in string format.
            :type file_path: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def check_mode(self, file_mode: str) -> None:
        '''
            Checks file mode in string format.

            :param file_mode: File mode in string format.
            :type file_mode: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def check_format(self, file_path: str, file_format: str) -> None:
        '''
            Checks file format by extension.

            :param file_path: File path in string format.
            :type file_path: <str>
            :param file_format: File format in string format (extension).
            :type file_format: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_file_ok(self) -> bool:
        '''
            Returns aggregated file status.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the IFileCheck as string representation.

            :return: The IFileCheck as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
