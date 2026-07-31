# -*- coding: UTF-8 -*-

'''
Module
    factory.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 =of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Factory for creating generator bundle.
'''

from __future__ import annotations

from ats_utilities.generation.setup.bundle import GeneratorBundle
from ats_utilities.generation.setup.options import GeneratorOptions
from ats_utilities.generation.setup.opt_validator import GeneratorOptionsValidator
from ats_utilities.generation.setup.dependencies import GeneratorDependencies
from ats_utilities.generation.setup.keys import GeneratorKeys
from ats_utilities.generation.setup.registry import GeneratorRegistry
from ats_utilities.generation.scheme.engine import SchemeLoader
from ats_utilities.generation.tar.engine import TarProcessor
from ats_utilities.generation.template.engine import TemplateProcessor
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.generation.template.itemplate_processor import ITemplateProcessor
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class GeneratorFactory:
    '''
        Factory for creating generator bundle.

        It defines:

            :methods:
                | create_default_bundle - Creates a default generator bundle using configuration options.
    '''

    @classmethod
    def create_default_bundle(cls, options: GeneratorOptions) -> GeneratorBundle:
        '''
            Creates a default generator bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :return: Generator bundle.
            :exceptions:
                | ATSValueError: Generator options must be provided and have proper values.
                | ATSTypeError:  Generator options must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
        '''
        GeneratorOptionsValidator.validate(options)

        context_bundle: ContextBundle = options.get(GeneratorKeys.CONTEXT_BUNDLE)

        scheme_loader: ISchemeLoader = SchemeLoader(context_bundle=context_bundle)
        template_processor: ITemplateProcessor = TemplateProcessor(context_bundle=context_bundle)
        tar_processor: ITarProcessor = TarProcessor(
            context_bundle=context_bundle,
            template_processor=template_processor
        )

        return GeneratorRegistry.create_bundle(
            GeneratorDependencies(
                scheme_loader=scheme_loader,
                tar_processor=tar_processor,
                context_bundle=context_bundle
            )
        )
