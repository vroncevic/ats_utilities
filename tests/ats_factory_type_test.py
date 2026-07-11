# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_type_test.py
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
    Defines classes ATSFactoryTypeTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS Factory Type.
Execute
    python3 -m unittest -v ats_factory_type_test
'''

from unittest import TestCase, main, mock
from typing import Union
from ats_utilities.factory_type import check_type
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class ATSFactoryTypeTestCase(TestCase):
    '''
        Defines classes ATSFactoryTypeTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Factory Type.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_check_type_single(self) -> None:
        '''Test check_type with a single type.'''
        check_type(123, int)
        check_type("test", str)

    def test_check_type_tuple(self) -> None:
        '''Test check_type with a tuple of types.'''
        check_type(123, (int, str))
        check_type("test", (int, str))

    def test_check_type_union(self) -> None:
        '''Test check_type with Union types.'''
        check_type(123, Union[int, str])
        check_type("test", Union[int, str])

    def test_check_type_new_union_operator(self) -> None:
        '''Test check_type with PEP 604 union operator (X | Y).'''
        check_type(123, int | str)
        check_type("test", int | str)

    def test_check_type_nested_union(self) -> None:
        '''Test check_type with nested Union types.'''
        check_type(12.3, Union[int, Union[str, float]])

    def test_check_type_tuple_with_union(self) -> None:
        '''Test check_type with a tuple containing Union types.'''
        check_type(123, (Union[int, str], float))
        check_type(12.3, (Union[int, str], float))

    def test_check_type_failure(self) -> None:
        '''Test check_type failure raises ATSTypeError.'''
        with self.assertRaises(ATSTypeError):
            check_type("not_int", int)

    def test_check_type_custom_exception(self) -> None:
        '''Test check_type with custom exception class.'''
        with self.assertRaises(ValueError):
            check_type("not_int", int, exception_class=ValueError)

    def test_check_type_with_message_path(self) -> None:
        '''Test check_type raises exception with path details.'''
        with self.assertRaises(ATSTypeError) as context:
            check_type("not_int", int, exc_message_path="some/config/path")
        self.assertIn("some/config/path", str(context.exception))

    @mock.patch('ats_utilities.factory_type.get_origin')
    def test_resolve_type_recursive_tuple(self, mock_get_origin) -> None:
        '''Test _resolve_type recursive tuple branch (line 62).'''
        class MockUnion1:
            __args__ = ('mock_inner',)

        def side_effect(t):
            if t == MockUnion1:
                return Union
            if t == 'mock_inner':
                return Union
            return None

        mock_get_origin.side_effect = side_effect
        # This will resolve to empty tuple () since mock_inner has no __args__
        check_type(123, (MockUnion1, int))


if __name__ == '__main__':
    main()
