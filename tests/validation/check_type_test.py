# -*- coding: UTF-8 -*-

'''
Module
    check_type_test.py
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
    Unit tests for type utility functions.
'''

from __future__ import annotations

from typing import Any, Union
import unittest

from ats_utilities.exceptions import ATSTypeError
from ats_utilities.validation.check_type import _resolve_type, istype

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CheckTypeTest(unittest.TestCase):
    '''
        Defines class CheckTypeTest with attribute(s) and method(s).
        Tests type validation utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_resolve_type_concrete - Tests resolving concrete types.
                | test_resolve_type_union - Tests resolving union types.
                | test_resolve_type_nested_union - Tests resolving nested union types.
                | test_resolve_type_nested_union_mock - Tests resolving nested union types using mocks.
                | test_resolve_type_generic - Tests resolving generic types.
                | test_istype_valid_single - Tests checking valid instances against a single type.
                | test_istype_valid_tuple - Tests checking valid instances against a tuple of types.
                | test_istype_valid_union - Tests checking valid instances against union types.
                | test_istype_invalid_single - Tests checking invalid instances against a single type.
                | test_istype_invalid_tuple - Tests checking invalid instances against a tuple of types.
                | test_istype_custom_exception - Tests custom exception class raising.
                | test_istype_custom_message - Tests custom exception message.
    '''

    def test_resolve_type_concrete(self) -> None:
        '''
            Tests resolving concrete types.

            :exceptions: None.
        '''
        self.assertEqual(_resolve_type(int), int)
        self.assertEqual(_resolve_type(str), str)

    def test_resolve_type_union(self) -> None:
        '''
            Tests resolving union types.

            :exceptions: None.
        '''
        self.assertEqual(_resolve_type(Union[int, str]), (int, str))
        self.assertEqual(_resolve_type(int | str), (int, str))

    def test_resolve_type_nested_union(self) -> None:
        '''
            Tests resolving nested union types.

            :exceptions: None.
        '''
        self.assertEqual(_resolve_type(Union[Union[int, str], float]), (int, str, float))
        self.assertEqual(_resolve_type((int | str) | float), (int, str, float))

    def test_resolve_type_nested_union_mock(self) -> None:
        '''
            Tests resolving nested union types using mocks to bypass
            automatic runtime flattening of standard Union types.

            :exceptions: None.
        '''
        from unittest.mock import patch, MagicMock

        mock_inner_union = MagicMock()
        mock_inner_union.__args__ = (int, str)

        mock_outer_union = MagicMock()
        mock_outer_union.__args__ = (mock_inner_union, float)

        def custom_get_origin(tp: Any) -> Any:
            if tp is mock_outer_union or tp is mock_inner_union:
                return Union
            return None

        with patch("ats_utilities.validation.check_type.get_origin", side_effect=custom_get_origin):
            result = _resolve_type(mock_outer_union)
            self.assertEqual(result, (int, str, float))

    def test_resolve_type_generic(self) -> None:
        '''
            Tests resolving generic types.

            :exceptions: None.
        '''
        self.assertEqual(_resolve_type(list[int]), list)
        self.assertEqual(_resolve_type(dict[str, int]), dict)
        self.assertEqual(_resolve_type(Union[list[int], dict[str, int]]), (list, dict))

    def test_istype_valid_single(self) -> None:
        '''
            Tests checking valid instances against a single type.

            :exceptions: None.
        '''
        try:
            istype(1, int, 'checktypetest::test_istype_valid_single')
            istype("test", str, 'checktypetest::test_istype_valid_single')
        except ATSTypeError:
            self.fail("istype raised ATSTypeError unexpectedly for valid inputs.")

    def test_istype_valid_tuple(self) -> None:
        '''
            Tests checking valid instances against a tuple of types.

            :exceptions: None.
        '''
        try:
            istype(1, (int, str), 'checktypetest::test_istype_valid_tuple')
            istype("test", (int, str), 'checktypetest::test_istype_valid_tuple')
            istype(1.5, (int | str, float), 'checktypetest::test_istype_valid_tuple')
        except ATSTypeError:
            self.fail("istype raised ATSTypeError unexpectedly for valid tuple inputs.")

    def test_istype_valid_union(self) -> None:
        '''
            Tests checking valid instances against union types.

            :exceptions: None.
        '''
        try:
            istype(1, int | str, 'checktypetest::test_istype_valid_union')
            istype("test", Union[int, str], 'checktypetest::test_istype_valid_union')
        except ATSTypeError:
            self.fail("istype raised ATSTypeError unexpectedly for valid union inputs.")

    def test_istype_invalid_single(self) -> None:
        '''
            Tests checking invalid instances against a single type.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError) as ctx:
            istype("test", int, 'checktypetest::test_istype_invalid_single')
        self.assertIn("expected <class 'int'> for instance, got str", str(ctx.exception))

    def test_istype_invalid_tuple(self) -> None:
        '''
            Tests checking invalid instances against a tuple of types.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError) as ctx:
            istype([1, 2], (int, str), 'checktypetest::test_istype_invalid_tuple')
        self.assertIn("expected (<class 'int'>, <class 'str'>) for instance, got list", str(ctx.exception))

    def test_istype_custom_exception(self) -> None:
        '''
            Tests custom exception class raising.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            istype("test", int, 'checktypetest::test_istype_custom_exception', exc_class=ValueError)

    def test_istype_custom_message(self) -> None:
        '''
            Tests custom exception message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError) as ctx:
            istype("test", int, 'checktypetest::test_istype_custom_message', exc_message="custom message")
        self.assertIn("checktypetest::test_istype_custom_message - custom message", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
