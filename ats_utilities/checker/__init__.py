# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates an API for checking parameters for methods and functions.
'''

from inspect import stack
from typing import Any, List, Tuple, OrderedDict, Optional, TypeAlias
from collections import OrderedDict as OrderedDictionary

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

CheckParams: TypeAlias = Tuple[Optional[str], Optional[int]]
ParamDesc: TypeAlias = List[Tuple[str, Any]]


class ATSChecker:
    '''
        Defines class ATSChecker with attribute(s) and method(s).
        Creates an API for checking parameters for methods and functions.
        Mechanism for checking function or method parameters (type or format).

        It defines:

            :attributes:
                | NO_ERROR - Marks no param error, error id (0).
                | TYPE_ERROR - Marks type param error, error id (1).
                | FORMAT_ERROR - Marks wrong format error, error id (2).
                | _start_message - Start segment of usage message.
                | _list_of_params - List of params for a method or function.
                | _error_type - List of mapped errors.
                | _error_type_index - Error type index.
            :methods:
                | __init__ - Initials ATSChecker constructor.
                | collect_params - Collects all params in one list.
                | usage_message - Prepares usage for method or function.
                | check_types - Checks params (types) for method or function.
                | priority_error - Sets priority error id (TYPE_ERROR).
                | check_params - Checks params for method or function.
    '''

    NO_ERROR: int = 0
    TYPE_ERROR: int = 1
    FORMAT_ERROR: int = 2

    def __init__(self) -> None:
        '''
            Initials ATSChecker constructor.

            :exceptions: None
        '''
        self._start_message: Optional[str] = None
        self._list_of_params: List[str] = []
        self._error_type: List[int] = [0, 0]
        self._error_type_index: List[int] = []

    def collect_params(self, params_desc: OrderedDict[str, Any]) -> bool:
        '''
            Collects all params in one list.

            :param params_desc: Description for params
            :type params_desc: <OrderedDict[str, Any]>
            :return: True (are collected) | False (failed to collect)
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not params_desc]):
            self._error_type[1] = self.FORMAT_ERROR
            return False
        for exp_type, inst in params_desc.items():
            pname: str = exp_type.split(sep=':')[1]
            ptype: str = exp_type.split(sep=':')[0]
            self._list_of_params.append(
                f'\n    expected {pname} <{ptype}> object at {hex(id(inst))}'
            )
        return True

    def usage_message(self) -> Optional[str]:
        '''
            Prepares usage for method or function.

            :return: Usage message for method or function | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        message: Optional[str] = self._start_message
        if bool(self._list_of_params):
            for index, param in enumerate(self._list_of_params):
                message = f'{message} {param}'
                if bool(self._error_type_index):
                    if index in set(self._error_type_index):
                        message = f'{message} wrong type'
        return message

    def check_types(self, params_desc: OrderedDict[str, Any]) -> bool:
        '''
            Checks params (types) for method or function.

            :param params_desc: Description for params
            :type params_desc: <OrderedDict[str, Any]>
            :return: True (type(s) is(are) ok) | False (type(s) is(are) not ok)
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not params_desc]):
            self._error_type[1] = self.FORMAT_ERROR
            return False
        for index, (exp_type, inst) in enumerate(params_desc.items()):
            param_type_name: List[str] = exp_type.split(sep=':')
            if len(param_type_name) == 2:
                if type(inst).__name__ != param_type_name[0]:
                    self._error_type[0] = self.TYPE_ERROR
                    self._error_type_index.append(index)
                    return False
            else:
                self._error_type[1] = self.FORMAT_ERROR
                return False
        return True

    def priority_error(self) -> Optional[int]:
        '''
            Sets priority error id (TYPE_ERROR).

            :return: Priority error id (0 | 1 | 2) | None
            :rtype: <Optional[int]>
            :exceptions: None
        '''
        priority_error_id: Optional[int] = None
        if self._error_type[1] == self.FORMAT_ERROR:
            return self.FORMAT_ERROR
        if self._error_type[0] == self.TYPE_ERROR:
            priority_error_id = self.TYPE_ERROR
        if all(error_type == 0 for error_type in self._error_type):
            priority_error_id = self.NO_ERROR
        return priority_error_id

    def check_params(self, params_desc: ParamDesc) -> CheckParams:
        '''
            Checks params for method or function.

            :param params_desc: Description for params
            :type params_desc: <ParamDesc>
            :return: error message, error id (0 | 1 | 2)
            :rtype: <CheckParams>
            :exceptions: None
        '''
        func: str = stack()[1][3]
        module: str = stack()[1][1]
        self._start_message = f'\nmod: {module}\n  def: {func}()'
        fail_any_check: bool = any([
            not self.collect_params(OrderedDictionary(params_desc)),
            not self.check_types(OrderedDictionary(params_desc))
        ])
        message: Optional[str] = self.usage_message()
        error_id: Optional[int] = self.priority_error()
        if any([error_id != 0, fail_any_check]):
            message = f'{message} format wrong during checking params'
        return message, error_id
