# -*- coding: UTF-8 -*-

'''
Module
    tar_processor.py
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
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.generator.tar.tar_process_member_bundle import TarProcessMemberBundle
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.context_bundle_inject import inject_context_bundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.utils.files import (
    normalize_path, resolve_relative_path, is_excluded_path, apply_path_replacements, write_content
)
from ats_utilities.exceptions import ATSGeneratorError
from ats_utilities.validation.check_value import not_satisfied, not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.exceptions.format_error import format_error_raw

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TarProcessor(ITarProcessor):
    '''
        Defines class TarProcessor with method(s).
        Handles tar archive extraction and template rendering.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _template_processor - Renders placeholders inside template files.
            :methods:
                | __init__ - Initializes TarProcessor constructor.
                | process_tar_member - Processes a single tar archive member.
                | process - Processes the tar archive members.
                | is_initialized - Checks if the processor is initialized.
                | __str__ - Returns the processor as string representation.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _template_processor: ITemplateProcessor

    def __init__(
        self,
        context_bundle: ContextBundle,
        template_processor: ITemplateProcessor
    ) -> None:
        '''
            Initializes TarProcessor constructor.

            :param context_bundle: Context bundle for tar processor.
            :type context_bundle: <ContextBundle>
            :param template_processor: Custom template rendering component.
            :type template_processor: <ITemplateProcessor>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Template processor must be an instance of ITemplateProcessor.   
        '''
        inject_context_bundle(self, context_bundle)
        not_none(template_processor, r'template processor must be provided')
        istype(template_processor, ITemplateProcessor, r'template processor must be an instance of ITemplateProcessor')
        self._template_processor = template_processor

    @override
    def process_tar_member(self, tar_process_member_bundle: TarProcessMemberBundle) -> None:
        '''
            Extracts and processes a single tar member (creates dirs or renders files).

            :param tar_process_member_bundle: Parameters defining what to do with the tar archive member.
            :type tar_process_member_bundle: <TarProcessMemberBundle>
            :exceptions:
                | ATSValueError: Tar process member bundle must be provided.
                | ATSTypeError: Tar process member bundle must be an instance of TarProcessMemberBundle.
        '''
        not_none(tar_process_member_bundle, r'tar process member bundle must be provided')
        istype(tar_process_member_bundle, TarProcessMemberBundle, r'tar process member bundle must be an instance of TarProcessMemberBundle')

        if tar_process_member_bundle.member.isdir():
            makedirs(tar_process_member_bundle.dest_full_path, exist_ok=True)
        elif tar_process_member_bundle.member.isfile():
            makedirs(dirname(tar_process_member_bundle.dest_full_path), exist_ok=True)
            f_obj = tar_process_member_bundle.tar.extractfile(tar_process_member_bundle.member)

            if f_obj is not None:
                raw_content = f_obj.read()
                rendered = self._template_processor.render(raw_content, tar_process_member_bundle.vals)
                write_content(tar_process_member_bundle.dest_full_path, rendered)

    @override
    def process(self, tar_process_bundle: TarProcessBundle) -> None:
        '''
            Processes the tar archive members.

            :param tar_process_bundle: Parameters defining what to do with the tar archive.
            :type tar_process_bundle: <TarProcessBundle>
            :exceptions:
                | ATSValueError: Tar process bundle must be provided.
                | ATSTypeError: Tar process bundle must be an instance of TarProcessBundle.
                | ATSGeneratorError: Archive processing or rendering failed.
        '''
        not_none(tar_process_bundle, r'tar process bundle must be provided')
        istype(tar_process_bundle, TarProcessBundle, r'tar process bundle must be an instance of TarProcessBundle')

        try:
            makedirs(tar_process_bundle.target_dir, exist_ok=True)

            with open(tar_process_bundle.archive_path, 'r:gz') as tar:
                source_dir_clean = normalize_path(tar_process_bundle.source_dir)

                for member in tar.getmembers():
                    normalized_name = normalize_path(member.name)
                    rel_path = resolve_relative_path(normalized_name, source_dir_clean)

                    if rel_path is None or not rel_path:
                        continue

                    if is_excluded_path(rel_path, tar_process_bundle.exclude_patterns):
                        continue

                    dest_rel_path = apply_path_replacements(rel_path, tar_process_bundle.path_replacements, tar_process_bundle.vals)
                    dest_full_path = join(tar_process_bundle.target_dir, dest_rel_path)

                    self.process_tar_member(
                        TarProcessMemberBundle(tar=tar, member=member, dest_full_path=dest_full_path, vals=tar_process_bundle.vals)
                    )

        except Exception as exc:
            msg: str = format_error_raw(self, exc)
            not_satisfied(True, f'TarProcessor execution failed: {msg}', ATSGeneratorError)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if tar processor component is initialized.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._template_processor.is_initialized()

    @override
    def __str__(self) -> str:
        '''
            Returns the TarProcessor as string representation.

            :return: The TarProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
