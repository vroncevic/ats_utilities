# -*- coding: UTF-8 -*-

'''
Module
    context_error_test.py
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
    Unit tests for context error functions.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSValueError
from ats_utilities.validation.context_error import raise_error

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ContextErrorTest(unittest.TestCase):
    '''
        Defines class ContextErrorTest with attribute(s) and method(s).
        Tests context and exception raising utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_raise_error_fallback - Tests raise_error with fallback message.
                | test_raise_error_fallback_custom_exception - Tests raise_error with custom exception.
                | test_raise_error_msg - Tests raise_error with custom message and context.
                | test_raise_error_msg_custom_exception - Tests raise_error with custom message, context and exception.
    '''

    def test_raise_error_fallback(self) -> None:
        '''
            Tests raise_error with fallback message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            raise_error("my_prefix", "my_fallback", "some_context")
        self.assertEqual(str(ctx.exception), "my_prefix - my_fallback")

    def test_raise_error_fallback_custom_exception(self) -> None:
        '''
            Tests raise_error with custom exception.

            :exceptions: None.
        '''
        with self.assertRaises(RuntimeError) as ctx:
            raise_error("my_prefix", "my_fallback", "some_context", exc_class=RuntimeError)
        self.assertEqual(str(ctx.exception), "my_prefix - my_fallback")

    def test_raise_error_msg(self) -> None:
        '''
            Tests raise_error with custom message and context.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            raise_error("my_prefix", "my_fallback", "some_context", exc_message="my message")
        self.assertEqual(str(ctx.exception), "some_context - my message")

    def test_raise_error_msg_custom_exception(self) -> None:
        '''
            Tests raise_error with custom message, context and exception.

            :exceptions: None.
        '''
        with self.assertRaises(RuntimeError) as ctx:
            raise_error("my_prefix", "my_fallback", "some_context", exc_message="my message", exc_class=RuntimeError)
        self.assertEqual(str(ctx.exception), "some_context - my message")


if __name__ == "__main__":
    unittest.main()
