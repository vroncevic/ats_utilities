# -*- coding: UTF-8 -*-

'''
Module
    iorganization.py
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
    Defines abstract class IOrganization with method(s).
    Interface for the organization mechanism.
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
class IOrganization[OrganizationType](Protocol):
    '''
        Defines abstract class IOrganization with method(s).
        Interface for the organization mechanism.
        Note: Organization is only prepared when it is set by user (not None).

        It defines:

            :methods:
                | organization - Property methods for set/get operations.
                | not_none - Checks if organization is not None.
                | __str__ - Returns the organization as string representation.
    '''

    @property
    def organization(self) -> OrganizationType | None:
        '''
            Property method for getting organization.
            Note: Organization is only prepared when it is set by user (not None).

            :return: The organization in OrganizationType format | None.
        '''
        ...

    @organization.setter
    def organization(self, organization: OrganizationType) -> None:
        '''
            Property method for setting organization.
            Note: Organization is only prepared when it is set by user (not None).

            :param organization: The organization in OrganizationType format.
        '''
        ...

    def not_none(self) -> bool:
        '''
            Checks if organization is not None.
            Note: Organization is only prepared when it is set by user (not None).

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the organization as string representation.

            :return: The organization as string representation.
        '''
        ...
