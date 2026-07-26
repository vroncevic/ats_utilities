# -*- coding: UTF-8 -*-

'''
Module
    igenerator.py
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
    Defines abstract class IGenerator with method(s).
    Provides an interface for template-based file generation from .tgz archives.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from ats_utilities.generator.data import GeneratorData

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IGenerator[ContextEnvironment](Protocol):
    '''
        Defines abstract class IGenerator with method(s).
        Provides an interface for template-based file generation from .tgz archives.

        It defines:

            :methods:
                | get_context - Returns the context.
                | prepare_template_values - Prepares template values.
                | generate - Generates project modules/files from a .tgz archive.
                | is_initialized - Checks if the generator component is initialized.
                | __str__ - Returns the generator as string representation.
    '''

    def get_context(self) -> ContextEnvironment:
        '''
            Returns the context.

            :return: Context.
            :exceptions: None.
        '''
        ...

    def prepare_template_values(self, template_values: Mapping[str, str]) -> dict[str, str]:
        '''
            Prepares template values.

            :param template_values: Input replacement values.
            :return: The updated template values dictionary.
            :exceptions: None.
        '''
        ...

    def generate(self, data: GeneratorData) -> bool:
        '''
            Generates project modules/files from a .tgz archive.

            :param data: Generator data containing template generation parameters.
            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if generator component is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the generator as string representation.

            :return: The generator as string representation.
            :exceptions: None.
        '''
        ...
