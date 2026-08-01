# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
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
    Unit tests for BaseKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.base.setup.keys import BaseKeys
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager


class TestBaseKeys(unittest.TestCase):
    """Unit tests for the BaseKeys class."""

    def test_get_dependency_to_type(self) -> None:
        """Test get_dependency_to_type returns correct MappingProxyType with all dependency classes."""
        dep_mapping = BaseKeys.get_dependency_to_type()
        self.assertIsInstance(dep_mapping, MappingProxyType)

        self.assertEqual(dep_mapping.get(BaseKeys.DEPENDENCY_CONTEXT_BUNDLE), ContextBundle)
        self.assertEqual(dep_mapping.get(BaseKeys.DEPENDENCY_INFO_MANAGER), IInfoManager)
        self.assertEqual(dep_mapping.get(BaseKeys.DEPENDENCY_OPTION_MANAGER), IOptionManager)
        self.assertEqual(dep_mapping.get(BaseKeys.DEPENDENCY_SPLASH_MANAGER), ISplashManager)
        self.assertEqual(dep_mapping.get(BaseKeys.DEPENDENCY_GENERATION_MANAGER), IGeneratorManager)

    def test_get_option_to_type(self) -> None:
        """Test get_option_to_type returns correct MappingProxyType with all option types."""
        opt_mapping = BaseKeys.get_option_to_type()
        self.assertIsInstance(opt_mapping, MappingProxyType)

        self.assertEqual(opt_mapping.get(BaseKeys.OPTION_INFO_FILE), str)
        self.assertEqual(opt_mapping.get(BaseKeys.OPTION_USE_GENERATOR), bool)
        self.assertEqual(opt_mapping.get(BaseKeys.OPTION_CONTEXT_BUNDLE), ContextBundle)


if __name__ == '__main__':
    unittest.main()
