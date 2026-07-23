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
from typing import override

from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TemplateProcessor(ITemplateProcessor):
    '''
        Defines class TemplateProcessor with method(s).
        Handles string rendering and template substitutions.

        It defines:

            :attributes:
                | _initialized - Status of the template processor.
            :methods:
                | __init__ - Initializes TemplateProcessor constructor.
                | render - Decodes and renders template placeholders.
                | is_initialized - Checks if the processor is initialized.
                | __str__ - Returns the processor as string representation.
    '''

    _initialized: bool
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes TemplateProcessor constructor.

            :param context_bundle: Context bundle for template processor | None.
            :type context_bundle: ContextBundle 
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        self._context = context_bundle
        self._initialized = True

    @override
    def render(self, raw_content: bytes, vals: Mapping[str, str]) -> str | bytes:
        '''
            Decodes and renders template placeholders.

            :param raw_content: The raw byte content of the file.
            :type raw_content: <bytes>
            :param vals: String replacement values.
            :type vals: Mapping[str, str]
            :return: Rendered text content, or raw bytes if binary format.
            :rtype: <str | bytes>
            :exceptions: None.
        '''
        try:
            content: str = raw_content.decode('utf-8')
            template: Template = Template(content)

            return template.safe_substitute(vals)

        except UnicodeDecodeError:
            return raw_content

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if template processor component is initialized.

            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        return self._initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the TemplateProcessor as string representation.

            :return: The TemplateProcessor as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
