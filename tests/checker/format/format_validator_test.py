# -*- coding: UTF-8 -*-

'''
Module
    format_validator_test.py
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

from ats_utilities.checker.format.format_validator import FormatValidator
from ats_utilities.exceptions import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FormatValidatorTest(unittest.TestCase):
    '''
        Defines class FormatValidatorTest with attribute(s) and method(s).
        Tests FormatValidator component logic.

        It defines:

            :attributes: None.
            :methods:
                | test_is_valid - Tests is_valid format checker.
                | test_split - Tests split logic.
                | test_str - Tests __str__ representation.
    '''

    def test_is_valid(self) -> None:
        validator = FormatValidator()
        self.assertTrue(validator.is_valid("str:param"))
        self.assertFalse(validator.is_valid("invalid_format"))
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


if __name__ == "__main__":
    unittest.main()
