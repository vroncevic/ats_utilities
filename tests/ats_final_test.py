# -*- coding: UTF-8 -*-

'''
 Module
     ats_final_test.py
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
     Defined classes ATSFinalTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ATSFinal.
 Execute
     python -m unittest -v ats_final_test
'''

import sys
import unittest

try:
    from ats_utilities.final import ATSFinal
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SimpleClass:
    '''Simple class which will be final.'''

    __metaclass__ = ATSFinal

    def __init__(self, verbose=False):
        '''Initial constructor.'''
        self.simple_instance_attr = 'init set'

    def simple_opertion(self, verbose=False):
        '''Simple method.'''
        self.simple_instance_attr = 'all looks good'


class ATSFinalTestCase(unittest.TestCase):
    '''
        Defined classes ATSFinalTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATSFinal.
        It defines:

            :attributes:
                | exception_message - expected exception message.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_inheritance - test for inheritance mechanism.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.exception_message = '{0} is final'.format(SimpleClass.__name__)

    def tearDown(self):
        '''Call after test case.'''
        self.exception_message = None

    def test_inheritance(self):
        '''Test for inheritance mechanism.'''
        with self.assertRaises(TypeError) as exception_obj:
            class InheritClass(SimpleClass):
                '''Simple class which will be final.'''

                def __init__(self, verbose=False):
                    '''Initial constructor.'''
                    SimpleClass.__init__(self)
                    self.simple_instance_attr = 'init set overwrite'

                def simple_opertion(self, verbose=False):
                    '''Simple method.'''
                    self.simple_instance_attr = 'all looks good again'

        self.assertEqual(
            self.exception_message, str(exception_obj.exception)
        )


if __name__ == '__main__':
    unittest.main()
