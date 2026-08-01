# -*- coding: UTF-8 -*-

'''
Module
    ibase.py
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
    Defines the IBase abstract class with method(s).
    An interface for the ATS base setup.
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
class IBase[ConfigType, ContextEnvironment](Protocol):
    '''
        Defines the IBase abstract class with method(s).
        An interface for the ATS base setup.

        It defines:

            :methods:
                | get_bundle - Gets the current configuration bundle.
                | update_bundle - Updates the configuration bundle.
                | get_context - Returns the context.
                | is_initialized - Checks if the App/Tool/Script base engine is initialized.
                | process - Processes and runs the App/Tool/Script (Abstract).
                | __str__ - Returns the App/Tool/Script base as string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets the current configuration bundle.

            :return: The configuration bundle.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates the configuration bundle.

            :param bundle: The configuration bundle.
            :return: True if the configuration bundle is updated successfully.
        '''
        ...

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: The context.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if the App/Tool/Script base engine is initialized.

            :return: True if successful, otherwise False.
        '''
        ...

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs the App/Tool/Script.

            :param verbose: The Enable/Disable the verbose option (default: False).
            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the App/Tool/Script base as string representation.

            :return: The App/Tool/Script base as a string representation.
        '''
        ...
