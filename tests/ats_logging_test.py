# -*- coding: UTF-8 -*-

'''
 Module
     ats_logging_test.py
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
     Defined class ATSLoggingTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ATSLogger.
 Execute
     python -m unittest -v ats_logging_test
'''

import sys
import unittest

try:
    from pathlib import Path
    from ats_utilities.logging import ATSLogger
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


class ATSLoggingTestCase(unittest.TestCase):
    '''
        Defined class ATSLoggingTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATSLogger.
        It defines:

            :attributes:
                | LOG_FILE - log file path.
                | tool_name - tool name.
                | log_file - tool log file path.
                | logger_ats - API for ATS logger.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_debug - test debug log.
                | test_warning - test warning log.
                | test_critical - test critical log.
                | test_error - test error log.
                | test_info - test info log.
    '''

    LOG_FILE = '/log/simple_tool.log'

    def setUp(self):
        '''Call before test case.'''
        self.log_file = '{0}{1}'.format(
            Path(__file__).resolve().parent, ATSLoggingTestCase.LOG_FILE
        )
        self.tool_name = 'simple_test'
        self.logger_ats = ATSLogger(
            self.tool_name, self.log_file, verbose=False
        )

    def tearDown(self):
        '''Call after test case.'''
        self.logger_ats = None
        self.log_file = None
        self.tool_name = None

    def test_debug(self):
        '''Test ATS debug log.'''
        self.logger_ats.write_log('simple debug', ATSLogger.ATS_DEBUG)

    def test_warning(self):
        '''Test ATS warning log.'''
        self.logger_ats.write_log('simple warning', ATSLogger.ATS_WARNING)

    def test_critical(self):
        '''Test ATS critical log.'''
        self.logger_ats.write_log('simple critical', ATSLogger.ATS_CRITICAL)

    def test_error(self):
        '''Test ATS error log.'''
        self.logger_ats.write_log('simple error', ATSLogger.ATS_ERROR)

    def test_info(self):
        '''Test ATS info log.'''
        self.logger_ats.write_log('simple info', ATSLogger.ATS_INFO)


if __name__ == '__main__':
    unittest.main()
