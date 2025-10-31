# -*- coding: UTF-8 -*-

'''
Module
    ats_exceptions_test.py
Copyright
    Copyright (C) 2017 - 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines classes ATSExceptionsTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS Exceptions.
Execute
    python3 -m unittest -v ats_exceptions_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from ats_utilities.exceptions.ats_key_error import ATSKeyError
    from ats_utilities.exceptions.ats_lookup_error import ATSLookupError
    from ats_utilities.exceptions.ats_parameter_error import ATSParameterError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2025, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSExceptionsTestCase(TestCase):
    '''
        Defines classes ATSExceptionsTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Exceptions.
        ATS Exceptions unittests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_ats_type_error - Test ATSTypeError.
                | test_ats_attribute_error - Test ATSAttributeError.
                | test_ats_bad_call_error - Test ATSBadCallError.
                | test_ats_file_error - Test ATSFileError.
                | test_ats_key_error - Test ATSKeyError.
                | test_ats_lookup_error - Test ATSLookupError.
                | test_ats_parameter_error - Test ATSParameterError.
                | test_ats_value_error - Test ATSValueError.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_ats_type_error(self) -> None:
        '''Test ATSTypeError'''
        with self.assertRaises(ATSTypeError):
            raise ATSTypeError('Simple type error')

    def test_ats_attribute_error(self) -> None:
        '''Test ATSAttributeError'''
        with self.assertRaises(ATSAttributeError):
            raise ATSAttributeError('Simple attribute error')

    def test_ats_bad_call_error(self) -> None:
        '''Test ATSBadCallError'''
        with self.assertRaises(ATSBadCallError):
            raise ATSBadCallError('Simple bad call error')

    def test_ats_file_error(self) -> None:
        '''Test ATSFileError'''
        with self.assertRaises(ATSFileError):
            raise ATSFileError('Simple file error')

    def test_ats_key_error(self) -> None:
        '''Test ATSKeyError'''
        with self.assertRaises(ATSKeyError):
            raise ATSKeyError('Simple key error')

    def test_ats_lookup_error(self) -> None:
        '''Test ATSLookupError'''
        with self.assertRaises(ATSLookupError):
            raise ATSLookupError('Simple lookup error')

    def test_ats_parameter_error(self) -> None:
        '''Test ATSParameterError'''
        with self.assertRaises(ATSParameterError):
            raise ATSParameterError('Simple parameter error')

    def test_ats_value_error(self) -> None:
        '''Test ATSValueError'''
        with self.assertRaises(ATSValueError):
            raise ATSValueError('Simple value error')


if __name__ == '__main__':
    main()
