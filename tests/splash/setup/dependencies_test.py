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
    Unit tests for SplashDependencies TypedDict.
'''

from __future__ import annotations

import unittest
from typing import get_type_hints
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.setup.dependencies import SplashDependencies
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties


class SplashDependenciesTest(unittest.TestCase):
    '''
        Defines class SplashDependenciesTest with attribute(s) and method(s).
        Tests SplashDependencies type annotations.
    '''

    def test_type_hints(self) -> None:
        hints = get_type_hints(SplashDependencies)
        self.assertEqual(hints["splash_property"], ISplashProperty)
        self.assertEqual(hints["terminal_property"], ITerminalProperties)
        self.assertEqual(hints["ext"], IExtInfrastructure)
        self.assertEqual(hints["pb"], IProgressBar)
        self.assertEqual(hints["context_bundle"], ContextBundle)

    def test_instantiation(self) -> None:
        mock_splash_property = MagicMock(spec=ISplashProperty)
        mock_terminal_property = MagicMock(spec=ITerminalProperties)
        mock_ext = MagicMock(spec=IExtInfrastructure)
        mock_pb = MagicMock(spec=IProgressBar)
        mock_context_bundle = MagicMock(spec=ContextBundle)

        deps: SplashDependencies = {
            "splash_property": mock_splash_property,
            "terminal_property": mock_terminal_property,
            "ext": mock_ext,
            "pb": mock_pb,
            "context_bundle": mock_context_bundle
        }

        self.assertEqual(deps["splash_property"], mock_splash_property)
        self.assertEqual(deps["terminal_property"], mock_terminal_property)
        self.assertEqual(deps["ext"], mock_ext)
        self.assertEqual(deps["pb"], mock_pb)
        self.assertEqual(deps["context_bundle"], mock_context_bundle)


if __name__ == "__main__":
    unittest.main()
