# -*- coding: UTF-8 -*-

'''
Module
    ats_logging_stdout_test.py
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
    Defines class ATSLoggingStreamTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSLogger.
Execute
    python -m unittest -v ats_logging_stdout_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.logging import ATSLogger
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


class ATSLoggingStreamTestCase(TestCase):
    '''
        Defines class ATSLoggingStreamTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSLogger.
        ATSLogger unit tests.

        It defines:

            :attributes:
                | tool_name - Tool name.
                | logger_ats - API for ATS logger.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test for ATSLogger not None
                | test_debug - Test debug log.
                | test_warning - Test warning log.
                | test_critical - Test critical log.
                | test_error - Test error log.
                | test_info - Test info log.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.tool_name: str = 'simple_test'
        self.logger_ats: ATSLogger = ATSLogger(
            ats_name=self.tool_name,
            ats_log_stdout=True,
            ats_log_file=None,
            ats_logger_status=True,
            verbose=False
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
