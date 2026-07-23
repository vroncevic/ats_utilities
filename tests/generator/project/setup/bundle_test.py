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
    Unit tests for ProjectBundle class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.project.ipro_config import IProConfig
from ats_utilities.generator.project.ipro_name import IProName
from ats_utilities.generator.project.itemplate_dir import ITemplateDir
from ats_utilities.generator.project.setup.bundle import ProjectBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProjectBundleTest(unittest.TestCase):
    '''
        Defines class ProjectBundleTest with attribute(s) and method(s).
        Tests ProjectBundle dataclass logic.
    '''

    def setUp(self) -> None:
        self.mock_pro_name = MagicMock(spec=IProName)
        self.mock_pro_config = MagicMock(spec=IProConfig)
        self.mock_template_dir = MagicMock(spec=ITemplateDir)
        self.mock_context = MagicMock(spec=ContextBundle)

        self.valid_params = {
            "pro_name": self.mock_pro_name,
            "pro_config": self.mock_pro_config,
            "template_dir": self.mock_template_dir,
            "context_bundle": self.mock_context
        }

    def test_init_valid(self) -> None:
        bundle = ProjectBundle(**self.valid_params)
        self.assertIs(bundle.pro_name, self.mock_pro_name)
        self.assertIs(bundle.pro_config, self.mock_pro_config)
        self.assertIs(bundle.template_dir, self.mock_template_dir)
        self.assertIs(bundle.context_bundle, self.mock_context)

    def test_immutability_frozen_slots(self) -> None:
        bundle = ProjectBundle(**self.valid_params)
        with self.assertRaises(FrozenInstanceError):
            bundle.context_bundle = MagicMock(spec=ContextBundle)  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        with self.assertRaises(TypeError):
            ProjectBundle(
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_pro_name,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_pro_config,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_template_dir,
                # pyrefly: ignore [unexpected-positional-argument]
                self.mock_context
            )

    def test_to_dict(self) -> None:
        bundle = ProjectBundle(**self.valid_params)
        exported_dict = bundle.to_dict()
        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict["pro_name"], self.mock_pro_name)
        self.assertEqual(exported_dict["pro_config"], self.mock_pro_config)
        self.assertEqual(exported_dict["template_dir"], self.mock_template_dir)
        self.assertEqual(exported_dict["context_bundle"], self.mock_context)


if __name__ == "__main__":
    unittest.main()
