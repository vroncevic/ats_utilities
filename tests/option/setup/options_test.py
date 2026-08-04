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
    Unit tests for OptionBundleOptions TypedDict.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.options import OptionBundleOptions


class OptionsTest(unittest.TestCase):
    '''
        Defines class OptionsTest with attribute(s) and method(s).
        Tests OptionBundleOptions structure.
    '''

    def test_options_structure(self) -> None:
        mock_context = MagicMock(spec=ContextBundle)
        params = {
            "name": "mytool",
            "version": "1.0.0"
        }

        opts: OptionBundleOptions = {
            "parameters": params,
            "context_bundle": mock_context
        }
        self.assertEqual(opts["parameters"], params)
        self.assertIs(opts["context_bundle"], mock_context)


if __name__ == "__main__":
    unittest.main()
