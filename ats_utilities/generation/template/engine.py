# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class TemplateProcessor with method(s).
    Handles string rendering and template substitutions.
'''

from __future__ import annotations

from collections.abc import Mapping
from string import Template

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TemplateProcessor:
    '''
        Defines class TemplateProcessor with method(s).
        Handles string rendering and template substitutions.

        It defines:

            :attributes:
                | _initialized - The status of the template processor.
            :methods:
                | __init__ - Initializes the TemplateProcessor instance.
                | render - Decodes and renders template placeholders.
                | is_initialized - Checks if the template processor is initialized.
                | __str__ - Returns the template processor as a string representation.
    '''

    _initialized: bool
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes the TemplateProcessor instance.

            :param context_bundle: Context bundle for template processor | None.
            :exceptions:
                | ATSValueError: Context bundle must be provided and have proper values.
                | ATSTypeError:  Context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
        '''
        ContextValidator.validate(context_bundle)
        self._context = context_bundle
        self._initialized = True

    def render(self, raw_content: bytes, vals: Mapping[str, str]) -> str | bytes:
        '''
            Decodes and renders template placeholders.

            :param raw_content: The raw byte content of the file.
            :param vals: The string replacement values.
            :return: The rendered text content, or raw bytes if binary format.
            :exceptions: None.
        '''
        try:
            content: str = raw_content.decode('utf-8')
            template: Template = Template(content)

            return template.safe_substitute(vals)

        except UnicodeDecodeError:
            return raw_content

    def is_initialized(self) -> bool:
        '''
            Checks if template processor is initialized.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return self._initialized

    def __str__(self) -> str:
        '''
            Returns the template processor as a string representation.

            :return: The Template processor as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
