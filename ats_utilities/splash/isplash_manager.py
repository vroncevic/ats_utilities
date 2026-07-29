# -*- coding: UTF-8 -*-

'''
Module
    isplash_manager.py
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
    Defines abstract class ISplashManager with method(s).
    Provides an interface for splash screen manager.
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
class ISplashManager[ConfigType, ContextEnvironment, PositionData](Protocol):
    '''
        Defines abstract class ISplashManager with method(s).
        Provides an interface for splash screen manager.

        It defines:

            :methods:
                | get_bundle - Gets current splash screen configuration bundle.
                | update_bundle - Updates splash screen configuration bundle.
                | get_context - Returns the context environment.
                | center - Centers console line and places text.
                | is_initialized - Checks if splash screen manager is initialized.
                | __str__ - Returns the splash screen manager as string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets current splash screen configuration bundle.

            :return: Splash screen configuration bundle.
            :exceptions: None.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates splash screen configuration bundle.

            :param bundle: Splash screen configuration bundle.
            :exceptions: None.
        '''
        ...

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context environment.

            :return: Context environment.
        '''
        ...

    def center(self, position: PositionData, text: str) -> None:
        '''
            Centers console line and places text.

            :param position: Position data for console output.
            :param text: Text to be centered.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if splash screen manager is initialized.

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the splash screen manager as string representation.

            :return: Splash screen manager as string representation.
        '''
        ...
