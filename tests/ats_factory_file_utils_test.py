# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_file_utils_test.py
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
    Defines class ATSFactoryFileUtilsTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of factory_file_utils functions.
Execute
    python3 -m unittest -v ats_factory_file_utils_test
'''

import os
from unittest import TestCase, main, mock
from ats_utilities.factory_file_utils import (
    check_file_exists, normalize_path, resolve_relative_path, is_excluded_path,
    format_casing_by_match, write_content, apply_path_replacements
)
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ATSFactoryFileUtilsTestCase(TestCase):
    '''
        Defines class ATSFactoryFileUtilsTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of factory_file_utils functions.
    '''

    def test_check_file_exists_success(self) -> None:
        check_file_exists(__file__)

    def test_check_file_exists_failure(self) -> None:
        with self.assertRaises(ATSValueError):
            check_file_exists("non_existing_file_path_12345.txt")

    def test_check_file_exists_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            check_file_exists(123)  # type: ignore

    def test_normalize_path(self) -> None:
        self.assertEqual(normalize_path('./foo/bar'), 'foo/bar')
        self.assertEqual(normalize_path('/foo/bar\\baz'), 'foo/bar/baz')
        with self.assertRaises(ATSTypeError):
            normalize_path(123)  # type: ignore

    @mock.patch('ats_utilities.factory_file_utils.normpath')
    def test_normalize_path_starts_with_dot_slash(self, mock_normpath) -> None:
        mock_normpath.return_value = './foo/bar'
        self.assertEqual(normalize_path('anything'), 'foo/bar')

    def test_resolve_relative_path(self) -> None:
        self.assertEqual(resolve_relative_path('foo/bar', 'foo'), 'bar')
        self.assertEqual(resolve_relative_path('foo', 'foo'), '')
        self.assertIsNone(resolve_relative_path('bar/baz', 'foo'))
        with self.assertRaises(ATSTypeError):
            resolve_relative_path(123, 'foo')  # type: ignore
        with self.assertRaises(ATSTypeError):
            resolve_relative_path('foo', 123)  # type: ignore

    def test_is_excluded_path(self) -> None:
        self.assertTrue(is_excluded_path('foo/bar', ['*.py', 'bar']))
        self.assertFalse(is_excluded_path('foo/bar', ['*.py', 'baz']))
        with self.assertRaises(ATSTypeError):
            is_excluded_path(123, [])  # type: ignore
        with self.assertRaises(ATSTypeError):
            is_excluded_path('foo', 123)  # type: ignore

    def test_format_casing_by_match(self) -> None:
        self.assertEqual(
            format_casing_by_match('TASK_CLI', 'default', 'upper', 'camel', 'dashed'),
            'upper'
        )
        self.assertEqual(
            format_casing_by_match('TaskCLI', 'default', 'upper', 'camel', 'dashed'),
            'camel'
        )
        self.assertEqual(
            format_casing_by_match('task-cli', 'default', 'upper', 'camel', 'dashed'),
            'dashed'
        )
        self.assertEqual(
            format_casing_by_match('task_cli', 'default', 'upper', 'camel', 'dashed'),
            'default'
        )
        with self.assertRaises(ATSTypeError):
            format_casing_by_match(123, 'a', 'b', 'c', 'd')  # type: ignore

    def test_write_content(self) -> None:
        import tempfile
        # Test text mode write
        with tempfile.NamedTemporaryFile(delete=False) as f:
            path = f.name
        try:
            write_content(path, "hello world")
            with open(path, 'r', encoding='utf-8') as f_read:
                self.assertEqual(f_read.read(), "hello world")
        finally:
            if os.path.exists(path):
                os.remove(path)

        # Test binary mode write
        with tempfile.NamedTemporaryFile(delete=False) as f:
            path = f.name
        try:
            write_content(path, b"hello binary")
            with open(path, 'rb') as f_read:
                self.assertEqual(f_read.read(), b"hello binary")
        finally:
            if os.path.exists(path):
                os.remove(path)

        # Test validation checks
        with self.assertRaises(ATSTypeError):
            write_content(123, "content")  # type: ignore
        with self.assertRaises(ATSTypeError):
            write_content("path.txt", 123)  # type: ignore

    def test_apply_path_replacements(self) -> None:
        path_replacements = {'task_cli': 'service_name'}
        vals = {
            'service_name': 'billing_service',
            'service_name_upper': 'BILLING_SERVICE',
            'service_name_camel': 'BillingService',
            'service_name_dashed': 'billing-service'
        }
        self.assertEqual(
            apply_path_replacements('task_cli/main.py', path_replacements, vals),
            'billing_service/main.py'
        )
        self.assertEqual(
            apply_path_replacements('TASK_CLI/main.py', path_replacements, vals),
            'BILLING_SERVICE/main.py'
        )
        self.assertEqual(
            apply_path_replacements('TaskCLI/main.py', path_replacements, vals),
            'BillingService/main.py'
        )
        self.assertEqual(
            apply_path_replacements('task-cli/main.py', path_replacements, vals),
            'billing-service/main.py'
        )

        # Test replacement_val is None (line 232)
        path_replacements_none = {'task_cli': 'missing_var'}
        self.assertEqual(
            apply_path_replacements('task_cli/main.py', path_replacements_none, {'other_var': 'value'}),
            'task_cli/main.py'
        )

        # Test empty words in old_str (lines 237-238)
        path_replacements_empty_words = {'-': 'hyphen'}
        self.assertEqual(
            apply_path_replacements('task-cli/main.py', path_replacements_empty_words, {'hyphen': 'bar'}),
            'taskbarcli/main.py'
        )

        # Edge cases and validation checks
        with self.assertRaises(ATSTypeError):
            apply_path_replacements(123, path_replacements, vals)  # type: ignore
        with self.assertRaises(ATSTypeError):
            apply_path_replacements('path', 123, vals)  # type: ignore
        with self.assertRaises(ATSTypeError):
            apply_path_replacements('path', path_replacements, 123)  # type: ignore

    def test_factory_file_utils_unhappy_paths(self) -> None:
        '''Test unhappy path checks in factory_file_utils raising ATSValueError.'''
        with self.assertRaises(ATSValueError):
            check_file_exists("")

        with self.assertRaises(ATSValueError):
            normalize_path("")

        with self.assertRaises(ATSValueError):
            resolve_relative_path("", "foo")
        with self.assertRaises(ATSValueError):
            resolve_relative_path("foo", "")

        with self.assertRaises(ATSValueError):
            is_excluded_path("", ["pattern"])
        with self.assertRaises(ATSValueError):
            is_excluded_path("foo", [])

        with self.assertRaises(ATSValueError):
            format_casing_by_match("", "d", "u", "c", "da")
        with self.assertRaises(ATSValueError):
            format_casing_by_match("foo", "", "u", "c", "da")
        with self.assertRaises(ATSValueError):
            format_casing_by_match("foo", "d", "", "c", "da")
        with self.assertRaises(ATSValueError):
            format_casing_by_match("foo", "d", "u", "", "da")
        with self.assertRaises(ATSValueError):
            format_casing_by_match("foo", "d", "u", "c", "")

        with self.assertRaises(ATSValueError):
            write_content("", "content")
        with self.assertRaises(ATSValueError):
            write_content("path", "")

        with self.assertRaises(ATSValueError):
            apply_path_replacements("", {"a": "b"}, {"b": "c"})
        with self.assertRaises(ATSValueError):
            apply_path_replacements("path", {}, {"b": "c"})
        with self.assertRaises(ATSValueError):
            apply_path_replacements("path", {"a": "b"}, {})


if __name__ == '__main__':
    main()
