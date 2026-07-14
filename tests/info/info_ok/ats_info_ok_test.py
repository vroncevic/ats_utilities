# -*- coding: UTF-8 -*-

'''
Module
    ats_info_ok_test.py
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
    Defines classes InfoOkTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of InfoOk.
Execute
    python3 -m unittest -v ats_info_ok_test
'''

from unittest import TestCase, main

from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.info.info_ok.engine import InfoOk
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoOkTestCase(TestCase):
    '''
        Defines classes InfoOkTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of InfoOk.
        InfoOk unit tests.

        It defines:

            :attributes:
                | instance - API for info_ok.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that InfoOk instance is not None.
                | test_info_ok_value_none_by_default - Test that info_ok value is None by default.
                | test_info_ok_try_to_set_none - Test setting info_ok to None.
                | test_info_ok_try_to_set_wrong_type - Test wrong type for info_ok.
                | test_info_ok_set_to_value - Test setting info_ok with value.
                | test_info_ok_set_twice - Test setting info_ok twice.
                | test_info_ok_set_then_changed - Test setting info_ok then changing it.
                | test_info_ok_not_none_after_set - Test that info_ok is not None after setting it.
                | test_info_ok_bool_after_set - Test that info_ok is a boolean after setting it.
                | test_info_ok_str_representation - Test string representation of info_ok.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = InfoOk()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default InfoOk instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, IInfoOk)

    def test_info_ok_value_not_none_by_default(self) -> None:
        '''Test info_ok value is not None by default.'''
        self.assertIsNotNone(self.instance.info_ok)
        self.assertTrue(self.instance.not_none())

    def test_info_ok_try_to_set_none(self) -> None:
        '''Test setting info_ok to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.info_ok = None

    def test_info_ok_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for info_ok.'''
        with self.assertRaises(ATSTypeError):
            self.instance.info_ok = r'True'

        with self.assertRaises(ATSTypeError):
            self.instance.info_ok = 123

        with self.assertRaises(ATSTypeError):
            self.instance.info_ok = [True]

        with self.assertRaises(ATSTypeError):
            self.instance.info_ok = (True,)

        with self.assertRaises(ATSTypeError):
            self.instance.info_ok = {'info_ok': True}

    def test_info_ok_set_to_value(self) -> None:
        '''Test setting info_ok with value.'''
        self.instance.info_ok = True
        self.assertTrue(self.instance.info_ok)
        self.assertTrue(self.instance.not_none())

    def test_info_ok_set_twice(self) -> None:
        '''Test setting info_ok twice.'''
        self.instance.info_ok = True
        self.instance.info_ok = True
        self.assertTrue(self.instance.info_ok)
        self.assertTrue(self.instance.not_none())

    def test_info_ok_set_then_changed(self) -> None:
        '''Test setting info_ok then changing it.'''
        self.instance.info_ok = True
        self.assertTrue(self.instance.info_ok)
        self.assertTrue(self.instance.not_none())
        self.instance.info_ok = False
        self.assertFalse(self.instance.info_ok)
        self.assertTrue(self.instance.not_none())

    def test_info_ok_not_none_after_set(self) -> None:
        '''Test that info_ok is not None after setting it.'''
        self.instance.info_ok = True
        self.assertTrue(self.instance.info_ok)

    def test_info_ok_bool_after_set(self) -> None:
        '''Test that info_ok is a boolean after setting it.'''
        self.instance.info_ok = True
        self.assertIsInstance(self.instance.info_ok, bool)

    def test_info_ok_str_representation(self) -> None:
        '''Test string representation of info_ok.'''
        self.instance.info_ok = True
        self.assertIsInstance(str(self.instance.info_ok), str)
        self.assertEqual(str(self.instance.info_ok), r'True')
        self.assertNotEqual(str(self.instance.info_ok), r'False')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
