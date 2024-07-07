# -*- coding: UTF-8 -*-

'''
Module
    ats_console_io_success_test.py
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
    Defines classes ATSSuccessTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS console.
Execute
    python -m unittest -v ats_console_io_success_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.console_io.success import success_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSSuccessTestCase(TestCase):
    '''
        Defines class ATSSuccessTestCase with attribute(s) and method(s).
        Creates test case for checking functionality of ATS success.
        success_message unit tests.

        It defines:

            :attributes:
                | message - success message.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_success_api - Test success API.
                | test_none_success - Test for None as message.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.message = 'Set success message'

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_success_api(self) -> None:
        '''Test success API.'''
        success_message([f'message {self.message}'])

    def test_none_success(self) -> None:
        '''Test for None as message'''
        with self.assertRaises(ATSTypeError):
            success_message(None)  # type: ignore


if __name__ == '__main__':
    main()
