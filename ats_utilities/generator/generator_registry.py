# -*- coding: UTF-8 -*-

'''
Module
    generator_registry.py
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
    Encapsulates core runtime components for simplification of GeneratorBundle creation.
'''

from __future__ import annotations

from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.generator_params import GeneratorParams
from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorRegistry(IRegistry[GeneratorBundle, GeneratorParams]):
    '''
        Encapsulates core runtime components for simplification of GeneratorBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a GeneratorBundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: GeneratorParams) -> GeneratorBundle:
        '''
            Creates a GeneratorBundle instance.

            :param params: Registry-specific orchestration parameters.
            :type params: GeneratorParams
            :return: GeneratorBundle instance.
            :rtype: <ContextBundle>
        '''
        return GeneratorBundle(
            template_processor=params.get('template_processor'),
            scheme_loader=params.get('scheme_loader'),
            tar_processor=params.get('tar_processor'),
            context_bundle=params.get('context_bundle')
        )
