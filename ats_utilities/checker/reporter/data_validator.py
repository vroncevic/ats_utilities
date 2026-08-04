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
    Validator for the check reporter runtime data.
'''

from __future__ import annotations

from collections.abc import Sequence

from ats_utilities.checker.setup.types import ParametersMeta
from ats_utilities.checker.reporter.data import CheckReporterData
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


class CheckReporterDataValidator:
    '''

        Validator for the check reporter runtime data.
        
        It defines:

            :methods:
                | validate - Validates the check reporter runtime data.
    '''

    @classmethod
    def validate(cls, data: CheckReporterData) -> None:
        '''
            Validates the check reporter runtime data.

            :param data: The check reporter runtime data to be validated.
            :exceptions:
                | ATSValueError: The data must be provided and have proper values.
                | ATSTypeError:  The data must be an instance of CheckReporterData
                |                and its attributes must be instances of their
                |                respective types.
        '''
        ctx: str = 'data_reporter_validator::validate(...)'

        msg_data_none: str = 'the check reporter data must be provided'
        msg_data_istype: str = 'the check reporter data must be an instance of CheckReporterData'
        msg_context_none: str = 'the context must be provided'
        msg_parameters_meta_none: str = 'the parameters meta must be provided'
        msg_err_indices_none: str = 'the error indices must be provided'
        msg_is_fmt_err_none: str = 'the is format error flag must be provided'
        msg_context_istype: str = 'the context must be a string'
        msg_parameters_meta_istype: str = 'the parameters meta must be a sequence of ParametersMeta'
        msg_err_indices_istype: str = 'the error indices must be a sequence of integers'
        msg_is_fmt_err_istype: str = 'the is format error flag must be a boolean'

        not_none(data, ctx, msg_data_none)
        istype(data, CheckReporterData, ctx, msg_data_istype)

        not_none(data.context, ctx, msg_context_none)
        not_none(data.parameters_meta, ctx, msg_parameters_meta_none)
        not_none(data.err_indices, ctx, msg_err_indices_none)
        not_none(data.is_fmt_err, ctx, msg_is_fmt_err_none)

        istype(data.context, str, ctx, msg_context_istype)
        istype(data.parameters_meta, Sequence[ParametersMeta], ctx, msg_parameters_meta_istype)
        istype(data.err_indices, Sequence[int], ctx, msg_err_indices_istype)
        istype(data.is_fmt_err, bool, ctx, msg_is_fmt_err_istype)
