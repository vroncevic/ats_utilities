# -*- coding: UTF-8 -*-

'''
Module
    data_test.py
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
    Unit tests for TarData and TarMemberData classes.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from tarfile import TarFile, TarInfo
from unittest.mock import MagicMock

from ats_utilities.generation.tar.data import TarData, TarMemberData


class TarDataTest(unittest.TestCase):
    '''
        Defines class TarDataTest with attribute(s) and method(s).
        Tests TarData and TarMemberData logic.
    '''

    def setUp(self) -> None:
        self.valid_tar_params = {
            "archive_path": "/path/to/archive.tgz",
            "target_dir": "/path/to/target",
            "source_dir": "templates/core",
            "path_replacements": {"__name__": "my_module"},
            "exclude_patterns": ["*.pyc"],
            "vals": {"author": "Vladimir"}
        }
        self.mock_tar = MagicMock(spec=TarFile)
        self.mock_member = MagicMock(spec=TarInfo)
        self.valid_member_params = {
            "tar": self.mock_tar,
            "member": self.mock_member,
            "dest_full_path": "/path/to/dest",
            "vals": {"author": "Vladimir"}
        }

    def test_tar_data_init_valid(self) -> None:
        data = TarData(**self.valid_tar_params)
        self.assertEqual(data.archive_path, "/path/to/archive.tgz")
        self.assertEqual(data.exclude_patterns, ["*.pyc"])

    def test_tar_data_frozen_slots(self) -> None:
        data = TarData(**self.valid_tar_params)
        with self.assertRaises(FrozenInstanceError):
            data.archive_path = "/new/path"  # type: ignore
        with self.assertRaises(AttributeError):
            data.__dict__  # type: ignore

    def test_tar_data_to_dict(self) -> None:
        data = TarData(**self.valid_tar_params)
        d = data.to_dict()
        self.assertEqual(d["archive_path"], "/path/to/archive.tgz")

    def test_tar_member_data_init_valid(self) -> None:
        data = TarMemberData(**self.valid_member_params)
        self.assertIs(data.tar, self.mock_tar)
        self.assertEqual(data.dest_full_path, "/path/to/dest")

    def test_tar_member_data_frozen_slots(self) -> None:
        data = TarMemberData(**self.valid_member_params)
        with self.assertRaises(FrozenInstanceError):
            data.dest_full_path = "/new/path"  # type: ignore
        with self.assertRaises(AttributeError):
            data.__dict__  # type: ignore

    def test_tar_member_data_to_dict(self) -> None:
        data = TarMemberData(**self.valid_member_params)
        d = data.to_dict()
        self.assertEqual(d["dest_full_path"], "/path/to/dest")


if __name__ == "__main__":
    unittest.main()
