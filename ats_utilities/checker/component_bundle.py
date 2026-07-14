# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle dataclass for dependency group simplification.
    Encapsulates checker components to minimize constructor overhead.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.type.type_validator import TypeValidator
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.format.format_validator import FormatValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.context.context_provider import ContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.reporter.check_reporter import CheckReporter
from ats_utilities.factory_component import validate_component
from ats_utilities.factory_type import check_type
from ats_utilities.factory_value import require_not_none


__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class CheckerComponentBundle:
    '''
        Defines component bundle dataclass for dependency group simplification.
        Encapsulates checker components to minimize constructor overhead.

        It defines:

            :attributes:
                | format_validator - Validator for parameters format (default None).
                | type_validator - Validator for parameters type (default None).
                | context_provider - Provider for call context (default None).
                | check_reporter - Formatter for message reports (default None).
            :methods:
                | __post_init__ - Post-initialization hook to set up default components if not provided.
                | validate - Validates that CheckerComponentBundle is valid (can be called after merge).
                | merge - Merges non-None values from another CheckerComponentBundle into this one.
                | to_dict - Converts the CheckerComponentBundle instance to a dictionary.
    '''

    format_validator: IFormatValidator | None = None
    type_validator: ITypeValidator | None = None
    context_provider: IContextProvider | None = None
    check_reporter: ICheckReporter | None = None

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to set up default validators and providers.

            :exceptions:
                | ATSTypeError: Format vcheck must be an instance of IFormatValidator.
                | ATSTypeError: Type vcheck must be an instance of ITypeValidator.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
        '''
        if self.format_validator is None:
            self.format_validator = FormatValidator()
            validate_component(self.format_validator, IFormatValidator, r'format_validator must be an IFormatValidator instance')

        if self.type_validator is None:
            self.type_validator = TypeValidator()
            validate_component(self.type_validator, ITypeValidator, r'type_validator must be an ITypeValidator instance')

        if self.context_provider is None:
            self.context_provider = ContextProvider()
            validate_component(self.context_provider, IContextProvider, r'context_provider must be an IContextProvider instance')

        if self.check_reporter is None:
            self.check_reporter = CheckReporter()
            validate_component(self.check_reporter, ICheckReporter, r'check_reporter must be an ICheckReporter instance')

    def validate(self) -> None:
        '''
            Validates that CheckerComponentBundle is valid (can be called after merge).
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format vcheck must be provided.
                | ATSValueError: Type vcheck must be provided.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
                | ATSTypeError: Format vcheck must be an instance of IFormatValidator.
                | ATSTypeError: Type vcheck must be an instance of ITypeValidator.
        '''
        require_not_none(self.context_provider, r'context provider must be provided')
        require_not_none(self.check_reporter, r'check reporter must be provided')
        require_not_none(self.format_validator, r'format vcheck must be provided')
        require_not_none(self.type_validator, r'type vcheck must be provided')
        check_type(self.context_provider, IContextProvider, r'context provider must be an instance of IContextProvider')
        check_type(self.check_reporter, ICheckReporter, r'check reporter must be an instance of ICheckReporter')
        check_type(self.format_validator, IFormatValidator, r'format vcheck must be an instance of IFormatValidator')
        check_type(self.type_validator, ITypeValidator, r'type vcheck must be an instance of ITypeValidator')

    def merge(self, other: CheckerComponentBundle) -> None:
        '''
            Merges non-None values from another CheckerComponentBundle into this one.

            :param other: Another CheckerComponentBundle to merge into this one.
            :type other: <CheckerComponentBundle>
            :exceptions:
                | ATSValueError: Other CheckerComponentBundle must be provided.
                | ATSTypeError: Other must be a CheckerComponentBundle instance.
        '''
        require_not_none(other, r'other CheckerComponentBundle must be provided')
        check_type(other, CheckerComponentBundle, r'other must be a CheckerComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the CheckerComponentBundle instance to a dictionary.

            :return: Dictionary representation of the CheckerComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }

