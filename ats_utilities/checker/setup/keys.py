# -*- coding: UTF-8 -*-

'''
Module
    keys.py
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
    Runtime components and interface constraints for checker bundle.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar
from types import MappingProxyType

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


class CheckerKeys:
    '''
        Runtime components and interface constraints for checker bundle.

        It defines:

            :attributes:
                | DEPENDENCY_FORMAT_VALIDATOR: Format validator interface constant.
                | DEPENDENCY_TYPE_VALIDATOR: Type validator interface constant.
                | DEPENDENCY_CONTEXT_PROVIDER: Context provider interface constant.
                | DEPENDENCY_CHECK_REPORTER: Check reporter interface constant.
                | OPTION_SEPARATOR: Separator option constant.
                | OPTION_ABSTRACT_TYPES: Abstract types option constant.
                | OPTION_STACK_INDEX_CALLER: Stack index caller option constant.
                | OPTION_MESSAGES_PROVIDER: Messages provider option constant.
            :methods:
                | get_dependency_to_type - Returns mapping of checker dependencies to their types.
                | get_option_to_type - Returns mapping of checker options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_FORMAT_VALIDATOR: ClassVar[str] = 'format_validator'
    DEPENDENCY_TYPE_VALIDATOR: ClassVar[str] = 'type_validator'
    DEPENDENCY_CONTEXT_PROVIDER: ClassVar[str] = 'context_provider'
    DEPENDENCY_CHECK_REPORTER: ClassVar[str] = 'check_reporter'

    # Option Keys
    OPTION_SEPARATOR: ClassVar[str] = 'separator'
    OPTION_ABSTRACT_TYPES: ClassVar[str] = 'abstract_types'
    OPTION_STACK_INDEX_CALLER: ClassVar[str] = 'stack_index_caller'
    OPTION_MESSAGES_PROVIDER: ClassVar[str] = 'messages_provider'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of checker dependencies to their types.

            :return: Mapping of checker dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_FORMAT_VALIDATOR: IFormatValidator,
            cls.DEPENDENCY_TYPE_VALIDATOR: ITypeValidator,
            cls.DEPENDENCY_CONTEXT_PROVIDER: IContextProvider,
            cls.DEPENDENCY_CHECK_REPORTER: ICheckReporter,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of checker options to their types.

            :return: Mapping of checker options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_SEPARATOR: str,
            cls.OPTION_ABSTRACT_TYPES: Mapping,
            cls.OPTION_STACK_INDEX_CALLER: int,
            cls.OPTION_MESSAGES_PROVIDER: Mapping,
        })
