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

from ats_utilities.generation.tar.data import TarData, TarMemberData
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TarDataValidator:
    '''

        Validator for tar data.
        
        It defines:

            :attributes:
                | 
            :methods:
                | validate - Validates tar data.
    '''

    @classmethod
    def validate(cls, data: TarData) -> None:
        '''
            Validates tar data.

            :param data: Tar data to be validated.
            :exceptions:
                | ATSValueError: Tar data must be provided and have proper values.
                | ATSTypeError:  Tar data must be an instance of TarData and
                |                its attributes must be instances of their respective types.
        '''
        ctx: str = 'tar_data_validator::validate(...)'
        msg_data_none: str = 'data must be provided'
        msg_data_istype: str = 'data must be an instance of TarData'
        msg_archive_path_none: str = 'archive_path must be provided'
        msg_target_dir_none: str = 'target_dir must be provided'
        msg_source_dir_none: str = 'source_dir must be provided'
        msg_path_replacements_none: str = 'path_replacements must be provided'
        msg_exclude_patterns_none: str = 'exclude_patterns must be provided'
        msg_vals_none: str = 'vals must be provided'
        msg_archive_path_istype: str = 'archive_path must be a string'
        msg_target_dir_istype: str = 'target_dir must be a string'
        msg_source_dir_istype: str = 'source_dir must be a string'
        msg_path_replacements_istype: str = 'path_replacements must be a mapping'
        msg_exclude_patterns_istype: str = 'exclude_patterns must be a sequence'
        msg_vals_istype: str = 'vals must be a mapping'

        not_none(data, ctx, msg_data_none)
        istype(data, TarData, ctx, msg_data_istype)

        not_none(data.archive_path, ctx, msg_archive_path_none)
        not_none(data.target_dir, ctx, msg_target_dir_none)
        not_none(data.source_dir, ctx, msg_source_dir_none)
        not_none(data.path_replacements, ctx, msg_path_replacements_none)
        not_none(data.exclude_patterns, ctx, msg_exclude_patterns_none)
        not_none(data.vals, ctx, msg_vals_none)

        istype(data.archive_path, str, ctx, msg_archive_path_istype)
        istype(data.target_dir, str, ctx, msg_target_dir_istype)
        istype(data.source_dir, str, ctx, msg_source_dir_istype)
        istype(data.path_replacements, Mapping, ctx, msg_path_replacements_istype)
        istype(data.exclude_patterns, Sequence, ctx, msg_exclude_patterns_istype)
        istype(data.vals, Mapping, ctx, msg_vals_istype)


class TarMemberDataValidator:
    '''

        Validator for tar member data.
        
        It defines:

            :attributes:
                | 
            :methods:
                | validate - Validates tar member data.
    '''

    @classmethod
    def validate(cls, data: TarMemberData) -> None:
        '''
            Validates tar member data.

            :param data: Tar member data to be validated.
            :exceptions:
                | ATSValueError: Tar member data must be provided and have proper values.
                | ATSTypeError:  Tar member data must be an instance of TarMemberData and
                |                its attributes must be instances of their respective types.
        '''
        ctx: str = 'tar_member_data_validator::validate(...)'
        msg_data_none: str = 'data must be provided'
        msg_data_istype: str = 'data must be an instance of TarMemberData'
        msg_tar_none: str = 'tar must be provided'
        msg_member_none: str = 'member must be provided'
        msg_dest_full_path_none: str = 'dest_full_path must be provided'
        msg_vals_none: str = 'vals must be provided'
        msg_tar_istype: str = 'tar must be a TarFile instance'
        msg_member_istype: str = 'member must be a TarInfo instance'
        msg_dest_full_path_istype: str = 'dest_full_path must be a string'
        msg_vals_istype: str = 'vals must be a mapping'

        not_none(data, ctx, msg_data_none)
        istype(data, TarMemberData, ctx, msg_data_istype)

        not_none(data.tar, ctx, msg_tar_none)
        not_none(data.member, ctx, msg_member_none)
        not_none(data.dest_full_path, ctx, msg_dest_full_path_none)
        not_none(data.vals, ctx, msg_vals_none)

        istype(data.tar, TarFile, ctx, msg_tar_istype)
        istype(data.member, TarInfo, ctx, msg_member_istype)
        istype(data.dest_full_path, str, ctx, msg_dest_full_path_istype)
        istype(data.vals, Mapping, ctx, msg_vals_istype)
