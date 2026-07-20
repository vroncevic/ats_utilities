# -*- coding: UTF-8 -*-

'''
Module
    info_registry_test.py
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
    Unit tests for InfoRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.info.info_bundle import InfoBundle
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.info.info_registry import InfoRegistry
from ats_utilities.info.info_params import InfoParams

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class InfoRegistryTest(unittest.TestCase):
    '''
        Defines class InfoRegistryTest with attribute(s) and method(s).
        Tests InfoRegistry logic.

        It defines:

            :attributes: None.
            :methods:
                | test_create_info_bundle_from_dict - Tests creation from a valid dictionary.
                | test_create_info_bundle_from_dict_invalid - Tests error cases with None/invalid types.
    '''

    def test_create_info_bundle_from_dict(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        info_data = {
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_VERSION: "3.4.3",
            InfoKeys.ATS_BUILD_DATE: "2026-07-18",
            InfoKeys.ATS_LICENCE: "GPLv3",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: "True",  # String "True" gets parsed to bool
            InfoKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoKeys.ATS_LOG_FILE: "/path/to/run.log",
            InfoKeys.ATS_INFO_OK: True
        }
        bundle = InfoRegistry.create_info_bundle_from_dict(info_data, context_bundle)
        self.assertIsInstance(bundle, InfoBundle)
        self.assertEqual(bundle.name.name, "ats_utilities")
        self.assertEqual(bundle.version.version, "3.4.3")
        self.assertEqual(bundle.build_date.build_date, "2026-07-18")
        self.assertEqual(bundle.licence.licence, "GPLv3")
        self.assertEqual(bundle.repository.repository, "https://github.com/vroncevic/ats_utilities")
        self.assertEqual(bundle.organization.organization, "vroncevic")
        self.assertTrue(bundle.use_github.use_github)
        self.assertEqual(bundle.logo.logo, "/path/to/logo.png")
        self.assertEqual(bundle.log_file.log_file, "/path/to/run.log")
        self.assertTrue(bundle.info_ok.info_ok)

    def test_create_info_bundle_from_dict_invalid(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        info_data = {}

        # Context bundle None
        with self.assertRaises(ATSValueError):
            InfoRegistry.create_info_bundle_from_dict(info_data, None)  # type: ignore

        # Info dict None
        with self.assertRaises(ATSValueError):
            InfoRegistry.create_info_bundle_from_dict(None, context_bundle)  # type: ignore

        # Invalid types
        with self.assertRaises(ATSTypeError):
            InfoRegistry.create_info_bundle_from_dict(info_data, object())  # type: ignore

        with self.assertRaises(ATSTypeError):
            InfoRegistry.create_info_bundle_from_dict("not a dict", context_bundle)  # type: ignore

    def test_create_info_bundle_from_dict_edge_cases(self) -> None:
        from unittest.mock import patch
        context_bundle = ContextRegistry.create_default_context_bundle()

        # 1. Use Github infrastructure is boolean False
        info_data_bool = {
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_VERSION: "3.4.3",
            InfoKeys.ATS_BUILD_DATE: "2026-07-18",
            InfoKeys.ATS_LICENCE: "GPLv3",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False,  # actual bool
            InfoKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoKeys.ATS_LOG_FILE: "/path/to/run.log",
            InfoKeys.ATS_INFO_OK: True
        }
        bundle = InfoRegistry.create_info_bundle_from_dict(info_data_bool, context_bundle)
        self.assertFalse(bundle.use_github.use_github)

        # 2. Use Github infrastructure is string "False"
        info_data_str_false = info_data_bool.copy()
        info_data_str_false[InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = "False"
        bundle_str_false = InfoRegistry.create_info_bundle_from_dict(info_data_str_false, context_bundle)
        self.assertFalse(bundle_str_false.use_github.use_github)

        # 3. Patch _ATTR_TO_CLASS to return None for a key to hit line 109
        original_attr_to_class = InfoRegistry._ATTR_TO_CLASS
        try:
            InfoRegistry._ATTR_TO_CLASS = dict(original_attr_to_class)
            InfoRegistry._ATTR_TO_CLASS[InfoKeys.ATS_NAME] = None
            with self.assertRaises(TypeError):
                InfoRegistry.create_info_bundle_from_dict(info_data_bool, context_bundle)
        finally:
            InfoRegistry._ATTR_TO_CLASS = original_attr_to_class

    def test_create_bundle(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        info_data = {
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_VERSION: "3.4.3",
            InfoKeys.ATS_BUILD_DATE: "2026-07-18",
            InfoKeys.ATS_LICENCE: "GPLv3",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: "True",
            InfoKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoKeys.ATS_LOG_FILE: "/path/to/run.log",
            InfoKeys.ATS_INFO_OK: True
        }
        bundle = InfoRegistry.create_bundle(InfoParams(info=info_data, context_bundle=context_bundle))
        self.assertIsInstance(bundle, InfoBundle)
        self.assertEqual(bundle.name.name, "ats_utilities")


if __name__ == "__main__":
    unittest.main()
