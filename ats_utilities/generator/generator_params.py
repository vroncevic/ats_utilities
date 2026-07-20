# -*- coding: UTF-8 -*-

'''
Module
    generator_params.py
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
    TypedDict for GeneratorRegistry parameters.
'''

from __future__ import annotations

from typing import TypedDict, NotRequired

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorParams(TypedDict):
    '''TypedDict defining parameter types for GeneratorRegistry.'''
    context_bundle: ContextBundle
    template_processor: NotRequired[ITemplateProcessor]
    scheme_loader: NotRequired[ISchemeLoader]
    tar_processor: NotRequired[ITarProcessor]

