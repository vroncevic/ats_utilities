# -*- coding: UTF-8 -*-

'''
Module
    ats_option_parser_test.py
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
    Defines classes OptionParserTestCase and OptionParserUnitTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSOptionManager.
Execute
    python3 -m unittest -v ats_option_parser_test
'''

from typing import List, Dict, Any
from unittest import TestCase, main, mock
from ats_utilities.option.engine import ATSOptionManager
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.option.iparser_strategy import IArgParserStrategy
from ats_utilities.option.parser_strategy import ATSArgParserStrategy
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
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


class ATSBaseOptionParser(ATSOptionManager):
    '''Simple Class for checking ATSOptionManager.'''

    def __init__(
        self,
        ats_info: Dict[str, Any],
        checker: IChecker = ATSChecker(),
        reporter: IReporter = ATSReporter(),
        verbose: bool = False
    ) -> None:
        '''Initial constructor.'''
        super().__init__(ats_info, ATSArgParserStrategy(reporter), checker, reporter, verbose)
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS option parser'])

    def is_tool_ok(self) -> bool:
        '''
            Check is option parser operational.

            :return: Is option parser operational
            :rtype: <bool>
        '''
        return True


class OptionParserTestCase(TestCase):
    '''
        Defines class OptionParserTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSOptionManager.
        ATSOptionManager unit tests.

        It defines:
            :attributes:
                | option_parser - API for checking option parser.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSOptionManager not None.
                | test_add_operation - Test adding operation.
                | test_add_version_operation - Test adding version operation.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_info = {
            'ats_name': 'TestTool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        self.option_parser: ATSBaseOptionParser = ATSBaseOptionParser(self.ats_info)

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create ATSOptionManager'''
        self.assertIsNotNone(self.option_parser)

    def test_add_operation(self) -> None:
        '''Test adding operation to parser.'''
        # Ne bi trebalo da baci izuzetak
        self.option_parser.add_operation('-t', '--test', help='test operation')

    def test_add_version_operation(self) -> None:
        '''Test adding version operation to parser.'''
        # Ne bi trebalo da baci izuzetak
        self.option_parser.add_version_operation('1.0.0')


class OptionParserUnitTestCase(TestCase):
    '''
        Unit tests for IOptionManager interface using mocks.

        It defines:
            :methods:
                | setUp - Set up test environment with mocks.
                | test_mock_add_operation - Test mock interaction for add_operation.
                | test_mock_parse_args - Test mock interaction for parse_args.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.mock_parser = mock.MagicMock(spec=IOptionManager)
        self.mock_strategy = mock.MagicMock(spec=IArgParserStrategy)
        self.mock_checker = mock.MagicMock(spec=IChecker)
        self.mock_reporter = mock.MagicMock(spec=IReporter)

    def test_mock_add_operation(self) -> None:
        '''Test mock interaction for add_operation.'''
        self.mock_parser.add_operation('-v', '--verbose', action='store_true')
        self.mock_parser.add_operation.assert_called_once_with(
            '-v', '--verbose', action='store_true'
        )

    def test_mock_parse_args(self) -> None:
        '''Test mock interaction for parse_args.'''
        self.mock_parser.parse_args.return_value = mock.MagicMock()
        result = self.mock_parser.parse_args(['-v'])
        self.assertIsNotNone(result)
        self.mock_parser.parse_args.assert_called_once_with(['-v'])


if __name__ == '__main__':
    main()
