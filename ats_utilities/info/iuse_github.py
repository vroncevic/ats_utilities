# -*- coding: UTF-8 -*-

'''
Module
    iuse_github.py
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
    Defines abstract class IUseGitHub with method(s).
    Interface for the ATS use GitHub infrastructure mechanism.
'''

from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IUseGitHub(ABC):
    '''
        Defines abstract class IUseGitHub with method(s).
        Interface for the ATS use GitHub infrastructure mechanism.

        It defines:

            :attributes: None
            :methods:
                | use_github - Property methods for set/get operations.
                | not_none - Checks if ATS use GitHub infrastructure is not None.
                | __str__ - Returns the ATS use GitHub infrastructure as string representation.
    '''

    @property
    @abstractmethod
    def use_github(self) -> bool | None:
        '''
            Property method for getting ATS use GitHub infrastructure status.

            :return: The ATS use GitHub infrastructure status | None.
            :rtype: <bool | None>
            :exceptions: NotImplementedError..
        '''
        raise NotImplementedError("Method use_github() must be implemented.")

    @use_github.setter
    @abstractmethod
    def use_github(self, use_github: bool | None) -> None:
        '''
            Property method for setting ATS use GitHub infrastructure status.

            :param use_github: The ATS use GitHub infrastructure status | None.
            :type use_github: <bool | None>
            :exceptions: NotImplementedError..
        '''
        raise NotImplementedError("Method use_github() must be implemented.")

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if ATS use GitHub infrastructure status is not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: NotImplementedError..
        '''
        raise NotImplementedError("Method not_none() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS use GitHub infrastructure as string representation.

            :return: The ATS use GitHub infrastructure as string representation.
            :rtype: <str>
            :exceptions: NotImplementedError..
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
