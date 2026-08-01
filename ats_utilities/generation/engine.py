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
    Defines the GeneratorManager class with attribute(s) and method(s).
    Provides an API for template-based generation of project files from .tgz archives.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.generation.setup.bundle import GeneratorBundle
from ats_utilities.generation.setup.validator import GeneratorValidator
from ats_utilities.generation.data import GeneratorData
from ats_utilities.generation.data_validator import GeneratorDataValidator
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.generation.tar.data import TarData
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.validation.check_value import not_satisfied, not_empty, not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class GeneratorManager:
    '''
        Defines the GeneratorManager class with attribute(s) and method(s).
        Provides an API for template-based generation of project files from .tgz archives.

        It defines:

            :attributes:
                | _context - The bundle of context.
                | _scheme_loader - The loader/resolver for the scheme configuration.
                | _tar_processor - The processor for the archive extraction and template rendering.
                | _is_initialized - The flag indicating if the generator manager is initialized.
            :methods:
                | __init__ - Initializes generator manager.
                | get_bundle - Returns the current generator configuration bundle.
                | update_bundle - Updates current generator configuration bundle.
                | _apply_bundle - Applies the generator configuration bundle.
                | get_context - Returns the current context.
                | generate - Generates project modules/files from a .tgz archive.
                | is_initialized - Checks if the generator manager is initialized.
                | __str__ - Returns the generator manager as a string representation.
    '''

    _context: ContextBundle
    _scheme_loader: ISchemeLoader
    _tar_processor: ITarProcessor
    _is_initialized: bool

    def __init__(self, own: GeneratorBundle) -> None:
        '''
            Initializes generator manager.

            :param own: The generator manager component bundle for generator.
            :exceptions:
                | ATSValueError: Generator manager component bundle must be provided and have proper values.
                | ATSTypeError:  Generator manager component bundle must be an instance of GeneratorBundle
                |                and its attributes must be instances of their respective types.
        '''
        self._is_initialized = False
        GeneratorValidator.validate(own)
        self._apply_bundle(own)
        self._is_initialized = True

    def get_bundle(self) -> GeneratorBundle:
        '''
            Gets current generator configuration bundle.

            :return: The generator configuration bundle.
            :exceptions: None.
        '''
        return GeneratorBundle(
            context_bundle=self._context,
            scheme_loader=self._scheme_loader,
            tar_processor=self._tar_processor
        )

    def update_bundle(self, bundle: GeneratorBundle) -> bool:
        '''
            Updates generator configuration bundle.

            :param bundle: The generator configuration bundle.
            :return: True if generator configuration bundle is updated successfully.
            :exceptions: None.
        '''
        try:
            self._is_initialized = False
            GeneratorValidator.validate(bundle)
            self._apply_bundle(bundle)
            self._is_initialized = True

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: GeneratorBundle) -> None:
        '''
            Applies generator configuration bundle.

            :param bundle: The generator configuration bundle.
            :exceptions: None.
        '''
        self._context = bundle.context_bundle
        self._scheme_loader = bundle.scheme_loader
        self._tar_processor = bundle.tar_processor

    def get_context(self) -> ContextBundle:
        '''
            Gets current context.

            :return: The current context.
            :exceptions: None.
        '''
        return self._context

    def prepare_template_values(self, template_values: Mapping[str, str]) -> dict[str, str]:
        '''
            Validates the and computes name case variations from template values instance.

            :param template_values: The input replacement values.
            :return: The updated template values dictionary.
            :exceptions:
                | ATSValueError: Template values must be provided.
                | ATSTypeError:  Template values must be a mapping.
                | ATSValueError: Template values is missing or empty.
        '''
        ctx: str = 'generator::prepare_template_values(...)'
        msg_template_values_none: str = 'template_values must be provided'
        msg_template_values_istype: str = 'template_values must be a mapping'
        msg_project_name_empty: str = 'template_values must contain a non-empty project_name'

        not_none(template_values, ctx, msg_template_values_none)
        istype(template_values, Mapping, ctx, msg_template_values_istype)
        project_name: str = template_values.get('project_name')
        not_empty(project_name, ctx, msg_project_name_empty)

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

    def generate(self, data: GeneratorData) -> bool:
        '''
            Generates project modules/files from a .tgz archive.

            :param data: The GeneratorManager data containing template generation parameters.
            :return: True if successful, otherwise False.
            :exceptions:
                | ATSValueError: Generator data must be provided and have proper values.
                | ATSTypeError:  Generator data must be an instance of GeneratorData and its attributes
                |                must be instances of their respective types.
        '''
        GeneratorDataValidator.validate(data)
        resolved_scheme = self._scheme_loader.load(data.scheme)
        project_scheme = resolved_scheme.get(data.template_key)

        ctx: str = 'generator::generate(...)'
        msg_template_key_not_found: str = f'template_key {data.template_key} not found in scheme configuration'
        msg_source_dir_not_specified: str = f'source_dir not specified for template_key {data.template_key}'

        not_satisfied(not project_scheme, ctx, msg_template_key_not_found)

        source_dir: str = project_scheme.get('source_dir')
        not_satisfied(not source_dir, ctx, msg_source_dir_not_specified)

        path_replacements: dict[str, str] = project_scheme.get('path_replacements', {})
        exclude_patterns: list[str] = project_scheme.get('exclude', [])

        vals: dict[str, str] = self.prepare_template_values(data.template_values)

        try:
            self._tar_processor.process(
                TarData(
                    archive_path=data.archive_path,
                    target_dir=data.target_dir,
                    source_dir=source_dir,
                    path_replacements=path_replacements,
                    exclude_patterns=exclude_patterns,
                    vals=vals
                )
            )

            return True

        except Exception as exc:
            not_satisfied(True, ctx, f'generation failed {exc}')

    def is_initialized(self) -> bool:
        '''
            Checks if generator manager is initialized.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return all([
            self._is_initialized,
            self._scheme_loader.is_initialized(),
            self._tar_processor.is_initialized()
        ])

    def __str__(self) -> str:
        '''
            Returns the generator manager as a string representation.

            :return: The Generator manager as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
