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
    Defines class CheckReporter with attribute(s) and method(s).
    Provides an API for building a message in context of a checker.
'''

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType

from ats_utilities.checker.reporter.data import CheckReporterData
from ats_utilities.checker.reporter.data_validator import CheckReporterValidator
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_empty

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class CheckReporter:
    '''
        Defines class CheckReporter with attribute(s) and method(s).
        Provides an API for building a message in context of a checker.

        It defines:

            :attributes:
                | _DEFAULT_MESSAGES - Default messages used to report findings.
                | _message_provider - Messages used to report findings.
            :methods:
                | __init__ - Initializes check reporter.
                | build_message - Builds a final message.
                | __str__ - Returns check reporter as string representation.
    '''

    _DEFAULT_MESSAGES: Mapping[str, str] = MappingProxyType({
        'param_entry': '\n    expected {pname} <{ptype}> object at {inst}',
        'wrong_type': ' wrong type',
        'format_wrong_during_checking_parameters_meta': ' format wrong during checking parameters_meta'
    })
    _message_provider: Mapping[str, str]

    def __init__(self, message_provider: Mapping[str, str] | None = None) -> None:
        '''
            Initializes check reporter.

            :param message_provider: Messages used to report findings | None.
            :exceptions:
                | ATSTypeError:  Message provider must be a mapping.
                | ATSValueError: Message provider must not be empty (key and value must be strings).
        '''
        if message_provider is not None:
            ctx: str = 'check_reporter::init(...)'
            istype(message_provider, Mapping, ctx, 'message_provider must be a mapping')
            not_empty(
                message_provider, ctx,
                'message_provider must not be empty (key and value must be strings)'
            )
            self._message_provider = MappingProxyType(message_provider)
        else:
            self._message_provider = self._DEFAULT_MESSAGES

    def build_message(self, data: CheckReporterData) -> str:
        '''
            Builds a final message.

            :param data: Data to be formatted.
            :return: Formatted message report.
            :exceptions:
                | ATSValueError: Data must be provided and have proper values.
                | ATSTypeError:  Data must be an instance of CheckReporterData
                |                and its attributes must be instances of their
                |                respective types.
        '''
        CheckReporterValidator.validate(data)
        message: str = data.context
        err_set: set[int] = set(data.err_indices)

        param_fmt: str = self._message_provider.get(
            'param_entry',
            self._DEFAULT_MESSAGES['param_entry']
        )
        wrong_type_msg: str = self._message_provider.get(
            'wrong_type',
            self._DEFAULT_MESSAGES['wrong_type']
        )
        fmt_err_msg: str = self._message_provider.get(
            'format_wrong_during_checking_parameters_meta',
            self._DEFAULT_MESSAGES['format_wrong_during_checking_parameters_meta']
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
            Returns check reporter as string representation.

            :return: Check reporter as string representation.
            :exceptions: None.
        '''
        return to_str(self)
