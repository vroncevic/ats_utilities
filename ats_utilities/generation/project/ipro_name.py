# -*- coding: UTF-8 -*-

'''
Module
    ipro_name.py
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
    Defines the IProName abstract class with method(s).
    Interface for the project name mechanism.
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
class IProName(Protocol):
    '''
        Defines the IProName abstract class with method(s).
        Interface for the project name mechanism.

        It defines:

            :methods:
                | pro_name - Property methods for setting and getting the respective property value.
                | not_none - Checks if the project name is not None.
                | __str__ - Returns the ATS project name as a string representation.
    '''

    @property
    def pro_name(self) -> str | None:
        '''
            Property method for getting the project name.

            :return: Formatted project name in string format | None.
        '''
        ...

    @pro_name.setter
    def pro_name(self, name: str) -> None:
        '''
            Property method for setting the project name.

            :param name: Project name in string format | None.
        '''
        ...

    def not_none(self) -> bool:
        '''
            Checks if the project name is not None.

            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the ATS project name as a string representation.

            :return: The ATS project name as a string representation.
        '''
        ...
