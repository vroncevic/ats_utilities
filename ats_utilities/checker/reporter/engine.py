# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines the class CheckReporter with attribute(s) and method(s).
    Provides an API for building the final message in the context of a checker.
'''

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

from ats_utilities.checker.reporter.data import CheckReporterData
from ats_utilities.checker.reporter.data_validator import CheckReporterDataValidator
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_empty

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class CheckReporter:
    '''
        Defines the class CheckReporter with attribute(s) and method(s).
        Provides an API for building the final message in the context of a checker.

        It defines:

            :attributes:
                | DEFAULT_MESSAGES - The default messages used to report findings.
                | _message_provider - The messages used to report findings.
            :methods:
                | __init__ - Initializes the check reporter.
                | build_message - Builds the final message.
                | __str__ - Returns the check reporter as a string representation.
    '''

    DEFAULT_MESSAGES: Final[MappingProxyType[str, str]] = MappingProxyType({
        'param_entry': '\n    expected {pname} <{ptype}> object at {inst}',
        'wrong_type': ' wrong type',
        'format_wrong_during_checking_parameters_meta': ' format wrong during checking parameters_meta'
    })
    _message_provider: Mapping[str, str]

    def __init__(self, message_provider: Mapping[str, str] | None = None) -> None:
        '''
            Initializes the check reporter.

            :param message_provider: Optional mapping with string keys and string values
                                     that are used to build the final message report | None.
            :exceptions:
                | ATSTypeError:  The message provider must be a mapping.
                | ATSValueError: The message provider must not be empty.
        '''
        if message_provider is not None:
            ctx: str = 'check_reporter::init(...)'
            msg_param_istype: str = 'the message provider must be a mapping'
            msg_param_empty: str = 'the message provider must not be empty'

            istype(message_provider, Mapping, ctx, msg_param_istype)
            not_empty(message_provider, ctx, msg_param_empty)

            self._message_provider = MappingProxyType(message_provider)
        else:
            self._message_provider = self.DEFAULT_MESSAGES

    def build_message(self, data: CheckReporterData) -> str:
        '''
            Builds the final message.

            :param data: The data to be formatted.
            :return: The final message.
            :exceptions:
                | ATSValueError: The data must be provided and have proper values.
                | ATSTypeError:  The data must be an instance of CheckReporterData
                |                and its attributes must be instances of their
                |                respective types.
        '''
        CheckReporterDataValidator.validate(data)
        message: str = data.context
        err_set: set[int] = set(data.err_indices)

        param_fmt: str = self._message_provider.get(
            'param_entry',
            self.DEFAULT_MESSAGES['param_entry']
        )
        wrong_type_msg: str = self._message_provider.get(
            'wrong_type',
            self.DEFAULT_MESSAGES['wrong_type']
        )
        fmt_err_msg: str = self._message_provider.get(
            'format_wrong_during_checking_parameters_meta',
            self.DEFAULT_MESSAGES['format_wrong_during_checking_parameters_meta']
        )

        for i, (pname, ptype, inst) in enumerate(data.parameters_meta):
            message += param_fmt.format(pname=pname, ptype=ptype, inst=hex(id(inst)))

            if i in err_set:
                message += wrong_type_msg

        if data.is_fmt_err:
            message += fmt_err_msg

        return message

    def __str__(self) -> str:
        '''
            Returns the check reporter as a string representation.

            :return: The check reporter as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
