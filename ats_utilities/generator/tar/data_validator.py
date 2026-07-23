# -*- coding: UTF-8 -*-

'''
Module
    data_validator.py
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
    Validator for generator data.
'''

from __future__ import annotations

from collections.abc import Sequence, Mapping
from tarfile import TarFile, TarInfo
from typing import override

from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.generator.tar.data import TarData, TarMemberData
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


class TarDataValidator(IDataValidator[TarData]):
    '''

        Validator for tar data.
        
        It defines:

            :attributes:
                | 
            :methods:
                | validate - Validates tar data.
    '''

    @classmethod
    @override
    def validate(cls, data: TarData) -> None:
        '''
            Validates tar data.

            :param data: Tar data to be validated.
            :type data: TarData
            :exceptions:
                | ATSValueError: Tar data must be provided.
                | ATSTypeError: Tar data must be an instance of TarData.
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
        context: str = r'tar_data_validator::validate(...)'

        not_none(data, context, r'data must be provided.')
        istype(data, TarData, context, r'data must be an instance of TarData.')
        
        not_none(data.archive_path, context, r'archive path must be provided.')
        not_none(data.target_dir, context, r'target dir must be provided.')
        not_none(data.source_dir, context, r'source dir must be provided.')
        not_none(data.path_replacements, context, r'path replacements must be provided.')
        not_none(data.exclude_patterns, context, r'exclude patterns must be provided.')
        not_none(data.vals, context, r'vals must be provided.')

        istype(data.archive_path, str, context, r'archive path must be a string.')
        istype(data.target_dir, str, context, r'target dir must be a string.')
        istype(data.source_dir, str, context, r'source dir must be a string.')
        istype(data.path_replacements, Mapping, context, r'path replacements must be a mapping.')
        istype(data.exclude_patterns, Sequence, context, r'exclude patterns must be a sequence.')
        istype(data.vals, Mapping, context, r'vals must be a mapping.')


class TarMemberDataValidator(IDataValidator[TarMemberData]):
    '''

        Validator for tar member data.
        
        It defines:

            :attributes:
                | 
            :methods:
                | validate - Validates tar member data.
    '''

    @classmethod
    @override
    def validate(cls, data: TarMemberData) -> None:
        '''
            Validates tar member data.

            :param data: Tar member data to be validated.
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
        '''
        context: str = r'tar_member_data_validator::validate(...)'

        not_none(data, context, r'data must be provided.')
        istype(data, TarMemberData, context, r'data must be an instance of TarMemberData.')
        
        not_none(data.tar, context, r'tar must be provided.')
        not_none(data.member, context, r'member must be provided.')
        not_none(data.dest_full_path, context, r'dest full path must be provided.')
        not_none(data.vals, context, r'vals must be provided.')

        istype(data.tar, TarFile, context, r'tar must be a TarFile instance.')
        istype(data.member, TarInfo, context, r'member must be a TarInfo instance.')
        istype(data.dest_full_path, str, context, r'dest full path must be a string.')
        istype(data.vals, Mapping, context, r'vals must be a mapping.')
