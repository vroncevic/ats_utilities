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
    Defines abstract class IChecker with attribute(s) and method(s).
    Creates an interface for Checker and other checker implementations.
'''

from abc import ABC, abstractmethod
from typing import Any, ClassVar
from enum import Enum, EnumMeta

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Validation resut type: (error message report, error id)
type ValidationResult = tuple[str, int]

# Specification for parameters: [(param name, param value), ...]
type ParametersSpecs = list[tuple[str, Any]]


class ErrorChecker(int, Enum):
    '''
        Defines class ErrorChecker with attribute(s).
        Marks error types for the Checker.

        It defines:

            :attributes:
                | NO_ERROR - Marks no param error report (0).
                | TYPE_ERROR - Marks type param error report (1).
                | FORMAT_ERROR - Marks wrong format error report (2).
            :methods: None.    '''
    NO_ERROR = 0
    TYPE_ERROR = 1
    FORMAT_ERROR = 2


class IChecker(ABC):
    '''
        Defines abstract class IChecker with attribute(s) and method(s).
        Creates an interface for Checker and other checker implementations.

        It defines:

            :attributes:
                | ERRORS - Marks error types for message reports (0 | 1 | 2).
            :methods:
                | validates_parameters - Validates parameters for method(s) or function(s).
                | is_initialized - Checks if checker component is initialized.
                | __str__ - Returns the checker as string representation.
    '''

    ERRORS: ClassVar[EnumMeta] = ErrorChecker

    @abstractmethod
    def validates_parameters(self, parameters: ParametersSpecs | None) -> ValidationResult:
        '''
            Validates parameters for a method(s) or function(s).

            :param parameters: Specification for parameters
            :type parameters: <ParametersSpecs | None>
            :return: Tuple of error message report and error id
            :rtype: <ValidationResult>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if checker component is initialized.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        raise NotImplementedError('Method is_initialized() must be implemented.')

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the checker as string representation.

            :return: The checker as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
