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
    Validator for option data.
'''

from __future__ import annotations

from collections.abc import Sequence


from ats_utilities.option.command.data import OptionData
from ats_utilities.utils.data.ivalidator import IDataValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionDataValidator(IDataValidator[OptionData]):
    '''
        Validator for option data.

        It defines:

            :methods:
                | validate - Validates an option data instance.
    '''

    @classmethod
    def validate(cls, data: OptionData) -> None:
        '''
            Validates an option data instance.

            :param data: option data instance to be validated.
            :exceptions:
                | ATSValueError: Data must be provided.
                | ATSTypeError: Data must be an instance of OptionData.
                | ATSValueError: Name must be provided.
                | ATSTypeError: Name must be a string.
                | ATSValueError: Help text must be provided.
                | ATSTypeError: Help text must be a string.
                | ATSTypeError: Action must be a string.
                | ATSTypeError: Required must be a boolean.
                | ATSTypeError: Choices must be a sequence.
                | ATSTypeError: Nargs must be a string or an integer.
        '''
        context: str = 'option_data_validator::validate(...)'
        not_none(data, context, 'data must be provided')
        istype(data, OptionData, context, 'data must be an instance of OptionData')

        not_none(data.name, context, 'name must be provided')
        istype(data.name, str, context, 'name must be a string')

        not_none(data.help_text, context, 'help text must be provided')
        istype(data.help_text, str, context, 'help text must be a string')

        if data.action is not None:
            istype(data.action, str, context, 'action must be a string')

        if data.required is not None:
            istype(data.required, bool, context, 'required must be a boolean')

        if data.choices is not None:
            istype(data.choices, Sequence, context, 'choices must be a sequence')

        if data.nargs is not None:
            istype(data.nargs, (str, int), context, 'nargs must be a string or an integer')
