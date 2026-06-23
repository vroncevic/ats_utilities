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
    Creates test cases for checking functionalities of OptionManager.
Execute
    python3 -m unittest -v ats_option_parser_test
'''

from typing import Any
from unittest import TestCase, main, mock
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.option.parser_strategy import ParserStrategy
from ats_utilities.option.arg_parser import ArgParser
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import Reporter
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.option.command_option import CommandOption
from ats_utilities.option.ioption_command import IOptionCommand
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


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


class DummyOptionCommand(IOptionCommand):
    '''
        Dummy option command implementation for test verification.

        It defines:

            :attributes: None
            :methods:
                | name - Returns the name of the command.
                | help_text - Returns the help text of the command.
                | options - Returns the list of options for the command.
                | __str__ - Returns the string representation of option command.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the name of the command.

            :return: Name of the command.
            :rtype: <str>
        '''
        return 'dummy'

    @property
    def help_text(self) -> str:
        '''
            Returns the help text of the command.

            :return: Help text of the command.
            :rtype: <str>
        '''
        return 'dummy help text'

    @property
    def options(self) -> list[CommandOption]:
        '''
            Returns the list of options for the command.

            :return: List of options for the command.
            :rtype: <list[CommandOption]>
        '''
        return [
            CommandOption(
                name='--param',
                help_text='param help',
                default='default_val',
                required=False,
                choices=['default_val', 'other_val']
            ),
            CommandOption(
                name='--req-param',
                help_text='required param help',
                required=True
            )
        ]

    def __str__(self) -> str:
        '''
            Returns the string representation of option command.

            :return: String representation of option command.
            :rtype: <str>
        '''
        return 'DummyOptionCommand'


class OptionParserTestCase(TestCase):
    '''
        Defines class OptionParserTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of OptionManager.
        OptionManager unit tests.

        It defines:
            :attributes:
                | option_parser - API for checking option parser.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is OptionManager not None.
                | test_add_operation - Test adding operation.
                | test_add_version_operation - Test adding version operation.
                | test_str - Test string representation.
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
        '''Test for create OptionManager'''
        self.assertIsNotNone(self.option_parser)

    def test_add_operation(self) -> None:
        '''Test adding operation to parser.'''
        # Ne bi trebalo da baci izuzetak
        self.option_parser.add_operation('-t', '--test', help='test operation')

    def test_add_version_operation(self) -> None:
        '''Test adding version operation to parser.'''
        # Ne bi trebalo da baci izuzetak
        self.option_parser.add_version_operation('1.0.0')

    def test_str(self) -> None:
        '''Test string representation of option parser classes.'''
        self.assertIsInstance(str(self.option_parser), str)
        strategy = ParserStrategy()
        self.assertIsInstance(str(strategy), str)
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

    def test_initialization_failure(self) -> None:
        '''Test OptionManager initialization failure when parameters are invalid.'''
        invalid_bundle = OptionComponentBundle(
            parameters=123,  # type: ignore
            strategy=ParserStrategy()
        )
        manager = OptionManager(invalid_bundle)
        self.assertFalse(manager.is_initialized())

    def test_parser_strategy_uninitialized_parse(self) -> None:
        '''Test ParserStrategy parse before it is initialized.'''
        strategy = ParserStrategy()
        with self.assertRaises(ATSValueError):
            strategy.parse(['-t'])

    def test_command_option_creation(self) -> None:
        '''Test CommandOption creation and attributes.'''
        opt = CommandOption(
            name='--test-opt',
            help_text='test help',
            default='def',
            required=True,
            choices=['def', 'other']
        )
        self.assertEqual(opt.name, '--test-opt')
        self.assertEqual(opt.help_text, 'test help')
        self.assertEqual(opt.default, 'def')
        self.assertTrue(opt.required)
        self.assertEqual(opt.choices, ['def', 'other'])

    def test_parser_strategy_uninitialized_methods(self) -> None:
        '''Test ParserStrategy methods before setup is called.'''
        strategy = ParserStrategy()
        cmd = DummyOptionCommand()
        with self.assertRaises(ATSValueError):
            strategy.register_commands([cmd])
        with self.assertRaises(ATSValueError):
            strategy.parse_command(['dummy'])

    def test_register_commands_and_parse_command(self) -> None:
        '''Test register_commands and parse_command with actual commands.'''
        cmd = DummyOptionCommand()
        self.option_parser.register_commands([cmd])

        # Test command string representation
        self.assertEqual(str(cmd), 'DummyOptionCommand')

        # Test parsing command with custom arguments
        command_name, params = self.option_parser.parse_command(['dummy', '--req-param', 'test_value'])
        self.assertEqual(command_name, 'dummy')
        self.assertEqual(params.get('req_param'), 'test_value')
        self.assertEqual(params.get('param'), 'default_val')

    def test_parse_command_fallback_to_sys_argv(self) -> None:
        '''Test parse_command fallback to sys.argv when arguments are None.'''
        cmd = DummyOptionCommand()
        self.option_parser.register_commands([cmd])

        # Mock sys.argv to simulate running command with CLI arguments
        with mock.patch('sys.argv', ['dummy_prog', 'dummy', '--req-param', 'cli_val']):
            command_name, params = self.option_parser.parse_command(None)
            self.assertEqual(command_name, 'dummy')
            self.assertEqual(params.get('req_param'), 'cli_val')

    def test_command_option_with_name_as_none(self) -> None:
        cmd: CommandOption = CommandOption(None, 'help_text')
        with self.assertRaises(ATSValueError):
            cmd.validate()

    def test_command_option_with_help_text_as_none(self) -> None:
        cmd: CommandOption = CommandOption('name', None)
        with self.assertRaises(ATSValueError):
            cmd.validate()

    def test_command_option_with_default_as_none(self) -> None:
        cmd: CommandOption = CommandOption('name', 'help_text', None)
        with self.assertRaises(ATSValueError):
            cmd.validate()

    def test_command_option_with_required_as_none(self) -> None:
        cmd: CommandOption = CommandOption('name', 'help_text', 33, None)
        with self.assertRaises(ATSValueError):
            cmd.validate()

    def test_command_option_with_choices_as_none(self) -> None:
        cmd: CommandOption = CommandOption('name', 'help_text', 33, True, None)
        with self.assertRaises(ATSValueError):
            cmd.validate()

    def test_command_option_with_all_parameters(self) -> None:
        cmd: CommandOption = CommandOption('name', 'help_text', default='default_value', required=True, choices=['choice1', 'choice2'])
        cmd.validate()
        self.assertEqual(cmd.name, 'name')
        self.assertEqual(cmd.help_text, 'help_text')
        self.assertEqual(cmd.default, 'default_value')
        self.assertTrue(cmd.required)
        self.assertEqual(cmd.choices, ['choice1', 'choice2'])

    def test_command_option_with_all_parameters_to_dict(self) -> None:
        cmd: CommandOption = CommandOption('name', 'help_text', default='default_value', required=True, choices=['choice1', 'choice2'])
        my_command = cmd.to_dict()
        self.assertEqual(cmd.name, my_command.get('name'))
        self.assertEqual(cmd.help_text, my_command.get('help_text'))
        self.assertEqual(cmd.default, my_command.get('default'))
        self.assertTrue(cmd.required, my_command.get('required'))
        self.assertEqual(cmd.choices, my_command.get('choices'))

    def test_command_option_merge(self) -> None:
        '''Test ATSConfigLoaderBundle methods.'''
        option1 = CommandOption('name1', 'help_text1', default='default_value1', required=True, choices=['choice1', 'choice2'])
        option2 = CommandOption('name2', 'help_text2', default='default_value2', required=True, choices=['choice1', 'choice2'])

        option1.merge(option2)
        self.assertEqual(option1.name, 'name2')
        self.assertEqual(option1.help_text, 'help_text2')
        self.assertEqual(option1.default, 'default_value2')
        self.assertTrue(option1.required)
        self.assertEqual(option1.choices, ['choice1', 'choice2'])

    def test_command_option_merge_validation(self) -> None:
        '''Test CommandOption merge validation exceptions.'''
        option1 = CommandOption('name1', 'help_text1', default='default_value1', required=True, choices=['choice1', 'choice2'])
        option2 = CommandOption(None, 'help_text2', default='default_value2', required=True, choices=['choice1', 'choice2'])

        option1.merge(option2)
        self.assertEqual(option1.name, 'name1')
        self.assertEqual(option1.help_text, 'help_text2')
        self.assertEqual(option1.default, 'default_value2')
        self.assertTrue(option1.required)
        self.assertEqual(option1.choices, ['choice1', 'choice2'])

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
        self.mock_strategy = mock.MagicMock(spec=IParserStrategy)
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
