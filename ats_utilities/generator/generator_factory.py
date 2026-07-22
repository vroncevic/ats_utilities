# -*- coding: UTF-8 -*-

'''
Module
    generator_factory.py
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
    Factory for creating GeneratorBundle components.
'''

from __future__ import annotations

from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.template.engine import TemplateProcessor
from ats_utilities.generator.scheme.engine import SchemeLoader
from ats_utilities.generator.tar.engine import TarProcessor
from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorFactory:
    '''
        Factory for creating GeneratorBundle components.
    '''

    @classmethod
    def create_default_generator_bundle(cls, context_bundle: ContextBundle) -> GeneratorBundle:
        '''
            Creates a default GeneratorBundle with pre-configured components.

            :param context_bundle: Context bundle for generator.
            :type context_bundle: <ContextBundle>
            :return: Default GeneratorBundle instance.
            :rtype: <GeneratorBundle>
            :exceptions:
                | ATSValueError: Context bundle must not be provided.
                | ATSTypeError: Context bundle must be of type ContextBundle.
        '''
        template_processor: TemplateProcessor = TemplateProcessor(context_bundle=context_bundle)
        scheme_loader: SchemeLoader = SchemeLoader(context_bundle=context_bundle)
        tar_processor: TarProcessor = TarProcessor(context_bundle=context_bundle, template_processor=template_processor)

        return GeneratorBundle(
            template_processor=template_processor,
            scheme_loader=scheme_loader,
            tar_processor=tar_processor,
            context_bundle=context_bundle
        )
