# -*- coding: UTF-8 -*-

'''
Module
    ats_logging_test.py
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
    Defines class ATSLoggingTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSLogger.
Execute
    python -m unittest -v ats_logging_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.logging import ATSLogger
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggingTestCase(TestCase):
    '''
        Defines class ATSLoggingTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSLogger.
        ATSLogger unit tests.

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

    def test_set_not_existing_file_path(self) -> None:
        '''Test set file path'''
        with self.assertRaises(ATSFileError):
            self.logger_ats.logger_path = 'not_simple_tool.log'

    def test_set_file_path_wrong_type(self) -> None:
        '''Test set file path'''
        with self.assertRaises(ATSTypeError):
            self.logger_ats.logger_path = None

    def test_set_logger_name_wrong_type(self) -> None:
        '''Test set file path'''
        with self.assertRaises(ATSTypeError):
            self.logger_ats.logger_name = None

    def test_set_logger_status_wrong_type(self) -> None:
        '''Test set file path'''
        with self.assertRaises(ATSTypeError):
            self.logger_ats.logger_status = None  # type: ignore

    def test_logger_write_log_wrong_type(self) -> None:
        '''Test set file path'''
        with self.assertRaises(ATSTypeError):
            self.logger_ats.logger_path = f'{dirname(__file__)}{self.LOG_FILE}'
            self.logger_ats.write_log(
                None, self.logger_ats.ATS_DEBUG
            )

    def test_logger_write_log_wrong_level(self) -> None:
        '''Test set file path'''
        with self.assertRaises(ATSBadCallError):
            self.logger_ats.logger_path = f'{dirname(__file__)}{self.LOG_FILE}'
            self.logger_ats.write_log('simple test', -1)

    def test_is_log_file_set(self) -> None:
        '''Test is log file set'''
        self.logger_ats.logger_path = self.log_file
        file_path: str | None = self.logger_ats.logger_path
        self.assertIsNotNone(file_path)

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
