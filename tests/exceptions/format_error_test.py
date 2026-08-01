# -*- coding: UTF-8 -*-

'''
Module
    format_error_test.py
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
    Unit tests for error formatting utilities.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions.format_error import (
    format_error,
    format_error_raw,
    get_debug_info,
)

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FormatErrorTest(unittest.TestCase):
    '''
        Defines class FormatErrorTest with attribute(s) and method(s).
        Tests error formatting functions.

        It defines:

            :attributes: None.
            :methods:
                | test_get_debug_info - Tests get_debug_info.
                | test_format_error_raw - Tests format_error_raw.
                | test_format_error - Tests format_error.
    '''

    def test_get_debug_info(self) -> None:
        '''
            Tests get_debug_info.

            :exceptions: None.
        '''
        try:
            # Raise exception to populate traceback
            raise ValueError("debug_test")
        except ValueError as e:
            exc = e

        debug_info = get_debug_info(exc)
        self.assertIn("format_error_test.py", debug_info)
        # Check that it ends with a line number (which should be integer)
        line_num_str = debug_info.split(":")[-1]
        self.assertTrue(line_num_str.isdigit())

    def test_format_error_raw(self) -> None:
        '''
            Tests format_error_raw.

            :exceptions: None.
        '''
        try:
            raise ValueError("raw_test")
        except ValueError as e:
            exc = e

        # Without debug
        self.assertEqual(format_error_raw(exc, debug=False), "raw_test")

        # With debug
        res_debug = format_error_raw(exc, debug=True)
        self.assertIn("raw_test at (", res_debug)
        self.assertIn("format_error_test.py", res_debug)

    def test_format_error(self) -> None:
        '''
            Tests format_error.

            :exceptions: None.
        '''
        try:
            raise ValueError("format_test")
        except ValueError as e:
            exc = e

        # Without prefix, without debug
        res1 = format_error(exc, prefix='', debug=False)
        self.assertEqual(res1, "\x1b[31mformat_test\x1b[0m\n")

        # With prefix, without debug
        res2 = format_error(exc, prefix='[ERROR]', debug=False)
        self.assertEqual(res2, "\x1b[31m[ERROR] format_test\x1b[0m\n")

        # Without prefix, with debug
        res3 = format_error(exc, prefix='', debug=True)
        self.assertTrue(res3.startswith("\x1b[31mformat_test at ("))
        self.assertIn("format_error_test.py", res3)
        self.assertTrue(res3.endswith("\x1b[0m\n"))

        # With prefix, with debug
        res4 = format_error(exc, prefix='[ERROR]', debug=True)
        self.assertTrue(res4.startswith("\x1b[31m[ERROR] format_test at ("))
        self.assertIn("format_error_test.py", res4)
        self.assertTrue(res4.endswith("\x1b[0m\n"))


if __name__ == "__main__":
    unittest.main()
