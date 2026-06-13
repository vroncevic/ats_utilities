# -*- coding: UTF-8 -*-

'''
Module
    iats_checker.py
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
    Defines abstract class IATSChecker with attribute(s) and method(s).
    Creates an interface for ATSChecker implementations.
'''

from abc import ABC, abstractmethod
from typing import Any, ClassVar, List, Tuple, Optional, TypeAlias, Protocol
from enum import Enum, EnumMeta

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Validation resut type: (error message report, error id)
ValidationResult: TypeAlias = Tuple[str, int]

# Specification for parameters: [(param name, param value), ...]
ParametersSpecs: TypeAlias = List[Tuple[str, Any]]


class ErrorChecker(int, Enum):
    '''
        Defines class ErrorChecker with attribute(s) and method(s).
        Marks error types for the ATSChecker.

        It defines:

            :attributes:
                | NO_ERROR - Marks no param error report (0).
                | TYPE_ERROR - Marks type param error report (1).
                | FORMAT_ERROR - Marks wrong format error report (2).
            :methods: None
    '''
    NO_ERROR = 0
    TYPE_ERROR = 1
    FORMAT_ERROR = 2


class ErrorCheckerProtocol(Protocol):
    '''
        Defines class ErrorCheckerProtocol with attribute(s) and method(s).
        Protocol for error types for the ATSChecker.

        It defines:

            :attributes:
                | NO_ERROR - Marks no param error report (0).
                | TYPE_ERROR - Marks type param error report (1).
                | FORMAT_ERROR - Marks wrong format error report (2).
            :methods: None
    '''
    NO_ERROR: ClassVar[int]
    TYPE_ERROR: ClassVar[int]
    FORMAT_ERROR: ClassVar[int]


class IATSChecker(ABC):
    '''
        Defines abstract class IATSChecker with attribute(s) and method(s).
        Creates an interface for ATSChecker implementations.

        It defines:

            :attributes:
                | ERRORS - Marks error types for message reports (0 | 1 | 2).
            :methods:
                | validate_parameters - Validates parameters for method(s) or function(s) (abstract).
    '''

    ERRORS: ClassVar[EnumMeta] = ErrorChecker

    @abstractmethod
    def validate_parameters(self, parameters: Optional[ParametersSpecs]) -> ValidationResult:
        '''
            Validates parameters for a method(s) or function(s).

            :param parameters: Specification for parameters
            :type parameters: <Optional[ParametersSpecs]>
            :return: tuple of error message report and error id
            :rtype: <ValidationResult>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method validate_parameters() must be implement")
