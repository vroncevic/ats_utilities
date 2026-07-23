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
    Defines class Checker with attribute(s) and method(s).
    Concrete implementation of the parameter(s) checker.
    Mechanism for parameters checking (methods/functions).
'''

from __future__ import annotations

from typing import ClassVar, override

from ats_utilities.checker.ichecker import (
    IChecker, ErrorChecker, ValidationResult, ParametersSpecs
)
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.validator import CheckerValidator
from ats_utilities.checker.reporter.data import (
    CheckReporterData, ParamMetadata
)
from ats_utilities.utils.reflection import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Checker(IChecker):
    '''
        Defines class Checker with attribute(s) and method(s).
        Concrete implementation of the parameter(s) checker.
        Mechanism for parameters checking (methods/functions).

        It defines:

            :attributes:
                | ERRORS - Marks error types for message reports.
                | _is_initialized - Indicates if the checker component is initialized (default False).
                | _format_validator - Validator for parameters format (default FormatValidator).
                | _type_validator - Validator for parameters type (default TypeValidator).
                | _context_provider - Provider for call context (default ContextProvider).
                | _check_reporter - Formatter for message reports (default CheckReporter).
            :methods:
                | __init__ - Initializes Checker constructor.
                | validates_parameters - Validates parameter(s) for method(s) or function(s).
                | is_initialized - Checks if checker component is initialized.
                | __str__ - Returns the checker as string representation.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker
    _is_initialized: bool
    _format_validator: IFormatValidator
    _type_validator: ITypeValidator
    _context_provider: IContextProvider
    _check_reporter: ICheckReporter

    def __init__(self, own: CheckerBundle) -> None:
        '''
            Initializes Checker constructor.

            :param own: Bundle with components.
            :type own: CheckerBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format validator must be provided.
                | ATSValueError: Type validator must be provided.
                | ATSTypeError: Bundle must be an instance of CheckerBundle.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
                | ATSTypeError: Format validator must be an instance of IFormatValidator.
                | ATSTypeError: Type validator must be an instance of ITypeValidator.
        '''
        CheckerValidator.validate(own)
        self._format_validator = own.format_validator
        self._type_validator = own.type_validator
        self._context_provider = own.context_provider
        self._check_reporter = own.check_reporter
        self._is_initialized = True

    @override
    def validates_parameters(self, parameters: ParametersSpecs) -> ValidationResult:
        '''
            Validates parameters for method(s) or function(s).

            :param parameters: Specification for parameters.
            :type parameters: ParametersSpecs
            :return: Tuple of error message report and error id.
            :rtype: ValidationResult
            :exceptions:
                | ATSValueError: Check reporter data must be provided.
                | ATSTypeError: Check reporter data must be an instance of CheckReporterData.
                | ATSValueError: Context must be provided.
                | ATSValueError: Parameters metadata must be provided.
                | ATSValueError: Error indices must be provided.
                | ATSValueError: Is format error must be provided.
                | ATSTypeError: Context must be a string.
                | ATSTypeError: Parameters metadata must be a sequence of ParamMetadata.
                | ATSTypeError: Error indices must be a sequence of integers.
                | ATSTypeError: Is format error must be a boolean.
        '''
        context: str = self._context_provider.get_context()
        params_meta: list[ParamMetadata] = []
        err_indices: list[int] = []
        error_id: int = self.ERRORS.NO_ERROR

        if parameters is None:
            return (
                self._check_reporter.build_message_format(
                    CheckReporterData(
                        context=context,
                        parameters_meta=(),
                        err_indices=(),
                        is_fmt_err=True
                    )
                ),
                self.ERRORS.FORMAT_ERROR
            )

        is_fmt_err: bool = False
        for index, (exp_type, inst) in enumerate(parameters):

            if not self._format_validator.is_valid(exp_type):
                is_fmt_err = True
                error_id = self.ERRORS.FORMAT_ERROR
                break

            ptype: str | None = None
            pname: str | None = None

            ptype, pname = self._format_validator.split(exp_type)
            params_meta.append((pname, ptype, inst))

            if not self._type_validator.is_match(inst, ptype):
                err_indices.append(index)

                if error_id == self.ERRORS.NO_ERROR:
                    error_id = self.ERRORS.TYPE_ERROR

        return self._check_reporter.build_message_format(
            CheckReporterData(
                context=context,
                parameters_meta=params_meta,
                err_indices=err_indices,
                is_fmt_err=is_fmt_err
            )
        ), error_id

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if checker component is initialized.

            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the Checker as string representation.

            :return: The Checker as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
