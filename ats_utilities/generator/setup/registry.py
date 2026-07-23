# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core runtime components for simplification of generator bundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.generator.setup.bundle import GeneratorBundle
from ats_utilities.generator.setup.dependencies import GeneratorDependencies
from ats_utilities.generator.setup.validator import GeneratorValidator
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorRegistry(IRegistry[GeneratorBundle, GeneratorDependencies]):
    '''
        Encapsulates core runtime components for simplification of generator bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a generator bundle instance.
                | create_generator_bundle - Orchestrates dependency injection and creates a generator bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: GeneratorDependencies) -> GeneratorBundle:
        '''
            Orchestrates dependency injection and creates a generator bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :type dependencies: GeneratorDependencies
            :return: Generator bundle instance.
            :rtype: GeneratorBundle
            :exceptions:
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
        bundle = GeneratorBundle(
            scheme_loader=dependencies.get('scheme_loader'),
            tar_processor=dependencies.get('tar_processor'),
            template_processor=dependencies.get('template_processor'),
            context_bundle=dependencies.get('context_bundle')
        )

        GeneratorValidator.validate(bundle)

        return bundle

    @classmethod
    def create_generator_bundle(
        cls,
        scheme_loader: ISchemeLoader,
        tar_processor: ITarProcessor,
        template_processor: ITemplateProcessor,
        context_bundle: ContextBundle
    ) -> GeneratorBundle:
        '''
            Orchestrates dependency injection and creates a generator bundle instance.
            Kept for backward compatibility.

            :param scheme_loader: Loader/resolver for scheme configuration.
            :type scheme_loader: ISchemeLoader
            :param tar_processor: Processor for archive extraction and template rendering.
            :type tar_processor: ITarProcessor
            :param template_processor: Processor for template rendering.
            :type template_processor: ITemplateProcessor
            :param context_bundle: Context bundle for generator.
            :type context_bundle: ContextBundle
            :return: Generator bundle instance.
            :rtype: GeneratorBundle
            :exceptions:
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
        return cls.create_bundle(
            GeneratorDependencies(
                scheme_loader=scheme_loader,
                tar_processor=tar_processor,
                template_processor=template_processor,
                context_bundle=context_bundle
            )
        )
