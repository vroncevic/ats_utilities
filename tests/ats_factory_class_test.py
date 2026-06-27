# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_class_test.py
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
    Defines classes ATSFactoryClassTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of factory_class functions.
Execute
    python3 -m unittest -v ats_factory_class_test
'''

from typing import Any
from unittest import TestCase, main
from ats_utilities.factory_class import (
    inject,
    get_private_attr,
    require_attributes,
    format_instance_to_string
)
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DummyDependency:
    '''Simple dummy class for testing dependency injection.'''

    def __init__(self, **kwargs: Any) -> None:
        '''Initial constructor.'''
        self.kwargs = kwargs


class ATSFactoryClassTestCase(TestCase):
    '''
        Defines class ATSFactoryClassTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of factory_class functions.
        Factory class functions unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_inject_passed_value - Test injecting non-None passed value.
                | test_inject_fallback_type_no_deps - Test injecting fallback type with no dependencies.
                | test_inject_fallback_type_single_dep - Test injecting fallback type with single dependency.
                | test_inject_fallback_type_multi_deps - Test injecting fallback type with multiple dependencies.
                | test_inject_fallback_value - Test injecting fallback raw value.
                | test_get_private_attr - Test retrieving private attributes.
                | test_require_attributes_success - Test decorator validation success.
                | test_require_attributes_failure - Test decorator validation failure.
                | test_format_instance_to_string - Test string representation utility.
    '''

    def test_inject_passed_value(self) -> None:
        '''
            Test injecting non-None passed value.

            :exceptions: None.
        '''
        class Target:
            pass

        inst = Target()
        inject(inst, ('my_attr', 'passed_value', 'fallback_val'))
        self.assertEqual(getattr(inst, '_my_attr'), 'passed_value')

    def test_inject_fallback_type_no_deps(self) -> None:
        '''
            Test injecting fallback type with no dependencies.

            :exceptions: None.
        '''
        class Target:
            pass

        inst = Target()
        inject(inst, ('my_attr', None, DummyDependency))
        resolved = getattr(inst, '_my_attr')
        self.assertIsInstance(resolved, DummyDependency)
        self.assertEqual(resolved.kwargs, {})

    def test_inject_fallback_type_single_dep(self) -> None:
        '''
            Test injecting fallback type with single dependency.

            :exceptions: None.
        '''
        class Target:
            pass

        inst = Target()
        inject(inst, ('dep1', 'val1', None))
        inject(inst, ('my_attr', None, DummyDependency, 'dep1'))
        resolved = getattr(inst, '_my_attr')
        self.assertIsInstance(resolved, DummyDependency)
        self.assertEqual(resolved.kwargs, {'dep1': 'val1'})

    def test_inject_fallback_type_multi_deps(self) -> None:
        '''
            Test injecting fallback type with multiple dependencies.

            :exceptions: None.
        '''
        class Target:
            pass

        inst = Target()
        inject(inst, ('dep1', 'val1', None))
        inject(inst, ('dep2', 'val2', None))
        inject(inst, ('my_attr', None, DummyDependency, ['dep1', 'dep2']))
        resolved = getattr(inst, '_my_attr')
        self.assertIsInstance(resolved, DummyDependency)
        self.assertEqual(resolved.kwargs, {'dep1': 'val1', 'dep2': 'val2'})

    def test_inject_fallback_value(self) -> None:
        '''
            Test injecting fallback raw value.

            :exceptions: None.
        '''
        class Target:
            pass

        inst = Target()
        inject(inst, ('my_attr', None, 'fallback_value'))
        self.assertEqual(getattr(inst, '_my_attr'), 'fallback_value')

    def test_get_private_attr(self) -> None:
        '''
            Test retrieving private attributes.

            :exceptions: None.
        '''
        class Target:
            def __init__(self) -> None:
                self._my_attr = 'secret'

        inst = Target()
        self.assertEqual(get_private_attr(inst, 'my_attr'), 'secret')
        self.assertEqual(get_private_attr(inst, '_my_attr'), 'secret')

    def test_require_attributes_success(self) -> None:
        '''
            Test decorator validation success.

            :exceptions: None.
        '''
        class Target:
            def __init__(self) -> None:
                self.attr1 = 'ok'
                self.attr2 = 'also_ok'

            @require_attributes('attr1', 'attr2')
            def execute(self) -> str:
                return 'success'

        inst = Target()
        self.assertEqual(inst.execute(), 'success')

    def test_require_attributes_failure(self) -> None:
        '''
            Test decorator validation failure.

            :exceptions: None.
        '''
        class Target:
            def __init__(self, val1: Any, val2: Any) -> None:
                self.attr1 = val1
                self.attr2 = val2

            @require_attributes('attr1', 'attr2')
            def execute(self) -> str:
                return 'success'

        # Missing completely
        class EmptyTarget:
            @require_attributes('attr1')
            def execute(self) -> str:
                return 'success'

        with self.assertRaises(ATSValueError):
            EmptyTarget().execute()

        # Set to None
        with self.assertRaises(ATSValueError):
            Target(None, 'ok').execute()

        # Set to empty string
        with self.assertRaises(ATSValueError):
            Target('ok', '').execute()

    def test_format_instance_to_string(self) -> None:
        '''
            Test string representation utility.

            :exceptions: None.
        '''
        class SimpleTarget:
            def __init__(self) -> None:
                self._val1 = 'test'
                self._val2 = 123
                self._val3 = 45.6
                self._val4 = True
                self.public = 'hello'

        class EmptyTarget:
            pass

        inst1 = SimpleTarget()
        inst2 = EmptyTarget()

        str_repr1 = format_instance_to_string(inst1)
        str_repr2 = format_instance_to_string(inst2)

        self.assertIn('SimpleTarget', str_repr1)
        self.assertIn('val1', str_repr1)
        self.assertIn('val2', str_repr1)
        self.assertIn('val3', str_repr1)
        self.assertIn('val4', str_repr1)
        self.assertIn('public', str_repr1)
        self.assertIn('EmptyTarget', str_repr2)


if __name__ == '__main__':
    main()
