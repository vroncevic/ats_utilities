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
    Unit tests for GeneratorData class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError

from ats_utilities.generation.data import GeneratorData


class GeneratorDataTest(unittest.TestCase):
    '''
        Defines class GeneratorDataTest with attribute(s) and method(s).
        Tests GeneratorData component logic.
    '''

    def setUp(self) -> None:
        self.valid_params = {
            "archive_path": "/path/to/archive.tgz",
            "target_dir": "/path/to/target",
            "template_key": "python_library",
            "scheme": {"author": "Vladimir"},
            "template_values": {"NAME": "ats_utilities"}
        }

    def test_init_valid(self) -> None:
        data = GeneratorData(**self.valid_params)
        self.assertEqual(data.archive_path, "/path/to/archive.tgz")
        self.assertEqual(data.target_dir, "/path/to/target")
        self.assertEqual(data.template_key, "python_library")
        self.assertEqual(data.scheme, {"author": "Vladimir"})
        self.assertEqual(data.template_values, {"NAME": "ats_utilities"})

    def test_frozen(self) -> None:
        data = GeneratorData(**self.valid_params)
        with self.assertRaises(FrozenInstanceError):
            data.archive_path = "/new/path"  # type: ignore

    def test_slots(self) -> None:
        data = GeneratorData(**self.valid_params)
        with self.assertRaises(AttributeError):
            data.__dict__  # type: ignore

    def test_kw_only(self) -> None:
        with self.assertRaises(TypeError):
            GeneratorData(
                # pyrefly: ignore [unexpected-positional-argument]
                "/path/to/archive.tgz",
                # pyrefly: ignore [unexpected-positional-argument]
                "/path/to/target",
                # pyrefly: ignore [unexpected-positional-argument]
                "python_library",
                # pyrefly: ignore [unexpected-positional-argument]
                {"author": "Vladimir"},
                # pyrefly: ignore [unexpected-positional-argument]
                {"NAME": "ats_utilities"}
            )

    def test_to_dict(self) -> None:
        data = GeneratorData(**self.valid_params)
        d = data.to_dict()
        self.assertEqual(d["archive_path"], "/path/to/archive.tgz")
        self.assertEqual(d["target_dir"], "/path/to/target")
        self.assertEqual(d["template_key"], "python_library")
        self.assertEqual(d["scheme"], {"author": "Vladimir"})
        self.assertEqual(d["template_values"], {"NAME": "ats_utilities"})


if __name__ == "__main__":
    unittest.main()
