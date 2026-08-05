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
    Defines the IRepository abstract class with method(s).
    Interface for the repository mechanism.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IRepository[RepositoryType](Protocol):
    '''
        Defines the IRepository abstract class with method(s).
        Interface for the repository mechanism.
        Note: The repository is only prepared when it is set by the user (not None).

        It defines:

            :methods:
                | repository - Property methods for setting and getting the respective property value.
                | not_none - Checks if the repository is not None.
                | __str__ - Returns the repository as a string representation.
    '''

    @property
    def repository(self) -> RepositoryType | None:
        '''
            Property method for getting the repository.
            Note: The repository is only prepared when it is set by the user (not None).

            :return: The repository in RepositoryType format | None.
        '''
        ...

    @repository.setter
    def repository(self, repository: RepositoryType) -> None:
        '''
            Property method for setting the repository.
            Note: The repository is only prepared when it is set by the user (not None).

            :param repository: The repository in RepositoryType format.
        '''
        ...

    def not_none(self) -> bool:
        '''
            Checks if the repository is not None.
            Note: The repository is only prepared when it is set by the user (not None).

            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the repository as a string representation.

            :return: The repository as a string representation.
        '''
        ...
