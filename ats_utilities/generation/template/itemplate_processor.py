# -*- coding: UTF-8 -*-

'''
Module
    itemplate_processor.py
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
    Defines the ITemplateProcessor abstract class with method(s).
    Interface for rendering template placeholders.
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
class ITemplateProcessor(Protocol):
    '''
        Defines the ITemplateProcessor abstract class with method(s).
        Interface for rendering template placeholders.

        It defines:

            :methods:
                | render - Decodes and renders template placeholders.
                | is_initialized - Checks if template processor is initialized.
                | __str__ - Returns the template processor as a string representation.
    '''

    def render(self, raw_content: bytes, vals: dict[str, str]) -> str | bytes:
        '''
            Decodes and renders template placeholders.

            :param raw_content: The raw byte content of the file.
            :param vals: The string replacement values.
            :return: The rendered text content string, or raw bytes if binary format.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if template processor is initialized.

            :return: True if successful, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the template processor as a string representation.

            :return: The Template processor as a string representation.
        '''
        ...
