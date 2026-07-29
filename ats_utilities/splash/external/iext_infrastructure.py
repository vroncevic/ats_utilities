# -*- coding: UTF-8 -*-

'''
Module
    iext_infrastructure.py
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
    Defines abstract class IExtInfrastructure with method(s).
    Interface for processing hyperlinks for splash screen.
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
class IExtInfrastructure[PropertyType, InfoTextType, IssueTextType, AuthorTextType](Protocol):
    '''
        Defines abstract class IExtInfrastructure with method(s).
        Interface for processing hyperlinks for splash screen.
        Note: Splash screen infrastructure comes from info configuration file as read only data.

        It defines:

            :methods:
                | infrastructure_property - Property methods for set/get operations.
                | get_info_text - Pre-processes info text for splash screen.
                | get_issue_text - Pre-processes issue text for splash screen.
                | get_author_text - Pre-processes author text for splash screen.
                | __str__ - Returns external infrastructure as string representation.
    '''

    @property
    def infrastructure_property(self) -> PropertyType:
        '''
            Property method for getting infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Formatted infrastructure property in PropertyType format (read only data).
        '''
        ...

    @infrastructure_property.setter
    def infrastructure_property(self, setup: PropertyType) -> None:
        '''
            Property method for setting project infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :param setup: Project infrastructure property in PropertyType format (read only data).
        '''
        ...

    def get_info_text(self) -> InfoTextType:
        '''
            Pre-processes info text for splash screen.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Formatted info text in InfoTextType format (read only data).
        '''
        ...

    def get_issue_text(self) -> IssueTextType:
        '''
            Pre-processes issue text for splash screen.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Formatted issue text in IssueTextType format (read only data).
        '''
        ...

    def get_author_text(self) -> AuthorTextType:
        '''
            Pre-processes author text for splash screen.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Formatted author text in AuthorTextType format (read only data).
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns external infrastructure as string representation.

            :return: External infrastructure as string representation.
        '''
        ...
