# -*- coding: UTF-8 -*-

'''
Module
    ats_exceptions_test.py
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
    Defines classes ATSExceptionsTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS Exceptions.
Execute
    python3 -m unittest -v tests/exceptions/ats_exceptions_test.py
'''

from unittest import TestCase, main
from ats_utilities.exceptions import (
    ATSAttributeError,
    ATSBadCallError,
    ATSFileError,
    ATSKeyError,
    ATSLookupError,
    ATSParameterError,
    ATSTypeError,
    ATSValueError
)

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


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
