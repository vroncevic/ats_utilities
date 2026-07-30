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


class OptionDataValidator:
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
                | ATSValueError: Option data must be provided and have proper values.
                | ATSTypeError:  Option data must be an instance of OptionData and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'option_data_validator::validate(...)'
        msg_data_none: str = 'data must be provided'
        msg_data_istype: str = 'data must be an instance of OptionData'
        msg_name_none: str = 'name must be provided'
        msg_name_istype: str = 'name must be a string'
        msg_help_text_none: str = 'help text must be provided'
        msg_help_text_istype: str = 'help text must be a string'
        msg_action_istype: str = 'action must be a string'
        msg_required_istype: str = 'required must be a boolean'
        msg_choices_istype: str = 'choices must be a sequence'
        msg_nargs_istype: str = 'nargs must be a string or an integer'

        not_none(data, ctx, msg_data_none)
        istype(data, OptionData, ctx, msg_data_istype)

        not_none(data.name, ctx, msg_name_none)
        istype(data.name, str, ctx, msg_name_istype)

        not_none(data.help_text, ctx, msg_help_text_none)
        istype(data.help_text, str, ctx, msg_help_text_istype)

        if data.action is not None:
            istype(data.action, str, ctx, msg_action_istype)

        if data.required is not None:
            istype(data.required, bool, ctx, msg_required_istype)

        if data.choices is not None:
            istype(data.choices, Sequence, ctx, msg_choices_istype)

        if data.nargs is not None:
            istype(data.nargs, (str, int), ctx, msg_nargs_istype)
