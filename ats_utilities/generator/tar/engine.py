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
    Defines class TarProcessor with method(s).
    Handles tar archive extraction and template rendering.
'''

from __future__ import annotations

from os import makedirs
from os.path import dirname, join
from tarfile import open
from typing import override

from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.tar.data import TarData, TarMemberData
from ats_utilities.generator.tar.data_validator import (
    TarDataValidator, TarMemberDataValidator
)
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.utils.files import (
    normalize_path,
    resolve_relative_path,
    is_excluded_path,
    apply_path_replacements,
    write_content
)
from ats_utilities.exceptions import ATSGeneratorError
from ats_utilities.validation.check_value import not_satisfied, not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.exceptions.format_error import format_error_raw

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TarProcessor(ITarProcessor):
    '''
        Defines class TarProcessor with method(s).
        Handles tar archive extraction and template rendering.

        It defines:

            :attributes:
                | _template_processor - Renders placeholders inside template files.
            :methods:
                | __init__ - Initializes TarProcessor constructor.
                | process_tar_member - Processes a single tar archive member.
                | process - Processes the tar archive members.
                | is_initialized - Checks if the processor is initialized.
                | __str__ - Returns the processor as string representation.
    '''

    _context: ContextBundle
    _template_processor: ITemplateProcessor

    def __init__(
        self,
        context_bundle: ContextBundle,
        template_processor: ITemplateProcessor
    ) -> None:
        '''
            Initializes TarProcessor constructor.

            :param context_bundle: Context bundle for tar processor.
            :type context_bundle: ContextBundle
            :param template_processor: Custom template rendering component.
            :type template_processor: <ITemplateProcessor>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Template processor must be an instance of ITemplateProcessor.   
        '''
        ctx: str = r'tar_processor::init(...)'

        not_none(context_bundle, ctx, r'context bundle must be provided')
        istype(
            context_bundle, ContextBundle, ctx,
            r'context bundle must be an instance of ContextBundle'
        )
        self._context = context_bundle

        not_none(template_processor, ctx, r'template processor must be provided')
        istype(
            template_processor, ITemplateProcessor, ctx,
            r'template processor must be an instance of ITemplateProcessor'
        )
        self._template_processor = template_processor

    @override
    def process_tar_member(self, data: TarMemberData) -> None:
        '''
            Extracts and processes a single tar member (creates dirs or renders files).

            :param data: Parameters defining what to do with the tar archive member.
            :type data: TarMemberData
            :exceptions:
                | ATSValueError: data must be provided.
                | ATSTypeError: data must be an instance of TarMemberData.
                | ATSValueError: tar must be provided.
                | ATSValueError: member must be provided.
                | ATSValueError: dest_full_path must be provided.
                | ATSValueError: vals must be provided.
                | ATSTypeError: tar must be a TarFile instance.
                | ATSTypeError: member must be a TarInfo instance.
                | ATSTypeError: dest_full_path must be a string.
                | ATSTypeError: vals must be a mapping.
                | ATSValueError: Error writing to file.
        '''
        TarMemberDataValidator.validate(data)

        if data.member.isdir():
            makedirs(data.dest_full_path, exist_ok=True)
        elif data.member.isfile():
            makedirs(dirname(data.dest_full_path), exist_ok=True)
            f_obj = data.tar.extractfile(data.member)

            if f_obj is not None:
                raw_content = f_obj.read()
                rendered = self._template_processor.render(raw_content, data.vals)

                ctx: str = r'tar_processor::process_tar_member(...)'
                write_content(
                    data.dest_full_path, rendered, ctx,
                    f'error writing to file {data.dest_full_path}'
                )

    @override
    def process(self, data: TarData) -> None:
        '''
            Processes the tar archive members.

            :param data: Parameters defining what to do with the tar archive.
            :type data: TarData
            :exceptions:
                | ATSValueError: data must be provided.
                | ATSTypeError: data must be an instance of TarData.
                | ATSValueError: archive path must be provided.
                | ATSTypeError: archive path must be a string.
                | ATSValueError: target directory must be provided.
                | ATSTypeError: target directory must be a string.
                | ATSValueError: source directory must be provided.
                | ATSTypeError: source directory must be a string.
                | ATSValueError: path replacements must be provided.
                | ATSTypeError: path replacements must be a mapping.
                | ATSValueError: exclude patterns must be provided.
                | ATSTypeError: exclude patterns must be a sequence.
                | ATSValueError: vals must be provided.
                | ATSTypeError: vals must be a mapping.
                | ATSValueError: Error writing to file.
                | ATSValueError: Error normalizing path.
                | ATSValueError: Error resolving relative path.
                | ATSValueError: Error checking for excluded path.
                | ATSValueError: Error applying path replacements.
                | ATSGeneratorError: Process execution failed.
        '''
        ctx: str = r'tar_processor::process(...)'
        try:
            TarDataValidator.validate(data)
            makedirs(data.target_dir, exist_ok=True)

            with open(data.archive_path, 'r:gz') as tar:
                source_dir_clean = normalize_path(data.source_dir, ctx)

                for member in tar.getmembers():
                    normalized_name = normalize_path(
                        member.name, ctx,
                        f'error normalizing path {member.name} in tar {data.archive_path}'
                    )
                    rel_path = resolve_relative_path(
                        normalized_name, source_dir_clean, ctx,
                        f'error resolving relative path {normalized_name}'
                        f' with source dir {source_dir_clean}'
                    )

                    if rel_path is None or not rel_path:
                        continue

                    if is_excluded_path(
                        rel_path, data.exclude_patterns, ctx,
                        f'error checking for excluded path {rel_path}'
                        f' with patterns {data.exclude_patterns}'
                    ):
                        continue

                    dest_rel_path = apply_path_replacements(
                        rel_path, data.path_replacements, data.vals, ctx,
                        f'error applying path replacements to {rel_path}'
                        f' with replacements {data.path_replacements}'
                    )
                    dest_full_path = join(data.target_dir, dest_rel_path)

                    self.process_tar_member(
                        TarMemberData(
                            tar=tar,
                            member=member,
                            dest_full_path=dest_full_path,
                            vals=data.vals
                        )
                    )

        except Exception as exc:
            msg: str = format_error_raw(exc, self._context.verbose)
            not_satisfied(True, ctx, f'process execution failed: {msg}', ATSGeneratorError)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if tar processor component is initialized.

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        return self._template_processor.is_initialized()

    @override
    def __str__(self) -> str:
        '''
            Returns the TarProcessor as string representation.

            :return: The TarProcessor as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
