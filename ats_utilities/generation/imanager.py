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
    Defines the IGeneratorManager abstract class with method(s).
    Provides an interface for template-based file generation from .tgz archives.
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
class IGeneratorManager[ConfigType, GeneratorTemplatesType, GeneratorDataType, ContextEnvironment](Protocol):
    '''
        Defines the IGeneratorManager abstract class with method(s).
        Provides an interface for template-based file generation from .tgz archives.

        It defines:

            :methods:
                | get_bundle - Gets current generator configuration bundle.
                | update_bundle - Updates generator configuration bundle.
                | get_context - Returns the context.
                | prepare_template_values - Prepares template values.
                | generate - Generates project modules/files from a .tgz archive.
                | is_initialized - Checks if the generator manager is initialized.
                | __str__ - Returns the generator manager as a string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets current generator configuration bundle.

            :return: The generator configuration bundle.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates generator configuration bundle.

            :param bundle: The generator configuration bundle.
            :return: True if generator configuration bundle is updated successfully.
        '''
        ...

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: The context.
        '''
        ...

    def prepare_template_values(self, template_values: GeneratorTemplatesType) -> GeneratorTemplatesType:
        '''
            Prepares template values.

            :param template_values: The input replacement values.
            :return: The updated template values dictionary.
        '''
        ...

    def generate(self, data: GeneratorDataType) -> bool:
        '''
            Generates project modules/files from a .tgz archive.

            :param data: The GeneratorManager data containing template generation parameters.
            :return: True if successful, otherwise False.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if generator manager is initialized.

            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the generator manager as a string representation.

            :return: The GeneratorManager manager as a string representation.
        '''
        ...
