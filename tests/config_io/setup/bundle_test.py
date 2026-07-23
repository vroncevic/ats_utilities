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
    Unit tests for ConfigIOBundle class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.setup.bundle import ConfigIOBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ConfigIOBundleTest(unittest.TestCase):
    '''
        Defines class ConfigIOBundleTest with attribute(s) and method(s).
        Tests ConfigIOBundle dataclass logic.
    '''

    def setUp(self) -> None:
        self.mock_processor = MagicMock(spec=IConfigProcessor)
        self.mock_context = MagicMock(spec=ContextBundle)

        self.valid_params = {
            "file_path": "/tmp/config.json",
            "scheme": {"key": "value"},
            "processor": self.mock_processor,
            "context_bundle": self.mock_context
        }

    def test_init_valid(self) -> None:
        bundle = ConfigIOBundle(**self.valid_params)
        self.assertEqual(bundle.file_path, "/tmp/config.json")
        self.assertEqual(bundle.scheme, {"key": "value"})
        self.assertIs(bundle.processor, self.mock_processor)
        self.assertIs(bundle.context_bundle, self.mock_context)

    def test_immutability_frozen_slots(self) -> None:
        bundle = ConfigIOBundle(**self.valid_params)
        with self.assertRaises(FrozenInstanceError):
            bundle.file_path = "/other/path.json"  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        with self.assertRaises(TypeError):
            ConfigIOBundle(
                # pyrefly: ignore [unexpected-positional-argument]
                "/tmp/config.json",
                # pyrefly: ignore [unexpected-positional-argument]
                {"key": "value"},
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_processor,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_context
            )

    def test_to_dict(self) -> None:
        bundle = ConfigIOBundle(**self.valid_params)
        exported_dict = bundle.to_dict()
        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict["file_path"], "/tmp/config.json")
        self.assertEqual(exported_dict["scheme"], {"key": "value"})
        self.assertEqual(exported_dict["processor"], self.mock_processor)
        self.assertEqual(exported_dict["context_bundle"], self.mock_context)


if __name__ == "__main__":
    unittest.main()
