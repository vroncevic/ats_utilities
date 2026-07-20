# -*- coding: UTF-8 -*-

'''
Module
    tar_process_registry.py
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
    Encapsulates core runtime components for creation of tar process bundle.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.generator.tar.tar_process_params import TarProcessParams

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TarProcessRegistry(IRegistry[TarProcessBundle, TarProcessParams]):
    '''
        Encapsulates core runtime components for creation of tar process bundle.

        It defines:

            :methods:
                | create_bundle - Creates a TarProcessBundle.
                | create_tar_process_bundle - Creates a TarProcessBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: TarProcessParams) -> TarProcessBundle:
        '''
            Creates a TarProcessBundle instance.

            :param params: Registry-specific orchestration parameters.
            :type params: TarProcessParams
            :return: TarProcessBundle instance.
            :rtype: <TarProcessBundle>
            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target dir must be provided.
                | ATSValueError: Source dir must be provided.
                | ATSValueError: Path replacements must be provided.
                | ATSValueError: Exclude patterns must be provided.
                | ATSValueError: Vals must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSTypeError: Target dir must be a string.
                | ATSTypeError: Source dir must be a string.
                | ATSTypeError: Path replacements must be a mapping.
                | ATSTypeError: Exclude patterns must be a sequence.
                | ATSTypeError: Vals must be a mapping.
                | ATSValueError: Archive file does not exist.
        '''
        archive_path: str = params.get('archive_path')
        target_dir: str = params.get('target_dir')
        source_dir: str = params.get('source_dir')
        path_replacements: Mapping[str, str] = params.get('path_replacements')
        exclude_patterns: Sequence[str] = params.get('exclude_patterns')
        vals: Mapping[str, str] = params.get('vals')

        return cls.create_tar_process_bundle(
            archive_path=archive_path,
            target_dir=target_dir,
            source_dir=source_dir,
            path_replacements=path_replacements,
            exclude_patterns=exclude_patterns,
            vals=vals,
        )

    @classmethod
    def create_tar_process_bundle(
        cls,
        archive_path: str,
        target_dir: str,
        source_dir: str,
        path_replacements: Mapping[str, str],
        exclude_patterns: Sequence[str],
        vals: Mapping[str, str]
    ) -> TarProcessBundle:
        '''
            Creates a TarProcessBundle with pre-configured components.

            :param archive_path: Path to the .tgz archive.
            :type archive_path: <str>
            :param target_dir: Target directory where output should be written.
            :type target_dir: <str>
            :param source_dir: Source directory in tar to extract.
            :type source_dir: <str>
            :param path_replacements: Mapping of strings to be replaced in paths.
            :type path_replacements: <Mapping[str, str]>
            :param exclude_patterns: Patterns of files/directories to exclude.
            :type exclude_patterns: <Sequence[str]>
            :param vals: Computed template values for substitution.
            :type vals: <Mapping[str, str]>
            :return: TarProcessBundle instance.
            :rtype: <TarProcessBundle>
            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSValueError: Target directory must be provided.
                | ATSTypeError: Target directory must be a string.
                | ATSValueError: Source directory must be provided.
                | ATSTypeError: Source directory must be a string.
                | ATSValueError: Path replacements must be provided.
                | ATSTypeError: Path replacements must be a mapping.
                | ATSValueError: Exclude patterns must be provided.
                | ATSTypeError: Exclude patterns must be a sequence.
                | ATSValueError: Values must be provided.
                | ATSTypeError: Values must be a mapping.
        '''
        return TarProcessBundle(
            archive_path=archive_path,
            target_dir=target_dir,
            source_dir=source_dir,
            path_replacements=path_replacements,
            exclude_patterns=exclude_patterns,
            vals=vals,
        )
