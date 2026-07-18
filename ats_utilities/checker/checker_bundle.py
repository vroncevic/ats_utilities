# -*- coding: UTF-8 -*-

'''
Module
    checker_bundle.py
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
    Encapsulates checker runtime components for simplification of CheckerBundle creation.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class CheckerBundle:
    '''
        Encapsulates checker runtime components for simplification of CheckerBundle creation.

        It defines:

            :attributes:
                | format_validator - Validator for parameters format.
                | type_validator - Validator for parameters type.
                | context_provider - Provider for call context.
                | check_reporter - Formatter for message reports.
            :methods:
                | __post_init__ - Post-initialization hook to validate checker bundle.
                | validate - Validates checker bundle.
                | to_dict - Converts checker bundle instance to a dictionary.
    '''

    format_validator: IFormatValidator
    type_validator: ITypeValidator
    context_provider: IContextProvider
    check_reporter: ICheckReporter

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate checker bundle.

            :exceptions:
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format mcheck must be provided.
                | ATSValueError: Type mcheck must be provided.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
                | ATSTypeError: Format mcheck must be an instance of IFormatValidator.
                | ATSTypeError: Type mcheck must be an instance of ITypeValidator.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates checker bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format mcheck must be provided.
                | ATSValueError: Type mcheck must be provided.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
                | ATSTypeError: Format mcheck must be an instance of IFormatValidator.
                | ATSTypeError: Type mcheck must be an instance of ITypeValidator.
        '''
        not_none(self.context_provider, r'context provider must be provided')
        not_none(self.check_reporter, r'check reporter must be provided')
        not_none(self.format_validator, r'format mcheck must be provided')
        not_none(self.type_validator, r'type mcheck must be provided')
        istype(self.context_provider, IContextProvider, r'context provider must be an instance of IContextProvider')
        istype(self.check_reporter, ICheckReporter, r'check reporter must be an instance of ICheckReporter')
        istype(self.format_validator, IFormatValidator, r'format mcheck must be an instance of IFormatValidator')
        istype(self.type_validator, ITypeValidator, r'type mcheck must be an instance of ITypeValidator')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts checker bundle instance to a dictionary.

            :return: Dictionary representation of the checker bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
