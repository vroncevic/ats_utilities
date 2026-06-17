# -*- coding: UTF-8 -*-

'''
Module
    check_reporter.py
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
    Defines class ATSCheckReporter with attribute(s) and method(s).
    Creates an API for checking parameters for methods and functions.
'''

from typing import List
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.icheck_reporter import IATSCheckReporter, ParamMetadata

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSCheckReporter(IATSCheckReporter):
    '''
        Defines class ATSCheckReporter with attribute(s) and method(s).
        Standard human-readable report formatter.
        Mechanism for checking function or method parameters (report).

        It defines:

            :attributes: None
            :methods:
                | build_message_format - Builds the final message report.
                | __str__ - Returns the string representation of ATSCheckReporter.
    '''

    def build_message_format(self, context: str, parameters_meta: List[ParamMetadata], err_indices: List[int], is_fmt_err: bool) -> str:
        '''
            Builds the final message report.

            :param context: The context string from the stack
            :type context: <str>
            :param parameters_meta: Metadata about processed parameters
            :type parameters_meta: <List[ParamMetadata]>
            :param err_indices: Indices of parameters with errors
            :type err_indices: <List[int]>
            :param is_fmt_err: Flag indicating a format error occurred
            :type is_fmt_err: <bool>
            :return: Formatted message report
            :rtype: <str>
            :exceptions: None
        '''
        message = context
        err_set = set(err_indices)

        for i, (pname, ptype, inst) in enumerate(parameters_meta):
            message += f'\n    expected {pname} <{ptype}> object at {hex(id(inst))}'

            if i in err_set:
                message += ' wrong type'

        if is_fmt_err or err_indices:
            message += ' format wrong during checking parameters_meta'

        return message

    def __str__(self) -> str:
        '''
            Returns the string representation of ATSCheckReporter.

            :return: String representation of ATSCheckReporter
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
