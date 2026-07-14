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
from os.path import exists
from typing import override
from sys import stderr

from ats_utilities.logger.ilogger import ILogger
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import (
    ATSAttributeError,
    ATSGeneratorError,
    ATSRuntimeError,
    ATSTypeError,
    ATSValueError
)
from ats_utilities.factory_class import to_str, cls_name
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.generator.component_bundle import GeneratorComponentBundle
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.factory_value import require_not_satisfied, require_not_empty

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Generator(IGenerator):
    '''
        Defines class Generator with attribute(s) and method(s).
        Template-based file generation from .tgz archives.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
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

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _shared_context: ContextBundle
    _scheme_loader: ISchemeLoader
    _tar_processor: ITarProcessor
    _is_initialized: bool

    def __init__(self, component_bundle: GeneratorComponentBundle | None = None) -> None:
        '''
            Initializes Generator constructor.

            :param component_bundle: Generator component bundle for generator | None.
            :type component_bundle: <GeneratorComponentBundle | None>
            :exceptions: ATSTypeError.
        '''
        self._is_initialized = False

        try:
            bundle = component_bundle or GeneratorComponentBundle()
            factory_context_bundle(self, bundle.context_bundle)
            self._shared_context = bundle.context_bundle
            self._scheme_loader = bundle.scheme_loader
            self._tar_processor = bundle.tar_processor

            # All components initialized successfully.
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            stderr.write(f'\x1b[31m{cls_name(self)} {exc}\x1b[0m\n')

        except Exception as exc:
            stderr.write(f'\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m\n')

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
                | ATSValueError: If project_name is missing or empty.
        '''
        project_name = template_values.get('project_name')
        require_not_empty(project_name, f'template values must contain a non-empty {project_name}')

        vals = template_values.copy()
        if 'project_name_dashed' not in vals:
            vals['project_name_dashed'] = project_name.replace('_', '-')
        if 'project_name_camel' not in vals:
            vals['project_name_camel'] = ''.join(
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
                | ATSTypeError: If parameters are of invalid type.
                | ATSValueError: If parameter constraints are violated.
                | ATSGeneratorError: If archive parsing or template rendering fails.
        '''
        generator_bundle.validate()
        require_not_satisfied(not exists(generator_bundle.archive_path), f'Archive file does not exist: {generator_bundle.archive_path}')
        resolved_scheme = self._scheme_loader.load(generator_bundle.scheme)
        project_scheme = resolved_scheme.get(generator_bundle.template_key)
        require_not_satisfied(not project_scheme, f'template_key {generator_bundle.template_key} not found in scheme configuration')
        source_dir = project_scheme.get('source_dir')
        require_not_satisfied(not source_dir, f'source_dir not specified for template_key {generator_bundle.template_key}')

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
            require_not_satisfied(True, f'generation failed {exc}', ATSGeneratorError)

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

