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
    Defines abstract class IReporter with attribute(s) and method(s).
    Creates an interface for reporting message.
'''

from abc import ABC, abstractmethod
from typing import Any, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IReporter(ABC):
    '''
        Defines abstract class IReporter with attribute(s) and method(s).
        Creates an interface for reporting message.

        It defines:

            :attributes: None
            :methods:
                | error - Report error message (abstract).
                | success - Report success message (abstract).
                | verbose - Report verbose message (abstract).
                | warning - Report warning message (abstract).
                | __str__ - Returns the string representation of ATS reporter (abstract).
    '''

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
        raise NotImplementedError("Method verbose() must be implemented.")

    @abstractmethod
    def success(self, message: List[Any]) -> None:
        '''
            Report success message.

            :param message: List with message
            :type message: <List[Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method success() must be implemented.")

    @abstractmethod
    def warning(self, message: List[Any]) -> None:
        '''
            Report warning message.

            :param message: List with message
            :type message: <List[Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method warning() must be implemented.")

    @abstractmethod
    def error(self, message: List[Any]) -> None:
        '''
            Report error message.

            :param message: List with message
            :type message: <List[Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method error() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS reporter.

            :return: ATS reporter instance as string representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
