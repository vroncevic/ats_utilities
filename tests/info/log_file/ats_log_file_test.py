# -*- coding: UTF-8 -*-

'''
Module
    ats_log_file_test.py
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
    Defines classes LogFileTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of LogFile.
Execute
    python3 -m unittest -v ats_log_file_test
'''

from unittest import TestCase, main

from ats_utilities.info.log_file.ilog_file import ILogFile
from ats_utilities.info.log_file.engine import LogFile
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LogFileTestCase(TestCase):
    '''
        Defines classes LogFileTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of LogFile.
        LogFile unit tests.

        It defines:

            :attributes:
                | instance - API for log_file.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that LogFile instance is not None.
                | test_log_file_value_is_none_by_default - Test that log_file value is None by default.
                | test_log_file_try_to_set_none - Test setting log_file to None.
                | test_log_file_try_to_set_wrong_type - Test wrong type for log_file.
                | test_log_file_set_to_value - Test setting log_file with value.
                | test_log_file_set_twice - Test setting log_file twice.
                | test_log_file_set_then_changed - Test setting log_file then changing it.
                | test_log_file_not_none_after_set - Test that log_file is not None after setting it.
                | test_log_file_string_after_set - Test that log_file is a string after setting it.
                | test_log_file_str_representation - Test string representation of log_file.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = LogFile()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default LogFile instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, ILogFile)

    def test_log_file_value_is_none_by_default(self) -> None:
        '''Test log_file value is None by default.'''
        self.assertIsNone(self.instance.log_file)
        self.assertFalse(self.instance.not_none())

    def test_log_file_try_to_set_none(self) -> None:
        '''Test setting log_file to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.log_file = None

    def test_log_file_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for log_file.'''
        with self.assertRaises(ATSTypeError):
            self.instance.log_file = True

        with self.assertRaises(ATSTypeError):
            self.instance.log_file = 123

        with self.assertRaises(ATSTypeError):
            self.instance.log_file = [r'tool.log']

        with self.assertRaises(ATSTypeError):
            self.instance.log_file = (r'tool.log',)

        with self.assertRaises(ATSTypeError):
            self.instance.log_file = {'log_file': r'tool.log'}

    def test_log_file_set_to_value(self) -> None:
        '''Test setting log_file with value.'''
        self.instance.log_file = r'tool.log'
        self.assertEqual(self.instance.log_file, r'tool.log')

    def test_log_file_set_twice(self) -> None:
        '''Test setting log_file twice.'''
        self.instance.log_file = r'tool.log'
        self.instance.log_file = r'tool.log'
        self.assertEqual(self.instance.log_file, r'tool.log')

    def test_log_file_set_then_changed(self) -> None:
        '''Test setting log_file then changing it.'''
        self.instance.log_file = r'tool.log'
        self.assertEqual(self.instance.log_file, r'tool.log')
        self.instance.log_file = r'debug.log'
        self.assertEqual(self.instance.log_file, r'debug.log')

    def test_log_file_not_none_after_set(self) -> None:
        '''Test that log_file is not None after setting it.'''
        self.instance.log_file = r'debug.log'
        self.assertTrue(self.instance.not_none())

    def test_log_file_string_after_set(self) -> None:
        '''Test that log_file is a string after setting it.'''
        self.instance.log_file = r'debug.log'
        self.assertIsInstance(self.instance.log_file, str)

    def test_log_file_str_representation(self) -> None:
        '''Test string representation of log_file.'''
        self.instance.log_file = r'debug.log'
        self.assertIsInstance(str(self.instance.log_file), str)
        self.assertEqual(str(self.instance.log_file), r'debug.log')
        self.assertNotEqual(str(self.instance.log_file), r'tool.log')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
