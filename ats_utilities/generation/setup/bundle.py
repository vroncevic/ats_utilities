# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Encapsulates generator runtime components for simplification of generator bundle.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import instance_to_dict

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class GeneratorBundle:
    '''
        Encapsulates generator runtime components for simplification of generator bundle.

        It defines:

            :attributes:
                | scheme_loader - The loader/resolver for the scheme configuration.
                | tar_processor - The processor for the archive extraction and template rendering.
                | context_bundle - The context bundle for generator.
            :methods:
                | to_dict - Converts generator bundle to a dictionary.
    '''

    scheme_loader: ISchemeLoader
    tar_processor: ITarProcessor
    context_bundle: ContextBundle

    def to_dict(self) -> dict[str, object]:
        '''
            Converts generator bundle to a dictionary.

            :return: The dictionary representation of the generator bundle.
            :exceptions:
                | ATSValueError: Instance must be provided.
                | ATSValueError: Instance must be a dataclass.
        '''
        return instance_to_dict(self)
