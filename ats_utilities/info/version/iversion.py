# -*- coding: UTF-8 -*-

'''
Module
    iversion.py
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
    Defines abstract class IVersion with method(s).
    Interface for the version mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IVersion(ABC):
    '''
        Defines abstract class IVersion with method(s).
        Interface for the version mechanism.
        Note: Version is only prepared when it is set by user (not None).

        It defines:

            :methods:
                | version - Property methods for set/get operations.
                | not_none - Checks if version is not None.
                | __str__ - Returns the version as string representation.
    '''

    @property
    @abstractmethod
    def version(self) -> str | None:
        '''
            Property method for getting version.
            Note: Version is only prepared when it is set by user (not None).

            :return: The version in string format | None.
            :rtype: str | None
            :exceptions: None.
        '''
        pass

    @version.setter
    @abstractmethod
    def version(self, version: str) -> None:
        '''
            Property method for setting version.
            Note: Version is only prepared when it is set by user (not None).

            :param version: The version in string format.
            :type version: str
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if version is not None.
            Note: Version is only prepared when it is set by user (not None).

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the version as string representation.

            :return: The version as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
