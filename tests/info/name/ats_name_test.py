# -*- coding: UTF-8 -*-

'''
Module
    ats_name_test.py
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
    Defines classes NameTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Name.
Execute
    python3 -m unittest -v ats_name_test
'''

from unittest import TestCase, main

from ats_utilities.info.name.iname import IName
from ats_utilities.info.name.engine import Name
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class NameTestCase(TestCase):
    '''
        Defines classes NameTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Name.
        Name unit tests.

        It defines:

            :attributes:
                | instance - API for name.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that Name instance is not None.
                | test_name_value_is_none_by_default - Test that name value is None by default.
                | test_name_try_to_set_none - Test setting name to None.
                | test_name_try_to_set_wrong_type - Test wrong type for name.
                | test_name_set_to_value - Test setting name with value.
                | test_name_set_twice - Test setting name twice.
                | test_name_set_then_changed - Test setting name then changing it.
                | test_name_not_none_after_set - Test that name is not None after setting it.
                | test_name_string_after_set - Test that name is a string after setting it.
                | test_name_str_representation - Test string representation of name.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = Name()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default Name instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, IName)

    def test_name_value_is_none_by_default(self) -> None:
        '''Test name value is None by default.'''
        self.assertIsNone(self.instance.name)
        self.assertFalse(self.instance.not_none())

    def test_name_try_to_set_none(self) -> None:
        '''Test setting name to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.name = None

    def test_name_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for name.'''
        with self.assertRaises(ATSTypeError):
            self.instance.name = True

        with self.assertRaises(ATSTypeError):
            self.instance.name = 123

        with self.assertRaises(ATSTypeError):
            self.instance.name = [r'App']

        with self.assertRaises(ATSTypeError):
            self.instance.name = (r'App',)

        with self.assertRaises(ATSTypeError):
            self.instance.name = {'name': r'App'}

    def test_name_set_to_value(self) -> None:
        '''Test setting name with value.'''
        self.instance.name = r'App'
        self.assertEqual(self.instance.name, r'App')

    def test_name_set_twice(self) -> None:
        '''Test setting name twice.'''
        self.instance.name = r'App'
        self.instance.name = r'App'
        self.assertEqual(self.instance.name, r'App')

    def test_name_set_then_changed(self) -> None:
        '''Test setting name then changing it.'''
        self.instance.name = r'App'
        self.assertEqual(self.instance.name, r'App')
        self.instance.name = r'Tool'
        self.assertEqual(self.instance.name, r'Tool')

    def test_name_not_none_after_set(self) -> None:
        '''Test that name is not None after setting it.'''
        self.instance.name = r'App'
        self.assertTrue(self.instance.not_none())

    def test_name_string_after_set(self) -> None:
        '''Test that name is a string after setting it.'''
        self.instance.name = r'App'
        self.assertIsInstance(self.instance.name, str)

    def test_name_str_representation(self) -> None:
        '''Test string representation of name.'''
        self.instance.name = r'App'
        self.assertIsInstance(str(self.instance.name), str)
        self.assertEqual(str(self.instance.name), r'App')
        self.assertNotEqual(str(self.instance.name), r'Tool')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
