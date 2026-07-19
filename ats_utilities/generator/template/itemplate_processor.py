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
    Defines abstract class ITemplateProcessor with method(s).
    Interface for rendering template placeholders.
'''

from __future__ import annotations

from ats_utilities.context.icontext_support import IContextSupport

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ITemplateProcessor(IContextSupport, ABC):
    '''
        Defines abstract class ITemplateProcessor with method(s).
        Interface for rendering template placeholders.

        It defines:

            :methods:
                | render - Decodes and renders template placeholders.
                | is_initialized - Checks if component is initialized.
                | __str__ - Returns the component as string representation.
    '''

    @abstractmethod
    def render(self, raw_content: bytes, vals: dict[str, str]) -> str | bytes:
        '''
            Decodes and renders template placeholders.

            :param raw_content: The raw byte content of the file.
            :type raw_content: <bytes>
            :param vals: String replacement values.
            :type vals: <dict[str, str]>
            :return: Rendered text content string, or raw bytes if binary format.
            :rtype: <str | bytes>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if component is initialized.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the component as string representation.

            :return: String representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
