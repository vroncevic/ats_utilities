# -*- coding: utf-8 -*-

'''
Module
    story_ats_checker_with_mcheck.py
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
    Use cases for ATS checker with usage of @fcheck decorator.
'''

from __future__ import annotations

from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.factory import CheckerBundleFactory
from ats_utilities.checker.proxy_validator import fcheck
from ats_utilities.exceptions import ATSTypeError

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@fcheck([
    ('str:arg1', None), ('int:arg2', None), ('float:arg3', None)
])
def use_case_type_error(arg1: str, arg2: int, arg3: float) -> tuple[str, int, float]:
    return  arg1, arg2, arg3


print('Checker [USE-CASE: 0] Format error')
try:
    @fcheck(
        ('str:arg1', None)
    )
    def use_case_format_error(arg1: str, arg2: int, arg3: float) -> tuple[str, int, float]:
        return  arg1, arg2, arg3
except ATSTypeError as exception:
    print(exception)
print('-'*100)


@fcheck(
    [('str:arg1', None), ('int:arg2', None), ('float:arg3', None)],
    checker=Checker(CheckerBundleFactory.create_bundle())
)
def use_case_no_error(arg1: str, arg2: int, arg3: float) -> tuple[str, int, float]:
    return  arg1, arg2, arg3


if __name__ == '__main__':
    print('Checker [USE-CASE: 1] No error')
    arg1, arg2, arg3 = use_case_type_error('test', 2, 3.0)
    print(arg1, arg2, arg3)
    print('-'*100)

    print('Checker [USE-CASE: 2] Type error')
    try:
        use_case_type_error(123, 2, 3.0)
    except ATSTypeError as exception:
        print(exception)
    print('-'*100)

    print('Checker [USE-CASE: 3] Type error')
    try:
        use_case_type_error('test', 2.0, 3.0)
    except ATSTypeError as exception:
        print(exception)
    print('-'*100)

    print('Checker [USE-CASE: 4] Type error')
    try:
        use_case_type_error('test', 2, '3.0')
    except ATSTypeError as exception:
        print(exception)
    print('-'*100)

    print('Checker [USE-CASE: 5] No error')
    arg1, arg2, arg3 = use_case_type_error('test', 2, 3.0)
    print(arg1, arg2, arg3)
    print('-'*100)

    print('Checker [USE-CASE: 6] No error')
    arg1, arg2, arg3 = use_case_no_error('test', 2, 3.0)
    print(arg1, arg2, arg3)
    print('-'*100)