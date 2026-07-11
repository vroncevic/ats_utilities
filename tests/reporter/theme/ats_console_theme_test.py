# -*- coding: UTF-8 -*-

'''
Module
    ats_console_theme_test.py
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
    Defines class ConsoleThemeTestCase with attribute(s) and method(s).
    Creates test cases for checking ConsoleTheme component.
Execute
    python3 -m unittest -v tests/reporter/theme/ats_console_theme_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ConsoleThemeTestCase(TestCase):
    '''
        Defines class ConsoleThemeTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ConsoleTheme.
    '''

    def test_console_theme_init(self) -> None:
        '''Test console theme initialization and validation.'''
        theme = ConsoleTheme()
        self.assertEqual(theme.get_color('verbose'), '\x1b[34m')

        custom_palette = {'verbose': '\x1b[35m', 'reset': '\x1b[0m'}
        theme_custom = ConsoleTheme(custom_palette)
        self.assertEqual(theme_custom.get_color('verbose'), '\x1b[35m')

        with self.assertRaises(ATSTypeError):
            ConsoleTheme("invalid_palette")

    def test_console_theme_get_color_failures(self) -> None:
        '''Test console theme get_color failures.'''
        theme = ConsoleTheme()

        with self.assertRaises(ATSValueError):
            theme.get_color(None)

        with self.assertRaises(ATSTypeError):
            theme.get_color(123)

        with self.assertRaises(ATSValueError):
            theme.get_color('non_existent')

    def test_console_theme_string_representation(self) -> None:
        '''Test console theme string representation.'''
        theme = ConsoleTheme()
        self.assertIn('ConsoleTheme', str(theme))


if __name__ == '__main__':
    main()
