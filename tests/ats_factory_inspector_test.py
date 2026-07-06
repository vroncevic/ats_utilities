# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_inspector_test.py
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
    Defines classes ATSFactoryInspectorTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS Factory Inspector.
Execute
    python3 -m unittest -v ats_factory_inspector_test
'''

from unittest import TestCase, main
from ats_utilities.factory_inspector import get_caller_context
from ats_utilities.factory_context_error import raise_context_error
from ats_utilities.exceptions import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DummyInspectorClass:
    def test_method(self):
        return get_caller_context(depth=1)

    @classmethod
    def test_classmethod(cls):
        return get_caller_context(depth=1)


class ATSFactoryInspectorTestCase(TestCase):
    '''
        Defines classes ATSFactoryInspectorTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Factory Inspector.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_get_caller_context_function(self) -> None:
        '''Test get_caller_context in a plain function context.'''
        def helper():
            return get_caller_context(depth=1)
        self.assertEqual(helper(), "helper")

    def test_get_caller_context_self(self) -> None:
        '''Test get_caller_context with an instance method (self).'''
        dummy = DummyInspectorClass()
        self.assertEqual(dummy.test_method(), "dummyinspectorclass::test_method")

    def test_get_caller_context_cls(self) -> None:
        '''Test get_caller_context with a class method (cls).'''
        self.assertEqual(DummyInspectorClass.test_classmethod(), "dummyinspectorclass::test_classmethod")

    def test_get_caller_context_excessive_depth(self) -> None:
        '''Test get_caller_context when depth goes beyond call stack.'''
        self.assertEqual(get_caller_context(depth=1000), "unknown")

    def test_raise_context_error(self) -> None:
        '''Test raise_context_error function.'''
        with self.assertRaises(ATSValueError) as context:
            raise_context_error(
                fallback_prefix="prefix",
                fallback_msg="message",
                exc_message_path=None,
                exception_class=ATSValueError
            )
        self.assertIn("prefix", str(context.exception))
        self.assertIn("message", str(context.exception))


if __name__ == '__main__':
    main()
