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
    A validator for the center data.
'''

from __future__ import annotations

from ats_utilities.splash.data import CenterData
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


class CenterDataValidator:
    '''
        A validator for the center data.

        It defines:

            :methods:
                | validate - Validates the center data.
    '''

    @classmethod
    def validate(cls, data: CenterData) -> None:
        '''
            Validates the center data.

            :param data: The center data to be validated.
            :exceptions:
                | ATSValueError: Columns count must be provided and have proper values.
                | ATSTypeError:  Columns count must be an instance of CenterData and its 
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'center_data_validator::validate(...)'
        msg_data_none: str = 'the center data must be provided'
        msg_data_type: str = 'the center data must be an instance of CenterData'
        msg_columns_none: str = 'the columns count must be provided'
        msg_columns_type: str = 'the columns count must be an integer'
        msg_columns_value: str = 'the columns count cannot be negative'
        msg_shifter_none: str = 'the additional shifter must be provided'
        msg_shifter_type: str = 'the additional shifter must be an integer'
        msg_shifter_value: str = 'the additional shifter cannot be negative'

        not_none(data, ctx, msg_data_none)
        istype(data, CenterData, ctx, msg_data_type)

        not_none(data.columns, ctx, msg_columns_none)
        istype(data.columns, int, ctx, msg_columns_type)
        not_satisfied(data.columns < 0, ctx, msg_columns_value)

        not_none(data.additional_shifter, ctx, msg_shifter_none)
        istype(data.additional_shifter, int, ctx, msg_shifter_type)
        not_satisfied(data.additional_shifter < 0, ctx, msg_shifter_value)
