# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for checker dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.checker.setup.dependencies import CheckerDependencies
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerDependenciesValidator(IDependenciesValidator[CheckerDependencies]):
    '''
        Validator for checker dependencies.

        It defines:

            :methods:
                | validate - Validates checker dependencies instance.
    '''

    @classmethod
    @override
    def validate(cls, dependencies: CheckerDependencies) -> None:
        '''
            Validates checker dependencies instance.

            :param dependencies: Checker dependencies instance to be validated.
            :type dependencies: CheckerDependencies
            :exceptions:
                | ATSValueError: Dependencies must be provided.
                | ATSTypeError: Dependencies must be a Mapping.
                | ATSTypeError: Format validator must be an instance of IFormatValidator.
                | ATSTypeError: Type validator must be an instance of ITypeValidator.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
        '''
        ctx: str = r'checker_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, r'dependencies must be provided')
        istype(dependencies, Mapping, ctx, r'dependencies must be a Mapping')

        format_validator = dependencies.get('format_validator')

        if format_validator is not None:
            istype(format_validator, IFormatValidator, ctx, r'format validator must be an instance of IFormatValidator')

        type_validator = dependencies.get('type_validator')

        if type_validator is not None:
            istype(type_validator, ITypeValidator, ctx, r'type validator must be an instance of ITypeValidator')

        context_provider = dependencies.get('context_provider')

        if context_provider is not None:
            istype(context_provider, IContextProvider, ctx, r'context provider must be an instance of IContextProvider')

        check_reporter = dependencies.get('check_reporter')

        if check_reporter is not None:
            istype(check_reporter, ICheckReporter, ctx, r'check reporter must be an instance of ICheckReporter')
