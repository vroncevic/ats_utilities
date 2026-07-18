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
    Unit tests for ConsoleTheme class.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.reporter.theme.engine import ConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests ConsoleTheme logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests ConsoleTheme initialization options.
                | test_get_color_valid - Tests get_color with valid keys.
                | test_get_color_invalid - Tests get_color with invalid arguments/keys.
                | test_str - Tests __str__ method.
    '''

    def test_init(self) -> None:
        # Default initialization
        theme = ConsoleTheme()
        self.assertEqual(theme.get_color("success"), "\x1b[32m")

        # Custom initialization
        custom_palette = {"custom": "\x1b[35m"}
        theme_custom = ConsoleTheme(custom_palette)
        self.assertEqual(theme_custom.get_color("custom"), "\x1b[35m")

        # Invalid initialization type
        with self.assertRaises(ATSTypeError):
            ConsoleTheme("invalid")  # type: ignore

    def test_get_color_valid(self) -> None:
        theme = ConsoleTheme()
        self.assertEqual(theme.get_color("verbose"), "\x1b[34m")
        self.assertEqual(theme.get_color("reset"), "\x1b[0m")

    def test_get_color_invalid(self) -> None:
        theme = ConsoleTheme()

        # None type
        with self.assertRaises(ATSValueError):
            theme.get_color(None)  # type: ignore

        # Wrong type
        with self.assertRaises(ATSTypeError):
            theme.get_color(123)  # type: ignore

        # Missing key
        with self.assertRaises(ATSValueError):
            theme.get_color("missing")

    def test_str(self) -> None:
        theme = ConsoleTheme()
        self.assertIn("ConsoleTheme", str(theme))


if __name__ == "__main__":
    unittest.main()
