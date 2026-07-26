# -*- coding: UTF-8 -*-

'''
Module
    ilicence.py
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
    Defines abstract class ILicence with method(s).
    Interface for the licence mechanism.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class ILicence(Protocol):
    '''
        Defines abstract class ILicence with method(s).
        Interface for the licence mechanism.
        Note: Info licence is only prepared when it is set by user (not None).

        It defines:

            :methods:
                | licence - Property methods for set/get operations.
                | not_none - Checks if licence is not None.
                | __str__ - Returns the licence as string representation.
    '''

    @property
    def licence(self) -> str | None:
        '''
            Property method for getting licence.
            Note: Info licence is only prepared when it is set by user (not None).

            :return: The licence in string format | None.
        '''
        ...

    @licence.setter
    def licence(self, licence: str) -> None:
        '''
            Property method for setting licence.
            Note: Info licence is only prepared when it is set by user (not None).

            :param licence: The licence in string format.
        '''
        ...

    def not_none(self) -> bool:
        '''
            Checks if licence is not None.
            Note: Info licence is only prepared when it is set by user (not None).

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the licence as string representation.

            :return: The licence as string representation.
        '''
        ...
