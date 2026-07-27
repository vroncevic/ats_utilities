# -*- coding: UTF-8 -*-

'''
Module
    ichecker.py
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
    Defines abstract class IChecker with method(s).
    Provides an interface for checking parameters of method(s) or function(s).
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IChecker[ConfigType, ParametersSpecification, ValidationResult](Protocol):
    '''
        Defines abstract class IChecker with method(s).
        Provides an interface for checking parameters used by method(s) or function(s).

        It defines:

            :methods:
                | get_bundle - Gets current checker configuration bundle.
                | update_bundle - Updates checker configuration bundle.
                | get_format_validator - Returns the format validator used in validation of parameters.
                | get_type_validator - Returns the type validator used in validation of parameters.
                | get_context_provider - Returns the context provider used in validation of parameters.
                | get_check_reporter - Returns the check reporter used in validation of parameters.
                | validates_parameters - Validates parameters used by method(s) or function(s).
                | is_initialized - Checks if checker component is initialized.
                | __str__ - Returns checker as string representation.
    '''

    def get_bundle(self) -> ConfigType:
        '''
            Gets current checker configuration bundle.

            :return: Checker configuration bundle.
            :exceptions: None.
        '''
        ...

    def update_bundle(self, bundle: ConfigType) -> bool:
        '''
            Updates checker configuration bundle.

            :param bundle: Checker configuration bundle.
            :exceptions: None.
        '''
        ...

    def get_format_validator(self) -> IFormatValidator:
        '''
            Returns the format validator used in validation of parameters.

            :return: Format validator used in validation of parameters.
        '''
        ...

    def get_type_validator(self) -> ITypeValidator:
        '''
            Returns the type validator used in validation of parameters.

            :return: Type validator used in validation of parameters.
        '''
        ...

    def get_context_provider(self) -> IContextProvider:
        '''
            Returns the context provider used in validation of parameters.

            :return: Context provider used in validation of parameters.
        '''
        ...

    def get_check_reporter(self) -> ICheckReporter:
        '''
            Returns the check reporter used in validation of parameters.

            :return: Check reporter used in validation of parameters.
        '''
        ...

    def validates_parameters(self, parameters: ParametersSpecification) -> ValidationResult:
        '''
            Validates parameters used by method(s) or function(s).

            :param parameters: Specification of parameters.
            :return: Result of validation.
        '''
        ...

    def is_initialized(self) -> bool:
        '''
            Checks if checker component is initialized.

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns checker as string representation.

            :return: Checker as string representation.
        '''
        ...
