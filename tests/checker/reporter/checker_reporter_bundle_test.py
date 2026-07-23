# -*- coding: UTF-8 -*-

'''
Module
    checker_reporter_bundle_test.py
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
    Unit tests for CheckReporterData class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.reporter.checker_reporter_bundle import CheckReporterData
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CheckerReporterBundleTest(unittest.TestCase):
    '''
        Defines class CheckerReporterBundleTest with attribute(s) and method(s).
        Tests CheckReporterData dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful CheckReporterData initialization.
                | test_init_invalid_none - Tests CheckReporterData initialization with None values.
                | test_init_invalid_type - Tests CheckReporterData initialization with wrong types.
                | test_to_dict - Tests CheckReporterData to_dict method.
    '''

    def test_init_valid(self) -> None:
        bundle = CheckReporterData(
            context="my_context",
            parameters_meta=[("param1", "str", "val")],
            err_indices=[0],
            is_fmt_err=True
        )
        self.assertEqual(bundle.context, "my_context")
        self.assertEqual(bundle.parameters_meta, [("param1", "str", "val")])
        self.assertEqual(bundle.err_indices, [0])
        self.assertTrue(bundle.is_fmt_err)

    def test_init_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            CheckReporterData(
                context=None,  # type: ignore
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err=False
            )

        with self.assertRaises(ATSValueError):
            CheckReporterData(
                context="ctx",
                parameters_meta=None,  # type: ignore
                err_indices=[0],
                is_fmt_err=False
            )

        with self.assertRaises(ATSValueError):
            CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=None,  # type: ignore
                is_fmt_err=False
            )

        with self.assertRaises(ATSValueError):
            CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err=None  # type: ignore
            )

    def test_init_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            CheckReporterData(
                context=123,  # type: ignore
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err=False
            )

        with self.assertRaises(ATSTypeError):
            CheckReporterData(
                context="ctx",
                parameters_meta=123,  # type: ignore
                err_indices=[0],
                is_fmt_err=False
            )

        with self.assertRaises(ATSTypeError):
            CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=123,  # type: ignore
                is_fmt_err=False
            )

        with self.assertRaises(ATSTypeError):
            CheckReporterData(
                context="ctx",
                parameters_meta=[("p", "t", "v")],
                err_indices=[0],
                is_fmt_err="invalid"  # type: ignore
            )

    def test_to_dict(self) -> None:
        bundle = CheckReporterData(
            context="ctx",
            parameters_meta=[("p", "t", "v")],
            err_indices=[0],
            is_fmt_err=False
        )
        expected = {
            "context": "ctx",
            "parameters_meta": [("p", "t", "v")],
            "err_indices": [0],
            "is_fmt_err": False
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
