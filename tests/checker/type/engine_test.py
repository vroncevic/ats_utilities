# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for TypeValidator class.
'''

from __future__ import annotations

import unittest
from collections.abc import Set

from ats_utilities.checker.type.engine import TypeValidator
from ats_utilities.exceptions import ATSTypeError


class TypeValidatorTest(unittest.TestCase):
    '''
        Defines class TypeValidatorTest with attribute(s) and method(s).
        Tests TypeValidator component logic.
    '''

    def test_init_default(self) -> None:
        validator = TypeValidator()
        self.assertIn("Mapping", validator._abstract_types)
        self.assertIn("Sequence", validator._abstract_types)
        self.assertIn("Iterable", validator._abstract_types)

    def test_init_custom(self) -> None:
        custom_types = {"CustomSet": Set}
        validator = TypeValidator(custom_types)
        self.assertIn("CustomSet", validator._abstract_types)
        self.assertNotIn("Mapping", validator._abstract_types)

    def test_init_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            TypeValidator("not a mapping")  # type: ignore

    def test_is_match(self) -> None:
        validator = TypeValidator()
        self.assertTrue(validator.is_match("hello", "str"))
        self.assertTrue(validator.is_match([1, 2], "Sequence"))
        self.assertFalse(validator.is_match("hello", "int"))
        with self.assertRaises(ATSTypeError):
            validator.is_match("hello", 123)  # type: ignore

    def test_is_subtype(self) -> None:
        validator = TypeValidator()
        self.assertTrue(validator.is_subtype("hello", "str"))
        self.assertTrue(validator.is_subtype([1, 2], "Sequence"))
        self.assertFalse(validator.is_subtype("hello", "int"))
        with self.assertRaises(ATSTypeError):
            validator.is_subtype("hello", 123)  # type: ignore

    def test_get_type_name(self) -> None:
        validator = TypeValidator()
        self.assertEqual(validator.get_type_name("hello"), "str")
        self.assertEqual(validator.get_type_name(123), "int")

    def test_str(self) -> None:
        validator = TypeValidator()
        self.assertIn("TypeValidator", str(validator))


if __name__ == "__main__":
    unittest.main()
