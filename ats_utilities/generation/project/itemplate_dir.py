# -*- coding: UTF-8 -*-

'''
Module
    itemplate_dir.py
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
    Defines the ITemplateDir abstract class with method(s).
    Interface for the project template directory mechanism.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class ITemplateDir(Protocol):
    '''
        Defines the ITemplateDir abstract class with method(s).
        Interface for the project template directory mechanism.

        It defines:

            :methods:
                | template_dir - Property methods for setting and getting the respective property value.
                | not_none - Checks if the project template directory is not None.
                | __str__ - Returns the ATS project template directory as a string representation.
    '''

    @property
    def template_dir(self) -> str | None:
        '''
            Property method for getting the template dir.

            :return: Formatted template dir in string format | None.
        '''
        ...

    @template_dir.setter
    def template_dir(self, dir_path: str) -> None:
        '''
            Property method for setting the project template dir.

            :param dir_path: Project template dir path in string format | None.
        '''
        ...

    def not_none(self) -> bool:
        '''
            Checks if the project template directory is not None.

            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the ATS project template directory as a string representation.

            :return: The ATS project template directory as a string representation.
        '''
        ...
