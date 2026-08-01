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
    Unit tests for InfoKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.info.name.iname import IName
from ats_utilities.info.name.engine import Name
from ats_utilities.info.version.iversion import IVersion
from ats_utilities.info.version.engine import Version
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.licence.engine import Licence
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.build_date.engine import BuildDate
from ats_utilities.info.repository.irepository import IRepository
from ats_utilities.info.repository.engine import Repository
from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.info.organization.engine import Organization
from ats_utilities.info.use_github.iuse_github import IUseGitHub
from ats_utilities.info.use_github.engine import UseGitHub
from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.info.logo.engine import Logo
from ats_utilities.info.log_file.ilog_file import ILogFile
from ats_utilities.info.log_file.engine import LogFile
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.info.info_ok.engine import InfoOk
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError


class TestInfoKeys(unittest.TestCase):
    """Unit tests for the InfoKeys class."""

    def test_get_dependency_to_type(self) -> None:
        """Test get_dependency_to_type returns correct MappingProxyType with all dependency classes."""
        dep_mapping = InfoKeys.get_dependency_to_type()
        self.assertIsInstance(dep_mapping, MappingProxyType)

        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_NAME), IName)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_VERSION), IVersion)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_LICENCE), ILicence)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_BUILD_DATE), IBuildDate)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_REPOSITORY), IRepository)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_ORGANIZATION), IOrganization)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE), IUseGitHub)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_LOGO_PATH), ILogo)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_LOG_FILE), ILogFile)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_INFO_OK), IInfoOk)
        self.assertEqual(dep_mapping.get(InfoKeys.DEPENDENCY_CONTEXT_BUNDLE), ContextBundle)

    def test_get_option_to_type(self) -> None:
        """Test get_option_to_type returns correct MappingProxyType with all option types."""
        opt_mapping = InfoKeys.get_option_to_type()
        self.assertIsInstance(opt_mapping, MappingProxyType)

        self.assertEqual(opt_mapping.get(InfoKeys.OPTION_CONTEXT_BUNDLE), ContextBundle)

    def test_get_config_keys(self) -> None:
        """Test that get_config_keys returns all expected information keys."""
        keys = InfoKeys.get_config_keys()
        self.assertIn(InfoKeys.ATS_NAME, keys)
        self.assertIn(InfoKeys.ATS_VERSION, keys)
        self.assertIn(InfoKeys.ATS_BUILD_DATE, keys)
        self.assertIn(InfoKeys.ATS_LICENCE, keys)

    def test_is_registered_config_key(self) -> None:
        """Test register checks for config keys."""
        self.assertTrue(InfoKeys.is_registered_config_key(InfoKeys.ATS_NAME))
        self.assertFalse(InfoKeys.is_registered_config_key("not_registered"))

    def test_get_optional_config_keys(self) -> None:
        """Test get_optional_config_keys sequence matches."""
        optional_keys = InfoKeys.get_optional_config_keys()
        self.assertIn(InfoKeys.ATS_REPOSITORY, optional_keys)
        self.assertNotIn(InfoKeys.ATS_NAME, optional_keys)

    def test_get_required_config_keys(self) -> None:
        """Test get_required_config_keys sequence matches."""
        required_keys = InfoKeys.get_required_config_keys()
        self.assertIn(InfoKeys.ATS_NAME, required_keys)
        self.assertNotIn(InfoKeys.ATS_REPOSITORY, required_keys)

    def test_get_name_of_config_key(self) -> None:
        """Test key to dependency name mapping."""
        self.assertEqual(
            InfoKeys.get_name_of_config_key(InfoKeys.ATS_NAME),
            InfoKeys.DEPENDENCY_NAME
        )
        with self.assertRaises(ATSValueError):
            InfoKeys.get_name_of_config_key("not_registered")

    def test_get_config_key_to_type(self) -> None:
        """Test configuration type mappings."""
        mapping = InfoKeys.get_config_key_to_type()
        self.assertEqual(mapping[InfoKeys.ATS_NAME], Name)
        self.assertEqual(mapping[InfoKeys.ATS_VERSION], Version)

    def test_get_info_getters(self) -> None:
        """Test utility config getters."""
        config = {
            InfoKeys.ATS_NAME: "my_app",
            InfoKeys.ATS_VERSION: "1.0.0",
            InfoKeys.ATS_BUILD_DATE: "2026-08-01",
            InfoKeys.ATS_LICENCE: "GPL"
        }

        self.assertEqual(InfoKeys.get_name(config), "my_app")
        with self.assertRaises(ATSValueError):
            InfoKeys.get_name({})


if __name__ == '__main__':
    unittest.main()
