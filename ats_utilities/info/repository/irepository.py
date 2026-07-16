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
    Interface for the repository mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IRepository(ABC):
    '''
        Defines abstract class IRepository with method(s).
        Interface for the repository mechanism.
        Note: Repository is only prepared when it is set by user (not None).

        It defines:

            :methods:
                | repository - Property methods for set/get operations.
                | not_none - Checks if repository is not None.
                | __str__ - Returns the repository as string representation.
    '''

    @property
    @abstractmethod
    def repository(self) -> str | None:
        '''
            Property method for getting repository.
            Note: Repository is only prepared when it is set by user (not None).

            :return: The repository in string format | None.
            :rtype: <str | None>
            :exceptions: None.
        '''
        pass

    @repository.setter
    @abstractmethod
    def repository(self, repository: str) -> None:
        '''
            Property method for setting repository.
            Note: Repository is only prepared when it is set by user (not None).

            :param repository: The repository in string format.
            :type repository: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if repository is not None.
            Note: Repository is only prepared when it is set by user (not None).

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the repository as string representation.

            :return: The repository as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
