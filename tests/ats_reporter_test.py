# -*- coding: UTF-8 -*-

'''
Module
    ats_reporter_test.py
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
    Defines classes ReporterTestCase and ReporterUnitTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSReporter.
Execute
    python3 -m unittest -v ats_reporter_test
'''

from typing import List
from unittest import TestCase, main, mock
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ReporterTestCase(TestCase):
    '''
        Defines class ReporterTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSReporter.
        ATSReporter unit tests.

        It defines:

            :attributes:
                | reporter - API for checking ATSReporter.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSReporter not None.
                | test_success - Test success message.
                | test_error - Test error message.
                | test_warning - Test warning message.
                | test_verbose - Test info message.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.reporter: ATSReporter = ATSReporter()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create ATSReporter'''
        self.assertIsNotNone(self.reporter)

    def test_success(self) -> None:
        '''Test success message'''
        self.reporter.success(['test success'])

    def test_error(self) -> None:
        '''Test error message'''
        self.reporter.error(['test error'])

    def test_warning(self) -> None:
        '''Test warning message'''
        self.reporter.warning(['test warning'])

    def test_verbose(self) -> None:
        '''Test info message'''
        self.reporter.verbose(True, ['test info'])


class ReporterUnitTestCase(TestCase):
    '''
        Unit tests for IReporter interface using mocks.

        It defines:

            :attributes:
                | mock_reporter - Mocked IReporter.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_mock_success - Test success call on mock.
                | test_mock_error - Test error call on mock.
                | test_mock_verbose - Test verbose call on mock.
                | test_mock_warning - Test warning call on mock.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.mock_reporter = mock.MagicMock(spec=IReporter)

    def test_mock_success(self) -> None:
        '''Test success call on mock.'''
        messages = ['mock success']
        self.mock_reporter.success(messages)
        self.mock_reporter.success.assert_called_once_with(messages)

    def test_mock_error(self) -> None:
        '''Test error call on mock.'''
        messages = ['mock error']
        self.mock_reporter.error(messages)
        self.mock_reporter.error.assert_called_once_with(messages)

    def test_mock_verbose(self) -> None:
        '''Test verbose call on mock.'''
        messages = ['mock verbose']
        verbose_flag = True
        self.mock_reporter.verbose(verbose_flag, messages)
        self.mock_reporter.verbose.assert_called_once_with(verbose_flag, messages)

    def test_mock_warning(self) -> None:
        '''Test error call on mock.'''
        messages = ['mock warning']
        self.mock_reporter.warning(messages)
        self.mock_reporter.warning.assert_called_once_with(messages)


if __name__ == '__main__':
    main()
