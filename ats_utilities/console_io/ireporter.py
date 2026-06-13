# -*- coding: utf-8 -*-

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
    Defines abstract class IATSReporter with attribute(s) and method(s).
    Creates an interface for reporting message.
'''

from abc import ABC, abstractmethod
from typing import Any, ClassVar, List
from ats_utilities.checker.ichecker import ErrorChecker

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IATSReporter(ABC):
    '''
        Defines abstract class IATSReporter with attribute(s) and method(s).
        Creates an interface for reporting message.

        It defines:

            :attributes:
                | ERRORS - Marks error types.
            :methods:
                | error - Report error message (abstract).
                | success - Report success message (abstract).
                | verbose - Report verbose message (abstract).
                | warning - Report warning message (abstract).
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    @abstractmethod
    def verbose(self, is_verbose: bool, message: List[Any]) -> None:
        '''
            Report verbose message.

            :param is_verbose: Enable/Disable verbose option
            :type is_verbose: <bool>
            :param message: List with message
            :type message: <List[Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement verbose method")

    @abstractmethod
    def success(self, message: List[Any]) -> None:
        '''
            Report success message.

            :param message: List with message
            :type message: <List[Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement success method")

    @abstractmethod
    def warning(self, message: List[Any]) -> None:
        '''
            Report warning message.

            :param message: List with message
            :type message: <List[Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement warning method")

    @abstractmethod
    def error(self, message: List[Any]) -> None:
        '''
            Report error message.

            :param message: List with message
            :type message: <List[Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement error method")
