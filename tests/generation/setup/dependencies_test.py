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
    Unit tests for GeneratorBundleDependencies class.
'''

from __future__ import annotations

import unittest
from typing import get_type_hints
from unittest.mock import MagicMock

from ats_utilities.generation.setup.dependencies import GeneratorBundleDependencies
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.context.bundle import ContextBundle


class GeneratorDependenciesTest(unittest.TestCase):
    '''
        Defines class GeneratorDependenciesTest with attribute(s) and method(s).
        Tests GeneratorBundleDependencies TypedDict structure.
    '''

    def test_type_hints(self) -> None:
        hints = get_type_hints(GeneratorBundleDependencies)
        self.assertEqual(hints['scheme_loader'], ISchemeLoader)
        self.assertEqual(hints['tar_processor'], ITarProcessor)
        self.assertEqual(hints['context_bundle'], ContextBundle)

    def test_instantiation(self) -> None:
        deps: GeneratorBundleDependencies = {
            'scheme_loader': MagicMock(spec=ISchemeLoader),
            'tar_processor': MagicMock(spec=ITarProcessor),
            'context_bundle': MagicMock(spec=ContextBundle)
        }
        self.assertEqual(len(deps), 3)


if __name__ == "__main__":
    unittest.main()
