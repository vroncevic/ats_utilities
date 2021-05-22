# -*- coding: UTF-8 -*-

'''
 Module
     ats_abstract_test.py
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
     Defined class ATSAbstractTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of AbstractMethod.
 Execute
     python -m unittest -v ats_abstract_test
'''

import sys
import unittest

try:
    from ats_utilities.abstract import AbstractMethod
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSAbstractClassTest:
    '''Simple Class for checking AbstractMethod.'''

    def __init__(self):
        '''Initial constructor.'''
        self.source_field = None
        self.target_field = None

    @AbstractMethod
    def setup_source(self):
        '''Abstract Method 1.'''

    @AbstractMethod
    def setup_target(self):
        '''Abstract Method 2.'''


class ATSAbstractTestCase(unittest.TestCase):
    '''
        Defined class ATSAbstractTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of AbstractMethod.
        It defines:

            :attributes:
                | ats_abastract_obj - API fo checking parameters.
                | class_name - Error message from ATSChecker.
                | status - Error status from ATSChecker.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_abs_method_first - test for first abstract method.
                | test_abs_method_second - test for second abstract method.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.class_abastract_obj = ATSAbstractClassTest()
        self.class_name = self.class_abastract_obj.__class__.__name__
        self.class_methods = []
        self.exception_messages = []
        for attribute in dir(ATSAbstractClassTest):
            check_attribute = all([
                callable(getattr(ATSAbstractClassTest, attribute)),
                attribute.startswith('__') is False
            ])
            if check_attribute:
                self.class_methods.append(attribute)
                self.exception_messages.append(
                    'from class {0}::{1}() not implemented'.format(
                        self.class_name, attribute
                    )
                )

    def tearDown(self):
        '''Call after test case.'''
        self.class_abastract_obj = None
        self.class_name = None
        self.class_methods = None
        self.exception_messages = None

    def test_abs_method_first(self):
        '''Test for first abstract method.'''
        with self.assertRaises(NotImplementedError) as exception_obj:
            self.class_abastract_obj.setup_source()
        self.assertEqual(
            self.exception_messages[0], str(exception_obj.exception)
        )

    def test_abs_method_second(self):
        '''Test for second abstract method.'''
        with self.assertRaises(NotImplementedError) as exception_obj:
            self.class_abastract_obj.setup_target()
        self.assertEqual(
            self.exception_messages[1], str(exception_obj.exception)
        )

if __name__ == '__main__':
    unittest.main()
