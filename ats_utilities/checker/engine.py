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
    Defines class ATSChecker with attribute(s) and method(s).
    Concrete implementation of the ATS parameter(s) checker.
'''

from typing import ClassVar, List, Optional
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.checker.ichecker import IChecker, ErrorChecker, ValidationResult, ParametersSpecs
from ats_utilities.checker.itype_validator import IATSTypeValidator
from ats_utilities.checker.type_validator import ATSTypeValidator
from ats_utilities.checker.iformat_validator import IATSFormatValidator
from ats_utilities.checker.format_validator import ATSFormatValidator
from ats_utilities.checker.icontext_provider import IATSContextProvider
from ats_utilities.checker.context_provider import ATSContextProvider
from ats_utilities.checker.icheck_reporter import IATSCheckReporter, ParamMetadata
from ats_utilities.checker.check_reporter import ATSCheckReporter
from ats_utilities.checker.component_bundle import ATSCheckerComponentBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSChecker(IChecker):
    '''
        Defines class ATSChecker with attribute(s) and method(s).
        Concrete implementation of the ATS parameter(s) checker.

        It defines:

            :attributes:
                | ERRORS - Marks error types for message reports.
                | __format_validator - Validator for parameters format (default ATSFormatValidator).
                | __type_validator - Validator for parameters type (default ATSTypeValidator).
                | __context_provider - Provider for call context (default ATSContextProvider).
                | __check_reporter - Formatter for message reports (default ATSCheckReporter).
            :methods:
                | __init__ - Initials ATSChecker constructor.
                | validates_parameters - Validates parameter(s) for method(s) or function(s).
                | __str__ - Returns the string representation of ATSChecker.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(self, component_bundle: Optional[ATSCheckerComponentBundle] = None) -> None:
        '''
            Initials ATSChecker constructor.

            :param component_bundle: Bundle with components | None
            :type component_bundle: <Optional[ATSCheckerComponentBundle]>
            :exceptions: ATSTypeError by validate_component()
        '''
        # No dependency injection then use default ones.
        components: ATSCheckerComponentBundle = component_bundle or ATSCheckerComponentBundle()
        self.__format_validator: IATSFormatValidator = make_component(components.format_validator, ATSFormatValidator, None)
        validate_component(self.__format_validator, ATSFormatValidator, "ATSFormatValidator")
        self.__type_validator: IATSTypeValidator = make_component(components.type_validator, ATSTypeValidator, None)
        validate_component(self.__type_validator, ATSTypeValidator, "ATSTypeValidator")
        self.__context_provider: IATSContextProvider = make_component(components.context_provider, ATSContextProvider, None)
        validate_component(self.__context_provider, ATSContextProvider, "ATSContextProvider")
        self.__check_reporter: IATSCheckReporter = make_component(components.check_reporter, ATSCheckReporter, None)
        validate_component(self.__check_reporter, ATSCheckReporter, "ATSCheckReporter")

    def validates_parameters(self, parameters: Optional[ParametersSpecs]) -> ValidationResult:
        '''
            Validates parameters for method(s) or function(s).

            :param parameters: Specification for parameters | None
            :type parameters: <Optional[ParametersSpecs]>
            :return: Tuple of error message report and error id
            :rtype: <ValidationResult>
            :exceptions: None
        '''
        context: str = self.__context_provider.get_context()
        params_meta: List[ParamMetadata] = []
        err_indices: List[int] = []
        error_id: int = self.ERRORS.NO_ERROR

        if parameters is None:
            return self.__check_reporter.build_message_format(context, [], [], True), self.ERRORS.FORMAT_ERROR

        is_fmt_err: bool = False
        for index, (exp_type, inst) in enumerate(parameters):

            if not self.__format_validator.is_valid(exp_type):
                is_fmt_err = True
                error_id = self.ERRORS.FORMAT_ERROR
                break

            ptype: Optional[str] = None
            pname: Optional[str] = None

            ptype, pname = self.__format_validator.split(exp_type)
            params_meta.append((pname, ptype, inst))

            if not self.__type_validator.is_match(inst, ptype):
                err_indices.append(index)

                if error_id == self.ERRORS.NO_ERROR:
                    error_id = self.ERRORS.TYPE_ERROR

        return self.__check_reporter.build_message_format(
            context, params_meta, err_indices, is_fmt_err
        ), error_id

    def __str__(self) -> str:
        '''
            Returns the string representation of ATSChecker.

            :return: String representation of ATSChecker instance
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
