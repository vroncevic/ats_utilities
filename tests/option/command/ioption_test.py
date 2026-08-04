# -*- coding: UTF-8 -*-

'''
Module
    ioption_test.py
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
    Unit tests for IOption protocol.
'''

from __future__ import annotations

import unittest
from collections.abc import Sequence

from ats_utilities.option.command.ioption import IOption

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyOptionValid:
    '''Dummy class that implements IOption completely.'''

    @property
    def name(self) -> str:
        return "--verbose"

    @property
    def help_text(self) -> str:
        return "Enable verbose logging"

    @property
    def action(self) -> str | None:
        return "store_true"

    @property
    def default(self) -> object | None:
        return False

    @property
    def required(self) -> bool:
        return False

    @property
    def choices(self) -> Sequence[object] | None:
        return None

    @property
    def nargs(self) -> str | int | None:
        return None

    def to_kwargs(self) -> dict[str, object]:
        return {
            "help": self.help_text,
            "action": self.action,
            "default": self.default,
            "required": self.required,
        }


class DummyOptionInvalid:
    '''Dummy class that does NOT implement IOption.'''
    pass


class IOptionTest(unittest.TestCase):
    '''
        Defines class IOptionTest with method(s).
        Tests IOption protocol behavior.

        It defines:

            :attributes: None.
            :methods:
                | test_isinstance_valid - Tests isinstance check with a valid implementation.
                | test_isinstance_invalid - Tests isinstance check with an invalid implementation.
    '''

    def test_isinstance_valid(self) -> None:
        '''
            Tests isinstance check with a valid implementation.

            :exceptions: None.
        '''
        dummy = DummyOptionValid()
        self.assertIsInstance(dummy, IOption)

    def test_isinstance_invalid(self) -> None:
        '''
            Tests isinstance check with an invalid implementation.

            :exceptions: None.
        '''
        dummy = DummyOptionInvalid()
        self.assertNotIsInstance(dummy, IOption)


if __name__ == "__main__":
    unittest.main()
