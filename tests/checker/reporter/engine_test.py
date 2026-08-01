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
    Unit tests for CheckReporter class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.reporter.engine import CheckReporter
from ats_utilities.checker.reporter.data import CheckReporterData
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class CheckReporterTest(unittest.TestCase):
    '''
        Defines class CheckReporterTest with attribute(s) and method(s).
        Tests CheckReporter component logic.
    '''

    def test_build_message_format_valid(self) -> None:
        reporter = CheckReporter()
        bundle = CheckReporterData(
            context="my_context",
            parameters_meta=[("param1", "str", "val")],
            err_indices=[],
            is_fmt_err=False
        )
        msg = reporter.build_message(bundle)
        self.assertIn("my_context", msg)
        self.assertIn("param1", msg)
        self.assertNotIn("wrong type", msg)
        self.assertNotIn("format wrong", msg)

    def test_build_message_format_with_errors(self) -> None:
        reporter = CheckReporter()
        bundle = CheckReporterData(
            context="my_context",
            parameters_meta=[("param1", "str", "val"), ("param2", "int", "not_int")],
            err_indices=[1],
            is_fmt_err=True
        )
        msg = reporter.build_message(bundle)
        self.assertIn("my_context", msg)
        self.assertIn("param1", msg)
        self.assertIn("param2", msg)
        self.assertIn("wrong type", msg)
        self.assertIn("format wrong", msg)

    def test_build_message_format_invalid_none(self) -> None:
        reporter = CheckReporter()
        with self.assertRaises(ATSValueError):
            reporter.build_message(None)  # type: ignore

    def test_build_message_format_invalid_type(self) -> None:
        reporter = CheckReporter()
        with self.assertRaises(ATSTypeError):
            reporter.build_message("invalid")  # type: ignore

    def test_str(self) -> None:
        reporter = CheckReporter()
        self.assertIn("CheckReporter", str(reporter))


if __name__ == "__main__":
    unittest.main()
