# -*- coding: UTF-8 -*-

'''
Module
    data_validator_test.py
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
    Unit tests for CheckReporterValidator class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.reporter.data import CheckReporterData
from ats_utilities.checker.reporter.data_validator import CheckReporterValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class CheckReporterValidatorTest(unittest.TestCase):
    '''
        Defines class CheckReporterValidatorTest with attribute(s) and method(s).
        Tests CheckReporterValidator component logic.
    '''

    def test_validate_valid(self) -> None:
        data = CheckReporterData(
            context="my_context",
            parameters_meta=[("param1", "str", "val")],
            err_indices=[0],
            is_fmt_err=True
        )
        CheckReporterValidator.validate(data)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            CheckReporterValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            CheckReporterValidator.validate("invalid")  # type: ignore

    def test_init_invalid_none_attributes(self) -> None:
        with self.assertRaises(ATSValueError):
            data = CheckReporterData(
                context=None,  # type: ignore
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err=False
            )
            CheckReporterValidator.validate(data)

        with self.assertRaises(ATSValueError):
            data = CheckReporterData(
                context="ctx",
                parameters_meta=None,  # type: ignore
                err_indices=[0],
                is_fmt_err=False
            )
            CheckReporterValidator.validate(data)

        with self.assertRaises(ATSValueError):
            data = CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=None,  # type: ignore
                is_fmt_err=False
            )
            CheckReporterValidator.validate(data)

        with self.assertRaises(ATSValueError):
            data = CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err=None  # type: ignore
            )
            CheckReporterValidator.validate(data)

    def test_init_invalid_type_attributes(self) -> None:
        with self.assertRaises(ATSTypeError):
            data = CheckReporterData(
                context=123,  # type: ignore
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err=False
            )
            CheckReporterValidator.validate(data)

        with self.assertRaises(ATSTypeError):
            data = CheckReporterData(
                context="ctx",
                parameters_meta=123,  # type: ignore
                err_indices=[0],
                is_fmt_err=False
            )
            CheckReporterValidator.validate(data)

        with self.assertRaises(ATSTypeError):
            data = CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=123,  # type: ignore
                is_fmt_err=False
            )
            CheckReporterValidator.validate(data)

        with self.assertRaises(ATSTypeError):
            data = CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err="invalid"  # type: ignore
            )
            CheckReporterValidator.validate(data)


if __name__ == "__main__":
    unittest.main()
