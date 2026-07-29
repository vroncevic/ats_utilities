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
    Defines abstract class ISplashProperty with method(s).
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
        Defines abstract class ISplashProperty with method(s).
        Interface for checking splash screen property.
        Note: Splash screen property comes from info configuration file as read only data.

        It defines:

            :methods:
                | splash_keys - Property methods for set/get splash keys.
                | validates - Validates splash keys.
                | __str__ - Returns the splash keys as string representation.
    '''

    @property
    def splash_keys(self) -> PropertyType:
        '''
            Property method for getting splash keys.
            Note: Splash screen property comes from info configuration file as read only data.

            :return: Formatted splash screen property in PropertyType format (read only data).
        '''
        ...

    @splash_keys.setter
    def splash_keys(self, setup: PropertyType) -> None:
        '''
            Property method for setting project splash keys.
            Note: Splash screen property comes from info configuration file as read only data.

            :param setup: Project splash keys in PropertyType format (read only data).
        '''
        ...

    def validates(self) -> bool:
        '''
            Validates splash keys.
            Note: Splash screen property comes from info configuration file as read only data.

            :return: True (success) else False (fail).
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the splash keys as string representation.

            :return: The splash keys as string representation.
        '''
        ...
