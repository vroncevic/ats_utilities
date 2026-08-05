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
    Defines the TarProcessor class with attribute(s) and method(s).
    Provides an API for tar archive extraction and template rendering.
'''

from __future__ import annotations

from os import makedirs
from os.path import dirname, join
from tarfile import open

from ats_utilities.generation.tar.data import TarData, TarMemberData
from ats_utilities.generation.tar.data_validator import (
    TarDataValidator, TarMemberDataValidator
)
from ats_utilities.generation.template.itemplate_processor import ITemplateProcessor
from ats_utilities.utils.reflection import to_str
from ats_utilities.utils.files import (
    normalize_path,
    resolve_relative_path,
    is_excluded_path,
    apply_path_replacements,
    write_content
)
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.exceptions import ATSGeneratorError
from ats_utilities.validation.check_value import not_satisfied, not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.exceptions.format_error import format_error_raw

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TarProcessor:
    '''
        Defines the TarProcessor class with attribute(s) and method(s).
        Provides an API for tar archive extraction and template rendering.

        It defines:

            :attributes:
                | _template_processor - The renders placeholders inside template files.
            :methods:
                | __init__ - Initializes the TarProcessor.
                | process_tar_member - Processes a single tar archive member.
                | process - Processes tar archive members.
                | is_initialized - Checks if tar processor is initialized.
                | __str__ - Returns the tar processor as a string representation.
    '''

    _context: ContextBundle
    _template_processor: ITemplateProcessor

    def __init__(self, context_bundle: ContextBundle, template_processor: ITemplateProcessor) -> None:
        '''
            Initializes the TarProcessor.

            :param context_bundle: The context bundle for tar processor.
            :param template_processor: The custom template rendering component.
            :exceptions:
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
                | ATSValueError: The template processor must be provided.
                | ATSTypeError:  The template processor must be an instance of ITemplateProcessor.   
        '''
        ContextBundleValidator.validate(context_bundle)
        self._context = context_bundle

        ctx: str = 'tar_processor::init(...)'
        msg_template_processor_none: str = 'the template processor must be provided'
        msg_template_processor_istype: str = 'the template processor must be an instance of ITemplateProcessor'

        not_none(template_processor, ctx, msg_template_processor_none)
        istype(template_processor, ITemplateProcessor, ctx, msg_template_processor_istype)

        self._template_processor = template_processor

    def process_tar_member(self, data: TarMemberData) -> None:
        '''
            Extracts and processes a single tar member (creates dirs or renders files).

            :param data: The parameters defining what to do with the tar archive member.
            :exceptions:
                | ATSValueError: The tar member data must be provided and have proper values.
                | ATSTypeError:  The tar member data must be an instance of TarMemberData and
                |                its attributes must be instances of their respective types.
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

                ctx: str = 'tar_processor::process_tar_member(...)'
                write_content(
                    data.dest_full_path, rendered, ctx,
                    f'the error writing to file {data.dest_full_path}'
                )

    def process(self, data: TarData) -> None:
        '''
            Processes the tar archive members.

            :param data: The parameters defining what to do with the tar archive.
            :exceptions:
                | ATSValueError: The tar data must be provided and have proper values.
                | ATSTypeError:  The tar data must be an instance of TarData and
                |                its attributes must be instances of their respective types.
        '''
        ctx: str = 'tar_processor::process(...)'
        try:
            TarDataValidator.validate(data)
            makedirs(data.target_dir, exist_ok=True)

            with open(data.archive_path, 'r:gz') as tar:
                source_dir_clean = normalize_path(data.source_dir, ctx)

                for member in tar.getmembers():
                    msg_path_err: str = f'the error normalizing path {member.name} in tar {data.archive_path}'
                    normalized_name = normalize_path(member.name, ctx, msg_path_err)

                    msg_resolve_path_err: str = f'the error resolving relative path {normalized_name}'
                    msg_resolve_path_err_with_source: str = f'{msg_resolve_path_err} with source dir {source_dir_clean}'
                    rel_path = resolve_relative_path(
                        normalized_name, source_dir_clean, ctx, msg_resolve_path_err_with_source
                    )

                    if rel_path is None or not rel_path:
                        continue

                    msg_exclude_path_err: str = f'the error checking for excluded path {rel_path}'
                    msg_exclude_path_err_with_patterns: str = f'{msg_exclude_path_err} with patterns {data.exclude_patterns}'

                    if is_excluded_path(rel_path, data.exclude_patterns, ctx, msg_exclude_path_err_with_patterns):
                        continue

                    msg_path_replace_err: str = f'the error applying path replacements to {rel_path}'
                    msg_path_replace_err_with_patterns: str = f'{msg_path_replace_err} with patterns {data.path_replacements}'
                    dest_rel_path = apply_path_replacements(
                        rel_path, data.path_replacements, data.vals, ctx, msg_path_replace_err_with_patterns
                    )

                    dest_full_path = join(data.target_dir, dest_rel_path)

                    self.process_tar_member(
                        TarMemberData(tar=tar, member=member, dest_full_path=dest_full_path, vals=data.vals)
                    )

        except Exception as exc:
            msg: str = format_error_raw(exc, self._context.verbose)
            msg_fail: str = f'the process execution failed: {msg}'
            not_satisfied(True, ctx, msg_fail, ATSGeneratorError)

    def is_initialized(self) -> bool:
        '''
            Checks if tar processor is initialized.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return self._template_processor.is_initialized()

    def __str__(self) -> str:
        '''
            Returns the tar processor as a string representation.

            :return: The Tar processor as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
