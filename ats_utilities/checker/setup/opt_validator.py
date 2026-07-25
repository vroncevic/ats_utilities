# -*- coding: UTF-8 -*-

'''
Module
    opt_validator.py
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
    Validator for checker options.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.checker.setup.options import CheckerOptions
from ats_utilities.utils.setup.iopt_validator import IOptionsValidator
from ats_utilities.checker.setup.keys import CheckerKeys
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerOptionsValidator(IOptionsValidator[CheckerOptions]):
    '''
        Validator for checker options.

        It defines:

            :methods:
                | validate - Validates checker options instance.
    '''

    @classmethod
    @override
    def validate(cls, options: CheckerOptions) -> None:
        '''
            Validates checker options instance.

            :param options: Checker options instance to be validated.
            :exceptions:
                | ATSValueError: Options must be provided and have proper attributes.
                | ATSTypeError:  Options must be an instance of CheckerOptions
                |                and its attributes must be instances of their
                |                respective types.
        '''
        ctx: str = r'checker_options_validator::validate(...)'

        not_none(options, ctx, r'options must be provided')
        istype(options, Mapping, ctx, r'options must be a Mapping')

        for opt_name, expected_type in CheckerKeys.get_option_to_type().items():
            value = options.get(opt_name)

            if value is not None:
                err_msg = f'{opt_name.replace("_", " ")} must be an instance of {expected_type.__name__}'
                istype(value, expected_type, ctx, err_msg)
