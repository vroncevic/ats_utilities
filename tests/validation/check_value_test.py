# -*- coding: UTF-8 -*-

'''
Module
    check_value_test.py
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
    Unit tests for value checking utility functions.
'''

from __future__ import annotations

from typing import Any
import unittest

from ats_utilities.exceptions import ATSValueError
from ats_utilities.validation.check_value import not_empty, not_none, not_satisfied

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CheckValueTest(unittest.TestCase):
    '''
        Defines class CheckValueTest with attribute(s) and method(s).
        Tests value checking utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_not_none_valid - Tests not_none with a non-None value.
                | test_not_none_invalid - Tests not_none with None.
                | test_not_none_custom_exception - Tests not_none raising a custom exception class.
                | test_not_none_custom_message - Tests not_none with a custom exception message.
                | test_not_empty_valid - Tests not_empty with non-empty values (including 0 and False).
                | test_not_empty_invalid - Tests not_empty with empty values.
                | test_not_empty_custom_exception - Tests not_empty raising a custom exception class.
                | test_not_empty_custom_message - Tests not_empty with a custom exception message.
                | test_not_satisfied_valid - Tests not_satisfied with False status.
                | test_not_satisfied_invalid - Tests not_satisfied with True status.
                | test_not_satisfied_custom_exception - Tests not_satisfied raising a custom exception class.
                | test_not_satisfied_custom_message - Tests not_satisfied with a custom exception message.
    '''

    def test_not_none_valid(self) -> None:
        '''
            Tests not_none with a non-None value.

            :exceptions: None.
        '''
        try:
            not_none(1)
            not_none("test")
            not_none([])
            not_none(False)
        except ATSValueError:
            self.fail("not_none raised ATSValueError unexpectedly for non-None values.")

    def test_not_none_invalid(self) -> None:
        '''
            Tests not_none with None.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            not_none(None)
        self.assertIn("value must not be None", str(ctx.exception))

    def test_not_none_custom_exception(self) -> None:
        '''
            Tests not_none raising a custom exception class.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            not_none(None, exception_class=ValueError)

    def test_not_none_custom_message(self) -> None:
        '''
            Tests not_none with a custom exception message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            not_none(None, exc_message="custom error msg")
        self.assertIn("checkvaluetest::test_not_none_custom_message - custom error msg", str(ctx.exception))

    def test_not_empty_valid(self) -> None:
        '''
            Tests not_empty with non-empty values.

            :exceptions: None.
        '''
        try:
            not_empty(1)
            not_empty("test")
            not_empty([1])
            not_empty(0)
            not_empty(False)
        except ATSValueError:
            self.fail("not_empty raised ATSValueError unexpectedly for non-empty values.")

    def test_not_empty_invalid(self) -> None:
        '''
            Tests not_empty with empty values.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            not_empty("")
        self.assertIn("value must not be empty", str(ctx.exception))

        with self.assertRaises(ATSValueError):
            not_empty([])

        with self.assertRaises(ATSValueError):
            not_empty({})

        with self.assertRaises(ATSValueError):
            not_empty(())

        with self.assertRaises(ATSValueError):
            not_empty(None)

    def test_not_empty_custom_exception(self) -> None:
        '''
            Tests not_empty raising a custom exception class.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            not_empty("", exception_class=ValueError)

    def test_not_empty_custom_message(self) -> None:
        '''
            Tests not_empty with a custom exception message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            not_empty("", exc_message="custom error msg")
        self.assertIn("checkvaluetest::test_not_empty_custom_message - custom error msg", str(ctx.exception))

    def test_not_satisfied_valid(self) -> None:
        '''
            Tests not_satisfied with False status.

            :exceptions: None.
        '''
        try:
            not_satisfied(False)
        except ATSValueError:
            self.fail("not_satisfied raised ATSValueError unexpectedly for False status.")

    def test_not_satisfied_invalid(self) -> None:
        '''
            Tests not_satisfied with True status.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            not_satisfied(True)
        self.assertIn("condition not satisfied", str(ctx.exception))

    def test_not_satisfied_custom_exception(self) -> None:
        '''
            Tests not_satisfied raising a custom exception class.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            not_satisfied(True, exception_class=ValueError)

    def test_not_satisfied_custom_message(self) -> None:
        '''
            Tests not_satisfied with a custom exception message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            not_satisfied(True, exc_message="custom error msg")
        self.assertIn("checkvaluetest::test_not_satisfied_custom_message - custom error msg", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
