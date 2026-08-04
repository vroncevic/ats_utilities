# -*- coding: UTF-8 -*-

'''
Module
    imanager.py
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
    Defines the ISplashManager abstract class with method(s).
    Provides an interface for splash screen manager.
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
class ISplashManager[ConfigType, ContextEnvironment, PositionData](Protocol):
    '''
        Defines the ISplashManager abstract class with method(s).
        Provides an interface for splash screen manager.

        It defines:

            :methods:
                | get_bundle - Gets current splash manager bundle.
                | update_bundle - Updates splash manager bundle.
                | get_context - Returns context environment.
                | show - Shows splash screen.
                | center - Centers console line and places text.
                | is_initialized - Checks if splash screen manager is initialized.
                | __str__ - Returns the splash screen manager as a string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets current splash manager bundle.

            :return: The splash manager bundle.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates splash manager bundle.

            :param bundle: The splash manager bundle.
        '''
        ...

    def get_context(self) -> ContextEnvironment:
        '''
            Returns context environment.

            :return: The context environment.
        '''
        ...

    def show(self) -> None:
        '''
            Shows splash screen.
        '''
        ...

    def center(self, position: PositionData, text: str) -> None:
        '''
            Centers console line and places text.

            :param position: The position data for console output.
            :param text: The text to be centered.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if splash screen manager is initialized.

            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the splash manager as a string representation.

            :return: The Splash manager as a string representation.
        '''
        ...
