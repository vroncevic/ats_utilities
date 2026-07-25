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
    Defines abstract class IChecker with method(s).
    Provides an interface for checking parameters of method(s) or function(s).
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IChecker[ParametersSpecification, ValidationResult, ParameterFormat, SplitParameterResult](ABC):
    '''
        Defines abstract class IChecker with method(s).
        Provides an interface for checking parameters of method(s) or function(s).

        It defines:

            :methods:
                | validates_parameters - Validates parameters for method(s) or function(s).
                | is_initialized - Checks if checker component is initialized.
                | __str__ - Returns checker as string representation.
    '''

    @abstractmethod
    def validates_parameters(self, parameters: ParametersSpecification) -> ValidationResult:
        '''
            Validates parameters for a method(s) or function(s).

            :param parameters: Specification for parameters.
            :return: Result of validation.
        '''
        pass

    @abstractmethod
    def split_parameter(self, parameter: ParameterFormat) -> SplitParameterResult:
        '''
            Splits a single parameter specification item.

            :param parameter: Parameter specification item to be splitted.
            :return: Result of splitting parameter specification item.
        '''
        pass

    @abstractmethod
    def get_separator(self) -> str:
        '''
            Returns the separator character used in parameter specifications.

            :return: Separator character.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if checker component is initialized.

            :return: True if successfully, otherwise False.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns checker as string representation.

            :return: Checker as string representation.
        '''
        pass
