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
from ats_utilities.validation.context_error import get_caller, raise_error

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


def helper_function() -> str:
    '''
        Helper function to test get_caller.

        :return: Caller name.
        :rtype: <str>
    '''
    return get_caller(depth=1)


def helper_nested() -> str:
    '''
        Helper nested function to test get_caller at depth 2.

        :return: Caller name.
        :rtype: <str>
    '''
    return get_caller(depth=2)


def helper_function_2() -> str:
    '''
        Helper function that calls helper_nested.

        :return: Caller name.
        :rtype: <str>
    '''
    return helper_nested()


class DummyClass:
    '''
        Defines class DummyClass to test class and method context extraction.

        It defines:

            :attributes: None.
            :methods:
                | dummy_method - Instance method returning caller context.
                | dummy_classmethod - Class method returning caller context.
    '''

    def dummy_method(self) -> str:
        '''
            Instance method returning caller context.

            :return: Caller context.
            :rtype: <str>
        '''
        return get_caller(depth=1)

    @classmethod
    def dummy_classmethod(cls) -> str:
        '''
            Class method returning caller context.

            :return: Caller context.
            :rtype: <str>
        '''
        return get_caller(depth=1)


class ContextErrorTest(unittest.TestCase):
    '''
        Defines class ContextErrorTest with attribute(s) and method(s).
        Tests context and exception raising utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_get_caller_function - Tests get_caller inside a regular function.
                | test_get_caller_nested_function - Tests get_caller with higher depth.
                | test_get_caller_method - Tests get_caller inside an instance method.
                | test_get_caller_classmethod - Tests get_caller inside a class method.
                | test_get_caller_unknown - Tests get_caller when depth is out of bounds.
                | test_raise_error_fallback - Tests raise_error with fallback message.
                | test_raise_error_fallback_custom_exception - Tests raise_error with custom exception.
                | test_raise_error_msg - Tests raise_error with custom message and default depth.
                | test_raise_error_msg_custom_exception - Tests raise_error with custom message and exception.
    '''

    def test_get_caller_function(self) -> None:
        '''
            Tests get_caller inside a regular function.

            :exceptions: None.
        '''
        self.assertEqual(helper_function(), "helper_function")

    def test_get_caller_nested_function(self) -> None:
        '''
            Tests get_caller with higher depth.

            :exceptions: None.
        '''
        self.assertEqual(helper_function_2(), "helper_function_2")

    def test_get_caller_method(self) -> None:
        '''
            Tests get_caller inside an instance method.

            :exceptions: None.
        '''
        self.assertEqual(DummyClass().dummy_method(), "dummyclass::dummy_method")

    def test_get_caller_classmethod(self) -> None:
        '''
            Tests get_caller inside a class method.

            :exceptions: None.
        '''
        self.assertEqual(DummyClass.dummy_classmethod(), "dummyclass::dummy_classmethod")

    def test_get_caller_unknown(self) -> None:
        '''
            Tests get_caller when depth is out of bounds.

            :exceptions: None.
        '''
        self.assertEqual(get_caller(depth=100), "unknown")

    def test_raise_error_fallback(self) -> None:
        '''
            Tests raise_error with fallback message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            raise_error("my_prefix", "my_fallback")
        self.assertEqual(str(ctx.exception), "my_prefix - my_fallback")

    def test_raise_error_fallback_custom_exception(self) -> None:
        '''
            Tests raise_error with custom exception.

            :exceptions: None.
        '''
        with self.assertRaises(RuntimeError) as ctx:
            raise_error("my_prefix", "my_fallback", exception_class=RuntimeError)
        self.assertEqual(str(ctx.exception), "my_prefix - my_fallback")

    def test_raise_error_msg(self) -> None:
        '''
            Tests raise_error with custom message and default depth.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            raise_error("my_prefix", "my_fallback", exc_message="my message")
        self.assertEqual(str(ctx.exception), "contexterrortest::test_raise_error_msg - my message")

    def test_raise_error_msg_custom_exception(self) -> None:
        '''
            Tests raise_error with custom message and exception.

            :exceptions: None.
        '''
        with self.assertRaises(RuntimeError) as ctx:
            raise_error("my_prefix", "my_fallback", exc_message="my message", exception_class=RuntimeError)
        self.assertEqual(str(ctx.exception), "contexterrortest::test_raise_error_msg_custom_exception - my message")


if __name__ == "__main__":
    unittest.main()
