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
    Validator for FileData class.
'''

from __future__ import annotations

from typing import override

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.config_io.data import FileData
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FileDataValidator(IDataValidator[FileData]):
    '''
        Validator for FileData class.

        It defines:

            :methods:
                | validate - Validates FileData instance.
    '''

    @classmethod
    @override
    def validate(cls, data: FileData) -> None:
        '''
            Validates FileData instance.

            :param data: FileData instance to be validated.
            :type data: FileData
            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: File mode must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: File mode must be a string.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        context: str = r'file_data_validator::validate(...)'
        not_none(data, context, r'file data must be provided')
        istype(data, FileData, context, r'file data must be an instance of FileData')

        not_none(data.file_path, context, r'file path must be provided')
        not_none(data.file_mode, context, r'file mode must be provided')
        not_none(data.context_bundle, context, r'context bundle must be provided')

        istype(data.file_path, str, context, r'file path must be a string')
        istype(data.file_mode, str, context, r'file mode must be a string')
        istype(data.context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')
