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


class CheckReporterValidator:
    '''

        Validator for check reporter data.
        
        It defines:

            :methods:
                | validate - Validates check reporter data.
    '''

    @classmethod
    def validate(cls, data: CheckReporterData) -> None:
        '''
            Validates check reporter data.

            :param data: Check reporter data to be validated.
            :exceptions:
                | ATSValueError: Check reporter data must be provided.
                | ATSTypeError:  Check reporter data must be an instance of CheckReporterData.
                | ATSValueError: Context must be provided.
                | ATSValueError: Parameters metadata must be provided.
                | ATSValueError: Error indices must be provided.
                | ATSValueError: Is format error flag must be provided.
                | ATSTypeError:  Context must be a string.
                | ATSTypeError:  Parameters metadata must be a sequence of ParametersMeta.
                | ATSTypeError:  Error indices must be a sequence of integers.
                | ATSTypeError:  Is format error flag must be a boolean.
        '''
        ctx: str = 'data_reporter_validator::validate(...)'

        not_none(data, ctx, 'check reporter data must be provided')
        istype(data, CheckReporterData, ctx, 'check reporter data must be an instance of CheckReporterData')

        not_none(data.context, ctx, 'context must be provided')
        not_none(data.parameters_meta, ctx, 'parameters meta must be provided')
        not_none(data.err_indices, ctx, 'error indices must be provided')
        not_none(data.is_fmt_err, ctx, 'is format error flag must be provided')

        istype(data.context, str, ctx, 'context must be a string')
        istype(data.parameters_meta, Sequence[ParametersMeta], ctx, 'parameters meta must be a sequence of ParametersMeta')
        istype(data.err_indices, Sequence[int], ctx, 'error indices must be a sequence of integers')
        istype(data.is_fmt_err, bool, ctx, 'is format error flag must be a boolean')
