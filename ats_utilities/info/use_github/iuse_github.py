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
    Interface for the use GitHub infrastructure mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IUseGitHub(ABC):
    '''
        Defines abstract class IUseGitHub with method(s).
        Interface for the use GitHub infrastructure mechanism.
        Note: Use GitHub is only prepared when it is set by user (not None).

        It defines:

            :methods:
                | use_github - Property methods for set/get operations.
                | not_none - Checks if use GitHub infrastructure is not None.
                | __str__ - Returns the use GitHub infrastructure as string representation.
    '''

    @property
    @abstractmethod
    def use_github(self) -> bool:
        '''
            Property method for getting use GitHub infrastructure status.
            Note: Use GitHub is only prepared when it is set by user (not None).

            :return: The use GitHub infrastructure status.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @use_github.setter
    @abstractmethod
    def use_github(self, use_github: bool) -> None:
        '''
            Property method for setting use GitHub infrastructure status.
            Note: Use GitHub is only prepared when it is set by user (not None).

            :param use_github: The use GitHub infrastructure status.
            :type use_github: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if use GitHub infrastructure status is not None.
            Note: Use GitHub is only prepared when it is set by user (not None).

            :return: True (not None) | False (None).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the use GitHub infrastructure as string representation.

            :return: The use GitHub infrastructure as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
