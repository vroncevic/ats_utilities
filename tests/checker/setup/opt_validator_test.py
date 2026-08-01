# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
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
    Unit tests for CheckerOptionsValidator class.
'''

from __future__ import annotations

import unittest
from collections.abc import Set

from ats_utilities.checker.setup.options import CheckerOptions
from ats_utilities.checker.setup.opt_validator import CheckerOptionsValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class CheckerOptionsValidatorTest(unittest.TestCase):
    '''
        Defines class CheckerOptionsValidatorTest with attribute(s) and method(s).
        Tests CheckerOptionsValidator component logic.
    '''

    def test_validate_valid_empty(self) -> None:
        options = CheckerOptions()
        CheckerOptionsValidator.validate(options)

    def test_validate_valid_full(self) -> None:
        options = CheckerOptions(
            separator="-",
            abstract_types={"MySet": Set},
            stack_index_caller=3,
            messages_provider={"err": "text"}
        )
        CheckerOptionsValidator.validate(options)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            CheckerOptionsValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            CheckerOptionsValidator.validate("not_a_mapping")  # type: ignore

    def test_validate_invalid_option_types(self) -> None:
        with self.assertRaises(ATSTypeError):
            CheckerOptionsValidator.validate(CheckerOptions(separator=123))  # type: ignore

        with self.assertRaises(ATSTypeError):
            CheckerOptionsValidator.validate(CheckerOptions(stack_index_caller="invalid"))  # type: ignore


if __name__ == "__main__":
    unittest.main()
