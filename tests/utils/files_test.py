# -*- coding: UTF-8 -*-

'''
Module
    files_test.py
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
    Unit tests for factory file utility functions.
'''

from __future__ import annotations

import os
import shutil
import tempfile
import unittest

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.utils.files import (
    apply_path_replacements,
    check_file_exists,
    format_casing_by_match,
    is_excluded_path,
    normalize_path,
    resolve_relative_path,
    write_content,
)

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FilesTest(unittest.TestCase):
    '''
        Defines class FilesTest with attribute(s) and method(s).
        Tests factory file utility functions.

        It defines:

            :attributes:
                | _temp_dir - Path to the temporary directory used for I/O tests.
            :methods:
                | setUp - Sets up temporary directory.
                | tearDown - Cleans up temporary directory.
                | test_check_file_exists_valid - Tests check_file_exists with valid file.
                | test_check_file_exists_invalid - Tests check_file_exists with missing file.
                | test_check_file_exists_empty_or_invalid_type - Tests check_file_exists exceptions.
                | test_normalize_path - Tests normalize_path logic.
                | test_normalize_path_mock_drive - Tests normalize_path with mocked drive path.
                | test_normalize_path_exceptions - Tests normalize_path error handling.
                | test_resolve_relative_path - Tests resolve_relative_path logic.
                | test_resolve_relative_path_exceptions - Tests resolve_relative_path error handling.
                | test_is_excluded_path - Tests is_excluded_path logic.
                | test_is_excluded_path_exceptions - Tests is_excluded_path error handling.
                | test_format_casing_by_match - Tests format_casing_by_match logic.
                | test_format_casing_by_match_exceptions - Tests format_casing_by_match error handling.
                | test_write_content - Tests write_content with string and bytes.
                | test_write_content_exceptions - Tests write_content error handling.
                | test_apply_path_replacements - Tests apply_path_replacements logic.
                | test_apply_path_replacements_exceptions - Tests apply_path_replacements error handling.
    '''

    def setUp(self) -> None:
        '''
            Sets up temporary directory.

            :exceptions: None.
        '''
        self._temp_dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        '''
            Cleans up temporary directory.

            :exceptions: None.
        '''
        shutil.rmtree(self._temp_dir)

    def test_check_file_exists_valid(self) -> None:
        '''
            Tests check_file_exists with valid file.

            :exceptions: None.
        '''
        file_path = os.path.join(self._temp_dir, "test.txt")
        with open(file_path, "w") as f:
            f.write("hello")
        try:
            check_file_exists(file_path, 'filestest::test_check_file_exists_valid')
        except ATSValueError:
            self.fail("check_file_exists raised ATSValueError unexpectedly.")

    def test_check_file_exists_invalid(self) -> None:
        '''
            Tests check_file_exists with missing file.

            :exceptions: None.
        '''
        file_path = os.path.join(self._temp_dir, "nonexistent.txt")
        with self.assertRaises(ATSValueError) as ctx:
            check_file_exists(file_path, 'filestest::test_check_file_exists_invalid')
        self.assertIn("file at the provided path does not exist", str(ctx.exception))

    def test_check_file_exists_empty_or_invalid_type(self) -> None:
        '''
            Tests check_file_exists exceptions.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            check_file_exists("", 'filestest::test_check_file_exists_empty_or_invalid_type')

        with self.assertRaises(ATSTypeError):
            check_file_exists(123, 'filestest::test_check_file_exists_empty_or_invalid_type')  # type: ignore

    def test_normalize_path(self) -> None:
        '''
            Tests normalize_path logic.

            :exceptions: None.
        '''
        self.assertEqual(normalize_path("a\\b\\c", 'filestest::test_normalize_path'), "a/b/c")
        self.assertEqual(normalize_path("/a/b/c", 'filestest::test_normalize_path'), "a/b/c")
        self.assertEqual(normalize_path("C:\\a\\b", 'filestest::test_normalize_path'), "C:/a/b")

    def test_normalize_path_mock_drive(self) -> None:
        '''
            Tests normalize_path with a mocked drive path.

            :exceptions: None.
        '''
        from unittest.mock import patch, MagicMock

        mock_path = MagicMock()
        mock_path.drive = "C:"
        mock_path.parts = ("C:", "a", "b")
        mock_path.as_posix.return_value = "a/b"

        with patch("ats_utilities.utils.files.PurePosixPath", return_value=mock_path):
            result = normalize_path("C:\\a\\b", 'filestest::test_normalize_path_mock_drive')
            self.assertEqual(result, "a/b")

    def test_normalize_path_exceptions(self) -> None:
        '''
            Tests normalize_path error handling.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            normalize_path("", 'filestest::test_normalize_path_exceptions')

        with self.assertRaises(ATSTypeError):
            normalize_path(123, 'filestest::test_normalize_path_exceptions')  # type: ignore

    def test_resolve_relative_path(self) -> None:
        '''
            Tests resolve_relative_path logic.

            :exceptions: None.
        '''
        self.assertEqual(resolve_relative_path("a/b/c", "a/b/c", 'filestest::test_resolve_relative_path'), "")
        self.assertEqual(resolve_relative_path("a/b/c", "a/b", 'filestest::test_resolve_relative_path'), "c")
        self.assertEqual(resolve_relative_path("a/b/c", "x/y", 'filestest::test_resolve_relative_path'), None)

    def test_resolve_relative_path_exceptions(self) -> None:
        '''
            Tests resolve_relative_path error handling.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            resolve_relative_path("", "a/b", 'filestest::test_resolve_relative_path_exceptions')
        with self.assertRaises(ATSValueError):
            resolve_relative_path("a/b", "", 'filestest::test_resolve_relative_path_exceptions')
        with self.assertRaises(ATSTypeError):
            resolve_relative_path(123, "a/b", 'filestest::test_resolve_relative_path_exceptions')  # type: ignore

    def test_is_excluded_path(self) -> None:
        '''
            Tests is_excluded_path logic.

            :exceptions: None.
        '''
        self.assertTrue(is_excluded_path("a/b/c.py", ["*.py"], 'filestest::test_is_excluded_path'))
        self.assertTrue(is_excluded_path("a/b/c", ["**/b/**"], 'filestest::test_is_excluded_path'))
        self.assertFalse(is_excluded_path("a/b/c.txt", ["*.py"], 'filestest::test_is_excluded_path'))

    def test_is_excluded_path_exceptions(self) -> None:
        '''
            Tests is_excluded_path error handling.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            is_excluded_path("", ["*.py"], 'filestest::test_is_excluded_path_exceptions')
        with self.assertRaises(ATSValueError):
            is_excluded_path("a/b", [], 'filestest::test_is_excluded_path_exceptions')
        with self.assertRaises(ATSTypeError):
            is_excluded_path(123, ["*.py"], 'filestest::test_is_excluded_path_exceptions')  # type: ignore

    def test_format_casing_by_match(self) -> None:
        '''
            Tests format_casing_by_match logic.

            :exceptions: None.
        '''
        self.assertEqual(format_casing_by_match("CLEAN", "def", "UPP", "Cam", "das", 'filestest::test_format_casing_by_match'), "UPP")
        self.assertEqual(format_casing_by_match("Clean", "def", "UPP", "Cam", "das", 'filestest::test_format_casing_by_match'), "Cam")
        self.assertEqual(format_casing_by_match("clean-str", "def", "UPP", "Cam", "das", 'filestest::test_format_casing_by_match'), "das")
        self.assertEqual(format_casing_by_match("clean_str", "def", "UPP", "Cam", "das", 'filestest::test_format_casing_by_match'), "def")

    def test_format_casing_by_match_exceptions(self) -> None:
        '''
            Tests format_casing_by_match error handling.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            format_casing_by_match("", "def", "UPP", "Cam", "das", 'filestest::test_format_casing_by_match_exceptions')
        with self.assertRaises(ATSValueError):
            format_casing_by_match("clean", "", "UPP", "Cam", "das", 'filestest::test_format_casing_by_match_exceptions')
        with self.assertRaises(ATSValueError):
            format_casing_by_match("clean", "def", "", "Cam", "das", 'filestest::test_format_casing_by_match_exceptions')
        with self.assertRaises(ATSValueError):
            format_casing_by_match("clean", "def", "UPP", "", "das", 'filestest::test_format_casing_by_match_exceptions')
        with self.assertRaises(ATSValueError):
            format_casing_by_match("clean", "def", "UPP", "Cam", "", 'filestest::test_format_casing_by_match_exceptions')
        with self.assertRaises(ATSTypeError):
            format_casing_by_match(123, "def", "UPP", "Cam", "das", 'filestest::test_format_casing_by_match_exceptions')  # type: ignore

    def test_write_content(self) -> None:
        '''
            Tests write_content with string and bytes.

            :exceptions: None.
        '''
        file_path_str = os.path.join(self._temp_dir, "subdir", "test_str.txt")
        file_path_bytes = os.path.join(self._temp_dir, "subdir", "test_bytes.bin")

        write_content(file_path_str, "hello world", 'filestest::test_write_content')
        self.assertTrue(os.path.exists(file_path_str))
        with open(file_path_str, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "hello world")

        write_content(file_path_bytes, b"hello bytes", 'filestest::test_write_content')
        self.assertTrue(os.path.exists(file_path_bytes))
        with open(file_path_bytes, "rb") as f:
            self.assertEqual(f.read(), b"hello bytes")

    def test_write_content_exceptions(self) -> None:
        '''
            Tests write_content error handling.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            write_content("", "hello", 'filestest::test_write_content_exceptions')
        with self.assertRaises(ATSValueError):
            write_content("path", "", 'filestest::test_write_content_exceptions')
        with self.assertRaises(ATSTypeError):
            write_content(123, "hello", 'filestest::test_write_content_exceptions')  # type: ignore

    def test_apply_path_replacements(self) -> None:
        '''
            Tests apply_path_replacements logic.

            :exceptions: None.
        '''
        replacements = {"project_name": "app_name"}
        vals = {
            "app_name": "my_new_app",
            "app_name_upper": "MY_NEW_APP",
            "app_name_camel": "MyNewApp",
            "app_name_dashed": "my-new-app",
        }

        self.assertEqual(
            apply_path_replacements("PROJECT-NAME/src", replacements, vals, 'filestest::test_apply_path_replacements'),
            "MY_NEW_APP/src"
        )
        self.assertEqual(
            apply_path_replacements("project-name/src", replacements, vals, 'filestest::test_apply_path_replacements'),
            "my-new-app/src"
        )
        self.assertEqual(
            apply_path_replacements("ProjectName/src", replacements, vals, 'filestest::test_apply_path_replacements'),
            "MyNewApp/src"
        )
        self.assertEqual(
            apply_path_replacements("PROJECT_NAME/src", replacements, vals, 'filestest::test_apply_path_replacements'),
            "MY_NEW_APP/src"
        )
        self.assertEqual(
            apply_path_replacements("project_name/src", replacements, vals, 'filestest::test_apply_path_replacements'),
            "my_new_app/src"
        )

        # Missing replacement variable
        self.assertEqual(
            apply_path_replacements("project_name/src", {"project_name": "missing_var"}, vals, 'filestest::test_apply_path_replacements'),
            "project_name/src"
        )

        # Empty words case in replacement
        self.assertEqual(
            apply_path_replacements("---/src", {"---": "val"}, {"val": "replacement"}, 'filestest::test_apply_path_replacements'),
            "replacement/src"
        )

    def test_apply_path_replacements_exceptions(self) -> None:
        '''
            Tests apply_path_replacements error handling.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            apply_path_replacements("", {"a": "b"}, {"b": "c"}, 'filestest::test_apply_path_replacements_exceptions')
        with self.assertRaises(ATSValueError):
            apply_path_replacements("a", {}, {"b": "c"}, 'filestest::test_apply_path_replacements_exceptions')
        with self.assertRaises(ATSValueError):
            apply_path_replacements("a", {"a": "b"}, {}, 'filestest::test_apply_path_replacements_exceptions')
        with self.assertRaises(ATSTypeError):
            apply_path_replacements(123, {"a": "b"}, {"b": "c"}, 'filestest::test_apply_path_replacements_exceptions')  # type: ignore


if __name__ == "__main__":
    unittest.main()
