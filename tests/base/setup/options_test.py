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
    Unit tests for BaseOptions class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.base.setup.options import BaseOptions
from ats_utilities.context.bundle import ContextBundle


class TestBaseOptions(unittest.TestCase):
    """Unit tests for the BaseOptions TypedDict structure."""

    def setUp(self) -> None:
        """Set up standard dependencies and mock components for options testing."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.info_file = "/opt/ats/config/info.json"

        self.valid_params = {
            "info_file": self.info_file,
            "use_generator": True,
            "context_bundle": self.mock_context_bundle
        }

    def test_successful_initialization(self) -> None:
        """Test successful initialization when all parameters match types and constraints."""
        options: BaseOptions = {
            "info_file": self.info_file,
            "use_generator": True,
            "context_bundle": self.mock_context_bundle
        }

        self.assertEqual(options["info_file"], self.info_file)
        self.assertTrue(options["use_generator"])
        self.assertEqual(options["context_bundle"], self.mock_context_bundle)


if __name__ == '__main__':
    unittest.main()
