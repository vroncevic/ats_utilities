# -*- coding: UTF-8 -*-

'''
 Module
     ats_checker_test.py
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
     Defined class ATSCheckerTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ATS CLI interfaces.
 Execute
     python -m unittest -v ats_checker_test
'''

import sys
import unittest

try:
    from ats_utilities.checker import ATSChecker
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSCheckerTestCase(unittest.TestCase):
    '''
        Defined class ATSCheckerTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATS CLI interfaces.
        It defines:

            :attributes:
                | checker - API for checking parameters.
                | error - error message from ATSChecker.
                | status - error status from ATSChecker.
            :methods:
                | setUp - call before every test case.
                | tearDown - call after every test case.
                | test_str_parameter - test for string param checking.
                | test_int_parameter - test for int param checking.
                | test_float_parameter - test for float param checking.
                | test_complex_parameter - test for complex param checking.
                | test_bool_parameter - test for bool param checking.
                | test_bytearray_parameter - test for bytearray param checking.
                | test_bytes_parameter - test for bytes param checking.
                | test_dict_parameter - test for dict param checking.
                | test_frozenset_parameter - test for frozenset param checking.
                | test_list_parameter - test for list param checking.
                | test_set_parameter - test for set param checking.
                | test_tuple_parameter - test for tuple param checking.
                | test_object_parameter - test for object param checking.
                | test_type_error - test for type param checking.
                | test_value_error - test for value param checking.
    '''

    def setUp(self):
        '''Call before every test case.'''
        self.checker = ATSChecker()
        self.error = None
        self.status = -1

    def tearDown(self):
        '''Call after every test case.'''
        self.error = None
        self.status = -1

    def test_str_parameter(self):
        '''Test for string param checking.'''
        simple_var = '8'
        self.error, self.status = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_int_parameter(self):
        '''Test for int param checking.'''
        simple_var = 2342425252
        self.error, self.status = self.checker.check_params([
            ('int:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_float_parameter(self):
        '''Test for float param checking.'''
        simple_var = 34.4546464
        self.error, self.status = self.checker.check_params([
            ('float:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_complex_parameter(self):
        '''Test for complex param checking.'''
        simple_var = 3 +6j
        self.error, self.status = self.checker.check_params([
            ('complex:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_bool_parameter(self):
        '''Test for bool param checking.'''
        simple_var = True
        self.error, self.status = self.checker.check_params([
            ('bool:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_bytearray_parameter(self):
        '''Test for bytearray param checking.'''
        simple_var = '8'
        self.error, self.status = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_bytes_parameter(self):
        '''Test for bytes param checking.'''
        simple_var = '8'
        self.error, self.status = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_dict_parameter(self):
        '''Test for dict param checking.'''
        simple_var = '8'
        self.error, self.status = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_frozenset_parameter(self):
        '''Test for frozenset param checking.'''
        simple_var = '8'
        self.error, self.status = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_list_parameter(self):
        '''Test for list param checking.'''
        simple_var = ['8', 34, 43.343533, {'a', 'bs'}]
        self.error, self.status = self.checker.check_params([
            ('list:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_set_parameter(self):
        '''Call test for set param checking.'''
        simple_var = {'apple', 'banana', 'cherry'}
        self.error, self.status = self.checker.check_params([
            ('set:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_tuple_parameter(self):
        '''Test for tuple param checking.'''
        simple_var = ('quick test', 8, 32.4, [-99, 8, 3.4])
        self.error, self.status = self.checker.check_params([
            ('tuple:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_object_parameter(self):
        '''Test for object param checking.'''
        simple_var = object()
        self.error, self.status = self.checker.check_params([
            ('object:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 0)

    def test_type_error(self):
        '''Test for type param checking.'''
        simple_var = ('quick test', 8, 32.4, [-99, 8, 3.4])
        self.error, self.status = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 1)

    def test_value_error(self):
        '''Test for value param checking.'''
        simple_var = ''
        self.error, self.status = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.status, 2)

if __name__ == '__main__':
    unittest.main()
