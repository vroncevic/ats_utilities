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
    Generator dependencies.
'''

from __future__ import annotations

from typing import TypedDict

from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class GeneratorDependencies(TypedDict):
    '''
        Generator dependencies.

        It defines:

            :attributes:
                | scheme_loader: Loader/resolver for scheme configuration.
                | tar_processor: Processor for archive extraction.
                | context_bundle: Context bundle for generator.
    '''

    scheme_loader: ISchemeLoader
    tar_processor: ITarProcessor
    context_bundle: ContextBundle
