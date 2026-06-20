# -*- coding: UTF-8 -*-

'''
Module
    irepository.py
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
    Defines abstract class IRepository with method(s).
    Interface for the ATS repository mechanism.
'''

from abc import ABC, abstractmethod
from typing import List, Optional

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IRepository(ABC):
    '''
        Defines abstract class IRepository with method(s).
        Interface for the ATS repository mechanism.

        It defines:

            :attributes: None
            :methods:
                | repository - Property methods for set/get operations.
                | not_none - Checks if ATS repository is not None.
                | __str__ - Returns the ATS repository as string representation.
    '''

    @property
    @abstractmethod
    def repository(self) -> Optional[str]:
        '''
            Property method for getting ATS repository.

            :return: The ATS repository in string format | None.
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method repository() must be implemented.")

    @repository.setter
    @abstractmethod
    def repository(self, repository: Optional[str]) -> None:
        '''
            Property method for setting ATS repository.

            :param repository: The ATS repository in string format | None.
            :type repository: <Optional[str]>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method repository() must be implemented.")

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if ATS repository is not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method not_none() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS repository as string representation.

            :return: The ATS repository as string representation.
            :rtype: <str>
            :exceptions: NotImplementedError.
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
