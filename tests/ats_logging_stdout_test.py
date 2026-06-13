# -*- coding: UTF-8 -*-

'''
Module
    ats_logging_stdout_test.py
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
    Defines class ATSLoggingStreamTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSLogger.
Execute
    python3 -m unittest -v ats_logging_stdout_test
'''

from typing import List
from unittest import TestCase, main
from ats_utilities.logging.ats_logger import ATSLogger
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseLoggingStream(ATSLogger):
    '''Simple Class for checking ATSLogger.'''

    def __init__(self, reporter: IATSReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        super().__init__(
            ats_name='simple_test',
            ats_log_stdout=True,
            ats_log_file=None,
            reporter=reporter,
            verbose=verbose
        )
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS logging stdout'])

    def is_tool_ok(self) -> bool:
        '''
            Check is logger operational.

            :return: Is logger operational
            :rtype: <bool>
        '''
        return True


class ATSLoggingStreamTestCase(TestCase):
    '''
        Defines class ATSLoggingStreamTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSLogger.
        ATSLogger unit tests.

        It defines:

            :attributes:
                | ats_base_logging - API for checking base logging.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseLoggingStream not None.
                | test_tool_operational - Test is logger operational.
                | test_debug - Test debug log.
                | test_warning - Test warning log.
                | test_critical - Test critical log.
                | test_error - Test error log.
                | test_info - Test info log.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_logging: ATSBaseLoggingStream = ATSBaseLoggingStream()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test not None'''
        self.assertIsNotNone(self.ats_base_logging)

    def test_tool_operational(self) -> None:
        '''Test is logger operational'''
        self.assertTrue(self.ats_base_logging.is_tool_ok())

    def test_debug(self) -> None:
        '''Test ATS debug log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple debug', self.ats_base_logging.ATS_DEBUG
            )
        )

    def test_warning(self) -> None:
        '''Test ATS warning log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple warning', self.ats_base_logging.ATS_WARNING
            )
        )

    def test_critical(self) -> None:
        '''Test ATS critical log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple critical', self.ats_base_logging.ATS_CRITICAL
            )
        )

    def test_error(self) -> None:
        '''Test ATS error log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple error', self.ats_base_logging.ATS_ERROR
            )
        )

    def test_info(self) -> None:
        '''Test ATS info log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple info', self.ats_base_logging.ATS_INFO
            )
        )


if __name__ == '__main__':
    main()
