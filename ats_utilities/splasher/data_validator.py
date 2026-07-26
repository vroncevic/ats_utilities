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
    Validator for CenterData class.
'''

from __future__ import annotations



from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.splasher.data import CenterData
from ats_utilities.validation.check_value import not_none, not_satisfied
from ats_utilities.validation.check_type import istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CenterDataValidator(IDataValidator[CenterData]):
    '''
        Validator for CenterData class.

        It defines:

            :methods:
                | validate - Validates CenterData instance.
    '''

    @classmethod
    def validate(cls, data: CenterData) -> None:
        '''
            Validates CenterData instance.

            :param data: CenterData instance to be validated.
            :exceptions:
                | ATSValueError: Columns count must be provided.
                | ATSTypeError: Columns count is not an integer.
                | ATSValueError: Columns count cannot be negative.
                | ATSValueError: Additional shifter must be provided.
                | ATSTypeError: Additional shifter is not an integer.
                | ATSValueError: Additional shifter cannot be negative.
        '''
        ctx: str = 'center_data_validator::validate(...)'
        not_none(data, ctx, 'center data must be provided')
        istype(data, CenterData, ctx, 'center data must be an instance of CenterData')

        not_none(data.columns, ctx, 'columns count must be provided')
        istype(data.columns, int, ctx, 'columns count must be an integer')
        not_satisfied(data.columns < 0, ctx, 'columns count cannot be negative')

        not_none(data.additional_shifter, ctx, 'additional shifter must be provided')
        istype(data.additional_shifter, int, ctx, 'additional shifter must be an integer')
        not_satisfied(data.additional_shifter < 0, ctx, 'additional shifter cannot be negative')
