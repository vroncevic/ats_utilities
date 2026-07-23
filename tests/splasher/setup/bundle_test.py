# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
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
    Unit tests for SplashBundle class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from typing import Any
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.setup.bundle import SplashBundle
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashBundleTest(unittest.TestCase):
    '''
        Defines class SplashBundleTest with attribute(s) and method(s).
        Tests SplashBundle dataclass logic.
    '''

    def _get_mocks(self) -> dict[str, Any]:
        return {
            "prop": {"enabled": True},
            "splash_property": MagicMock(spec=ISplashProperty),
            "property_validated": True,
            "terminal_property": MagicMock(spec=ITerminalProperties),
            "ext": MagicMock(spec=IExtInfrastructure),
            "pb": MagicMock(spec=IProgressBar),
            "context_bundle": MagicMock(spec=ContextBundle),
        }

    def test_init_valid(self) -> None:
        mocks = self._get_mocks()
        bundle = SplashBundle(**mocks)
        for key, val in mocks.items():
            self.assertIs(getattr(bundle, key), val)

    def test_immutability_frozen_slots(self) -> None:
        mocks = self._get_mocks()
        bundle = SplashBundle(**mocks)
        with self.assertRaises(FrozenInstanceError):
            bundle.context_bundle = MagicMock(spec=ContextBundle)  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        mocks = self._get_mocks()
        with self.assertRaises(TypeError):
            SplashBundle(
                # pyrefly: ignore [unexpected-positional-argument]
                mocks["prop"],
                # pyrefly: ignore [unexpected-positional-argument]
                mocks["splash_property"],
                # pyrefly: ignore [unexpected-positional-argument]
                mocks["property_validated"],
                # pyrefly: ignore [unexpected-positional-argument]
                mocks["terminal_property"],
                # pyrefly: ignore [unexpected-positional-argument]
                mocks["ext"],
                # pyrefly: ignore [unexpected-positional-argument]
                mocks["pb"],
                # pyrefly: ignore [unexpected-positional-argument]
                mocks["context_bundle"]
            )

    def test_to_dict(self) -> None:
        mocks = self._get_mocks()
        bundle = SplashBundle(**mocks)
        self.assertEqual(bundle.to_dict(), mocks)


if __name__ == "__main__":
    unittest.main()
