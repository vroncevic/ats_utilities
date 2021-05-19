# -*- coding: UTF-8 -*-

'''
 Module
     ats_console_io_test.py
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
     Defined classes ATSXXXXTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ATS console.
 Execute
     python -m unittest -v ats_console_io_test
'''

import sys
import unittest

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.warning import warning_message
    from ats_utilities.console_io.success import success_message
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSVerboseTestCase(unittest.TestCase):
    '''
        Defined class ATSVerboseTestCase with attribute(s) and method(s).
        Created test case for checking functionality of ATS verbose.
        It defines:

            :attributes:
                | verbose_path - verbose path.
                | verbose - verbose flag.
                | message - verbose message.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_verbose_api - test verbose API.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.verbose_path = 'ATS_CONSOLE_IO_VERBOSE_TEST_CASE'
        self.verbose = True
        self.message = 'Set verbose message'

    def tearDown(self):
        '''Call after test case.'''
        self.verbose_path = None
        self.verbose = None
        self.message = None

    def test_verbose_api(self):
        '''Test verbose API.'''
        verbose_message(self.verbose_path, self.verbose, self.message)

class ATSErrorTestCase(unittest.TestCase):
    '''
        Defined class ATSErrorTestCase with attribute(s) and method(s).
        Created test case for checking functionality of ATS error.
        It defines:

            :attributes:
                | error_path - error path.
                | message - error message.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_error_api - test error API.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.error_path = 'ATS_ERROR_TEST_CASE'
        self.message = 'Set error message'

    def tearDown(self):
        '''Call after test case.'''
        self.error_path = None
        self.message = None

    def test_error_api(self):
        '''Test error API.'''
        error_message(self.error_path, self.message)

class ATSWarningTestCase(unittest.TestCase):
    '''
        Defined class ATSWarningTestCase with attribute(s) and method(s).
        Created test case for checking functionality of ATS warning.
        It defines:

            :attributes:
                | warning_path - warning path.
                | message - warning message.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_warning_api - test warning API.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.warning_path = 'ATS_WARNING_TEST_CASE'
        self.message = 'Set warning message'

    def tearDown(self):
        '''Call after test case.'''
        self.warning_path = None
        self.message = None

    def test_warning_api(self):
        '''Test warning API.'''
        warning_message(self.warning_path, self.message)

class ATSSuccessTestCase(unittest.TestCase):
    '''
        Defined class ATSSuccessTestCase with attribute(s) and method(s).
        Created test case for checking functionality of ATS success.
        It defines:

            :attributes:
                | success_path - success path.
                | message - success message.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_success_api - test success API.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.success_path = 'ATS_SUCCESS_TEST_CASE'
        self.message = 'Set success message'

    def tearDown(self):
        '''Call after test case.'''
        self.success_path = None
        self.message = None

    def test_success_api(self):
        '''Test success API.'''
        success_message(self.success_path, self.message)

if __name__ == '__main__':
    unittest.main()
