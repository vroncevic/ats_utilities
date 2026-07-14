# -*- coding: UTF-8 -*-

'''
Module
    ats_parser_strategy_test.py
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
    Creates test cases for checking ParserStrategy.
Execute
    python3 -m unittest -v tests/option/strategy/ats_parser_strategy_test.py
'''

from typing import Any
from unittest import TestCase, main, mock
from ats_utilities.option.strategy.parser_strategy import ParserStrategy
from ats_utilities.option.command.command_option import CommandOption
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.context_bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class DummyOptionCommand(IOptionCommand):
    '''Dummy option command implementation for test verification.'''

    @property
    def name(self) -> str:
        return 'dummy'

    @property
    def help_text(self) -> str:
        return 'dummy help text'

    @property
    def options(self) -> list[CommandOption]:
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
        return 'DummyOptionCommand'


class DummyActionNargsCommand(IOptionCommand):
    '''Dummy command with action and nargs.'''

    @property
    def name(self) -> str:
        return 'custom'

    @property
    def help_text(self) -> str:
        return 'custom help text'

    @property
    def options(self) -> list[CommandOption]:
        return [
            CommandOption(
                name='--flag',
                help_text='flag help',
                action='store_true',
                required=False
            ),
            CommandOption(
                name='--items',
                help_text='items list help',
                nargs='*',
                required=False
            )
        ]

    def __str__(self) -> str:
        return 'DummyActionNargsCommand'


class ParserStrategyTestCase(TestCase):
    '''Test cases for ParserStrategy.'''

    def setUp(self) -> None:
        self.ats_info = {
            'ats_name': 'TestTool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        self.context = ContextBundle()
        self.strategy = ParserStrategy(self.context)

    def test_parser_strategy_uninitialized_methods(self) -> None:
        '''Test ParserStrategy methods before setup is called.'''
        cmd = DummyOptionCommand()
        with self.assertRaises(ATSValueError):
            self.strategy.register_commands([cmd])
        with self.assertRaises(ATSValueError):
            self.strategy.parse_command(['dummy'])
        with self.assertRaises(ATSValueError):
            self.strategy.parse(['-t'])

    def test_register_and_parse_commands(self) -> None:
        '''Test register_commands and parse_command with actual commands.'''
        self.strategy.setup(self.ats_info)
        cmd = DummyOptionCommand()
        
        # Test registering commands
        self.strategy.register_commands([cmd])
        self.assertEqual(str(cmd), 'DummyOptionCommand')

        # Test parsing command with custom arguments
        command_name, params = self.strategy.parse_command(['dummy', '--req-param', 'test_value'])
        self.assertEqual(command_name, 'dummy')
        self.assertEqual(params.get('req_param'), 'test_value')
        self.assertEqual(params.get('param'), 'default_val')

    def test_parse_command_fallback_to_sys_argv(self) -> None:
        '''Test parse_command fallback to sys.argv when arguments are None.'''
        self.strategy.setup(self.ats_info)
        cmd = DummyOptionCommand()
        self.strategy.register_commands([cmd])

        with mock.patch('sys.argv', ['dummy_prog', 'dummy', '--req-param', 'cli_val']):
            command_name, params = self.strategy.parse_command(None)
            self.assertEqual(command_name, 'dummy')
            self.assertEqual(params.get('req_param'), 'cli_val')

    def test_parser_strategy_more_coverage(self) -> None:
        '''Test strategy where subparsers is already initialized, options have action/nargs.'''
        self.strategy.setup(self.ats_info)
        cmd1 = DummyActionNargsCommand()
        
        # Register first time (initializes _subparsers)
        self.strategy.register_commands([cmd1])
        
        # Define a second command with a different name to avoid argparse conflicts
        class DummySecondCommand(DummyActionNargsCommand):
            @property
            def name(self) -> str:
                return 'custom_other'
        
        cmd2 = DummySecondCommand()
        # Register second time (re-uses existing _subparsers, covering 178->183 branch)
        self.strategy.register_commands([cmd2])

        # Test options with action and nargs (covers lines 190 and 196)
        command_name, params = self.strategy.parse_command(['custom', '--flag', '--items', 'a', 'b'])
        self.assertEqual(command_name, 'custom')
        self.assertTrue(params.get('flag'))
        self.assertEqual(params.get('items'), ['a', 'b'])

    def test_str(self) -> None:
        '''Test string representation.'''
        self.assertIsInstance(str(self.strategy), str)


if __name__ == '__main__':
    main()
