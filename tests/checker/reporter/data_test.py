# -*- coding: UTF-8 -*-

'''
Module
    data_test.py
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
from dataclasses import FrozenInstanceError

from ats_utilities.checker.reporter.data import CheckReporterData


class CheckReporterDataTest(unittest.TestCase):
    '''
        Defines class CheckReporterDataTest with attribute(s) and method(s).
        Tests CheckReporterData component logic.
    '''

    def test_init_valid(self) -> None:
        data = CheckReporterData(
            context="my_context",
            parameters_meta=[("param1", "str", "val")],
            err_indices=[0],
            is_fmt_err=True
        )
        self.assertEqual(data.context, "my_context")
        self.assertEqual(data.parameters_meta, [("param1", "str", "val")])
        self.assertEqual(data.err_indices, [0])
        self.assertTrue(data.is_fmt_err)

    def test_frozen(self) -> None:
        data = CheckReporterData(
            context="my_context",
            parameters_meta=[],
            err_indices=[],
            is_fmt_err=False
        )
        with self.assertRaises(FrozenInstanceError):
            data.context = "new_context"  # type: ignore

    def test_slots(self) -> None:
        data = CheckReporterData(
            context="my_context",
            parameters_meta=[],
            err_indices=[],
            is_fmt_err=False
        )
        with self.assertRaises(AttributeError):
            data.__dict__  # type: ignore

    def test_to_dict(self) -> None:
        data = CheckReporterData(
            context="my_context",
            parameters_meta=[("param1", "str", "val")],
            err_indices=[0],
            is_fmt_err=True
        )
        d = data.to_dict()
        self.assertEqual(d["context"], "my_context")
        self.assertEqual(d["parameters_meta"], [("param1", "str", "val")])
        self.assertEqual(d["err_indices"], [0])
        self.assertTrue(d["is_fmt_err"])


if __name__ == "__main__":
    unittest.main()
