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
    Factory for creating generator bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.generator.setup.bundle import GeneratorBundle
from ats_utilities.generator.setup.dependencies import (
    GeneratorOptions, GeneratorDependencies
)
from ats_utilities.generator.setup.registry import GeneratorRegistry
from ats_utilities.generator.scheme.engine import SchemeLoader
from ats_utilities.generator.tar.engine import TarProcessor
from ats_utilities.generator.template.engine import TemplateProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorFactory(IFactory[GeneratorBundle, GeneratorOptions]):
    '''
        Factory for creating generator bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default generator bundle using configuration options.
                | create_default_generator_bundle - Creates a default generator bundle using configuration options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: GeneratorOptions) -> GeneratorBundle:
        '''
            Creates a default generator bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :type options: GeneratorOptions
            :return: Generator bundle instance.
            :rtype: GeneratorBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Scheme loader must be provided.
                | ATSValueError: Tar processor must be provided.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Bundle must be an instance of GeneratorBundle.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Scheme loader must be an ISchemeLoader instance.
                | ATSTypeError: Tar processor must be an ITarProcessor instance.
                | ATSTypeError: Template processor must be an ITemplateProcessor instance.
        '''
        ctx: str = r'generator_factory::create_default_bundle(...)'
        not_none(options, ctx, r'options must be provided')
        istype(options, dict, ctx, r'options must be a dictionary')

        context_bundle: ContextBundle = options.get('context_bundle')
        not_none(context_bundle, ctx, r'context_bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context_bundle must be ContextBundle instance')

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
                template_processor=template_processor,
                context_bundle=context_bundle
            )
        )

    @classmethod
    def create_default_generator_bundle(cls, context_bundle: ContextBundle) -> GeneratorBundle:
        '''
            Creates a default generator bundle.
            Kept for backward compatibility.

            :param context_bundle: Context bundle for generator.
            :type context_bundle: ContextBundle
            :return: Generator bundle instance.
            :rtype: GeneratorBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Scheme loader must be provided.
                | ATSValueError: Tar processor must be provided.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Bundle must be an instance of GeneratorBundle.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Scheme loader must be an ISchemeLoader instance.
                | ATSTypeError: Tar processor must be an ITarProcessor instance.
                | ATSTypeError: Template processor must be an ITemplateProcessor instance.
        '''
        return cls.create_default_bundle(
            GeneratorOptions(context_bundle=context_bundle)
        )
