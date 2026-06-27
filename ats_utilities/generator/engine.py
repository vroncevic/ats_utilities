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

from typing import override
from os.path import exists
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.generator.component_bundle import GeneratorComponentBundle
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.ischeme_loader import ISchemeLoader
from ats_utilities.generator.scheme_loader import SchemeLoader
from ats_utilities.generator.itar_processor import ITarProcessor
from ats_utilities.generator.tar_processor import TarProcessor
from ats_utilities.generator.tar_process_bundle import TarProcessBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_generator_error import ATSGeneratorError
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import get_class_name, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Generator(IGenerator):
    '''
        Defines class Generator with attribute(s) and method(s).
        Template-based file generation from .tgz archives.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _scheme_loader - Loader/resolver for scheme configuration.
                | _tar_processor - Processor for archive extraction and template rendering.
            :methods:
                | __init__ - Initializes Generator constructor.
                | generate - Generates project modules/files from a .tgz archive.
                | is_initialized - Checks if the generator component is initialized.
                | __str__ - Returns the string representation of Generator.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, component_bundle: GeneratorComponentBundle | None = None) -> None:
        '''
            Initializes Generator constructor.

            :param component_bundle: Generator component bundle for generator | None.
            :type component_bundle: <GeneratorComponentBundle | None>
            :exceptions: ATSTypeError.
        '''
        # No dependency injection then use default ones.
        bundle = component_bundle or GeneratorComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        self._is_initialized: bool = False

        try:
            self._scheme_loader: ISchemeLoader = make_component(
                bundle.scheme_loader, SchemeLoader, {'context_bundle': bundle.context_bundle}
            )
            validate_component(self._scheme_loader, SchemeLoader)
            self._tar_processor: ITarProcessor = make_component(
                bundle.tar_processor, TarProcessor, {
                    'context_bundle': bundle.context_bundle,
                    'template_processor': bundle.template_processor
                }
            )
            validate_component(self._tar_processor, TarProcessor)
            self._is_initialized = True

        except (ATSTypeError, ATSValueError) as exc:
            self._reporter.error([f'{get_class_name(self)} {exc}'])
        except Exception as exc:
            self._reporter.error([f'{get_class_name(self)} unexpected exception: {exc}'])

    @override
    def prepare_template_values(self, template_values: dict[str, str]) -> dict[str, str]:
        '''
            Validates and computes name case variations from template values.

            :param template_values: Input replacement values.
            :type template_values: <dict[str, str]>
            :return: The updated template values dictionary.
            :rtype: <dict[str, str]>
            :exceptions:
                | ATSValueError - If project_name is missing or empty.
        '''
        project_name = template_values.get('project_name', '')

        if not project_name:
            raise ATSValueError("template_values must contain a non-empty 'project_name'")

        vals = template_values.copy()
        if 'project_name_dashed' not in vals:
            vals['project_name_dashed'] = project_name.replace('_', '-')
        if 'project_name_camel' not in vals:
            vals['project_name_camel'] = "".join(
                word.capitalize() for word in project_name.replace('-', '_').split('_')
            )
        if 'project_name_upper' not in vals:
            vals['project_name_upper'] = project_name.upper().replace('-', '_')

        return vals

    @override
    def generate(self, generator_bundle: GeneratorBundle) -> bool:
        '''
            Generates project modules/files from a .tgz archive.

            :param generator_bundle: Generator bundle containing template generation parameters.
            :type generator_bundle: <GeneratorBundle>
            :return: True if generation was successful, False otherwise.
            :rtype: <bool>
            :exceptions:
                | ATSTypeError - If parameters are of invalid type.
                | ATSValueError - If parameter constraints are violated.
                | ATSGeneratorError - If archive parsing or template rendering fails.
        '''
        generator_bundle.validate()
        if not exists(generator_bundle.archive_path):
            raise ATSValueError(f"Archive file does not exist: '{generator_bundle.archive_path}'")

        resolved_scheme = self._scheme_loader.load(generator_bundle.scheme)
        project_scheme = resolved_scheme.get(generator_bundle.template_key)

        if not project_scheme:
            raise ATSValueError(f"template_key '{generator_bundle.template_key}' not found in scheme configuration")

        source_dir = project_scheme.get('source_dir')

        if not source_dir:
            raise ATSValueError(f"source_dir not specified for template_key '{generator_bundle.template_key}'")

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
            raise ATSGeneratorError(f"generation failed {exc}")

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if generator component is initialized.

            :return: True (success) | False (fail).
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
        return format_instance_to_string(self)

