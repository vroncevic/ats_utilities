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
    Unit tests for OptionData class.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.command.data import OptionData
from ats_utilities.option.command.data_validator import OptionDataValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CommandOptionTest(unittest.TestCase):
    '''
        Defines class CommandOptionTest with attribute(s) and method(s).
        Tests OptionData and OptionDataValidator logic.
    '''

    def test_init(self) -> None:
        '''
            Tests init logic of OptionData.
        '''
        opt = OptionData(
            name="test",
            help_text="help",
            choices=[1, 2],
            action=None,
            default=None,
            required=False,
            nargs=None
        )
        self.assertEqual(opt.choices, (1, 2))

    def test_validate_success(self) -> None:
        '''
            Tests successful validation.
        '''
        opt = OptionData(
            name="test",
            help_text="help",
            action="store",
            default="default_val",
            required=True,
            choices=[1, 2],
            nargs=1
        )
        try:
            OptionDataValidator.validate(opt)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised exception: {e}")

    def test_validate_failures(self) -> None:
        '''
            Tests validation exceptions.
        '''
        # Missing name (not possible since dataclass requires it, but let's check None via type bypass if needed or validation checks)
        # Instead, let's ... invalid type for name
        opt_type = OptionData(
            name=123,  # type: ignore
            help_text="help",
            action=None,
            default=None,
            required=False,
            choices=None,
            nargs=None
        )
        with self.assertRaises(ATSTypeError):
            OptionDataValidator.validate(opt_type)

        # Missing help text (invalid type)
        opt_help = OptionData(
            name="test",
            help_text=None,  # type: ignore
            action=None,
            default=None,
            required=False,
            choices=None,
            nargs=None
        )
        with self.assertRaises(ATSValueError):
            OptionDataValidator.validate(opt_help)

        # Wrong action type
        opt_action = OptionData(
            name="test",
            help_text="help",
            action=123,  # type: ignore
            default=None,
            required=False,
            choices=None,
            nargs=None
        )
        with self.assertRaises(ATSTypeError):
            OptionDataValidator.validate(opt_action)

        # Wrong required type
        opt_required = OptionData(
            name="test",
            help_text="help",
            action=None,
            default=None,
            required="not a bool",  # type: ignore
            choices=None,
            nargs=None
        )
        with self.assertRaises(ATSTypeError):
            OptionDataValidator.validate(opt_required)

    def test_validate_none_fields(self) -> None:
        opt = OptionData(
            name="test",
            help_text="help",
            action=None,
            default=None,
            required=None,  # type: ignore
            choices=None,
            nargs=None
        )
        try:
            OptionDataValidator.validate(opt)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised exception: {e}")

    def test_to_dict(self) -> None:
        '''
            Tests to_dict conversion.
        '''
        opt = OptionData(
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
