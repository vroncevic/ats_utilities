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
from typing import override

from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.generator.data import GeneratorData
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.files import check_file_exists


__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorDataValidator(IDataValidator[GeneratorData]):
    '''

        Validator for generator data.
        
        It defines:

            :attributes:
                | 
            :methods:
                | validate - Validates generator data.
    '''

    @classmethod
    @override
    def validate(cls, data: GeneratorData) -> None:
        '''
            Validates generator data.

            :param data: Generator data to be validated.
            :type data: GeneratorData
            :exceptions:
                | ATSValueError: Generator data must be provided.
                | ATSTypeError: Generator data must be an instance of GeneratorData.
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target directory must be provided.
                | ATSValueError: Template key must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSTypeError: Target directory must be a string.
                | ATSTypeError: Template key must be a string.
                | ATSTypeError: Scheme must be a string or a mapping.
                | ATSTypeError: Template values must be a mapping.
                | ATSValueError: Archive file does not exist.
                | ATSValueError: Scheme file does not exist.
        '''
        ctx: str = r'generator_data_validator::validate(...)'

        not_none(data, ctx, r'generator data must be provided')
        istype(data, GeneratorData, ctx, r'generator data must be an instance of GeneratorData')

        not_none(data.archive_path, ctx, r'archive_path must be provided')
        not_none(data.target_dir, ctx, r'target_dir must be provided')
        not_none(data.template_key, ctx, r'template_key must be provided')
        not_none(data.scheme, ctx, r'scheme must be provided')
        not_none(data.template_values, ctx, r'template_values must be provided')

        istype(data.archive_path, str, ctx, r'archive_path must be a string')
        istype(data.target_dir, str, ctx, r'target_dir must be a string')
        istype(data.template_key, str, ctx, r'template_key must be a string')
        istype(data.scheme, (str, Mapping), ctx, r'scheme must be a string or a mapping')
        istype(data.template_values, Mapping, ctx, r'template_values must be a mapping')

        check_file_exists(data.archive_path, ctx, f'archive file does not exist: {data.archive_path}')

        if isinstance(data.scheme, str):
            check_file_exists(data.scheme, ctx, f'scheme file does not exist: {data.scheme}')
