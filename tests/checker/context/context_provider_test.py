# -*- coding: UTF-8 -*-

'''
Module
    context_provider_test.py
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
    Unit tests for ContextProvider class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.context.context_provider import ContextProvider
from ats_utilities.exceptions import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ContextProviderTest(unittest.TestCase):
    '''
        Defines class ContextProviderTest with attribute(s) and method(s).
        Tests ContextProvider component logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_default - Tests default ContextProvider initialization.
                | test_set_stack_index_caller - Tests setting stack index caller.
                | test_get_context - Tests getting calling context.
                | test_get_context_overflow - Tests get_context when index exceeds stack depth.
                | test_get_context_decorated_wrapper - Tests get_context resolution inside decorator wrapper.
                | test_str - Tests __str__ representation.
    '''

    def test_init_default(self) -> None:
        provider = ContextProvider()
        self.assertEqual(provider._stack_index_caller, 2)

    def test_set_stack_index_caller(self) -> None:
        provider = ContextProvider()
        provider.set_stack_index_caller(5)
        self.assertEqual(provider._stack_index_caller, 5)
        with self.assertRaises(ATSTypeError):
            provider.set_stack_index_caller("invalid")  # type: ignore

    def test_get_context(self) -> None:
        provider = ContextProvider(stack_index_caller=1)
        ctx = provider.get_context()
        self.assertIn("test_get_context", ctx)

    def test_get_context_overflow(self) -> None:
        provider = ContextProvider(stack_index_caller=9999)
        ctx = provider.get_context()
        self.assertIsNotNone(ctx)

    def test_get_context_decorated_wrapper(self) -> None:
        provider = ContextProvider(stack_index_caller=1)

        def my_real_function() -> str:
            return provider.get_context()

        def wrapper() -> str:
            func = my_real_function  # captured locally
            return func()

        ctx = wrapper()
        self.assertIn("my_real_function", ctx)

    def test_get_context_decorated_wrapper_no_name(self) -> None:
        provider = ContextProvider(stack_index_caller=1)

        def wrapper() -> str:
            func = object()  # Has no __name__
            return provider.get_context()

        ctx = wrapper()
        self.assertIn("wrapper", ctx)

    def test_str(self) -> None:
        provider = ContextProvider()
        self.assertIn("ContextProvider", str(provider))


if __name__ == "__main__":
    unittest.main()
