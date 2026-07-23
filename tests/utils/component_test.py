# -*- coding: UTF-8 -*-

'''
Module
    component_test.py
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
    Unit tests for factory component utilities.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions import ATSTypeError
from ats_utilities.utils.component import make_component, validate_component

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyComponent:
    '''
        Defines class DummyComponent used for component instantiation testing.

        It defines:

            :attributes:
                | arg1 - First test argument (default None).
                | arg2 - Second test argument (default None).
            :methods:
                | __init__ - Initializes DummyComponent constructor.
    '''

    def __init__(self, arg1: str | None = None, arg2: int | None = None) -> None:
        '''
            Initializes DummyComponent constructor.

            :param arg1: First test argument | None.
            :type arg1: str | None
            :param arg2: Second test argument | None.
            :type arg2: <int | None>
            :exceptions: None.
        '''
        self.arg1 = arg1
        self.arg2 = arg2


class ComponentTest(unittest.TestCase):
    '''
        Defines class ComponentTest with attribute(s) and method(s).
        Tests factory component utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_make_component_existing - Tests make_component with an existing instance.
                | test_make_component_default_no_args - Tests make_component instantiating class with no arguments.
                | test_make_component_default_with_args - Tests make_component instantiating class with arguments.
                | test_validate_component_valid - Tests validate_component with a valid type.
                | test_validate_component_invalid - Tests validate_component with an invalid type.
                | test_validate_component_custom_exception - Tests validate_component with a custom exception class.
                | test_validate_component_custom_message - Tests validate_component with a custom exception message.
    '''

    def test_make_component_existing(self) -> None:
        '''
            Tests make_component with an existing instance.

            :exceptions: None.
        '''
        existing = DummyComponent()
        result = make_component(existing, DummyComponent)
        self.assertIs(result, existing)

    def test_make_component_default_no_args(self) -> None:
        '''
            Tests make_component instantiating class with no arguments.

            :exceptions: None.
        '''
        result = make_component(None, DummyComponent)
        self.assertIsInstance(result, DummyComponent)
        self.assertIsNone(result.arg1)
        self.assertIsNone(result.arg2)

    def test_make_component_default_with_args(self) -> None:
        '''
            Tests make_component instantiating class with arguments.

            :exceptions: None.
        '''
        args = {"arg1": "value", "arg2": 42}
        result = make_component(None, DummyComponent, factory_args=args)
        self.assertIsInstance(result, DummyComponent)
        self.assertEqual(result.arg1, "value")
        self.assertEqual(result.arg2, 42)

    def test_validate_component_valid(self) -> None:
        '''
            Tests validate_component with a valid type.

            :exceptions: None.
        '''
        instance = DummyComponent()
        try:
            validate_component(instance, DummyComponent, 'componenttest::test_validate_component_valid')
        except ATSTypeError:
            self.fail("validate_component raised ATSTypeError unexpectedly for valid component type.")

    def test_validate_component_invalid(self) -> None:
        '''
            Tests validate_component with an invalid type.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError) as ctx:
            validate_component("not a component", DummyComponent, 'componenttest::test_validate_component_invalid')
        self.assertIn("instance is not of expected type", str(ctx.exception))

    def test_validate_component_custom_exception(self) -> None:
        '''
            Tests validate_component with a custom exception class.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            validate_component("not a component", DummyComponent, 'componenttest::test_validate_component_custom_exception', exc_class=ValueError)

    def test_validate_component_custom_message(self) -> None:
        '''
            Tests validate_component with a custom exception message.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError) as ctx:
            validate_component("not a component", DummyComponent, 'componenttest::test_validate_component_custom_message', exc_message="custom message")
        self.assertIn("componenttest::test_validate_component_custom_message - custom message", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
