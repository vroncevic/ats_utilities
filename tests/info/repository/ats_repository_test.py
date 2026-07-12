# -*- coding: UTF-8 -*-

'''
Module
    ats_repository_test.py
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
    Defines classes RepositoryTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Repository.
Execute
    python3 -m unittest -v ats_repository_test
'''

from unittest import TestCase, main

from ats_utilities.info.repository.irepository import IRepository
from ats_utilities.info.repository.engine import Repository
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class RepositoryTestCase(TestCase):
    '''
        Defines classes RepositoryTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Repository.
        Repository unit tests.

        It defines:

            :attributes:
                | instance - API for repository.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that Repository instance is not None.
                | test_repository_value_is_none_by_default - Test that repository value is None by default.
                | test_repository_try_to_set_none - Test setting repository to None.
                | test_repository_try_to_set_wrong_type - Test wrong type for repository.
                | test_repository_set_to_value - Test setting repository with value.
                | test_repository_set_twice - Test setting repository twice.
                | test_repository_set_then_changed - Test setting repository then changing it.
                | test_repository_not_none_after_set - Test that repository is not None after setting it.
                | test_repository_string_after_set - Test that repository is a string after setting it.
                | test_repository_str_representation - Test string representation of repository.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = Repository()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default Repository instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, IRepository)

    def test_repository_value_is_none_by_default(self) -> None:
        '''Test repository value is None by default.'''
        self.assertIsNone(self.instance.repository)
        self.assertFalse(self.instance.not_none())

    def test_repository_try_to_set_none(self) -> None:
        '''Test setting repository to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.repository = None

    def test_repository_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for repository.'''
        with self.assertRaises(ATSTypeError):
            self.instance.repository = True

        with self.assertRaises(ATSTypeError):
            self.instance.repository = 123

        with self.assertRaises(ATSTypeError):
            self.instance.repository = [r'myrepository']

        with self.assertRaises(ATSTypeError):
            self.instance.repository = (r'myrepository',)

        with self.assertRaises(ATSTypeError):
            self.instance.repository = {'repository': r'myrepository'}

    def test_repository_set_to_value(self) -> None:
        '''Test setting repository with value.'''
        self.instance.repository = r'myrepository'
        self.assertEqual(self.instance.repository, r'myrepository')

    def test_repository_set_twice(self) -> None:
        '''Test setting repository twice.'''
        self.instance.repository = r'myrepository'
        self.instance.repository = r'myrepository'
        self.assertEqual(self.instance.repository, r'myrepository')

    def test_repository_set_then_changed(self) -> None:
        '''Test setting repository then changing it.'''
        self.instance.repository = r'myrepository'
        self.assertEqual(self.instance.repository, r'myrepository')
        self.instance.repository = r'notmyrepository'
        self.assertEqual(self.instance.repository, r'notmyrepository')

    def test_repository_not_none_after_set(self) -> None:
        '''Test that repository is not None after setting it.'''
        self.instance.repository = r'notmyrepository'
        self.assertTrue(self.instance.not_none())

    def test_repository_string_after_set(self) -> None:
        '''Test that repository is a string after setting it.'''
        self.instance.repository = r'notmyrepository'
        self.assertIsInstance(self.instance.repository, str)

    def test_repository_str_representation(self) -> None:
        '''Test string representation of repository.'''
        self.instance.repository = r'notmyrepository'
        self.assertIsInstance(str(self.instance.repository), str)
        self.assertEqual(str(self.instance.repository), r'notmyrepository')
        self.assertNotEqual(str(self.instance.repository), r'myrepository')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
