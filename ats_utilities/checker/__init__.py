# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates API fo checking parameters for object methods and functions.
'''

from inspect import stack
from typing import Any, List, Tuple, OrderedDict
from collections import OrderedDict as OrderedDictionary

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSChecker:
    '''
        Defines class ATSChecker with attribute(s) and method(s).
        Creates API fo checking parameters for object methods and functions.
        Mechanism for checking function/method parameters (type/value).

        It defines:

            :attributes:
                | NO_ERROR - No error, error id (0).
                | TYPE_ERROR - Type param error id (1).
                | VALUE_ERROR - Value param error id (2).
                | FORMAT_ERROR - Wrong format error id (3).
                | _start_message - Start segment of usage message.
                | _list_of_params - List of parameters for method/function.
                | _error_type - List of mapped errors.
                | _error_type_index - Error type index.
                | _error_value_index - Error value index.
            :methods:
                | __init__ - Initial ATSChecker constructor.
                | collect_params - Collect all parameters in one list.
                | usage_message - Prepare usage message for method/function.
                | check_types - Check parameters (types) for method/function.
                | check_values - Check parameters (values) for method/function.
                | priority_error - Set priority error id (TYPE_ERROR).
                | check_params - Check parameters for method/function.
    '''

    NO_ERROR = 0
    TYPE_ERROR = 1
    VALUE_ERROR = 2
    FORMAT_ERROR = 3

    def __init__(self) -> None:
        '''
            Initial ATSChecker constructor.

            :exceptions: None
        '''
        self._start_message: str | None = None
        self._list_of_params: List[str] = []
        self._error_type: List[int] = [0, 0, 0]
        self._error_type_index: List[int] = []
        self._error_value_index: List[int] = []

    def collect_params(
        self, params_description: OrderedDict[str, Any]
    ) -> bool:
        '''
            Collect all parameters in one list.

            :param params_description: Description for parameters
            :type params_description: <OrderedDict[str, Any]>
            :return: True (collected) | False (failed to collect)
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not params_description]):
            self._error_type[2] = self.FORMAT_ERROR
            return False
        for exp_type, inst in params_description.items():
            pname: str = exp_type.split(sep=':')[1]
            ptype: str = exp_type.split(sep=':')[0]
            self._list_of_params.append(
                f'\n    expected {pname} <{ptype}> object at {hex(id(inst))}'
            )
        return True

    def usage_message(self) -> str | None:
        '''
            Prepare usage message for method/function.

            :return: Usage message for method/function | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        message: str | None = self._start_message
        if bool(self._list_of_params):
            for index, param in enumerate(self._list_of_params):
                message = f'{message} {param}'
                if bool(self._error_type_index):
                    if index in set(self._error_type_index):
                        message = f'{message} wrong type'
                if bool(self._error_value_index):
                    if index in set(self._error_value_index):
                        message = f'{message} wrong value'
        return message

    def check_types(self, params_description: OrderedDict[str, Any]) -> bool:
        '''
            Check parameters (types) for method/function.

            :param params_description: Description for parameters
            :type params_description: <OrderedDict[str, Any]>
            :return: True (types ok) | False (types are not ok)
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not bool(params_description)]):
            self._error_type[2] = self.FORMAT_ERROR
            return False
        for index, (exp_type, inst) in enumerate(params_description.items()):
            param_typ_name: list[str] = exp_type.split(sep=':')
            if len(param_typ_name) == 2:
                if type(inst).__name__ != param_typ_name[0]:
                    self._error_type[0] = self.TYPE_ERROR
                    self._error_type_index.append(index)
            else:
                self._error_type[2] = self.FORMAT_ERROR
                return False
        return True

    def check_values(self, params_description: OrderedDict[str, Any]) -> bool:
        '''
            Check parameters (values) for method/function.

            :param params_description: Description for parameters
            :type params_description: <OrderedDict[str, Any]>
            :return: True (values are ok) | False (values are not ok)
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not bool(params_description)]):
            self._error_type[2] = self.FORMAT_ERROR
            return False
        for index, inst in enumerate(params_description.values()):
            if inst is None:
                self._error_type[1] = self.VALUE_ERROR
                self._error_value_index.append(index)
            any_base_type: bool = any([
                isinstance(inst, dict), isinstance(inst, list),
                isinstance(inst, tuple), isinstance(inst, set),
                isinstance(inst, frozenset), isinstance(inst, bytearray),
                isinstance(inst, bytes)
            ])
            if any_base_type:
                if not bool(inst):
                    self._error_type[1] = self.VALUE_ERROR
                    self._error_value_index.append(index)
        return True

    def priority_error(self) -> int | None:
        '''
            Set priority error id (TYPE_ERROR).

            :return: Priority error id (0 | 1 | 2 | 3) | None
            :rtype: <int> | <NoneType>
            :exceptions: None
        '''
        priority_error_id: int | None = None
        if self._error_type[2] == self.FORMAT_ERROR:
            return self.FORMAT_ERROR
        if self._error_type[1] == self.VALUE_ERROR:
            priority_error_id = self.VALUE_ERROR
        if self._error_type[0] == self.TYPE_ERROR:
            priority_error_id = self.TYPE_ERROR
        if all(error_type == 0 for error_type in self._error_type):
            priority_error_id = self.NO_ERROR
        return priority_error_id

    def check_params(
        self, params_description: List[Tuple[str, Any]]
    ) -> tuple[str | None, int | None]:
        '''
            Check parameters for method/function.

            :param params_description: Description for parameters
            :type params_description: <List[Tuple[str, Any]]>
            :return: usage message, status (0 | 1 | 2 | 3)
            :rtype: <str> | <NoneType>, <int> | <NoneType>
            :exceptions: None
        '''
        func: str = stack()[1][3]
        module: str = stack()[1][1]
        self._start_message = f'\nmod: {module}\n  def: {func}()'
        fail_any_check: bool = any([
            not self.collect_params(OrderedDictionary(params_description)),
            not self.check_types(OrderedDictionary(params_description)),
            not self.check_values(OrderedDictionary(params_description))
        ])
        message: str | None = self.usage_message()
        error_id: int | None = self.priority_error()
        if any([error_id is None, fail_any_check]):
            message = f'{message} format wrong during checking params'
            error_id = self.FORMAT_ERROR
        return message, error_id
