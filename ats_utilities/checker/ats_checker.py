# -*- coding: UTF-8 -*-

'''
Module
    ats_checker.py
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
    Defines class ATSChecker with attribute(s) and method(s).
    Concrete implementation of the ATS parameter checker.
'''

from typing import ClassVar, List, Optional
from .iats_checker import (
    IATSChecker, ErrorChecker, ValidationResult, ParametersSpecs
)
from .itype_validator import ITypeValidator
from .iformat_validator import IFormatValidator
from .icontext_provider import IContextProvider
from .icheck_reporter import ICheckReporter, ParamMetadata
from .default_format_validator import DefaultFormatValidator
from .default_type_validator import DefaultTypeValidator
from .default_context_provider import DefaultContextProvider
from .default_check_reporter import DefaultCheckReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSChecker(IATSChecker):
    '''
        Defines class ATSChecker with attribute(s) and method(s).
        Concrete implementation of the ATS parameter checker.
        Creates an API for validating parameters for method(s) and function(s).
        Main class module for validating function(s) or method(s) parameters (type or format).

        It defines:

            :attributes:
                | ERRORS - Marks error types for message reports.
                | _format_validator - Validator for parameters format.
                | _type_validator - Validator for parameters type.
                | _context_provider - Provider for call context.
                | _check_reporter - Formatter for message reports.
            :methods:
                | __init__ - Initials ATSChecker constructor.
                | validate_parameters - Validates parameters for method(s) or function(s).
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        format_validator: Optional[IFormatValidator] = None,
        type_validator: Optional[ITypeValidator] = None,
        context_provider: Optional[IContextProvider] = None,
        check_reporter: Optional[ICheckReporter] = None
    ) -> None:
        '''
            Initials ATSChecker constructor.

            :param format_validator: Validator for parameters format
            :type format_validator: :class:`~ats_utilities.checker.iformat_validator.IFormatValidator`
            :param type_validator: Validator for parameters type
            :type type_validator: :class:`~ats_utilities.checker.itype_validator.ITypeValidator`
            :param context_provider: Provider for call context
            :type context_provider: :class:`~ats_utilities.checker.icontext_provider.IContextProvider`
            :param check_reporter: Formatter for message reports
            :type check_reporter: :class:`~ats_utilities.checker.icheck_reporter.ICheckReporter`cker.icheck_reporter.ICheckReporter`
            :exceptions: None
        '''
        # If no custom implementations are provided, use default ones.
        self._format_validator: IFormatValidator = format_validator or DefaultFormatValidator()
        self._type_validator: ITypeValidator = type_validator or DefaultTypeValidator()
        self._context_provider: IContextProvider = context_provider or DefaultContextProvider()
        self._check_reporter: ICheckReporter = check_reporter or DefaultCheckReporter()

    def validate_parameters(self, parameters: Optional[ParametersSpecs]) -> ValidationResult:
        '''
            Validates parameters for method(s) or function(s).

            :param parameters: Specification for parameters
            :type parameters: :class:`~ats_utilities.checker.iats_checker.ParametersSpecs` 
            :return: tuple of error message report and error id
            :rtype: <ValidationResult>
            :exceptions: None
        '''
        context = self._context_provider.get_context()
        params_meta: List[ParamMetadata] = []
        err_indices: List[int] = []
        error_id = self.ERRORS.NO_ERROR

        if parameters is None:
            return self._check_reporter.build_message_format(context, [], [], True), self.ERRORS.FORMAT_ERROR

        is_fmt_err = False
        for index, (exp_type, inst) in enumerate(parameters):

            if not self._format_validator.is_valid(exp_type):
                is_fmt_err = True
                error_id = self.ERRORS.FORMAT_ERROR
                break

            ptype, pname = self._format_validator.split(exp_type)
            params_meta.append((pname, ptype, inst))

            if not self._type_validator.is_match(inst, ptype):
                err_indices.append(index)

                if error_id == self.ERRORS.NO_ERROR:
                    error_id = self.ERRORS.TYPE_ERROR

        return self._check_reporter.build_message_format(
            context, params_meta, err_indices, is_fmt_err
        ), error_id
