# -*- coding: UTF-8 -*-

'''
Module
    types_test.py
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
    Unit tests for MessageKey enum.
'''

from __future__ import annotations

import unittest

from ats_utilities.reporter.theme.types import MessageKey


class TypesTest(unittest.TestCase):
    '''
        Defines class TypesTest with attribute(s) and method(s).
        Tests MessageKey enum logic.
    '''

    def test_message_keys(self) -> None:
        self.assertEqual(MessageKey.VERBOSE, "verbose")
        self.assertEqual(MessageKey.SUCCESS, "success")
        self.assertEqual(MessageKey.WARNING, "warning")
        self.assertEqual(MessageKey.ERROR, "error")
        self.assertEqual(MessageKey.RESET, "reset")


if __name__ == "__main__":
    unittest.main()
