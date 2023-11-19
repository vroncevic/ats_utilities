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

import sys
from inspect import stack
from typing import Any, List, Tuple, OrderedDict
from collections import OrderedDict as OrderedDictionary

try:
    from ats_utilities import auto_str, VerboseRoot
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@auto_str
class ATSChecker(metaclass=VerboseRoot):
    '''
        Defines class ATSChecker with attribute(s) and method(s).
        Creates API fo checking parameters for object methods and functions.
        Mechanism for checking function/method parameters (type/value).

        It defines:

            :attributes:
                | no_error - No error, error id (0).
                | type_error - Type param error id (1).
                | value_error - Value param error id (2).
                | format_error - Wrong format error id (3).
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
                | priority_error - Set priority error id (type_error).
                | check_params - Check parameters for method/function.
    '''

    no_error: int = 0
    type_error: int = 1
    value_error: int = 2
    format_error: int = 3

    _start_message: str | None
    _list_of_params: List[Any]
    _error_type: List[int]
    _error_type_index: List[int]
    _error_value_index: List[int]

    def __init__(self) -> None:
        '''
            Initial ATSChecker constructor.

            :exceptions: None
        '''
        self._start_message = None
        self._list_of_params = []
        self._error_type = [0, 0, 0]
        self._error_type_index = []
        self._error_value_index = []

    def collect_params(
        self, params_description: OrderedDict[str, Any]
    ) -> bool:
        '''
            Collect all parameters in one list.

            :param params_description: Description for parameters.
            :type params_description: <OrderedDict[str, Any]>
            :return: True (collected) | False (failed to collect).
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not bool(params_description)]):
            self._error_type[2] = ATSChecker.format_error
            return False
        for exp_type, inst in params_description.items():
            pname: str = exp_type.split(':')[1]
            ptype: str = exp_type.split(':')[0]
            self._list_of_params.append(
                f'\n    expected {pname} <{ptype}> object at {hex(id(inst))}'
            )
        return True

    def usage_message(self) -> str | None:
        '''
            Prepare usage message for method/function.

            :return: Usage message for method/function.
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

            :param params_description: Description for parameters.
            :type params_description: <OrderedDict[str, Any]>
            :return: True (types ok) | False (types are not ok).
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not bool(params_description)]):
            self._error_type[2] = ATSChecker.format_error
            return False
        for index, (exp_type, inst) in enumerate(params_description.items()):
            param_typ_name: list[str] = exp_type.split(':')
            if len(param_typ_name) == 2:
                if type(inst).__name__ != param_typ_name[0]:
                    self._error_type[0] = ATSChecker.type_error
                    self._error_type_index.append(index)
            else:
                self._error_type[2] = ATSChecker.format_error
                return False
        return True

    def check_values(self, params_description: OrderedDict[str, Any]) -> bool:
        '''
            Check parameters (values) for method/function.

            :param params_description: Description for parameters.
            :type params_description: <OrderedDict[str, Any]>
            :return: True (values are ok) | False (values are not ok).
            :rtype: <bool>
            :exceptions: None
        '''
        if any([not bool(params_description)]):
            self._error_type[2] = ATSChecker.format_error
            return False
        for index, inst in enumerate(params_description.values()):
            if inst is None:
                self._error_type[1] = ATSChecker.value_error
                self._error_value_index.append(index)
            any_base_type: bool = any([
                isinstance(inst, dict), isinstance(inst, list),
                isinstance(inst, tuple), isinstance(inst, set),
                isinstance(inst, frozenset), isinstance(inst, bytearray),
                isinstance(inst, bytes)
            ])
            if any_base_type:
                if not bool(inst):
                    self._error_type[1] = ATSChecker.value_error
                    self._error_value_index.append(index)
        return True

    def priority_error(self) -> int | None:
        '''
            Set priority error id (type_error).

            :return: Priority error id (0 | 1 | 2 | 3) | None.
            :rtype: <int> | <NoneType>
            :exceptions: None
        '''
        priority_error_id: int | None = None
        if self._error_type[2] == ATSChecker.format_error:
            return ATSChecker.format_error
        if self._error_type[1] == ATSChecker.value_error:
            priority_error_id = ATSChecker.value_error
        if self._error_type[0] == ATSChecker.type_error:
            priority_error_id = ATSChecker.type_error
        if all(error_type == 0 for error_type in self._error_type):
            priority_error_id = ATSChecker.no_error
        return priority_error_id

    def check_params(
        self, params_description: List[Tuple[str, Any]]
    ) -> tuple[str | None, int | None]:
        '''
            Check parameters for method/function.

            :param params_description: Description for parameters.
            :type params_description: <List[Tuple[str, Any]]>
            :return: usage message, status (0 | 1 | 2 | 3).
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
            error_id = ATSChecker.format_error
        return message, error_id
