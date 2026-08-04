# -*- coding: UTF-8 -*-

'''
Module
    dependencies_test.py
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
    Unit tests for ConfigIOBundleDependencies class.
'''

from __future__ import annotations

import unittest
from typing import get_type_hints
from unittest.mock import MagicMock

from ats_utilities.config_io.setup.dependencies import ConfigIOBundleDependencies
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.bundle import ContextBundle


class ConfigIODependenciesTest(unittest.TestCase):
    '''
        Defines class ConfigIODependenciesTest with attribute(s) and method(s).
        Tests ConfigIOBundleDependencies TypedDict structure.
    '''

    def test_type_hints(self) -> None:
        hints = get_type_hints(ConfigIOBundleDependencies)
        self.assertEqual(hints['file_path'], str)
        self.assertEqual(hints['processor'], IConfigProcessor)
        self.assertEqual(hints['context_bundle'], ContextBundle)

    def test_instantiation(self) -> None:
        deps: ConfigIOBundleDependencies = {
            'file_path': "/path/to/file",
            'processor': MagicMock(spec=IConfigProcessor),
            'context_bundle': MagicMock(spec=ContextBundle)
        }
        self.assertEqual(len(deps), 3)


if __name__ == "__main__":
    unittest.main()
