# -*- coding: UTF-8 -*-

'''
Module
    check_reporter_test.py
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
from unittest.mock import MagicMock

from ats_utilities.checker.reporter.check_reporter import CheckReporter
from ats_utilities.checker.reporter.checker_reporter_bundle import CheckReporterData
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CheckReporterTest(unittest.TestCase):
    '''
        Defines class CheckReporterTest with attribute(s) and method(s).
        Tests CheckReporter component logic.

        It defines:

            :attributes: None.
            :methods:
                | test_build_message_format_valid - Tests build_message_format with valid bundle.
                | test_build_message_format_with_errors - Tests message formatting with errors.
                | test_build_message_format_invalid_none - Tests build_message_format with None bundle.
                | test_build_message_format_invalid_type - Tests build_message_format with wrong type.
                | test_str - Tests __str__ representation.
    '''

    def test_build_message_format_valid(self) -> None:
        reporter = CheckReporter()
        bundle = CheckReporterData(
            context="my_context",
            parameters_meta=[("param1", "str", "val")],
            err_indices=[],
            is_fmt_err=False
        )
        msg = reporter.build_message_format(bundle)
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
        msg = reporter.build_message_format(bundle)
        self.assertIn("my_context", msg)
        self.assertIn("param1", msg)
        self.assertIn("param2", msg)
        self.assertIn("wrong type", msg)
        self.assertIn("format wrong", msg)

    def test_build_message_format_invalid_none(self) -> None:
        reporter = CheckReporter()
        with self.assertRaises(ATSValueError):
            reporter.build_message_format(None)  # type: ignore

    def test_build_message_format_invalid_type(self) -> None:
        reporter = CheckReporter()
        with self.assertRaises(ATSTypeError):
            reporter.build_message_format("invalid")  # type: ignore

    def test_str(self) -> None:
        reporter = CheckReporter()
        self.assertIn("CheckReporter", str(reporter))


if __name__ == "__main__":
    unittest.main()
