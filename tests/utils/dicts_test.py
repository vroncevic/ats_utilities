# -*- coding: UTF-8 -*-

'''
Module
    dicts_test.py
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
    Unit tests for factory dict utility functions.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.utils.dicts import (
    cherry_pick_dict,
    get_first_available,
    has_required_keys,
    require_keys,
)

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DictsTest(unittest.TestCase):
    '''
        Defines class DictsTest with attribute(s) and method(s).
        Tests factory dict utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_cherry_pick_dict - Tests cherry_pick_dict logic.
                | test_has_required_keys - Tests has_required_keys logic.
                | test_require_keys_valid - Tests require_keys when all keys are present.
                | test_require_keys_missing - Tests require_keys when some keys are missing.
                | test_require_keys_invalid_types - Tests require_keys type validation.
                | test_require_keys_custom_exception - Tests require_keys raising custom exception.
                | test_require_keys_custom_message - Tests require_keys with custom error message.
                | test_get_first_available - Tests get_first_available logic.
                | test_get_first_available_invalid_types - Tests get_first_available type validation.
    '''

    def test_cherry_pick_dict(self) -> None:
        '''
            Tests cherry_pick_dict logic.

            :exceptions: None.
        '''
        source = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(cherry_pick_dict(source, frozenset(["a", "c"])), {"a": 1, "c": 3})
        self.assertEqual(cherry_pick_dict(source, frozenset(["a", "z"])), {"a": 1})
        self.assertEqual(cherry_pick_dict(source, frozenset()), {})
        self.assertEqual(cherry_pick_dict({}, frozenset(["a"])), {})

    def test_has_required_keys(self) -> None:
        '''
            Tests has_required_keys logic.

            :exceptions: None.
        '''
        source = {"a": 1, "b": 2}
        self.assertTrue(has_required_keys(source, frozenset(["a"])))
        self.assertTrue(has_required_keys(source, frozenset(["a", "b"])))
        self.assertFalse(has_required_keys(source, frozenset(["a", "c"])))
        self.assertFalse(has_required_keys({}, frozenset(["a"])))

    def test_require_keys_valid(self) -> None:
        '''
            Tests require_keys when all keys are present.

            :exceptions: None.
        '''
        try:
            require_keys({"a": 1, "b": 2}, frozenset(["a", "b"]))
        except ATSValueError:
            self.fail("require_keys raised ATSValueError unexpectedly.")

    def test_require_keys_missing(self) -> None:
        '''
            Tests require_keys when some keys are missing.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            require_keys({"a": 1}, frozenset(["a", "b"]))
        self.assertIn("mapping is missing required keys", str(ctx.exception))
        self.assertIn("b", str(ctx.exception))

    def test_require_keys_invalid_types(self) -> None:
        '''
            Tests require_keys type validation.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError):
            require_keys("not a dict", frozenset(["a"]))  # type: ignore

        with self.assertRaises(ATSTypeError):
            require_keys({"a": 1}, ["a"])  # type: ignore

    def test_require_keys_custom_exception(self) -> None:
        '''
            Tests require_keys raising custom exception.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            require_keys({"a": 1}, frozenset(["a", "b"]), exception_class=ValueError)

    def test_require_keys_custom_message(self) -> None:
        '''
            Tests require_keys with custom error message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            require_keys({"a": 1}, frozenset(["a", "b"]), exc_message="custom message")
        self.assertIn("dictstest::test_require_keys_custom_message - custom message", str(ctx.exception))

    def test_get_first_available(self) -> None:
        '''
            Tests get_first_available logic.

            :exceptions: None.
        '''
        source = {"a": "", "b": 0, "c": False, "d": "value"}

        self.assertEqual(get_first_available(source, ["a", "b"]), 0)
        self.assertEqual(get_first_available(source, ["a", "c"]), False)
        self.assertEqual(get_first_available(source, ["a", "d"]), "value")
        self.assertEqual(get_first_available(source, ["x", "y"]), None)
        self.assertEqual(get_first_available({}, ["a"]), None)
        self.assertEqual(get_first_available(source, []), None)

    def test_get_first_available_invalid_types(self) -> None:
        '''
            Tests get_first_available type validation.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError):
            get_first_available("not a dict", ["a"])  # type: ignore

        with self.assertRaises(ATSTypeError):
            get_first_available({"a": 1}, 123)  # type: ignore


if __name__ == "__main__":
    unittest.main()
