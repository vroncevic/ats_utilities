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
    Creates an interface for template-based file generation from .tgz archives.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.data import GeneratorData

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IGenerator(ABC):
    '''
        Defines abstract class IGenerator with method(s).
        Creates an interface for template-based file generation from .tgz archives.

        It defines:

            :methods:
                | get_context - Returns the context.
                | prepare_template_values - Prepares template values.
                | generate - Generates project modules/files from a .tgz archive.
                | is_initialized - Checks if the generator component is initialized.
                | __str__ - Returns the generator as string representation.
    '''

    @abstractmethod
    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :rtype: ContextBundle
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def prepare_template_values(self, template_values: Mapping[str, str]) -> dict[str, str]:
        '''
            Prepares template values.

            :param template_values: Input replacement values.
            :type template_values: Mapping[str, str]
            :return: The updated template values dictionary.
            :rtype: dict[str, str]
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def generate(self, data: GeneratorData) -> bool:
        '''
            Generates project modules/files from a .tgz archive.

            :param data: Generator data containing template generation parameters.
            :type data: GeneratorData
            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if generator component is initialized.

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the generator as string representation.

            :return: The generator as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
