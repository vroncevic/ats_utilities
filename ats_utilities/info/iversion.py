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
    Interface for the ATS version mechanism.
'''

from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IVersion(ABC):
    '''
        Defines abstract class IVersion with method(s).
        Interface for the ATS version mechanism.

        It defines:

            :attributes: None
            :methods:
                | version - Property methods for set/get operations.
                | not_none - Checks if ATS version is not None.
                | __str__ - Returns the ATS version as string representation.
    '''

    @property
    @abstractmethod
    def version(self) -> str | None:
        '''
            Property method for getting ATS version.

            :return: The ATS version in string format | None
            :rtype: <str | None>
            :exceptions: None.
        '''
        pass

    @version.setter
    @abstractmethod
    def version(self, version: str | None) -> None:
        '''
            Property method for setting ATS version.

            :param version: The ATS version in string format | None
            :type version: <str | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if ATS version is not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS version as string representation.

            :return: The ATS version as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
