# -*- coding: UTF-8 -*-

'''
Module
    ats_option_engine_test.py
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
    Creates test cases for checking OptionManager.
Execute
    python3 -m unittest -v tests/option/ats_option_engine_test.py
'''

from typing import Any
from unittest import TestCase, main, mock
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.option.strategy.parser_strategy import ParserStrategy
from ats_utilities.option.parser.engine import ArgParser
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import Reporter
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ATSBaseOptionParser(OptionManager):
    '''Simple Class for checking OptionManager.'''

    def __init__(
        self,
        ats_info: dict[str, Any],
        checker: IChecker = Checker(),
        reporter: IReporter = Reporter(),
        verbose: bool = False
    ) -> None:
        '''Initial constructor.'''
        context = ContextBundle(
            checker=checker,
            reporter=reporter,
            verbose=verbose
        )
        bundle = OptionComponentBundle(
            parameters=ats_info,
            strategy=ParserStrategy(),
            context_bundle=context
        )
        super().__init__(bundle)
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
    '''Test cases for OptionManager.'''

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
        '''Test for create OptionManager'''
        self.assertIsNotNone(self.option_parser)

    def test_add_operation(self) -> None:
        '''Test adding operation to parser.'''
        self.option_parser.add_operation('-t', '--test', help='test operation')

    def test_add_version_operation(self) -> None:
        '''Test adding version operation to parser.'''
        self.option_parser.add_version_operation('1.0.0')

    def test_str(self) -> None:
        '''Test string representation of option parser classes.'''
        self.assertIsInstance(str(self.option_parser), str)
        arg_parser = ArgParser(self.ats_info)
        self.assertIsInstance(str(arg_parser), str)

    def test_arg_parser_error(self) -> None:
        '''Test ArgParser error method.'''
        arg_parser = ArgParser(self.ats_info)
        with self.assertRaises(SystemExit) as cm:
            arg_parser.error('Test error message')
        self.assertEqual(cm.exception.code, 2)

    def test_parse_arguments(self) -> None:
        '''Test actual parse_args and parse_input_args in OptionManager.'''
        self.option_parser.add_operation('-t', '--test', help='test operation')
        res1 = self.option_parser.parse_args(['-t', 'value'])
        self.assertIsNotNone(res1)
        res2 = self.option_parser.parse_input_args(['-t', 'value'])
        self.assertIsNotNone(res2)

    def test_add_version_operation_none(self) -> None:
        '''Test adding version operation with None/empty version.'''
        self.option_parser.add_version_operation(None)
        self.option_parser.add_version_operation('')

    def test_register_and_parse_commands(self) -> None:
        '''Test register_commands and parse_command in OptionManager.'''
        from ats_utilities.option.command.command_option import CommandOption
        from ats_utilities.option.command.ioption_command import IOptionCommand
        
        class LocalDummyCommand(IOptionCommand):
            @property
            def name(self) -> str:
                return 'dummy'
            @property
            def help_text(self) -> str:
                return 'help'
            @property
            def options(self) -> list[CommandOption]:
                return [
                    CommandOption(name='--param', help_text='p', required=True)
                ]
            def __str__(self) -> str:
                return 'LocalDummyCommand'

        cmd = LocalDummyCommand()
        self.option_parser.register_commands([cmd])
        cmd_name, params = self.option_parser.parse_command(['dummy', '--param', 'value'])
        self.assertEqual(cmd_name, 'dummy')
        self.assertEqual(params.get('param'), 'value')

    def test_initialization_failure(self) -> None:
        '''Test OptionManager initialization failure when parameters are invalid.'''
        invalid_bundle = OptionComponentBundle(
            parameters=123,  # type: ignore
            strategy=ParserStrategy()
        )
        manager = OptionManager(invalid_bundle)
        self.assertFalse(manager.is_initialized())

    @mock.patch('ats_utilities.option.component_bundle.make_component')
    def test_initialization_unexpected_exception(self, mock_make_component) -> None:
        '''Test OptionManager initialization unexpected exception.'''
        mock_make_component.side_effect = Exception('Unexpected')
        manager = OptionManager()
        with self.assertRaises(ATSValueError):
            manager.is_initialized()
        self.assertFalse(manager._is_initialized)

    def test_get_shared_context(self) -> None:
        '''Test get_shared_context returns ContextBundle.'''
        context = self.option_parser.get_shared_context()
        self.assertIsInstance(context, ContextBundle)


class OptionParserUnitTestCase(TestCase):
    '''Unit tests for IOptionManager interface using mocks.'''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.mock_parser = mock.MagicMock(spec=IOptionManager)

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
