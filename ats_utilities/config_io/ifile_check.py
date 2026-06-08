# -*- coding: utf-8 -*-

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

from abc import ABC, abstractmethod
from typing import List, Optional

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.roncevic@gmail.com'
__status__: str = 'Updated'


class IFileCheck(ABC):
    '''
        Defines abstract class IFileCheck with attribute(s) and method(s).
        Creates an interface for file checking operations.

        It defines:

            :attributes:
                | MODES - Mode file operations.
                | TRUSTED_EXTENSIONS - List of trusted file extensions.
            :methods:
                | check_path - Check file path (abstract).
                | check_mode - Check file mode (abstract).
                | check_format - Check file format by extension (abstract).
                | is_file_ok - Return aggregated file status (abstract).
    '''

    MODES: List[str] = ['r', 'w', 'a', 'b', 'x', 't', '+']
    TRUSTED_EXTENSIONS: List[str] = ['makefile']

    @abstractmethod
    def check_path(self, file_path: Optional[str], verbose: bool = False) -> None:
        '''
            Check file path.

            :param file_path: File path | None
            :type file_path: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement check_path method")

    @abstractmethod
    def check_mode(self, file_mode: Optional[str], verbose: bool = False) -> None:
        '''
            Check file mode.

            :param file_mode: File mode | None
            :type file_mode: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement check_mode method")

    @abstractmethod
    def check_format(self, file_path: Optional[str], file_format: Optional[str], verbose: bool = False) -> None:
        '''
            Check file format by extension.

            :param file_path: File path | None
            :type file_path: <Optional[str]>
            :param file_format: File format (extension) | None
            :type file_format: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement check_format method")

    @abstractmethod
    def is_file_ok(self) -> bool:
        '''
            Return aggregated file status.

            :return: True if file checks passed | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement is_file_ok method")
