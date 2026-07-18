# -*- coding: UTF-8 -*-

'''
Module
    command_option_test.py
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
    Unit tests for CommandOption class.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.command.command_option import CommandOption

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CommandOptionTest(unittest.TestCase):
    '''
        Defines class CommandOptionTest with attribute(s) and method(s).
        Tests CommandOption dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests init logic of CommandOption.
                | test_validate_success - Tests successful validation.
                | test_validate_failures - Tests validation exceptions.
                | test_merge - Tests merge logic.
                | test_merge_exceptions - Tests merge error cases.
                | test_to_dict - Tests to_dict conversion.
    '''

    def test_init(self) -> None:
        '''
            Tests init logic of CommandOption.

            :exceptions: None.
        '''
        opt = CommandOption(name="test", help_text="help", choices=[1, 2])
        self.assertEqual(opt.choices, (1, 2))

    def test_validate_success(self) -> None:
        '''
            Tests successful validation.

            :exceptions: None.
        '''
        opt = CommandOption(
            name="test",
            help_text="help",
            action="store",
            default="default_val",
            required=True,
            choices=[1, 2],
            nargs=1
        )
        try:
            opt.validate()
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised exception: {e}")

    def test_validate_failures(self) -> None:
        '''
            Tests validation exceptions.

            :exceptions: None.
        '''
        # Missing required parameter
        opt_missing = CommandOption(name="test", help_text="help")
        with self.assertRaises(ATSValueError):
            opt_missing.validate()

        # Wrong types
        opt_type1 = CommandOption(
            name="test",
            help_text="help",
            action="store",
            default="default_val",
            required="not a bool",  # type: ignore
            choices=[1, 2],
            nargs=1
        )
        with self.assertRaises(ATSTypeError):
            opt_type1.validate()

        opt_type2 = CommandOption(
            name="test",
            help_text="help",
            action="store",
            default="default_val",
            required=True,
            choices=[1, 2],
            nargs=1
        )
        opt_type2.choices = 123  # type: ignore
        with self.assertRaises(ATSTypeError):
            opt_type2.validate()

        opt_type3 = CommandOption(
            name="test",
            help_text="help",
            action="store",
            default="default_val",
            required=True,
            choices=[1, 2],
            nargs=[]  # type: ignore
        )
        with self.assertRaises(ATSTypeError):
            opt_type3.validate()

    def test_merge(self) -> None:
        '''
            Tests merge logic.

            :exceptions: None.
        '''
        opt1 = CommandOption(name="opt1", help_text="help1", action="store")
        opt2 = CommandOption(
            name="opt1",
            help_text="help2",
            action="store",
            default="val",
            required=True,
            choices=[1, 2],
            nargs=1
        )
        opt1.merge(opt2)
        self.assertEqual(opt1.help_text, "help2")
        self.assertEqual(opt1.default, "val")
        self.assertTrue(opt1.required)
        self.assertEqual(opt1.choices, (1, 2))
        self.assertEqual(opt1.nargs, 1)

        # Merge with an option that has None for optional fields
        opt3 = CommandOption(
            name="opt1",
            help_text="help3",
            action="store",
            default="val",
            required=True,
            choices=[1, 2],
            nargs=None
        )
        opt4 = CommandOption(
            name="opt1",
            help_text="help4",
            action=None,
            default=None,
            required=None,  # type: ignore
            choices=None,
            nargs=1
        )
        opt3.merge(opt4)
        self.assertEqual(opt3.help_text, "help4")
        self.assertEqual(opt3.nargs, 1)

    def test_merge_exceptions(self) -> None:
        '''
            Tests merge error cases.

            :exceptions: None.
        '''
        opt = CommandOption(name="opt1", help_text="help1")
        with self.assertRaises(ATSValueError):
            opt.merge(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            opt.merge("not a CommandOption")  # type: ignore

    def test_to_dict(self) -> None:
        '''
            Tests to_dict conversion.

            :exceptions: None.
        '''
        opt = CommandOption(
            name="test",
            help_text="help",
            action="store",
            default="val",
            required=True,
            choices=[1, 2],
            nargs=1
        )
        expected = {
            "name": "test",
            "help_text": "help",
            "action": "store",
            "default": "val",
            "required": True,
            "choices": (1, 2),
            "nargs": 1
        }
        self.assertEqual(opt.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
