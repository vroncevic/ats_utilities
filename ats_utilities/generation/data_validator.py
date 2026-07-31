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

from collections.abc import Mapping

from ats_utilities.generation.data import GeneratorData
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.files import check_file_exists

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class GeneratorDataValidator:
    '''

        Validator for generator data.
        
        It defines:

            :attributes:
                | 
            :methods:
                | validate - Validates generator data.
    '''

    @classmethod
    def validate(cls, data: GeneratorData) -> None:
        '''
            Validates generator data.

            :param data: Generator data to be validated.
            :exceptions:
                | ATSValueError: Generator data must be provided and have proper values.
                | ATSTypeError:  Generator data must be an instance of GeneratorData and
                |                its attributes must be instances of their respective types.
        '''
        ctx: str = 'generator_data_validator::validate(...)'
        msg_data_none: str = 'generator data must be provided'
        msg_data_istype: str = 'generator data must be an instance of GeneratorData'
        msg_archive_path_none: str = 'archive_path must be provided'
        msg_target_dir_none: str = 'target_dir must be provided'
        msg_template_key_none: str = 'template_key must be provided'
        msg_scheme_none: str = 'scheme must be provided'
        msg_template_values_none: str = 'template_values must be provided'
        msg_archive_path_istype: str = 'archive_path must be a string'
        msg_target_dir_istype: str = 'target_dir must be a string'
        msg_template_key_istype: str = 'template_key must be a string'
        msg_scheme_istype: str = 'scheme must be a string or a mapping'
        msg_template_values_istype: str = 'template_values must be a mapping'
        msg_archive_file_not_exists: str = 'archive file does not exist'
        msg_scheme_file_not_exists: str = 'scheme file does not exist'

        not_none(data, ctx, msg_data_none)
        istype(data, GeneratorData, ctx, msg_data_istype)

        not_none(data.archive_path, ctx, msg_archive_path_none)
        not_none(data.target_dir, ctx, msg_target_dir_none)
        not_none(data.template_key, ctx, msg_template_key_none)
        not_none(data.scheme, ctx, msg_scheme_none)
        not_none(data.template_values, ctx, msg_template_values_none)

        istype(data.archive_path, str, ctx, msg_archive_path_istype)
        istype(data.target_dir, str, ctx, msg_target_dir_istype)
        istype(data.template_key, str, ctx, msg_template_key_istype)
        istype(data.scheme, (str, Mapping), ctx, msg_scheme_istype)
        istype(data.template_values, Mapping, ctx, msg_template_values_istype)

        check_file_exists(data.archive_path, ctx, msg_archive_file_not_exists)

        if isinstance(data.scheme, str):
            check_file_exists(data.scheme, ctx, msg_scheme_file_not_exists)
