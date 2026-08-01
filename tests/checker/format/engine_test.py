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
    Unit tests for FormatValidator class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.format.engine import FormatValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class FormatValidatorTest(unittest.TestCase):
    '''
        Defines class FormatValidatorTest with attribute(s) and method(s).
        Tests FormatValidator component logic.
    '''

    def test_is_valid(self) -> None:
        validator = FormatValidator()
        self.assertTrue(validator.is_valid("str:param"))
        with self.assertRaises(ATSValueError):
            validator.is_valid("invalid_format")
        with self.assertRaises(ATSTypeError):
            validator.is_valid(123)  # type: ignore

    def test_split(self) -> None:
        validator = FormatValidator()
        ptype, pname = validator.split("str:param")
        self.assertEqual(ptype, "str")
        self.assertEqual(pname, "param")
        with self.assertRaises(ATSTypeError):
            validator.split(123)  # type: ignore

    def test_str(self) -> None:
        validator = FormatValidator()
        self.assertIn("FormatValidator", str(validator))

    def test_custom_separator(self) -> None:
        validator = FormatValidator(separator="-")
        self.assertEqual(validator.get_separator(), "-")
        self.assertTrue(validator.is_valid("str-param"))
        ptype, pname = validator.split("str-param")
        self.assertEqual(ptype, "str")
        self.assertEqual(pname, "param")

    def test_set_and_get_separator(self) -> None:
        validator = FormatValidator()
        validator.set_separator("_")
        self.assertEqual(validator.get_separator(), "_")
        
        # Test setter invalid cases (type error, value error)
        with self.assertRaises(ATSTypeError):
            validator.set_separator(123)  # type: ignore
        with self.assertRaises(ATSValueError):
            validator.set_separator("")


if __name__ == "__main__":
    unittest.main()
