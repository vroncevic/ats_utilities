# -*- coding: UTF-8 -*-

'''
Module
    ats_build_date_test.py
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
    Defines classes BuildDateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of BuildDate.
Execute
    python3 -m unittest -v ats_build_date_test
'''

from unittest import TestCase, main

from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.build_date.engine import BuildDate
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class BuildDateTestCase(TestCase):
    '''
        Defines classes BuildDateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of BuildDate.
        BuildDate unit tests.

        It defines:

            :attributes:
                | instance - API for build date.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that BuildDate instance is not None.
                | test_build_date_value_is_none_by_default - Test that build date value is None by default.
                | test_build_date_try_to_set_none - Test setting build date to None.
                | test_build_date_try_to_set_wrong_type - Test wrong type for build date.
                | test_build_date_set_to_value - Test setting build date with value.
                | test_build_date_set_twice - Test setting build date twice.
                | test_build_date_set_then_changed - Test setting build date then changing it.
                | test_build_date_not_none_after_set - Test that build date is not None after setting it.
                | test_build_date_string_after_set - Test that build date is a string after setting it.
                | test_build_date_str_representation - Test string representation of build date.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = BuildDate()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default BuildDate instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, IBuildDate)

    def test_build_date_value_is_none_by_default(self) -> None:
        '''Test build date value is None by default.'''
        self.assertIsNone(self.instance.build_date)
        self.assertFalse(self.instance.not_none())

    def test_build_date_try_to_set_none(self) -> None:
        '''Test setting build date to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.build_date = None

    def test_build_date_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for build date.'''
        with self.assertRaises(ATSTypeError):
            self.instance.build_date = True

        with self.assertRaises(ATSTypeError):
            self.instance.build_date = 123

        with self.assertRaises(ATSTypeError):
            self.instance.build_date = [r'Sun 25 Apr 2021 08:12:40 PM CEST']

        with self.assertRaises(ATSTypeError):
            self.instance.build_date = (r'Sun 25 Apr 2021 08:12:40 PM CEST',)

        with self.assertRaises(ATSTypeError):
            self.instance.build_date = {'build_date': r'Sun 25 Apr 2021 08:12:40 PM CEST'}

    def test_build_date_set_to_value(self) -> None:
        '''Test setting build date with value.'''
        self.instance.build_date = r'Sun 25 Apr 2021 08:12:40 PM CEST'
        self.assertEqual(self.instance.build_date, r'Sun 25 Apr 2021 08:12:40 PM CEST')

    def test_build_date_set_twice(self) -> None:
        '''Test setting build date twice.'''
        self.instance.build_date = r'Sun 25 Apr 2021 08:12:40 PM CEST'
        self.instance.build_date = r'Sun 25 Apr 2021 08:12:40 PM CEST'
        self.assertEqual(self.instance.build_date, r'Sun 25 Apr 2021 08:12:40 PM CEST')

    def test_build_date_set_then_changed(self) -> None:
        '''Test setting build date then changing it.'''
        self.instance.build_date = r'Sun 25 Apr 2021 08:12:40 PM CEST'
        self.assertEqual(self.instance.build_date, r'Sun 25 Apr 2021 08:12:40 PM CEST')
        self.instance.build_date = r'Sun 25 Apr 2022 08:12:40 PM CEST'
        self.assertEqual(self.instance.build_date, r'Sun 25 Apr 2022 08:12:40 PM CEST')

    def test_build_date_not_none_after_set(self) -> None:
        '''Test that build date is not None after setting it.'''
        self.instance.build_date = r'Sun 25 Apr 2022 08:12:40 PM CEST'
        self.assertTrue(self.instance.not_none())

    def test_build_date_string_after_set(self) -> None:
        '''Test that build date is a string after setting it.'''
        self.instance.build_date = r'Sun 25 Apr 2022 08:12:40 PM CEST'
        self.assertIsInstance(self.instance.build_date, str)

    def test_build_date_str_representation(self) -> None:
        '''Test string representation of build date.'''
        self.instance.build_date = r'Sun 25 Apr 2022 08:12:40 PM CEST'
        self.assertIsInstance(str(self.instance.build_date), str)
        self.assertEqual(str(self.instance.build_date), r'Sun 25 Apr 2022 08:12:40 PM CEST')
        self.assertNotEqual(str(self.instance.build_date), r'Sun 25 Apr 2022 08:12:41 PM CEST')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
