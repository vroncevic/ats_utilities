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
    Validator for check reporter data.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import override

from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.checker.reporter.data import CheckReporterData, ParamMetadata
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckReporterValidator(IDataValidator[CheckReporterData]):
    '''

        Validator for check reporter data.
        
        It defines:

            :attributes:
                | 
            :methods:
                | validate - Validates check reporter data.
    '''

    @classmethod
    @override
    def validate(cls, data: CheckReporterData) -> None:
        '''
            Validates check reporter data.

            :param data: Check reporter data to be validated.
            :type data: CheckReporterData
            :exceptions:
                | ATSValueError: Check reporter data must be provided.
                | ATSTypeError: Check reporter data must be an instance of CheckReporterData.
                | ATSValueError: Context must be provided.
                | ATSValueError: Parameters metadata must be provided.
                | ATSValueError: Error indices must be provided.
                | ATSValueError: Is format error must be provided.
                | ATSTypeError: Context must be a string.
                | ATSTypeError: Parameters metadata must be a sequence of ParamMetadata.
                | ATSTypeError: Error indices must be a sequence of integers.
                | ATSTypeError: Is format error must be a boolean.
        '''
        ctx: str = r'data_reporter_validator::validate(...)'

        not_none(data, ctx, r'check reporter data must be provided')
        istype(data, CheckReporterData, ctx, r'check reporter data must be an instance of CheckReporterData')

        not_none(data.context, ctx, r'context must be provided')
        not_none(data.parameters_meta, ctx, r'parameters_meta must be provided')
        not_none(data.err_indices, ctx, r'err_indices must be provided')
        not_none(data.is_fmt_err, ctx, r'is_fmt_err must be provided')

        istype(data.context, str, ctx, r'context must be a string')
        istype(data.parameters_meta, Sequence[ParamMetadata], ctx, r'parameters_meta must be a sequence of ParamMetadata')
        istype(data.err_indices, Sequence[int], ctx, r'err_indices must be a sequence of integers')
        istype(data.is_fmt_err, bool, ctx, r'is_fmt_err must be a boolean')
