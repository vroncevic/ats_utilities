# -*- coding: UTF-8 -*-

'''
Module
    boolean_test.py
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
    Unit tests for factory boolean utilities.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSValueError
from ats_utilities.utils.boolean import str_bool_to_bool

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class BooleanTest(unittest.TestCase):
    '''
        Defines class BooleanTest with attribute(s) and method(s).
        Tests factory boolean utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_str_bool_to_bool_true - Tests str_bool_to_bool with 'True'.
                | test_str_bool_to_bool_false - Tests str_bool_to_bool with 'False'.
                | test_str_bool_to_bool_invalid - Tests str_bool_to_bool with an invalid string.
                | test_str_bool_to_bool_custom_exception - Tests str_bool_to_bool with a custom exception class.
                | test_str_bool_to_bool_custom_message - Tests str_bool_to_bool with a custom exception message.
    '''

    def test_str_bool_to_bool_true(self) -> None:
        '''
            Tests str_bool_to_bool with 'True'.

            :exceptions: None.
        '''
        self.assertTrue(str_bool_to_bool('True', 'booleantest::test_str_bool_to_bool_true'))

    def test_str_bool_to_bool_false(self) -> None:
        '''
            Tests str_bool_to_bool with 'False'.

            :exceptions: None.
        '''
        self.assertFalse(str_bool_to_bool('False', 'booleantest::test_str_bool_to_bool_false'))

    def test_str_bool_to_bool_invalid(self) -> None:
        '''
            Tests str_bool_to_bool with an invalid string.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            str_bool_to_bool('abc', 'booleantest::test_str_bool_to_bool_invalid')
        self.assertIn("can not convert abc to bool", str(ctx.exception))

    def test_str_bool_to_bool_custom_exception(self) -> None:
        '''
            Tests str_bool_to_bool with a custom exception class.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            str_bool_to_bool('abc', 'booleantest::test_str_bool_to_bool_custom_exception', exc_class=ValueError)

    def test_str_bool_to_bool_custom_message(self) -> None:
        '''
            Tests str_bool_to_bool with a custom exception message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            str_bool_to_bool('abc', 'booleantest::test_str_bool_to_bool_custom_message', exc_message="custom message")
        self.assertIn("booleantest::test_str_bool_to_bool_custom_message - custom message", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
