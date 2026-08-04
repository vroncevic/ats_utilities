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
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.exceptions import ATSAttributeError, ATSTypeError, ATSValueError
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.keys import InfoBundleKeys
from ats_utilities.info.setup.schema import InfoSchema
from ats_utilities.info.setup.factory import InfoBundleFactory


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests InfoManager logic.
    '''

    def _get_valid_info_data(self) -> dict[str, object]:
        return {
            InfoBundleKeys.ATS_NAME: "ats_utilities",
            InfoBundleKeys.ATS_VERSION: "3.4.4",
            InfoBundleKeys.ATS_BUILD_DATE: "2026-07-18",
            InfoBundleKeys.ATS_LICENCE: "GPLv3",
            InfoBundleKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoBundleKeys.ATS_ORGANIZATION: "vroncevic",
            InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE: "True",
            InfoBundleKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoBundleKeys.ATS_LOG_FILE: "/path/to/run.log",
            InfoBundleKeys.ATS_INFO_OK: True
        }

    def _get_bundle(self, context_bundle: ContextBundle) -> InfoBundle:
        return InfoBundleFactory.create_bundle({
            "info": self._get_valid_info_data(),
            "context_bundle": context_bundle
        })

    def test_init(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
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
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertIs(manager.get_context(), context_bundle)

    def test_set_and_get_info(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        new_info = {
            InfoBundleKeys.ATS_NAME: "new_name",
            InfoBundleKeys.ATS_VERSION: "1.0.0",
            InfoBundleKeys.ATS_BUILD_DATE: "2026-07-19",
            InfoBundleKeys.ATS_LICENCE: "MIT",
            InfoBundleKeys.ATS_REPOSITORY: "https://github.com/vroncevic/new_repo",
            InfoBundleKeys.ATS_ORGANIZATION: "new_org",
            InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE: "True",
            InfoBundleKeys.ATS_LOGO_PATH: "/new/logo.png",
            InfoBundleKeys.ATS_LOG_FILE: "/new/run.log",
            InfoBundleKeys.ATS_INFO_OK: True
        }

        manager.set_info(new_info)
        retrieved = manager.get_info()
        self.assertEqual(retrieved[InfoBundleKeys.ATS_NAME], "new_name")
        self.assertEqual(retrieved[InfoBundleKeys.ATS_VERSION], "1.0.0")
        self.assertEqual(retrieved[InfoBundleKeys.ATS_LOG_FILE], "/new/run.log")
        self.assertTrue(retrieved[InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE])

        # Test log file None and github infrastructure "False"
        another_info = new_info.copy()
        another_info[InfoBundleKeys.ATS_LOG_FILE] = None
        another_info[InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = "False"
        manager.set_info(another_info)
        self.assertFalse(manager.use_github)

        # Test github infrastructure as direct boolean to bypass isinstance(val, str)
        third_info = new_info.copy()
        third_info[InfoBundleKeys.ATS_LOG_FILE] = "/new/run2.log"
        third_info[InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False
        manager.set_info(third_info)
        self.assertFalse(manager.use_github)

    def test_set_info_invalid(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        # Missing key
        invalid_info_1 = self._get_valid_info_data().copy()
        del invalid_info_1[InfoBundleKeys.ATS_NAME]
        with self.assertRaises(ATSValueError):
            manager.set_info(invalid_info_1)

        # Null value for required key
        invalid_info_2 = self._get_valid_info_data().copy()
        invalid_info_2[InfoBundleKeys.ATS_NAME] = None  # type: ignore
        with self.assertRaises(ATSValueError):
            manager.set_info(invalid_info_2)

    def test_dynamic_attributes(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
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
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)

        # Get invalid attribute
        with self.assertRaises(ATSAttributeError):
            _ = manager.invalid_attr

    def test_is_initialized(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertTrue(manager.is_initialized())

        # If we unset a required field, info_ok should refresh to False
        bundle.name._name = None  # Bypass decorator to set to None
        manager.refresh_status()
        self.assertFalse(manager.is_initialized())

    def test_str(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertIn("InfoManager", str(manager))

    def test_setattr_edge_cases(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
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

    def test_get_bundle(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        self.assertIs(manager.get_bundle(), bundle)

    def test_update_bundle(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        
        # Valid update
        new_bundle = self._get_bundle(context_bundle)
        self.assertTrue(manager.update_bundle(new_bundle))
        self.assertIs(manager.get_bundle(), new_bundle)

        # Invalid update
        self.assertFalse(manager.update_bundle("invalid" * 10))  # type: ignore

    def test_is_initialized_false(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        
        manager._is_initialized = False
        self.assertFalse(manager.is_initialized())
        
        manager._is_initialized = True
        manager._components = None  # type: ignore
        self.assertFalse(manager.is_initialized())

    def test_refresh_status_none(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        manager._components = None  # type: ignore
        # Should not raise exception
        manager.refresh_status()

    def test_refresh_status_info_ok_none(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        # Delete info_ok attribute from bundle
        object.__delattr__(bundle, InfoBundleKeys.DEPENDENCY_INFO_OK)
        # Should not raise exception
        manager.refresh_status()

    def test_get_info_missing_components(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        
        # Set some component to None
        object.__setattr__(bundle, "logo", None)
        info = manager.get_info()
        self.assertNotIn(InfoBundleKeys.ATS_LOGO_PATH, info)

        # Set component attribute to None
        class DummyLogo:
            logo = None
        object.__setattr__(bundle, "logo", DummyLogo())
        info = manager.get_info()
        self.assertNotIn(InfoBundleKeys.ATS_LOGO_PATH, info)

        # Required component itself is None
        object.__setattr__(bundle, "version", None)
        manager.refresh_status()
        self.assertFalse(manager.is_initialized())

    @patch("ats_utilities.info.engine.InfoSchema.get_names_of_required_config_keys")
    def test_refresh_status_required_keys_contains_info_ok(self, mock_get_req_keys: MagicMock) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        bundle = self._get_bundle(context_bundle)
        manager = InfoManager(bundle)
        
        # Force required keys to contain info_ok to trigger the continue branch
        mock_get_req_keys.return_value = [InfoBundleKeys.DEPENDENCY_INFO_OK]
        manager.refresh_status()


if __name__ == "__main__":
    unittest.main()
