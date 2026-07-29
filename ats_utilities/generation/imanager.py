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
    Defines abstract class IGeneratorManager with method(s).
    Provides an interface for template-based file generation from .tgz archives.
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
class IGeneratorManager[GeneratorTemplatesType, GeneratorDataType, ContextEnvironment](Protocol):
    '''
        Defines abstract class IGeneratorManager with method(s).
        Provides an interface for template-based file generation from .tgz archives.

        It defines:

            :methods:
                | get_context - Returns the context.
                | prepare_template_values - Prepares template values.
                | generate - Generates project modules/files from a .tgz archive.
                | is_initialized - Checks if the generator manager is initialized.
                | __str__ - Returns generator manager as string representation.
    '''

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: Context.
        '''
        ...

    def prepare_template_values(self, template_values: GeneratorTemplatesType) -> GeneratorTemplatesType:
        '''
            Prepares template values.

            :param template_values: Input replacement values.
            :return: The updated template values dictionary.
        '''
        ...

    def generate(self, data: GeneratorDataType) -> bool:
        '''
            Generates project modules/files from a .tgz archive.

            :param data: GeneratorManager data containing template generation parameters.
            :return: True if successfully, otherwise False.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if generator manager is initialized.

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns generator manager as string representation.

            :return: GeneratorManager manager as string representation.
        '''
        ...
