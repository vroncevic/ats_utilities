# -*- coding: UTF-8 -*-

'''
Module
    ireporter.py
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
    Defines abstract class IReporter with method(s).
    Creates an interface for reporting message.
'''

from __future__ import annotations

from collections.abc import Sequence
from abc import ABC, abstractmethod
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class IReporter(ABC):
    '''
        Defines abstract class IReporter with method(s).
        Creates an interface for reporting message.

        It defines:

            :methods:
                | verbose - Reports verbose message.
                | success - Reports success message.
                | warning - Reports warning message.
                | error - Reports error message.
                | is_initialized - Checks if the reporter component is initialized.
                | __str__ - Returns the reporter as string representation.
    '''

    @abstractmethod
    def verbose(self, is_verbose: bool, message: Sequence[Any]) -> None:
        '''
            Reports verbose message.

            :param is_verbose: Enable/Disable verbose option.
            :type is_verbose: <bool>
            :param message: Sequence with message.
            :type message: <Sequence[Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def success(self, message: Sequence[Any]) -> None:
        '''
            Reports success message.

            :param message: Sequence with message.
            :type message: <Sequence[Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def warning(self, message: Sequence[Any]) -> None:
        '''
            Reports warning message.

            :param message: Sequence with message.
            :type message: <Sequence[Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def error(self, message: Sequence[Any]) -> None:
        '''
            Reports error message.

            :param message: Sequence with message.
            :type message: <Sequence[Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Returns whether the reporter component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the reporter as string representation.

            :return: The reporter as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
