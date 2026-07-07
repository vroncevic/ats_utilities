# -*- coding: UTF-8 -*-

'''
Module
    ats_command_option_test.py
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
    Creates test cases for checking CommandOption.
Execute
    python3 -m unittest -v tests/option/command/ats_command_option_test.py
'''

from unittest import TestCase, main
from ats_utilities.option.command.command_option import CommandOption
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class CommandOptionTestCase(TestCase):
    '''Test cases for CommandOption.'''

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
        self.assertEqual(opt.choices, ('def', 'other'))

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
        cmd: CommandOption = CommandOption('name', 'help_text', action='store', default='default_value', required=True, choices=['choice1', 'choice2'], nargs=1)
        cmd.validate()
        self.assertEqual(cmd.name, 'name')
        self.assertEqual(cmd.help_text, 'help_text')
        self.assertEqual(cmd.action, 'store')
        self.assertEqual(cmd.default, 'default_value')
        self.assertTrue(cmd.required)
        self.assertEqual(cmd.choices, ('choice1', 'choice2'))
        self.assertEqual(cmd.nargs, 1)

    def test_command_option_with_all_parameters_to_dict(self) -> None:
        cmd: CommandOption = CommandOption('name', 'help_text', action='store', default='default_value', required=True, choices=['choice1', 'choice2'], nargs=1)
        my_command = cmd.to_dict()
        self.assertEqual(cmd.name, my_command.get('name'))
        self.assertEqual(cmd.help_text, my_command.get('help_text'))
        self.assertEqual(cmd.action, my_command.get('action'))
        self.assertEqual(cmd.default, my_command.get('default'))
        self.assertTrue(cmd.required, my_command.get('required'))
        self.assertEqual(cmd.choices, my_command.get('choices'))
        self.assertEqual(cmd.nargs, my_command.get('nargs'))

    def test_command_option_merge(self) -> None:
        '''Test CommandOption merge.'''
        option1 = CommandOption('name1', 'help_text1', action='store1', default='default_value1', required=True, choices=['choice1', 'choice2'], nargs=1)
        option2 = CommandOption('name2', 'help_text2', action='store2', default='default_value2', required=True, choices=['choice1', 'choice2'], nargs=2)

        option1.merge(option2)
        self.assertEqual(option1.name, 'name2')
        self.assertEqual(option1.help_text, 'help_text2')
        self.assertEqual(option1.action, 'store2')
        self.assertEqual(option1.default, 'default_value2')
        self.assertTrue(option1.required)
        self.assertEqual(option1.choices, ('choice1', 'choice2'))
        self.assertEqual(option1.nargs, 2)

    def test_command_option_merge_validation(self) -> None:
        '''Test CommandOption merge validation exceptions.'''
        option1 = CommandOption('name1', 'help_text1', action='store1', default='default_value1', required=True, choices=['choice1', 'choice2'], nargs=1)
        option2 = CommandOption(None, 'help_text2', action='store2', default='default_value2', required=True, choices=['choice1', 'choice2'], nargs=2)

        option1.merge(option2)
        self.assertEqual(option1.name, 'name1')
        self.assertEqual(option1.help_text, 'help_text2')
        self.assertEqual(option1.action, 'store2')
        self.assertEqual(option1.default, 'default_value2')
        self.assertTrue(option1.required)
        self.assertEqual(option1.choices, ('choice1', 'choice2'))
        self.assertEqual(option1.nargs, 2)

    def test_command_option_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a CommandOption.'''
        option = CommandOption('name1', 'help_text1')
        with self.assertRaises(ATSTypeError):
            option.merge("not_a_command_option")


if __name__ == '__main__':
    main()
