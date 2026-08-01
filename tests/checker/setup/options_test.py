# -*- coding: UTF-8 -*-

'''
Module
    options_test.py
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
    Unit tests for CheckerOptions class.
'''

from __future__ import annotations

import unittest
from typing import get_type_hints, NotRequired

from ats_utilities.checker.setup.options import CheckerOptions


class CheckerOptionsTest(unittest.TestCase):
    '''
        Defines class CheckerOptionsTest with attribute(s) and method(s).
        Tests CheckerOptions TypedDict structure.
    '''

    def test_type_hints(self) -> None:
        hints = get_type_hints(CheckerOptions)
        self.assertEqual(hints['separator'], str)
        self.assertEqual(hints['stack_index_caller'], int)

    def test_instantiation(self) -> None:
        options: CheckerOptions = {
            'separator': "-",
            'stack_index_caller': 3
        }
        self.assertEqual(options['separator'], "-")
        self.assertEqual(options['stack_index_caller'], 3)


if __name__ == "__main__":
    unittest.main()
