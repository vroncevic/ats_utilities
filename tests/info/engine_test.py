# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for InfoManager class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSAttributeError, ATSTypeError, ATSValueError
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.info.setup.schema import InfoSchema
from ats_utilities.info.setup.factory import InfoFactory


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests InfoManager logic.
    '''

    def _get_valid_info_data(self) -> dict[str, object]:
        return {
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_VERSION: "3.4.4",
            InfoKeys.ATS_BUILD_DATE: "2026-07-18",
            InfoKeys.ATS_LICENCE: "GPLv3",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: "True",
            InfoKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoKeys.ATS_LOG_FILE: "/path/to/run.log",
            InfoKeys.ATS_INFO_OK: True
        }

    def _get_bundle(self, context_bundle: ContextBundle) -> InfoBundle:
        return InfoFactory.create_bundle({
            "info": self._get_valid_info_data(),
            "context_bundle": context_bundle
        })

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertIsInstance(manager, InfoManager)
        self.assertTrue(manager.is_initialized())

    def test_init_invalid(self) -> None:
        with self.assertRaises(ATSValueError):
            InfoManager(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            InfoManager(object())  # type: ignore

    def test_get_context(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertIs(manager.get_context(), context_bundle)

    def test_set_and_get_info(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        new_info = {
            InfoKeys.ATS_NAME: "new_name",
            InfoKeys.ATS_VERSION: "1.0.0",
            InfoKeys.ATS_BUILD_DATE: "2026-07-19",
            InfoKeys.ATS_LICENCE: "MIT",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/new_repo",
            InfoKeys.ATS_ORGANIZATION: "new_org",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: "True",
            InfoKeys.ATS_LOGO_PATH: "/new/logo.png",
            InfoKeys.ATS_LOG_FILE: "/new/run.log",
            InfoKeys.ATS_INFO_OK: True
        }

        manager.set_info(new_info)
        retrieved = manager.get_info()
        self.assertEqual(retrieved[InfoKeys.ATS_NAME], "new_name")
        self.assertEqual(retrieved[InfoKeys.ATS_VERSION], "1.0.0")
        self.assertEqual(retrieved[InfoKeys.ATS_LOG_FILE], "/new/run.log")
        self.assertTrue(retrieved[InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE])

        # Test log file None and github infrastructure "False"
        another_info = new_info.copy()
        another_info[InfoKeys.ATS_LOG_FILE] = None
        another_info[InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = "False"
        manager.set_info(another_info)
        self.assertFalse(manager.use_github)

        # Test github infrastructure as direct boolean to bypass isinstance(val, str)
        third_info = new_info.copy()
        third_info[InfoKeys.ATS_LOG_FILE] = "/new/run2.log"
        third_info[InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False
        manager.set_info(third_info)
        self.assertFalse(manager.use_github)

    def test_set_info_invalid(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        # Missing key
        invalid_info_1 = self._get_valid_info_data().copy()
        del invalid_info_1[InfoKeys.ATS_NAME]
        with self.assertRaises(ATSValueError):
            manager.set_info(invalid_info_1)

        # Null value for required key
        invalid_info_2 = self._get_valid_info_data().copy()
        invalid_info_2[InfoKeys.ATS_NAME] = None  # type: ignore
        with self.assertRaises(ATSValueError):
            manager.set_info(invalid_info_2)

    def test_dynamic_attributes(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        # Get managed attribute
        self.assertEqual(manager.name, "ats_utilities")
        self.assertEqual(manager.version, "3.4.4")

        # Set managed attribute
        manager.name = "changed_name"
        self.assertEqual(manager.name, "changed_name")
        self.assertEqual(bundle.name.name, "changed_name")

    def test_dynamic_attributes_invalid(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        # Get invalid attribute
        with self.assertRaises(ATSAttributeError):
            _ = manager.invalid_attr

    def test_is_initialized(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertTrue(manager.is_initialized())

        # If we unset a required field, info_ok should refresh to False
        bundle.name._name = None  # Bypass decorator to set to None
        manager.refresh_status()
        self.assertFalse(manager.is_initialized())

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertIn("InfoManager", str(manager))

    def test_setattr_edge_cases(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        # Set a private/protected attribute on manager itself (starts with '_')
        manager._some_custom_attr = "hello"
        self.assertEqual(manager._some_custom_attr, "hello")

        # Replace _components with object() that has no attributes,
        # then set a managed attribute (e.g. name) to hit component=None branch
        manager._components = object()
        with self.assertRaises(ATSAttributeError):
            manager.name = "new_name"


if __name__ == "__main__":
    unittest.main()
