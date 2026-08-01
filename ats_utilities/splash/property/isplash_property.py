# -*- coding: UTF-8 -*-

'''
Module
    isplash_property.py
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
    Defines the ISplashProperty abstract class with method(s).
    Interface for checking splash screen property.
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
class ISplashProperty[PropertyType](Protocol):
    '''
        Defines the ISplashProperty abstract class with method(s).
        Interface for checking splash screen property.
        Note: Splash screen property comes from info configuration file as read only data.

        It defines:

            :methods:
                | settings - Property methods for setting and getting the splash keys.
                | is_settings_enabled - Checks if settings are enabled.
                | __str__ - Returns the splash keys as a string representation.
    '''

    @property
    def settings(self) -> PropertyType:
        '''
            Property method for getting the splash screen property.
            Note: Splash screen property comes from info configuration file as read only data.

            :return: The formatted splash screen property in PropertyType format (read only data).
        '''
        ...

    @settings.setter
    def settings(self, setup: PropertyType) -> None:
        '''
            Property method for setting the project splash screen property.
            Note: Splash screen property comes from info configuration file as read only data.

            :param setup: The project splash screen property in PropertyType format (read only data).
        '''
        ...

    def is_settings_enabled(self) -> bool:
        '''
            Checks if settings are enabled.

            :return: True if settings are enabled, False otherwise.
        '''
        ...

    def get_name(self) -> str | None:
        '''
            Returns application/tool/script name.

            :return: Application/tool/script name | None.
        '''
        ...

    def get_repository(self) -> str | None:
        '''
            Returns application/tool/script repository.

            :return: Application/tool/script repository | None.
        '''
        ...

    def get_organization(self) -> str | None:
        '''
            Returns application/tool/script organization.

            :return: Application/tool/script organization | None.
        '''
        ...

    def get_logo(self) -> str | None:
        '''
            Returns application/tool/script logo path.

            :return: Application/tool/script logo path | None.
        '''
        ...

    def get_use_github_infrastructure(self) -> bool:
        '''
            Returns True if application/tool/script uses github infrastructure.

            :return: True if application/tool/script uses github infrastructure, False otherwise.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the splash keys as a string representation.

            :return: The splash keys as a string representation.
        '''
        ...
