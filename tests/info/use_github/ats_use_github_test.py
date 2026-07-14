# -*- coding: UTF-8 -*-

'''
Module
    ats_use_github_test.py
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
    Defines classes UseGitHubTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of UseGitHub.
Execute
    python3 -m unittest -v ats_use_github_test
'''

from unittest import TestCase, main

from ats_utilities.info.use_github.iuse_github import IUseGitHub
from ats_utilities.info.use_github.engine import UseGitHub
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class UseGitHubTestCase(TestCase):
    '''
        Defines classes UseGitHubTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of UseGitHub.
        UseGitHub unit tests.

        It defines:

            :attributes:
                | instance - API for use_github.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that UseGitHub instance is not None.
                | test_use_github_value_is_false_by_default - Test that use_github value is false by default.
                | test_use_github_try_to_set_none - Test setting use_github to None.
                | test_use_github_try_to_set_wrong_type - Test wrong type for use_github.
                | test_use_github_set_to_value - Test setting use_github with value.
                | test_use_github_set_twice - Test setting use_github twice.
                | test_use_github_set_then_changed - Test setting use_github then changing it.
                | test_use_github_not_none_after_set - Test that use_github is not None after setting it.
                | test_use_github_string_after_set - Test that use_github is a string after setting it.
                | test_use_github_str_representation - Test string representation of use_github.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = UseGitHub()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default UseGitHub instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, IUseGitHub)

    def test_use_github_value_is_false_by_default(self) -> None:
        '''Test use_github value is false by default.'''
        self.assertFalse(self.instance.use_github)
        self.assertTrue(self.instance.not_none())

    def test_use_github_try_to_set_none(self) -> None:
        '''Test setting use_github to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.use_github = None

    def test_use_github_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for use_github.'''
        with self.assertRaises(ATSTypeError):
            self.instance.use_github = 'True'

        with self.assertRaises(ATSTypeError):
            self.instance.use_github = 123

        with self.assertRaises(ATSTypeError):
            self.instance.use_github = [True]

        with self.assertRaises(ATSTypeError):
            self.instance.use_github = (True,)

        with self.assertRaises(ATSTypeError):
            self.instance.use_github = {'use_github': True}

    def test_use_github_set_to_value(self) -> None:
        '''Test setting use_github with value.'''
        self.instance.use_github = True
        self.assertEqual(self.instance.use_github, True)

    def test_use_github_set_twice(self) -> None:
        '''Test setting use_github twice.'''
        self.instance.use_github = True
        self.instance.use_github = True
        self.assertEqual(self.instance.use_github, True)

    def test_use_github_set_then_changed(self) -> None:
        '''Test setting use_github then changing it.'''
        self.instance.use_github = True
        self.assertEqual(self.instance.use_github, True)
        self.instance.use_github = False
        self.assertEqual(self.instance.use_github, False)

    def test_use_github_not_none_after_set(self) -> None:
        '''Test that use_github is not None after setting it.'''
        self.instance.use_github = True
        self.assertTrue(self.instance.not_none())

    def test_use_github_bool_after_set(self) -> None:
        '''Test that use_github is a bool after setting it.'''
        self.instance.use_github = True
        self.assertIsInstance(self.instance.use_github, bool)

    def test_use_github_str_representation(self) -> None:
        '''Test string representation of use_github.'''
        self.instance.use_github = True
        self.assertIsInstance(str(self.instance.use_github), str)
        self.assertEqual(str(self.instance.use_github), r'True')
        self.assertNotEqual(str(self.instance.use_github), 'False')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
