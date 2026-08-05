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
    Validator for the file data.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.config_io.data import FileData
from ats_utilities.validation.check_value import not_none, not_empty
from ats_utilities.validation.check_type import istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FileDataValidator:
    '''
        Validator for the file data.

        It defines:

            :methods:
                | validate - Validates the file data.
    '''

    @classmethod
    def validate(cls, data: FileData) -> None:
        '''
            Validates the file data.

            :param data: The file data to be validated.
            :exceptions:
                | ATSValueError: The file data must be provided and have proper values.
                | ATSTypeError:  The file data must be an instance of FileData and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'file_data_validator::validate(...)'
        msg_data_none: str = 'the file data must be provided'
        msg_data_istype: str = 'the file data must be an instance of FileData'
        msg_path_none: str = 'the file path must be provided'
        msg_mode_none: str = 'the file mode must be provided'
        msg_context_none: str = 'the context bundle must be provided'
        msg_path_istype: str = 'the file path must be a string'
        msg_mode_istype: str = 'the file mode must be a string'
        msg_context_istype: str = 'the context bundle must be a ContextBundle instance'
        msg_path_empty: str = 'the file path must not be empty'
        msg_mode_empty: str = 'the file mode must not be empty'

        not_none(data, ctx, msg_data_none)
        istype(data, FileData, ctx, msg_data_istype)

        not_none(data.file_path, ctx, msg_path_none)
        not_none(data.file_mode, ctx, msg_mode_none)
        not_none(data.context_bundle, ctx, msg_context_none)

        istype(data.file_path, str, ctx, msg_path_istype)
        istype(data.file_mode, str, ctx, msg_mode_istype)
        istype(data.context_bundle, ContextBundle, ctx, msg_context_istype)

        not_empty(data.file_path, ctx, msg_path_empty)
        not_empty(data.file_mode, ctx, msg_mode_empty)

        ContextBundleValidator.validate(data.context_bundle)
