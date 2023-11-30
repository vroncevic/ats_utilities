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
    Defines class ATSLoggingTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSLogger.
Execute
    python -m unittest -v ats_logging_test
'''

import sys
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.logging import ATSLogger
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggingTestCase(TestCase):
    '''
        Defines class ATSLoggingTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSLogger.

        It defines:

            :attributes:
                | LOG_FILE - Log file path.
                | tool_name - Tool name.
                | log_file - Tool log file path.
                | logger_ats - API for ATS logger.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_debug - Test debug log.
                | test_warning - Test warning log.
                | test_critical - Test critical log.
                | test_error - Test error log.
                | test_info - Test info log.
    '''

    LOG_FILE = '/log/simple_tool.log'

    def setUp(self) -> None:
        '''Call before test case.'''
        self.log_file: str = f'{dirname(__file__)}{self.LOG_FILE}'
        self.tool_name: str = 'simple_test'
        self.logger_ats: ATSLogger = ATSLogger(
            self.tool_name, self.log_file, verbose=False
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test not None'''
        self.assertIsNotNone(self.logger_ats)

    def test_debug(self) -> None:
        '''Test ATS debug log.'''
        self.assertTrue(
            self.logger_ats.write_log(
                'simple debug', self.logger_ats.ATS_DEBUG
            )
        )

    def test_warning(self) -> None:
        '''Test ATS warning log.'''
        self.assertTrue(
            self.logger_ats.write_log(
                'simple warning', self.logger_ats.ATS_WARNING
            )
        )

    def test_critical(self) -> None:
        '''Test ATS critical log.'''
        self.assertTrue(
            self.logger_ats.write_log(
                'simple critical', self.logger_ats.ATS_CRITICAL
            )
        )

    def test_error(self) -> None:
        '''Test ATS error log.'''
        self.assertTrue(
            self.logger_ats.write_log(
                'simple error', self.logger_ats.ATS_ERROR
            )
        )

    def test_info(self) -> None:
        '''Test ATS info log.'''
        self.assertTrue(
            self.logger_ats.write_log(
                'simple info', self.logger_ats.ATS_INFO
            )
        )


if __name__ == '__main__':
    main()
