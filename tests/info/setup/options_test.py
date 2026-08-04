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
    Unit tests for InfoBundleOptions TypedDict.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.info.setup.options import InfoBundleOptions
from ats_utilities.context.bundle import ContextBundle


class TestInfoOptions(unittest.TestCase):
    """Unit tests for the InfoBundleOptions TypedDict structure."""

    def test_info_options_dict(self) -> None:
        """Test creating and accessing InfoBundleOptions structure."""
        mock_context_bundle = MagicMock(spec=ContextBundle)
        info_data = {"project_name": "ats_utilities"}

        opts: InfoBundleOptions = {
            "info": info_data,
            "context_bundle": mock_context_bundle
        }

        self.assertEqual(opts["info"], info_data)
        self.assertEqual(opts["context_bundle"], mock_context_bundle)


if __name__ == '__main__':
    unittest.main()
