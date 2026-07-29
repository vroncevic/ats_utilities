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
    Validator for file data.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.config_io.data import FileData
from ats_utilities.validation.check_value import not_none, not_empty
from ats_utilities.validation.check_type import istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FileDataValidator:
    '''
        Validator for file data.

        It defines:

            :methods:
                | validate - Validates file data.
    '''

    @classmethod
    def validate(cls, data: FileData) -> None:
        '''
            Validates file data.

            :param data: File data to be validated.
            :exceptions:
                | ATSValueError: File data must be provided and have proper values.
                | ATSTypeError:  File data must be an instance of FileData and its
                |                attributes must be instances of their respective types.
        '''
        context: str = 'file_data_validator::validate(...)'
        not_none(data, context, 'file data must be provided')
        istype(data, FileData, context, 'file data must be an instance of FileData')

        not_none(data.file_path, context, 'file path must be provided')
        not_none(data.file_mode, context, 'file mode must be provided')
        not_none(data.context_bundle, context, 'context bundle must be provided')

        istype(data.file_path, str, context, 'file path must be a string')
        istype(data.file_mode, str, context, 'file mode must be a string')
        istype(data.context_bundle, ContextBundle, context, 'context bundle must be a ContextBundle instance')

        not_empty(data.file_path, context, 'file path must not be empty')
        not_empty(data.file_mode, context, 'file mode must not be empty')
        ContextValidator.validate(data.context_bundle)
