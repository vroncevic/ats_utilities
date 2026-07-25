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
from typing import ClassVar, override
from types import MappingProxyType

from ats_utilities.utils.setup.ikeys import IKeys
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerKeys(IKeys[str, type]):
    '''
        Runtime components and interface constraints for checker bundle.

        It defines:

            :attributes:
                | FORMAT_VALIDATOR: Format validator interface constant.
                | TYPE_VALIDATOR: Type validator interface constant.
                | CONTEXT_PROVIDER: Context provider interface constant.
                | CHECK_REPORTER: Check reporter interface constant.
                | SEPARATOR: Separator option constant.
                | ABSTRACT_TYPES: Abstract types option constant.
                | STACK_INDEX_CALLER: Stack index caller option constant.
                | MESSAGES_PROVIDER: Messages provider option constant.
            :methods:
                | get_dependency_to_type - Returns mapping of checker dependencies to their types.
                | get_option_to_type - Returns mapping of checker options to their types.
    '''

    # Dependency Keys
    FORMAT_VALIDATOR: ClassVar[str] = 'format_validator'
    TYPE_VALIDATOR: ClassVar[str] = 'type_validator'
    CONTEXT_PROVIDER: ClassVar[str] = 'context_provider'
    CHECK_REPORTER: ClassVar[str] = 'check_reporter'

    # Option Keys
    SEPARATOR: ClassVar[str] = 'separator'
    ABSTRACT_TYPES: ClassVar[str] = 'abstract_types'
    STACK_INDEX_CALLER: ClassVar[str] = 'stack_index_caller'
    MESSAGES_PROVIDER: ClassVar[str] = 'messages_provider'

    @classmethod
    @override
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of checker dependencies to their types.

            :return: Mapping of checker dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.FORMAT_VALIDATOR: IFormatValidator,
            cls.TYPE_VALIDATOR: ITypeValidator,
            cls.CONTEXT_PROVIDER: IContextProvider,
            cls.CHECK_REPORTER: ICheckReporter,
        })

    @classmethod
    @override
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of checker options to their types.

            :return: Mapping of checker options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.SEPARATOR: str,
            cls.ABSTRACT_TYPES: Mapping,
            cls.STACK_INDEX_CALLER: int,
            cls.MESSAGES_PROVIDER: Mapping,
        })
