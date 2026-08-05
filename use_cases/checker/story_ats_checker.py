# -*- coding: utf-8 -*-

'''
Module
    story_ats_checker.py
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
    Use cases for ATS checker with usage of .validate_parameters method.
'''

from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.factory import CheckerBundleFactory
from ats_utilities.checker.setup.types import (
    Parameters, Result, CheckerErrorType
)

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def use_case_no_and_type_error(arg1: str, arg2: int, arg3: float) -> Result:
    ats_checker = Checker(own=CheckerBundleFactory.create_bundle())

    parameters: Parameters = (
        ('str:arg1', arg1),
        ('int:arg2', arg2),
        ('float:arg3', arg3)
    )

    return  ats_checker.validates_parameters(parameters)

def use_case_format_error(arg1: str, arg2: int, arg3: float) -> Result:
    ats_checker = Checker(own=CheckerBundleFactory.create_bundle())

    parameters: Parameters = (
        (arg1, 'str:arg1'),
        (arg2, 'int:arg2'),
        (arg3, 'float:arg3')
    )

    return  ats_checker.validates_parameters(parameters)


def print_result(result: Result) -> None:
    message, error_id = result

    if error_id == CheckerErrorType.TYPE_ERROR:
        print(f'Type error: {message}')
    elif error_id == CheckerErrorType.FORMAT_ERROR:
        print(f'Format error: {message}')
    else:
        print(f'No error: {message}')

if __name__ == '__main__':
    print('Checker [USE-CASE: 1] No error')
    print_result(use_case_no_and_type_error('test', 2, 3.0))
    print('-'*100)
    print('Checker [USE-CASE: 2] Type error')
    print_result(use_case_no_and_type_error(None, 2, 3.0))
    print('-'*100)
    print('Checker [USE-CASE: 3] Type error')
    print_result(use_case_no_and_type_error('test', None, 3.0))
    print('-'*100)
    print('Checker [USE-CASE: 4] Type error')
    print_result(use_case_no_and_type_error('test', 2, None))
    print('-'*100)
    print('Checker [USE-CASE: 5] Type error')
    print_result(use_case_no_and_type_error(None, None, None))
    print('-'*100)
    print('Checker [USE-CASE: 6] Type error')
    print_result(use_case_no_and_type_error(1, 2, 3.0))
    print('-'*100)
    print('Checker [USE-CASE: 7] Type error')
    print_result(use_case_no_and_type_error('1', 2.0, 3.0))
    print('-'*100)
    print('Checker [USE-CASE: 8] Type error')
    print_result(use_case_no_and_type_error('1', 2, '3.0'))
    print('-'*100)
    print('Checker [USE-CASE: 9] No error')
    print_result(use_case_no_and_type_error('test', 2, 3.0))
    print('-'*100)
    print('Checker [USE-CASE: 10] Format error')
    print_result(use_case_format_error('test', 2, 3.0))
