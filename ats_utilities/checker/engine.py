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
'''

from __future__ import annotations

from typing import ClassVar, override
from sys import stderr

from ats_utilities.checker.ichecker import IChecker, ErrorChecker, ValidationResult, ParametersSpecs
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.component_bundle import CheckerComponentBundle
from ats_utilities.checker.reporter.checker_reporter_bundle import CheckerReporterBundle, ParamMetadata
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.factory_class import cls_name, to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Checker(IChecker):
    '''
        Defines class Checker with attribute(s) and method(s).
        Concrete implementation of the parameter(s) checker.
        Mechanism for application, tool, or script parameters checker.

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

    def __init__(self, component_bundle: CheckerComponentBundle | None = None) -> None:
        '''
            Initializes Checker constructor.

            :param component_bundle: Bundle with components | None.
            :type component_bundle: <CheckerComponentBundle | None>
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            # No dependency injection then use default ones.
            components: CheckerComponentBundle = component_bundle or CheckerComponentBundle()
            self._format_validator = components.format_validator
            self._type_validator = components.type_validator
            self._context_provider = components.context_provider
            self._check_reporter = components.check_reporter

            # All components initialized successfully.
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            stderr.write(f"\x1b[31m{cls_name(self)} {exc}\x1b[0m\n")

        except Exception as exc:
            stderr.write(f"\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m\n")

    @override
    def validates_parameters(self, parameters: ParametersSpecs) -> ValidationResult:
        '''
            Validates parameters for method(s) or function(s).

            :param parameters: Specification for parameters.
            :type parameters: <ParametersSpecs>
            :return: Tuple of error message report and error id.
            :rtype: <ValidationResult>
            :exceptions: None.
        '''
        context: str = self._context_provider.get_context()
        params_meta: list[ParamMetadata] = []
        err_indices: list[int] = []
        error_id: int = self.ERRORS.NO_ERROR

        if parameters is None:
            return (
                self._check_reporter.build_message_format(
                    CheckerReporterBundle(
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
            CheckerReporterBundle(
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

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the Checker as string representation.

            :return: The Checker as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
