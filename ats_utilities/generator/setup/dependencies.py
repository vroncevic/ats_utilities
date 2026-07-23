# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    Generator dependencies and options for generator bundle creation.
'''

from __future__ import annotations

from typing import TypedDict

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorDependencies(TypedDict):
    '''
        Generator dependencies for generator bundle creation.

        It defines:

            :attributes:
                | scheme_loader: Loader/resolver for scheme configuration.
                | tar_processor: Processor for archive extraction and template rendering.
                | template_processor: Processor for template rendering.
                | context_bundle: Context bundle for generator.
    '''
    scheme_loader: ISchemeLoader
    tar_processor: ITarProcessor
    template_processor: ITemplateProcessor
    context_bundle: ContextBundle


class GeneratorOptions(TypedDict):
    '''
        Generator options for generator bundle creation.

        It defines:

            :attributes:
                | context_bundle: Context bundle for generator.
    '''
    context_bundle: ContextBundle
