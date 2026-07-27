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

from ats_utilities.checker.setup.types import (
    Parameters, ParametersMeta, Result, CheckerErrorType
)
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.validator import CheckerValidator
from ats_utilities.checker.reporter.data import CheckReporterData
from ats_utilities.utils.reflection import to_str
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class Checker:
    '''
        Defines class Checker with attribute(s) and method(s).
        Concrete implementation of the parameter(s) checker.
        Mechanism for parameters checking (methods/functions).

        It defines:

            :attributes:
                | _is_initialized - Indicates if the checker component is initialized (default False).
                | _format_validator - Validator for parameters format (default FormatValidator).
                | _type_validator - Validator for parameters type (default TypeValidator).
                | _context_provider - Provider for call context (default ContextProvider).
                | _check_reporter - Formatter for message reports (default CheckReporter).
            :methods:
                | __init__ - Initializes Checker constructor.
                | get_bundle - Gets current checker configuration bundle.
                | update_bundle - Updates checker configuration bundle.
                | get_format_validator - Returns the format validator used in validation of parameters.
                | get_type_validator - Returns the type validator used in validation of parameters.
                | get_context_provider - Returns the context provider used in validation of parameters.
                | get_check_reporter - Returns the check reporter used in validation of parameters.
                | validates_parameters - Validates parameter(s) used by method(s) or function(s).
                | is_initialized - Checks if checker component is initialized.
                | __str__ - Returns the checker as string representation.
    '''

    _is_initialized: bool
    _format_validator: IFormatValidator
    _type_validator: ITypeValidator
    _context_provider: IContextProvider
    _check_reporter: ICheckReporter

    def __init__(self, own: CheckerBundle) -> None:
        '''
            Initializes Checker constructor.

            :param own: Checker bundle with components.
            :exceptions:
                | ATSValueError: Checker bundle must be provided and have proper values.
                | ATSTypeError:  Checker bundle must be an instance of CheckerBundle
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        CheckerValidator.validate(own)
        self._format_validator = own.format_validator
        self._type_validator = own.type_validator
        self._context_provider = own.context_provider
        self._check_reporter = own.check_reporter
        self._is_initialized = True

    def get_bundle(self) -> CheckerBundle:
        '''
            Gets current checker configuration bundle.

            :return: Checker configuration bundle.
            :exceptions: None.
        '''
        return CheckerBundle(
            format_validator=self._format_validator,
            type_validator=self._type_validator,
            context_provider=self._context_provider,
            check_reporter=self._check_reporter
        )

    def update_bundle(self, bundle: CheckerBundle) -> bool:
        '''
            Updates checker configuration bundle.

            :param bundle: Checker configuration bundle.
            :return: True if configuration was successfully updated, False otherwise.
            :exceptions: None.
        '''
        try:
            CheckerValidator.validate(bundle)
            self._format_validator = bundle.format_validator
            self._type_validator = bundle.type_validator
            self._context_provider = bundle.context_provider
            self._check_reporter = bundle.check_reporter

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def get_format_validator(self) -> IFormatValidator:
        '''
            Returns the format validator used in validation of parameters.

            :return: Format validator used in validation of parameters.
            :exceptions: None.
        '''
        return self._format_validator

    def get_type_validator(self) -> ITypeValidator:
        '''
            Returns the type validator used in validation of parameters.

            :return: Type validator used in validation of parameters.
            :exceptions: None.
        '''
        return self._type_validator

    def get_context_provider(self) -> IContextProvider:
        '''
            Returns the context provider used in validation of parameters.

            :return: Context provider used in validation of parameters.
            :exceptions: None.
        '''
        return self._context_provider

    def get_check_reporter(self) -> ICheckReporter:
        '''
            Returns the check reporter used in validation of parameters.

            :return: Check reporter used in validation of parameters.
            :exceptions: None.
        '''
        return self._check_reporter

    def validates_parameters(self, parameters: Parameters) -> Result:
        '''
            Validates parameters used by method(s) or function(s).

            :param parameters: Specification of parameters.
            :return: Result of validation (message report and error id).
            :exceptions: None.
        '''
        context: str = self._context_provider.get_context()
        parameters_meta: list[ParametersMeta] = []
        err_indices: list[int] = []
        error_id: int = CheckerErrorType.NO_ERROR

        if parameters is None:
            msg: str = f'{context} format wrong during checking parameters'

            try:
                msg = self._check_reporter.build_message(
                    CheckReporterData(
                        context=context,
                        parameters_meta=(),
                        err_indices=(),
                        is_fmt_err=True
                    )
                )

            except (ATSValueError, ATSTypeError):
                pass

            return msg, CheckerErrorType.FORMAT_ERROR

        is_fmt_err: bool = False

        for index, (exp_type, inst) in enumerate(parameters):

            try:
                if not self._format_validator.is_valid(exp_type):
                    is_fmt_err = True
                    error_id = CheckerErrorType.FORMAT_ERROR
                    break

                ptype, pname = self._format_validator.split(exp_type)
                parameters_meta.append((pname, ptype, inst))

            except (ATSValueError, ATSTypeError):
                is_fmt_err = True
                error_id = CheckerErrorType.FORMAT_ERROR
                break

            try:
                if not self._type_validator.is_match(inst, ptype):
                    err_indices.append(index)

                    if error_id == CheckerErrorType.NO_ERROR:
                        error_id = CheckerErrorType.TYPE_ERROR

            except (ATSValueError, ATSTypeError):
                err_indices.append(index)

                if error_id == CheckerErrorType.NO_ERROR:
                    error_id = CheckerErrorType.TYPE_ERROR

        report_msg: str = f'{context} error during building check report'

        try:
            report_msg = self._check_reporter.build_message(
                CheckReporterData(
                    context=context,
                    parameters_meta=parameters_meta,
                    err_indices=err_indices,
                    is_fmt_err=is_fmt_err
                )
            )
        except (ATSValueError, ATSTypeError):
            pass

        return report_msg, error_id

    def is_initialized(self) -> bool:
        '''
            Checks if checker component is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    def __str__(self) -> str:
        '''
            Returns checker as string representation.

            :return: Checker as string representation.
            :exceptions: None.
        '''
        return to_str(self)
