# -*- coding: UTF-8 -*-

'''
Module
    ats_licence_test.py
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
    Defines classes LicenceTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Licence.
Execute
    python3 -m unittest -v ats_licence_test
'''

from unittest import TestCase, main

from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.licence.engine import Licence
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LicenceTestCase(TestCase):
    '''
        Defines classes LicenceTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Licence.
        Licence unit tests.

        It defines:

            :attributes:
                | instance - API for licence.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that Licence instance is not None.
                | test_licence_value_is_none_by_default - Test that licence value is None by default.
                | test_licence_try_to_set_none - Test setting licence to None.
                | test_licence_try_to_set_wrong_type - Test wrong type for licence.
                | test_licence_set_to_value - Test setting licence with value.
                | test_licence_set_twice - Test setting licence twice.
                | test_licence_set_then_changed - Test setting licence then changing it.
                | test_licence_not_none_after_set - Test that licence is not None after setting it.
                | test_licence_string_after_set - Test that licence is a string after setting it.
                | test_licence_str_representation - Test string representation of licence.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = Licence()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default Licence instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, ILicence)

    def test_licence_value_is_none_by_default(self) -> None:
        '''Test licence value is None by default.'''
        self.assertIsNone(self.instance.licence)
        self.assertFalse(self.instance.not_none())

    def test_licence_try_to_set_none(self) -> None:
        '''Test setting licence to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.licence = None

    def test_licence_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for licence.'''
        with self.assertRaises(ATSTypeError):
            self.instance.licence = True

        with self.assertRaises(ATSTypeError):
            self.instance.licence = 123

        with self.assertRaises(ATSTypeError):
            self.instance.licence = [r'GPLv2']

        with self.assertRaises(ATSTypeError):
            self.instance.licence = (r'GPLv2',)

        with self.assertRaises(ATSTypeError):
            self.instance.licence = {'licence': r'GPLv2'}

    def test_licence_set_to_value(self) -> None:
        '''Test setting licence with value.'''
        self.instance.licence = r'GPLv2'
        self.assertEqual(self.instance.licence, r'GPLv2')

    def test_licence_set_twice(self) -> None:
        '''Test setting licence twice.'''
        self.instance.licence = r'GPLv2'
        self.instance.licence = r'GPLv2'
        self.assertEqual(self.instance.licence, r'GPLv2')

    def test_licence_set_then_changed(self) -> None:
        '''Test setting licence then changing it.'''
        self.instance.licence = r'GPLv2'
        self.assertEqual(self.instance.licence, r'GPLv2')
        self.instance.licence = r'MIT'
        self.assertEqual(self.instance.licence, r'MIT')

    def test_licence_not_none_after_set(self) -> None:
        '''Test that licence is not None after setting it.'''
        self.instance.licence = r'MIT'
        self.assertTrue(self.instance.not_none())

    def test_licence_string_after_set(self) -> None:
        '''Test that licence is a string after setting it.'''
        self.instance.licence = r'MIT'
        self.assertIsInstance(self.instance.licence, str)

    def test_licence_str_representation(self) -> None:
        '''Test string representation of licence.'''
        self.instance.licence = r'MIT'
        self.assertIsInstance(str(self.instance.licence), str)
        self.assertEqual(str(self.instance.licence), r'MIT')
        self.assertNotEqual(str(self.instance.licence), r'GPLv2')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
