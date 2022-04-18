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
     Defined class ATSChecker with attribute(s) and method(s).
     Created API fo checking parameters for object methods and functions.
'''

import sys
from inspect import stack
from collections import OrderedDict

try:
    from six import add_metaclass
    from ats_utilities.final import ATSFinal
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(ATSFinal)
class ATSChecker:
    '''
        Defined class ATSChecker with attribute(s) and method(s).
        Created API fo checking parameters for object methods and functions.
        It defines:

            :attributes:
                | NO_ERROR - no error, error id (0).
                | TYPE_ERROR - type param error id (1).
                | VALUE_ERROR - value param error id (2).
                | FORMAT_ERROR - wrong format error id (3).
                | __start_message - start segment of usage message.
                | __list_of_params - list of parameters for method/function.
                | __error_type - list of mapped errors.
                | __error_type_index - error type index.
                | __error_value_index - error value index.
            :methods:
                | __init__ - initial constructor.
                | collect_params - collect all parameters in one list.
                | usage_message - prepare usage message for method/function.
                | check_types - check parameters (types) for method/function.
                | check_values - check parameters (values) for method/function.
                | priority_error - set priority error id (TYPE_ERROR).
                | check_params - check parameters for method/function.
                | __str__ - str dunder method for object ATSChecker.
    '''

    NO_ERROR, TYPE_ERROR, VALUE_ERROR, FORMAT_ERROR = 0, 1, 2, 3

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__start_message = None
        self.__list_of_params = []
        self.__error_type = [0, 0, 0]
        self.__error_type_index = []
        self.__error_value_index = []

    def collect_params(self, params_description):
        '''
            Collect all parameters in one list.

            :param params_description: description for parameters.
            :type params_description: <OrderedDict>
            :return: True (format for params ok) | False.
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        check_format = any([
            not bool(params_description),
            not isinstance(params_description, OrderedDict)
        ])
        if check_format:
            self.__error_type[2] = ATSChecker.FORMAT_ERROR
            return False
        for exp_type, inst in params_description.items():
            parameter_name = exp_type.split(':')[1]
            parameter_type = exp_type.split(':')[0]
            param_check = '\n    expected {0} <{1}> object at {2}'.format(
                parameter_name, parameter_type, hex(id(inst))
            )
            self.__list_of_params.append(param_check)
        return True

    def usage_message(self):
        '''
            Prepare usage message for method/function.

            :return: usage message for method/function.
            :rtype: <str>
            :exceptions: None
        '''
        message = self.__start_message
        if bool(self.__list_of_params):
            for index, param in enumerate(self.__list_of_params):
                message = '{0}{1}'.format(message, param)
                if bool(self.__error_type_index):
                    error_type_index = set(self.__error_type_index)
                    if index in error_type_index:
                        message = '{0} {1}'.format(message, 'wrong type')
                if bool(self.__error_value_index):
                    error_value_index = set(self.__error_value_index)
                    if index in error_value_index:
                        message = '{0} {1}'.format(message, 'wrong value')
        return message

    def check_types(self, params_description):
        '''
            Check parameters (types) for method/function.

            :param params_description: parameters description.
            :type params_description: <OrderedDict>
            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        check_format = any([
            not bool(params_description),
            not isinstance(params_description, OrderedDict)
        ])
        if check_format:
            self.__error_type[2] = ATSChecker.FORMAT_ERROR
            return False
        for index, (exp_type, inst) in enumerate(params_description.items()):
            param_typ_name = exp_type.split(':')
            if len(param_typ_name) == 2:
                expected_type = param_typ_name[0]
                if type(inst).__name__ != expected_type:
                    self.__error_type[0] = ATSChecker.TYPE_ERROR
                    self.__error_type_index.append(index)
            else:
                self.__error_type[2] = ATSChecker.FORMAT_ERROR
                return False
        return True

    def check_values(self, params_description):
        '''
            Check parameters (values) for method/function.

            :param params_description: parameters description.
            :type params_description: <OrderedDict>
            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        check_format = any([
            not bool(params_description),
            not isinstance(params_description, OrderedDict)
        ])
        if check_format:
            self.__error_type[2] = ATSChecker.FORMAT_ERROR
            return False
        for index, inst in enumerate(params_description.values()):
            if inst is None:
                self.__error_type[1] = ATSChecker.VALUE_ERROR
                self.__error_value_index.append(index)
            any_base_type = any([
                isinstance(inst, dict), isinstance(inst, list),
                isinstance(inst, tuple), isinstance(inst, set),
                isinstance(inst, frozenset), isinstance(inst, bytearray),
                isinstance(inst, bytes)
            ])
            if any_base_type:
                if not bool(inst):
                    self.__error_type[1] = ATSChecker.VALUE_ERROR
                    self.__error_value_index.append(index)
        return True

    def priority_error(self):
        '''
            Set priority error id (TYPE_ERROR).

            :return: priority error id (0 | 1 | 2 | 3) | None.
            :rtype: <int> | <NoneType>
            :exceptions: None
        '''
        priority_error_id = None
        if self.__error_type[2] == ATSChecker.FORMAT_ERROR:
            return ATSChecker.FORMAT_ERROR
        if self.__error_type[1] == ATSChecker.VALUE_ERROR:
            priority_error_id = ATSChecker.VALUE_ERROR
        if self.__error_type[0] == ATSChecker.TYPE_ERROR:
            priority_error_id = ATSChecker.TYPE_ERROR
        if all(error_type == 0 for error_type in self.__error_type):
            priority_error_id = ATSChecker.NO_ERROR
        return priority_error_id

    def check_params(self, params_description):
        '''
            Check parameters for method/function.

            :param params_description: parameters description.
            :type params_description: <list>
            :return: usage message, status (0 | 1 | 2 | 3).
            :rtype: <str>, <int>
            :exceptions: None
        '''
        func, module, error_id = stack()[1][3], stack()[1][1], 0
        param_error_message, header = None, '\nmod: {0}\n  def: {1}()'
        self.__start_message = header.format(module, func)
        fail_any_check = any([
            not self.collect_params(OrderedDict(params_description)),
            not self.check_types(OrderedDict(params_description)),
            not self.check_values(OrderedDict(params_description))
        ])
        param_error_message = self.usage_message()
        error_id = self.priority_error()
        if any([error_id is None, fail_any_check]):
            param_error_message = '{0} {1}'.format(
                param_error_message, 'format wrong during checking params'
            )
            error_id = ATSChecker.FORMAT_ERROR
        return param_error_message, error_id

    def __str__(self):
        '''
            Dunder str method for object ATSChecker.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__, self.__start_message,
            str(self.__list_of_params), str(self.__error_type),
            str(self.__error_type_index), str(self.__error_value_index)
        )
