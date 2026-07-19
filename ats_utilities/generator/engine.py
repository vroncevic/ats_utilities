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
    Defines class Generator with attribute(s) and method(s).
    Template-based file generation from .tgz archives.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.gen_params_bundle import GenParamsBundle
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.validation.check_value import not_satisfied, not_empty, not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Generator(ContextSupport, IGenerator):
    '''
        Defines class Generator with attribute(s) and method(s).
        Template-based file generation from .tgz archives.

        It defines:

            :attributes:
                | _shared_context - Bundle of shared context.
                | _scheme_loader - Loader/resolver for scheme configuration.
                | _tar_processor - Processor for archive extraction and template rendering.
                | _is_initialized - Flag indicating if the generator is initialized.
            :methods:
                | __init__ - Initializes Generator constructor.
                | get_shared_context - Returns the shared context.
                | generate - Generates project modules/files from a .tgz archive.
                | is_initialized - Checks if the generator component is initialized.
                | __str__ - Returns the string representation of Generator.
    '''

    _shared_context: ContextBundle
    _scheme_loader: ISchemeLoader
    _tar_processor: ITarProcessor
    _is_initialized: bool

    def __init__(self, component_bundle: GeneratorBundle) -> None:
        '''
            Initializes Generator constructor.

            :param component_bundle: Generator component bundle for generator.
            :type component_bundle: <GeneratorBundle>
            :exceptions:
                | ATSValueError: Component bundle must be provided.
                | ATSValueError: Component bundle must not be provided.
                | ATSValueError: Context bundle must not be provided.
                | ATSValueError: Scheme loader must be provided.
                | ATSValueError: Tar processor must be provided.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Scheme loader must be an ISchemeLoader instance.
                | ATSTypeError: Tar processor must be an ITarProcessor instance.
                | ATSTypeError: Template processor must be an ITemplateProcessor instance.
                | ATSTypeError: Component bundle must be of type GeneratorBundle.
                | ATSTypeError: Context bundle must be of type ContextBundle.
        '''
        not_none(
            component_bundle,
            r'generator::init(...)',
            r'component bundle must not be provided'
        )
        istype(
            component_bundle, GeneratorBundle,
            r'generator::init(...)',
            r'component bundle must be of type GeneratorBundle'
        )
        self._shared_context = component_bundle.context_bundle
        ContextSupport.__init__(self, self._shared_context)
        self._scheme_loader = component_bundle.scheme_loader
        self._tar_processor = component_bundle.tar_processor
        self._is_initialized = True

    @override
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        return self._shared_context

    @override
    def prepare_template_values(self, template_values: Mapping[str, str]) -> dict[str, str]:
        '''
            Validates and computes name case variations from template values.

            :param template_values: Input replacement values.
            :type template_values: <Mapping[str, str]>
            :return: The updated template values dictionary.
            :rtype: <dict[str, str]>
            :exceptions:
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Template values must be a mapping.
                | ATSValueError: Template values is missing or empty.
        '''
        not_none(
            template_values,
            r'generator::prepare_template_values(...)'
            r'template_values must be provided'
        )
        istype(
            template_values, Mapping,
            r'generator::prepare_template_values(...)'
            r'template_values must be a mapping'
        )

        project_name = template_values.get('project_name')
        not_empty(
            project_name,
            r'generator::prepare_template_values(...)'
            r'template_values must contain a non-empty project_name'
        )

        values = template_values.copy()
        if 'project_name_dashed' not in values:
            values['project_name_dashed'] = project_name.replace('_', '-')
        if 'project_name_camel' not in values:
            values['project_name_camel'] = ''.join(
                word.capitalize() for word in project_name.replace('-', '_').split('_')
            )
        if 'project_name_upper' not in values:
            values['project_name_upper'] = project_name.upper().replace('-', '_')

        return values

    @override
    def generate(self, generator_bundle: GenParamsBundle) -> bool:
        '''
            Generates project modules/files from a .tgz archive.

            :param generator_bundle: Generator bundle containing template generation parameters.
            :type generator_bundle: <GenParamsBundle>
            :return: True if generation was successful, False otherwise.
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target dir must be provided.
                | ATSValueError: Template key must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSTypeError: Target dir must be a string.
                | ATSTypeError: Template key must be a string.
                | ATSTypeError: Scheme must be a string or a mapping.
                | ATSTypeError: Template values must be a mapping.
                | ATSValueError: Archive file does not exist.
                | ATSValueError: Scheme file does not exist.
                | ATSTypeError: Parameters are of invalid type.
                | ATSValueError: Parameter constraints are violated.
                | ATSGeneratorError: Archive parsing or template rendering fails.
        '''
        resolved_scheme = self._scheme_loader.load(generator_bundle.scheme)
        project_scheme = resolved_scheme.get(generator_bundle.template_key)
        not_satisfied(
            not project_scheme,
            r'generator::generate(...)'
            f'template_key {generator_bundle.template_key} not found in scheme configuration'
        )
        source_dir = project_scheme.get('source_dir')
        not_satisfied(
            not source_dir,
            r'generator::generate(...)'
            f'source_dir not specified for template_key {generator_bundle.template_key}'
        )
        path_replacements: dict[str, str] = project_scheme.get('path_replacements', {})
        exclude_patterns: list[str] = project_scheme.get('exclude', [])
        vals = self.prepare_template_values(generator_bundle.template_values)

        try:
            self._tar_processor.process(
                TarProcessBundle(
                    archive_path=generator_bundle.archive_path,
                    target_dir=generator_bundle.target_dir,
                    source_dir=source_dir,
                    path_replacements=path_replacements,
                    exclude_patterns=exclude_patterns,
                    vals=vals
                )
            )

            return True

        except Exception as exc:
            not_satisfied(
                True,
                r'generator::generate(...)'
                f'generation failed {exc}'
            )

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if generator component is initialized.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return all([
            self._is_initialized,
            self._scheme_loader.is_initialized(),
            self._tar_processor.is_initialized()
        ])

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of Generator.

            :return: The Generator as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)

