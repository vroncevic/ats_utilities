# -*- coding: UTF-8 -*-

'''
Module
    options_test.py
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
    Unit tests for ConfigIOOptions class.
'''

from __future__ import annotations

import unittest
from collections.abc import Mapping
from typing import get_type_hints
from unittest.mock import MagicMock

from ats_utilities.config_io.setup.options import ConfigIOOptions
from ats_utilities.context.bundle import ContextBundle


class ConfigIOOptionsTest(unittest.TestCase):
    '''
        Defines class ConfigIOOptionsTest with attribute(s) and method(s).
        Tests ConfigIOOptions TypedDict structure.
    '''

    def test_type_hints(self) -> None:
        hints = get_type_hints(ConfigIOOptions)
        self.assertEqual(hints['file_path'], str)
        self.assertEqual(hints['scheme'], Mapping[str, str])
        self.assertEqual(hints['context_bundle'], ContextBundle)

    def test_instantiation(self) -> None:
        options: ConfigIOOptions = {
            'file_path': "/path/to/file",
            'scheme': {"key": "val"},
            'context_bundle': MagicMock(spec=ContextBundle)
        }
        self.assertEqual(len(options), 3)


if __name__ == "__main__":
    unittest.main()
